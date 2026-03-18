# 🇲🇴 Macau Tourist Statistics

自動獲取澳門旅客數據並生成統計圖表 | Automatic Macau Tourist Data Fetcher with Interactive Charts

[![Update Statistics](https://github.com/john-fb-agent/macao-tourist-stats/actions/workflows/update-stats.yml/badge.svg)](https://github.com/john-fb-agent/macao-tourist-stats/actions/workflows/update-stats.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![View Dashboard](https://img.shields.io/badge/view-dashboard-blue)](https://john-fb-agent.github.io/macao-tourist-stats/)

---

## 📋 項目簡介 | Project Overview

本項目自動從澳門政府數據開放平台 (data.gov.mo) 獲取旅客人數統計數據，並生成**交互式可視化圖表**（HTML + JavaScript）。

This project automatically fetches tourist arrival statistics from Macau Government Data Platform (data.gov.mo) and generates **interactive visualization charts** (HTML + JavaScript).

### ✨ 功能特點 | Features

- 🔄 **自動更新** - GitHub Actions 每週一自動獲取最新數據
- 📊 **交互式圖表** - 使用 Chart.js 生成可交互的 HTML 圖表
- 📈 **數據分析** - 自動計算總數、平均值、最高/最低值
- 🇲🇴 **官方數據** - 直接來自澳門政府數據開放平台
- 🌐 **GitHub Pages** - 可直接在瀏覽器查看儀表板

---

## 📊 數據來源 | Data Source

**澳門政府數據開放平台** | Macau Government Data Platform

- **網站**: https://data.gov.mo
- **數據集**: 入境旅客統計 | Tourist Arrival Statistics
- **數據集 ID**: `3546225a-2a34-4645-b01e-6752aed03993`
- **API 文檔**: https://data.gov.mo/api/resource/{dataset_id}

---

## 📁 目錄結構 | Directory Structure

```
macao-tourist-stats/
├── .github/
│   └── workflows/
│       └── update-stats.yml      # GitHub Actions 自動化腳本
├── scripts/
│   └── fetch_data.py             # 數據獲取腳本
├── data/
│   ├── latest_data.json          # 最新原始數據
│   └── statistics.json           # 統計摘要
├── index.html                    # 📊 交互式儀表板 (Interactive Dashboard)
├── requirements.txt              # Python 依賴
├── README.md                     # 本文件
└── WORKFLOW-INSTRUCTIONS.md      # GitHub Actions 設置指南
```

---

## 🚀 快速開始 | Quick Start

### 1. 克隆倉庫 | Clone Repository

```bash
git clone https://github.com/john-fb-agent/macao-tourist-stats.git
cd macao-tourist-stats
```

### 2. 安裝依賴 | Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. 配置 API 認證 | Configure API Authentication

**方法 1: 環境變數** | Method 1: Environment Variable

```bash
export MACAO_DATA_APPCODE="your-appcode-here"
```

**方法 2: 直接修改腳本** | Method 2: Modify Script Directly

編輯 `scripts/fetch_data.py`，將 `APPCODE` 改為你的值。

### 4. 運行腳本 | Run Scripts

```bash
# 獲取數據
python scripts/fetch_data.py

# 在瀏覽器打開儀表板
# Mac/Linux:
open index.html  # macOS
xdg-open index.html  # Linux

# Windows:
start index.html
```

---

## 📊 交互式儀表板 | Interactive Dashboard

### 圖表類型 | Chart Types

1. **📈 旅客趨勢圖** | Tourist Arrivals Trend Line Chart
   - 顯示每月總旅客人數變化
   - 可交互查看具體數值

2. **📊 區域分佈圖** | Visitors by Region Bar Chart
   - 對比不同地區旅客總數
   - 中國內地、香港、台灣、其他

3. **🌏 區域對比圖** | Regional Comparison Over Time
   - 堆疊面積圖顯示各地區趨勢
   - 可比較不同時期各地區表現

### 查看儀表板 | View Dashboard

**本地查看** | Local:
```bash
open index.html
```

**GitHub Pages** (啟用後):
```
https://john-fb-agent.github.io/macao-tourist-stats/
```

---

## ⚙️ GitHub Actions 自動化 | Automation

### 觸發條件 | Triggers

- **定時**: 每週一 00:00 UTC (週一 08:00 北京/澳門時間)
- **手動**: 在 Actions 頁面點擊 "Run workflow"

### 配置 Secrets | Configure Secrets

在 GitHub 倉庫設置中添加：

1. 進入 **Settings** → **Secrets and variables** → **Actions**
2. 點擊 **New repository secret**
3. 添加：
   - Name: `MACAO_DATA_APPCODE`
   - Value: 你的 data.gov.mo APPCODE

### 工作流程 | Workflow

```yaml
name: Update Macau Tourist Statistics

on:
  schedule:
    - cron: '0 0 * * 1'  # 每週一
  workflow_dispatch:      # 手動觸發
```

---

## 📈 統計指標 | Statistics Metrics

儀表板顯示的統計數據：

| 指標 | 說明 |
|------|------|
| Total | 總旅客人數 |
| Average | 平均每月旅客人數 |
| Maximum | 最高單月旅客人數 |
| Minimum | 最低單月旅客人數 |
| Records | 數據記錄數（月數） |

---

## 🔧 本地開發 | Local Development

### 測試數據獲取 | Test Data Fetch

```bash
python scripts/fetch_data.py
```

### 查看數據 | View Data

```bash
cat data/latest_data.json | jq
cat data/statistics.json | jq
```

### 本地預覽儀表板 | Preview Dashboard

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html

# 或使用 Python 簡單 HTTP 服務器
python -m http.server 8000
# 然後訪問 http://localhost:8000
```

---

## 🌐 啟用 GitHub Pages | Enable GitHub Pages

1. 進入 **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: Select `main` → `/ (root)`
4. Click **Save**
5. 等待幾分鐘，訪問: `https://john-fb-agent.github.io/macao-tourist-stats/`

---

## 📝 API 使用示例 | API Usage Examples

### Python

```python
import requests

headers = {
    "Authorization": "APPCODE YOUR_APPCODE"
}

url = "https://data.gov.mo/api/resource/3546225a-2a34-4645-b01e-6752aed03993"

response = requests.get(url, headers=headers)
data = response.json()

print(data)
```

### cURL

```bash
curl -H "Authorization: APPCODE YOUR_APPCODE" \
  "https://data.gov.mo/api/resource/3546225a-2a34-4645-b01e-6752aed03993"
```

---

## 🗓️ 更新歷史 | Update History

| 日期 | 更新內容 |
|------|----------|
| 2026-03-18 | v2.0 - 改用 HTML + JavaScript 交互式圖表 |
| 2026-03-18 | v1.0 - 初始版本 - 數據獲取 + Python 生成圖表 |

---

## 📄 許可證 | License

MIT License - 詳見 [LICENSE](LICENSE) 文件

---

## 🤝 貢獻 | Contributing

歡迎提交 Issue 和 Pull Request！

1. Fork 本倉庫
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

---

## 📧 聯絡方式 | Contact

- **GitHub**: [@john-fb-agent](https://github.com/john-fb-agent)
- **Data Source**: [data.gov.mo](https://data.gov.mo)

---

## 🔗 相關連結 | Related Links

- [澳門政府數據開放平台](https://data.gov.mo)
- [澳門統計暨普查局](https://www.dsec.gov.mo)
- [澳門旅遊局](https://www.macaotourism.gov.mo)
- [Chart.js 文檔](https://www.chartjs.org/)

---

<div align="center">

**Made with ❤️ for Macau Data Analysis**

⭐ 如果對你有幫助，請給個 Star！

📊 [View Live Dashboard](https://john-fb-agent.github.io/macao-tourist-stats/)

</div>
