# 數據處理流程 | Data Processing Workflow

**Version**: 2.2.0  
**Last Updated**: 2026-03-19

---

## 📊 Overview

This document describes how tourist arrival data flows from the Macau DSEC API to the interactive dashboard.

---

## 🔄 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    Macau DSEC API                                │
│  https://dsec.apigateway.data.gov.mo                            │
│  /public/KeyIndicator/VisitorArrivals                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ POST request (weekly)
                              │ Headers: Authorization: APPCODE xxx
                              │ Payload: {from_year, to_year, lang}
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              GitHub Actions (fetch_data.py)                      │
│  1. Send API request                                             │
│  2. Receive JSON response                                        │
│  3. Parse nested JSON structure                                  │
│  4. Convert to standard format                                   │
│  5. Save to data/latest_data.json                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Git commit & push
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              GitHub Repository                                   │
│  data/                                                           │
│    ├── latest_data.json (raw API response)                      │
│    └── processed_data.json (converted format)                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ GitHub Pages auto-deploy
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Interactive Dashboard (index.html)                  │
│  1. Load data/latest_data.json via fetch API                    │
│  2. Parse JSON data                                              │
│  3. Extract labels and values                                    │
│  4. Render Chart.js charts                                       │
│  5. Display statistics                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ User views in browser
                              ▼
                    https://john-fb-agent.github.io/
                    macao-tourist-stats/
```

---

## 📡 Step 1: API Request

### Endpoint Details

| Property | Value |
|----------|-------|
| **URL** | `https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals` |
| **Method** | POST |
| **Auth** | `Authorization: APPCODE {appcode}` |
| **Content-Type** | `application/json` |

### Request Payload

```python
payload = {
    "from_year": 2008,
    "to_year": 2026,
    "lang": "zh-MO"
}
```

### Response Format

```json
{
  "requestId": "...",
  "success": true,
  "value": {
    "title": "入境旅客",
    "unit": "人次",
    "minYear": "2008",
    "maxYear": "2026",
    "periodType": "月度",
    "values": [
      {
        "value": "1900592",
        "periodString": "2008 年 1 月",
        "remarks": null
      }
    ]
  }
}
```

---

## 🐍 Step 2: Data Fetching (Python)

### Script: `scripts/fetch_data.py`

```python
def fetch_tourist_data():
    """Fetch tourist arrival data from Macau government API"""
    
    headers = {
        "Authorization": f"APPCODE {APPCODE}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    payload = {
        "from_year": 2008,
        "to_year": 2026,
        "lang": "zh-MO"
    }
    
    response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    data = response.json()
    
    # Save raw data
    with open("data/latest_data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return data
```

### Error Handling

- **Timeout**: 30 seconds
- **Invalid APPCODE**: Falls back to sample data
- **Network Error**: Logs error, continues with sample data
- **JSON Parse Error**: Logs error, continues with sample data

---

## 🔄 Step 3: Data Processing

### Script: `scripts/fetch_data.py` (process_data function)

```python
def process_data(data):
    """Convert API response to standard format"""
    
    if 'value' in data and 'values' in data['value']:
        api_data = data['value']
        raw_values = api_data.get('values', [])
        
        records = []
        for item in raw_values:
            period = item.get('periodString', '')  # "2008 年 1 月"
            value = item.get('value', '0')
            
            # Parse year-month
            year_month = period.replace('年', '-').replace('月', '')
            
            records.append({
                "periodString": period,
                "year_month": year_month,
                "value": int(value),
                "value_formatted": f"{int(value):,}"
            })
        
        # Save processed data
        processed_output = {
            "title": api_data.get('title'),
            "unit": api_data.get('unit'),
            "minYear": api_data.get('minYear'),
            "maxYear": api_data.get('maxYear'),
            "periodType": api_data.get('periodType'),
            "records": records,
            "count": len(records)
        }
        
        with open("data/processed_data.json", "w") as f:
            json.dump(processed_output, f, ensure_ascii=False, indent=2)
        
        return processed_output
```

---

## 📁 Step 4: Data Storage

### File Structure

```
data/
├── latest_data.json          # Raw API response
├── processed_data.json       # Converted format
└── statistics.json           # Calculated statistics
```

### latest_data.json

```json
{
  "requestId": "...",
  "success": true,
  "value": {
    "title": "入境旅客",
    "unit": "人次",
    "minYear": "2008",
    "maxYear": "2026",
    "values": [...]
  }
}
```

### processed_data.json

```json
{
  "title": "入境旅客",
  "unit": "人次",
  "minYear": "2008",
  "maxYear": "2026",
  "periodType": "月度",
  "records": [
    {
      "periodString": "2008 年 1 月",
      "year_month": "2008-01",
      "value": 1900592,
      "value_formatted": "1,900,592"
    }
  ],
  "count": 218
}
```

---

## 🌐 Step 5: Dashboard Rendering

### Script: `index.html` (JavaScript)

```javascript
async function loadData() {
    const response = await fetch('data/latest_data.json');
    const data = await response.json();
    
    // Parse nested structure
    const records = data.value.values;
    
    // Extract labels and values
    const labels = records.map(r => r.periodString);
    const values = records.map(r => parseInt(r.value));
    
    // Create Chart.js chart
    createLineChart(labels, values);
}
```

### Charts Generated

1. **Line Chart** - Monthly tourist arrivals trend
2. **Bar Chart** - Visitors by region comparison
3. **Area Chart** - Regional breakdown over time

---

## ⚙️ Step 6: Automation (GitHub Actions)

### Workflow: `.github/workflows/update-stats.yml`

```yaml
name: Update Macau Tourist Statistics

on:
  schedule:
    - cron: '0 0 * * 1'  # Every Monday 8:00 AM Macau time
  workflow_dispatch:      # Manual trigger

jobs:
  update-stats:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - run: pip install -r requirements.txt
      
      - name: Fetch tourist data
        env:
          MACAO_DATA_APPCODE: ${{ secrets.MACAO_DATA_APPCODE }}
        run: python scripts/fetch_data.py
      
      - name: Commit and push
        run: |
          git add data/
          git commit -m "📊 Update tourist statistics $(date +%Y-%m-%d)"
          git push
```

### Schedule

- **Frequency**: Weekly (every Monday)
- **Time**: 00:00 UTC (08:00 Asia/Shanghai)
- **Trigger**: Automatic + Manual

---

## 📊 Data Transformation Summary

| Stage | Format | Location |
|-------|--------|----------|
| **API Response** | Nested JSON (`value.values[]`) | API |
| **Raw Storage** | Same as API response | `data/latest_data.json` |
| **Processed** | Flattened records | `data/processed_data.json` |
| **Dashboard** | Chart.js datasets | Browser (client-side) |

---

## 🔐 Security Considerations

### API Key Management

| Environment | Storage Method |
|-------------|----------------|
| **Local Development** | `.env` file (git-ignored) |
| **GitHub Actions** | GitHub Secrets |
| **Production** | Environment variables |

### What's Protected

- ✅ `MACAO_DATA_APPCODE` stored in GitHub Secrets
- ✅ Not committed to git history
- ✅ Not logged in workflow output
- ✅ Only accessible to authorized workflows

### What's Public

- ✅ Processed data (no API keys)
- ✅ Charts and visualizations
- ✅ Historical statistics

---

## 🧪 Testing

### Local Testing

```bash
# Test data fetching
python scripts/fetch_data.py

# Test data processing
python -c "
import json
with open('data/latest_data.json') as f:
    data = json.load(f)
print(f'Records: {len(data[\"value\"][\"values\"])}')
"
```

### GitHub Actions Testing

1. Go to **Actions** tab
2. Click **Update Macau Tourist Statistics**
3. Click **Run workflow**
4. Check logs for errors
5. Verify data updated in repository

---

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| **API Response Time** | ~500ms - 2s |
| **Data Processing** | <100ms |
| **Total Workflow Time** | ~2-5 minutes |
| **Data Size** | ~50KB (JSON) |
| **Chart Load Time** | <1s (client-side) |

---

## 🛠️ Troubleshooting

### Issue: API returns HTML instead of JSON

**Cause**: Wrong endpoint or invalid APPCODE

**Solution**: 
- Use correct endpoint: `dsec.apigateway.data.gov.mo`
- Include `APPCODE ` prefix in Authorization header

### Issue: No data in charts

**Cause**: Data file not found or malformed JSON

**Solution**:
- Check `data/latest_data.json` exists
- Verify JSON is valid
- Check browser console for errors

### Issue: Workflow fails

**Cause**: Invalid APPCODE secret

**Solution**:
- Verify `MACAO_DATA_APPCODE` secret is set correctly
- Check workflow logs for error messages

---

<div align="center">

**Data processing workflow for Macau Tourist Statistics**

Last Updated: 2026-03-19 | Version: 2.2.0

</div>
