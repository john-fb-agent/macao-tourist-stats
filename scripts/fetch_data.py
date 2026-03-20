#!/usr/bin/env python3
"""
Macau Tourist Statistics Data Fetcher

Fetches tourist arrival data from Macau DSEC API and saves to JSON.

Environment Variables:
    MACAO_DATA_APPCODE: API authentication code (required)
    MACAO_DATA_OUTPUT: Output file path (default: data/data.json)
    MACAO_DATA_APP_JSON: App info file path (default: data/app.json)

Usage:
    python3 fetch_data.py
    MACAO_DATA_OUTPUT=/custom/path/data.json python3 fetch_data.py
"""

import os
import sys
import json
import requests
from datetime import datetime, timezone

# Configuration from environment variables
API_URL = "https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals"
APPCODE = os.getenv("MACAO_DATA_APPCODE")
OUTPUT_FILE = os.getenv("MACAO_DATA_OUTPUT", "data/data.json")
APP_JSON_FILE = os.getenv("MACAO_DATA_APP_JSON", "data/app.json")


def fetch_data():
    """Fetch tourist data from DSEC API"""
    if not APPCODE:
        print("❌ Error: MACAO_DATA_APPCODE environment variable is required")
        print("   Get your APPCODE from: https://data.gov.mo")
        sys.exit(1)
    
    headers = {
        "Authorization": f"APPCODE {APPCODE}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "from_year": 2008,
        "to_year": datetime.now().year,
        "lang": "zh-MO"
    }
    
    print(f"📊 Fetching data from DSEC API...")
    print(f"   URL: {API_URL}")
    print(f"   Output: {OUTPUT_FILE}")
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        if not data.get('success'):
            print(f"❌ API returned error: {data.get('errorMessage', 'Unknown error')}")
            sys.exit(1)
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        sys.exit(1)


def save_data(data, output_file):
    """Save data to JSON file"""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Data saved to: {output_file}")


def save_app_info(data, app_json_file):
    """Save app metadata including run datetime"""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(app_json_file), exist_ok=True)
    
    app_info = {
        "name": "Macau Tourist Statistics",
        "version": "1.5.0",
        "lastRun": datetime.now(timezone.utc).isoformat(),
        "lastRunLocal": datetime.now().isoformat(),
        "timezone": "Asia/Shanghai",
        "dataSource": "Macau DSEC API",
        "apiUrl": "https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals",
        "outputFile": OUTPUT_FILE,
        "records": len(data.get('value', {}).get('values', [])),
        "dataRange": {
            "from": data.get('value', {}).get('minYear', 'N/A'),
            "to": data.get('value', {}).get('maxYear', 'N/A')
        }
    }
    
    with open(app_json_file, 'w', encoding='utf-8') as f:
        json.dump(app_info, f, indent=2, ensure_ascii=False)
    
    print(f"✅ App info saved to: {app_json_file}")


def main():
    """Main entry point"""
    print("=" * 60)
    print("🇲🇴 Macau Tourist Statistics - Data Fetcher")
    print("=" * 60)
    print()
    
    # Fetch data
    data = fetch_data()
    
    # Verify data structure
    if 'value' not in data or 'values' not in data.get('value', {}):
        print("❌ Invalid data structure received from API")
        sys.exit(1)
    
    records = data['value']['values']
    print(f"📈 Records fetched: {len(records)}")
    print(f"📅 Data range: {data['value'].get('minYear', '?')} - {data['value'].get('maxYear', '?')}")
    print()
    
    # Save data
    save_data(data, OUTPUT_FILE)
    
    # Save app info with timestamp
    save_app_info(data, APP_JSON_FILE)
    
    print()
    print("=" * 60)
    print("✅ Data fetch complete!")
    print("=" * 60)
    print()
    print("Files created:")
    print(f"  - {OUTPUT_FILE}")
    print(f"  - {APP_JSON_FILE}")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
