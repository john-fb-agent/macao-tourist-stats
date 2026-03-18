# 系統設計 | System Design

**Version**: 2.0.0  
**Last Updated**: 2026-03-18  
**Project**: Macau Tourist Statistics

---

## 📋 概述 | Overview

本專案自動從澳門政府數據開放平台 (data.gov.mo) 獲取入境旅客統計數據，並生成交互式可視化儀表板。

This project automatically fetches tourist arrival statistics from Macau Government Data Platform and generates an interactive visualization dashboard.

---

## 🏗️ 系統架構 | System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    GitHub Repository                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐ │
│  │   scripts/  │  │   data/     │  │   index.html    │ │
│  │ fetch_data.py│  │latest_data.json│  │  (Dashboard)  │ │
│  └─────────────┘  └─────────────┘  └─────────────────┘ │
│         │                │                    │         │
│         ▼                ▼                    │         │
│  ┌─────────────────────────────────────────────┘         │
│  │                                                        │
└──┼────────────────────────────────────────────────────────┘
   │
   │ GitHub Actions (Weekly)
   ▼
┌─────────────────────────────────────────────────────────┐
│              External Services                           │
│  ┌──────────────────┐  ┌─────────────────────────────┐ │
│  │  data.gov.mo API │  │  GitHub Pages (Hosting)     │ │
│  │  (Tourist Data)  │  │  john-fb-agent.github.io    │ │
│  └──────────────────┘  └─────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 數據流 | Data Flow

```
1. GitHub Actions Trigger (Every Monday 8:00 AM)
         │
         ▼
2. Checkout Repository
         │
         ▼
3. Install Python Dependencies
         │
         ▼
4. Fetch Data from data.gov.mo API
         │
         ▼
5. Save to data/latest_data.json
         │
         ▼
6. Commit & Push (if data changed)
         │
         ▼
7. GitHub Pages Auto-Deploy
         │
         ▼
8. Dashboard Shows Latest Data
```

---

## 🔧 組件說明 | Components

### 1. 數據獲取腳本 | Data Fetcher (`scripts/fetch_data.py`)

**Purpose**: Fetch tourist data from Macau government API

**Input**: 
- API endpoint: `https://data.gov.mo/api/resource/3546225a-2a34-4645-b01e-6752aed03993`
- Authentication: `APPCODE` (stored in GitHub Secrets)

**Output**:
- `data/latest_data.json` - Raw API response
- `data/statistics.json` - Calculated statistics

**Error Handling**:
- API unavailable → Generate sample data
- Invalid response → Log error, exit with code 1

---

### 2. 交互式儀表板 | Interactive Dashboard (`index.html`)

**Purpose**: Display tourist statistics with interactive charts

**Technology**: 
- Chart.js 4.4.0 - Chart rendering
- Vanilla JavaScript - Data processing
- Responsive CSS - Mobile-friendly design

**Charts**:
1. **Line Chart** - Tourist arrivals trend over time
2. **Bar Chart** - Visitors by region comparison
3. **Area Chart** - Regional breakdown over time

**Data Source**: `data/latest_data.json` (loaded via fetch API)

---

### 3. GitHub Actions Workflow | 自動化工作流

**File**: `.github/workflows/update-stats.yml`

**Triggers**:
- Schedule: Every Monday 00:00 UTC (08:00 Asia/Shanghai)
- Manual: `workflow_dispatch` event

**Steps**:
1. Checkout repository
2. Setup Python 3.11
3. Install dependencies
4. Fetch tourist data (with API secret)
5. Commit and push if data changed

**Permissions**: `contents: write` (for auto-commit)

---

## 🔐 安全性 | Security

### Credentials Management

| Secret | Storage | Usage |
|--------|---------|-------|
| `MACAO_DATA_APPCODE` | GitHub Secrets | API authentication |

### Sensitive Files (Git-Ignored)

```gitignore
# Environment files
.env
.env.local

# Python
__pycache__/
*.pyc

# OS
.DS_Store
```

### API Security

- ✅ API key stored in GitHub Secrets (not in code)
- ✅ HTTPS for all API calls
- ✅ No credentials logged
- ✅ Rate limiting respected

---

## 📁 目錄結構 | Directory Structure

```
macao-tourist-stats/
├── .github/
│   └── workflows/
│       └── update-stats.yml      # GitHub Actions workflow
├── scripts/
│   └── fetch_data.py             # Data fetching script
├── data/
│   ├── latest_data.json          # Latest API response
│   └── statistics.json           # Calculated stats
├── docs/
│   ├── DESIGN.md                 # This file
│   └── CHANGELOG.md              # Version history
├── index.html                    # Interactive dashboard
├── README.md                     # Project overview
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore rules
└── LICENSE                       # MIT License
```

---

## 🔄 更新流程 | Update Process

### Weekly Auto-Update

1. **Trigger**: Monday 8:00 AM (Macau time)
2. **Fetch**: Latest data from data.gov.mo
3. **Compare**: Check if data changed
4. **Commit**: Save new data (if changed)
5. **Deploy**: GitHub Pages auto-updates

### Manual Update

1. Go to Actions tab
2. Click "Run workflow"
3. Wait for completion

---

## 📊 數據結構 | Data Structure

### API Response Format

```json
{
  "result": [
    {
      "月份": "2024-01",
      "Month": "2024-01",
      "總訪客數": 2500000,
      "Total Visitors": 2500000,
      "中國內地": 1750000,
      "Mainland China": 1750000,
      "香港": 375000,
      "Hong Kong": 375000,
      "台灣": 200000,
      "Taiwan": 200000,
      "其他": 175000,
      "Other": 175000
    }
  ],
  "count": 15
}
```

### Statistics Format

```json
{
  "總訪客數": {
    "total": 42278436,
    "mean": 2818562,
    "min": 2082547,
    "max": 3469499,
    "records": 15
  }
}
```

---

## 🧪 測試 | Testing

### Local Testing

```bash
# Test data fetching
python scripts/fetch_data.py

# View dashboard locally
open index.html  # macOS
xdg-open index.html  # Linux
```

### GitHub Actions Testing

1. Trigger workflow manually
2. Check workflow logs
3. Verify data updated
4. Check dashboard reflects changes

---

## 📈 效能考量 | Performance Considerations

| Aspect | Strategy |
|--------|----------|
| **API Calls** | Once per week (scheduled) |
| **Data Size** | ~5KB JSON (minimal) |
| **Dashboard Load** | Client-side rendering (fast) |
| **Chart.js** | CDN-hosted (cached) |
| **GitHub Pages** | Global CDN (fast worldwide) |

---

## 🔮 未來擴展 | Future Enhancements

### Potential Features

- [ ] Add more data sources (hotel occupancy, casino revenue)
- [ ] Historical data comparison (year-over-year)
- [ ] Export charts as PNG/PDF
- [ ] Multi-language support (EN/ZH/PT)
- [ ] Real-time data updates (if API supports)

### Technical Improvements

- [ ] Add automated testing (pytest)
- [ ] Implement data caching
- [ ] Add error notifications (email/Discord)
- [ ] Create API documentation (docs/API.md)
- [ ] Add user guide (docs/USER_GUIDE.md)

---

## 📚 參考文檔 | References

| Document | URL |
|----------|-----|
| data.gov.mo API | https://data.gov.mo |
| Chart.js Documentation | https://www.chartjs.org/ |
| GitHub Actions Docs | https://docs.github.com/actions |
| GitHub Pages | https://pages.github.com/ |

---

## 📝 決策記錄 | Decision Records

### Decision: Use Chart.js Instead of Server-Side Image Generation

**Date**: 2026-03-18  
**Status**: Accepted

**Context**: Initial version used Python matplotlib to generate PNG charts.

**Decision**: Switch to client-side Chart.js for interactive charts.

**Consequences**:
- ✅ No server-side image generation needed
- ✅ Interactive charts (hover, zoom)
- ✅ Faster page load (CDN-hosted)
- ✅ Easier to maintain (no matplotlib dependencies)
- ⚠️ Requires JavaScript enabled in browser

---

### Decision: Use GitHub Actions for Automation

**Date**: 2026-03-18  
**Status**: Accepted

**Context**: Need weekly auto-update of tourist data.

**Decision**: Use GitHub Actions instead of external cron service.

**Consequences**:
- ✅ Free (no hosting cost)
- ✅ Integrated with repository
- ✅ Secure (GitHub Secrets for API keys)
- ✅ Easy to monitor (Actions tab)
- ⚠️ Limited to 2000 minutes/month (sufficient for weekly runs)

---

<div align="center">

**Design is a living document. Update as the system evolves.** 📚

</div>
