#!/usr/bin/env python3
"""
Macau Tourist Statistics Chart Generator
Generates line charts and statistics from tourist arrival data
"""

import json
import os
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

# Output directory for charts
CHARTS_DIR = os.path.join(os.path.dirname(__file__), "..", "charts")
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_data():
    """Load processed tourist data"""
    data_file = os.path.join(DATA_DIR, "latest_data.json")
    
    if not os.path.exists(data_file):
        print(f"❌ Data file not found: {data_file}")
        return None
    
    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return data.get("result", [])

def create_line_chart(records, output_file):
    """Create line chart showing tourist arrivals over time"""
    print(f"📈 Creating line chart...")
    
    # Convert to DataFrame
    df = pd.DataFrame(records)
    
    # Try to extract date and visitor columns
    # Adjust column names based on actual data structure
    date_col = None
    visitor_col = None
    
    for col in df.columns:
        if "年" in col or "Year" in col:
            date_col = col
        if "總訪客" in col or "Total" in col or "Visitors" in col:
            visitor_col = col
    
    if not visitor_col:
        # Use first numeric column
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            visitor_col = numeric_cols[0]
    
    if not visitor_col:
        print("❌ Could not find visitor count column")
        return False
    
    # Create figure
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Plot data
    if visitor_col:
        ax.plot(df.index, df[visitor_col], marker='o', linewidth=2, markersize=6, label='Total Visitors')
    
    # Customize chart
    ax.set_xlabel('Time Period', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Visitors', fontsize=12, fontweight='bold')
    ax.set_title('🇲🇴 Macau Tourist Arrivals Over Time', fontsize=16, fontweight='bold', pad=20)
    
    # Rotate x-axis labels
    plt.xticks(rotation=45, ha='right')
    
    # Add grid
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Add legend
    ax.legend(loc='upper left', fontsize=10)
    
    # Tight layout
    plt.tight_layout()
    
    # Save chart
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Chart saved to: {output_file}")
    return True

def create_comparison_chart(records, output_file):
    """Create comparison chart for different regions"""
    print(f"📊 Creating comparison chart...")
    
    df = pd.DataFrame(records)
    
    # Find region columns
    region_cols = []
    for col in df.columns:
        if any(region in col for region in ["中國", "內地", "Mainland", "香港", "Hong Kong", "台灣", "Taiwan", "其他", "Other"]):
            region_cols.append(col)
    
    if not region_cols:
        print("⚠️  No region columns found, skipping comparison chart")
        return False
    
    # Create figure
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Plot each region
    colors = plt.cm.Set3(range(len(region_cols)))
    for i, col in enumerate(region_cols):
        ax.plot(df.index, df[col], marker='s', linewidth=2, markersize=5, 
                label=col, color=colors[i % len(colors)])
    
    # Customize chart
    ax.set_xlabel('Time Period', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Visitors', fontsize=12, fontweight='bold')
    ax.set_title('🇲🇴 Macau Tourist Arrivals by Region', fontsize=16, fontweight='bold', pad=20)
    
    # Rotate x-axis labels
    plt.xticks(rotation=45, ha='right')
    
    # Add grid
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Add legend
    ax.legend(loc='upper left', fontsize=9, bbox_to_anchor=(1, 1))
    
    # Tight layout
    plt.tight_layout()
    
    # Save chart
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Comparison chart saved to: {output_file}")
    return True

def generate_statistics(records):
    """Generate summary statistics"""
    print(f"📋 Generating statistics...")
    
    df = pd.DataFrame(records)
    
    # Find numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    
    stats = {}
    for col in numeric_cols:
        stats[col] = {
            "total": float(df[col].sum()) if not df[col].isna().all() else 0,
            "mean": float(df[col].mean()) if not df[col].isna().all() else 0,
            "min": float(df[col].min()) if not df[col].isna().all() else 0,
            "max": float(df[col].max()) if not df[col].isna().all() else 0,
            "records": len(df)
        }
    
    # Save statistics
    stats_file = os.path.join(DATA_DIR, "statistics.json")
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Statistics saved to: {stats_file}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY STATISTICS")
    print("=" * 60)
    for col, data in stats.items():
        print(f"\n{col}:")
        print(f"  Total: {data['total']:,.0f}")
        print(f"  Average: {data['mean']:,.0f}")
        print(f"  Min: {data['min']:,.0f}")
        print(f"  Max: {data['max']:,.0f}")
        print(f"  Records: {data['records']}")
    
    return stats

def main():
    """Main entry point"""
    print("=" * 60)
    print("🇲🇴 Macau Tourist Statistics Chart Generator")
    print("=" * 60)
    
    # Load data
    records = load_data()
    
    if not records:
        print("❌ No data to process")
        return 1
    
    print(f"✅ Loaded {len(records)} records")
    
    # Create charts directory
    os.makedirs(CHARTS_DIR, exist_ok=True)
    
    # Generate line chart
    line_chart_file = os.path.join(CHARTS_DIR, "tourist_arrivals_line.png")
    create_line_chart(records, line_chart_file)
    
    # Generate comparison chart
    comparison_chart_file = os.path.join(CHARTS_DIR, "tourist_arrivals_by_region.png")
    create_comparison_chart(records, comparison_chart_file)
    
    # Generate statistics
    generate_statistics(records)
    
    print("\n" + "=" * 60)
    print("✅ Chart generation complete!")
    print("=" * 60)
    print(f"\n📁 Charts saved to: {CHARTS_DIR}")
    print("   - tourist_arrivals_line.png")
    print("   - tourist_arrivals_by_region.png")
    
    return 0

if __name__ == "__main__":
    exit(main())
