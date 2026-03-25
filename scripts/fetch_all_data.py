#!/usr/bin/env python3
"""
Macau DSEC Multi-Indicator Data Fetcher

Fetches multiple indicators from Macau DSEC API:
- Visitor Arrivals (入境旅客)
- Hotel Occupancy Rate (酒店業場所入住率)

Usage:
    python3 fetch_all_data.py
    python3 fetch_all_data.py --indicator hotel
"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime, timezone
from typing import Optional, Dict, Any

# Configuration
APPCODE = os.getenv("MACAO_DATA_APPCODE", "09d43a591fba407fb862412970667de4")
BASE_URL = "https://dsec.apigateway.data.gov.mo/public/KeyIndicator"

INDICATORS = {
    "visitor": {
        "endpoint": f"{BASE_URL}/VisitorArrivals",
        "name": "入境旅客",
        "name_en": "Visitor Arrivals",
        "unit": "人次",
        "min_year": 2008,
        "data_type": "int"
    },
    "hotel": {
        "endpoint": f"{BASE_URL}/HotelEstablishmentOccupancyRate",
        "name": "酒店業場所入住率",
        "name_en": "Hotel Occupancy Rate",
        "unit": "%",
        "min_year": 1997,
        "data_type": "float"
    }
}


def fetch_indicator(indicator_key: str, from_year: Optional[int] = None, 
                    to_year: Optional[int] = None) -> Dict[str, Any]:
    """
    Fetch data from DSEC API for a specific indicator
    
    Args:
        indicator_key: Key from INDICATORS dict
        from_year: Starting year (optional)
        to_year: Ending year (optional)
    
    Returns:
        Parsed API response
    """
    if indicator_key not in INDICATORS:
        raise ValueError(f"Unknown indicator: {indicator_key}. "
                        f"Available: {list(INDICATORS.keys())}")
    
    config = INDICATORS[indicator_key]
    
    # Set default years if not provided
    current_year = datetime.now().year
    if from_year is None:
        from_year = config["min_year"]
    if to_year is None:
        to_year = current_year
    
    headers = {
        "Authorization": f"APPCODE {APPCODE}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "from_year": from_year,
        "to_year": to_year,
        "lang": "zh-MO"
    }
    
    print(f"📊 Fetching {config['name']} ({indicator_key})...")
    print(f"   Years: {from_year}-{to_year}")
    
    try:
        response = requests.post(
            config["endpoint"],
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        
        raw_data = response.json()
        
        # Handle different response formats
        if "data" in raw_data and isinstance(raw_data["data"], str):
            # Hotel API format - JSON string in data field
            result = json.loads(raw_data["data"])
        else:
            # Visitor API format - direct JSON
            result = raw_data
        
        if not result.get("success"):
            error_msg = result.get("errorMessage", "Unknown error")
            raise Exception(f"API error: {error_msg}")
        
        # Add metadata
        result["_indicator"] = indicator_key
        result["_fetched_at"] = datetime.now(timezone.utc).isoformat()
        result["_config"] = config
        
        values = result.get("value", {}).get("values", [])
        print(f"✅ Fetched {len(values)} records")
        
        return result
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON: {e}")


def save_data(data: Dict[str, Any], output_dir: str = "data") -> str:
    """Save indicator data to JSON file"""
    indicator = data.get("_indicator", "unknown")
    filename = f"{indicator}_data.json"
    filepath = os.path.join(output_dir, filename)
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return filepath


def save_combined_data(all_data: Dict[str, Any], output_dir: str = "data") -> str:
    """Save combined data from all indicators"""
    filepath = os.path.join(output_dir, "combined_data.json")
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Create summary
    summary = {
        "lastUpdated": datetime.now(timezone.utc).isoformat(),
        "timezone": "Asia/Shanghai",
        "indicators": {}
    }
    
    for key, data in all_data.items():
        config = data.get("_config", {})
        values = data.get("value", {}).get("values", [])
        
        summary["indicators"][key] = {
            "name": config.get("name"),
            "name_en": config.get("name_en"),
            "unit": config.get("unit"),
            "records": len(values),
            "minYear": data.get("value", {}).get("minYear"),
            "maxYear": data.get("value", {}).get("maxYear"),
            "dataFile": f"{key}_data.json"
        }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    return filepath


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Macau DSEC indicator data"
    )
    parser.add_argument(
        "--indicator",
        choices=list(INDICATORS.keys()),
        help="Specific indicator to fetch (default: all)"
    )
    parser.add_argument(
        "--from-year",
        type=int,
        help="Starting year"
    )
    parser.add_argument(
        "--to-year",
        type=int,
        help="Ending year"
    )
    parser.add_argument(
        "--output-dir",
        default="data",
        help="Output directory (default: data)"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🇲🇴 Macau DSEC Multi-Indicator Data Fetcher")
    print("=" * 60)
    print()
    
    # Determine which indicators to fetch
    if args.indicator:
        indicators_to_fetch = [args.indicator]
    else:
        indicators_to_fetch = list(INDICATORS.keys())
    
    all_data = {}
    
    for indicator_key in indicators_to_fetch:
        try:
            data = fetch_indicator(
                indicator_key,
                args.from_year,
                args.to_year
            )
            all_data[indicator_key] = data
            
            # Save individual file
            filepath = save_data(data, args.output_dir)
            print(f"💾 Saved to: {filepath}")
            print()
            
        except Exception as e:
            print(f"❌ Error fetching {indicator_key}: {e}")
            print()
    
    # Save combined summary
    if all_data:
        summary_path = save_combined_data(all_data, args.output_dir)
        print(f"📋 Summary saved to: {summary_path}")
        print()
    
    print("=" * 60)
    print(f"✅ Fetched {len(all_data)}/{len(indicators_to_fetch)} indicators")
    print("=" * 60)
    
    return 0 if len(all_data) == len(indicators_to_fetch) else 1


if __name__ == "__main__":
    sys.exit(main())