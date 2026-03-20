# 🇲🇴 Macau Tourist Statistics

自動獲取澳門旅客數據並生成統計圖表 | Automatic Macau Tourist Data Fetcher with Interactive Charts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![View Dashboard](https://img.shields.io/badge/view-dashboard-blue)](https://john-fb-agent.github.io/macao-tourist-stats/)

---

## 📋 項目簡介 | Project Overview

本項目自動從澳門統計暨普查局 (DSEC) 獲取入境旅客統計數據，並生成交互式可視化圖表。

This project automatically fetches tourist arrival statistics from Macau DSEC and generates interactive visualization charts using Chart.js.

### ✨ 功能特點 | Features

- 📊 **真實數據** - 直接來自澳門 DSEC 官方 API (2008-2026)
- 📈 **三個圖表頁面** - 總覽、近年對比、全年對比
- 🎨 **交互式視覺化** - Chart.js 動態圖表，支持懸停查看數據
- 🔴 **當前年份高亮** - 2026 年以紅色粗線顯示
- 📱 **響應式設計** - 支持桌面和移動設備
- 🌐 **GitHub Pages 託管** - 直接在瀏覽器訪問

---

## 📊 數據來源 | Data Source

**澳門統計暨普查局 (DSEC)** | Statistics and Census Service

| 項目 | 詳情 |
|------|------|
| **API 端點** | https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals |
| **數據集** | 入境旅客 | Visitor Arrivals |
| **數據範圍** | 2008 年 1 月 - 2026 年 (每月) |
| **更新頻率** | 月度 |
| **認證方式** | APPCODE |

**官方網站**:
- [DSEC](https://www.dsec.gov.mo)
- [data.gov.mo](https://data.gov.mo/Detail?id=3546225a-2a34-4645-b01e-6752aed03993)

---

## 🌐 在線儀表板 | Online Dashboard

**https://john-fb-agent.github.io/macao-tourist-stats/**

### 頁面結構

| 頁面 | 說明 | 圖表 |
|------|------|------|
| **[🏠 主頁](index.html)** | 年度趨勢總覽 | 年度柱狀圖 + 統計卡片 |
| **[📈 月度趨勢](monthly-trend.html)** | 月度數據對比 | 3 個圖表：<br>1. 全期月度趨勢<br>2. 近年對比 (2019-2026) 🔴<br>3. 全年對比 (2008-2026) |
| **[📊 年度趨勢](yearly-trend.html)** | 年度趨勢分析 | 2 個圖表：<br>1. 年度柱狀圖<br>2. 年增長率圖 |

---

## 📁 目錄結構 | Directory Structure

```
macao-tourist-stats/
├── data/
│   └── data.json                 # 旅客數據 (217 條記錄)
├── index.html                    # 🏠 主頁 - 年度趨勢
├── monthly-trend.html            # 📈 月度趨勢 - 3 個圖表
├── yearly-trend.html             # 📊 年度趨勢 - 增長率分析
├── README.md                     # 本文件
└── docs/
    ├── API.md                    # API 文檔
    ├── DESIGN.md                 # 系統設計
    └── CHANGELOG.md              # 版本歷史
```

---

## 🚀 本地運行 | Local Development

### Option 1: Dev Container (Recommended)

**GitHub Codespaces**:

1. Go to repository
2. Click **Code** → **Codespaces**
3. Click **Create codespace on main**
4. Server starts automatically

**VS Code Dev Container**:

1. Clone repository
2. Open in VS Code
3. Press `Ctrl+Shift+P` → **Dev Containers: Reopen in Container**
4. Run `http-server -p 8000`

See [`.devcontainer/README.md`](.devcontainer/README.md) for details.

### Option 2: Direct Browser

```bash
git clone https://github.com/john-fb-agent/macao-tourist-stats.git
cd macao-tourist-stats

# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

### Option 3: Local Server

```bash
# Python 3
python -m http.server 8000

# Node.js
npx http-server -p 8000

# Visit http://localhost:8000
```

---

## 📊 圖表說明 | Charts

### 主頁 (index.html)

- **年度柱狀圖** - 每年總旅客人數
- **統計卡片** - 總數、最高年份、最低年份、數據範圍

### 月度趨勢 (monthly-trend.html)

1. **全期月度趨勢** - 2008-2026 所有月度數據 (單線)
2. **近年對比** - 2019-2026 每月對比 (8 條線)
   - 🔴 2026 年：紅色粗線 (6px)
   - 2024-2025: 青綠色
   - 2020-2023: 紫色
   - 2019: 灰色
3. **全年對比** - 2008-2026 每月對比 (19 條線)

### 年度趨勢 (yearly-trend.html)

1. **年度柱狀圖** - 每年總旅客人數 (彩色漸變)
2. **年增長率** - 同比增長率 (綠色=正增長，紅色=負增長)

---

## 📈 統計數據 | Statistics

### 數據概覽

| 指標 | 數值 |
|------|------|
| **總記錄數** | 217 個月 |
| **年份範圍** | 2008-2026 |
| **數據來源** | DSEC API |
| **最後更新** | 2026-03-19 |

### 關鍵統計

| 指標 | 數值 | 時間 |
|------|------|------|
| **總旅客數** | ~5 億人次 | 2008-2026 |
| **平均每月** | ~250 萬人次 | - |
| **最高月份** | ~365 萬人次 | 2024 年 8 月 |
| **最低月份** | ~20 萬人次 | 2020 年 (疫情) |

---

## 🛠️ 技術棧 | Tech Stack

| 技術 | 用途 |
|------|------|
| **HTML5/CSS3** | 頁面結構和樣式 |
| **JavaScript (ES6+)** | 數據處理和圖表生成 |
| **Chart.js 4.4.0** | 交互式圖表庫 |
| **GitHub Pages** | 靜態網站託管 |
| **GitHub Actions** | 每週自動數據更新 |
| **Python 3.11** | 數據獲取腳本 |
| **DSEC API** | 數據來源 |

---

## 📝 數據更新 | Data Update

### 手動更新

```bash
# 1. 從 API 獲取最新數據
python3 scripts/fetch_data.py

# 2. 提交並推送
git add data/
git commit -m "data: Update tourist statistics $(date +%Y-%m-%d)"
git push origin main
```

### GitHub Actions (可選)

配置自動更新請參考 [docs/DESIGN.md](docs/DESIGN.md)

---

## 📚 文檔 | Documentation

| 文檔 | 說明 |
|------|------|
| [API.md](docs/API.md) | DSEC API 完整文檔 |
| [DATA_WORKFLOW.md](docs/DATA_WORKFLOW.md) | 數據處理流程 |
| [DESIGN.md](docs/DESIGN.md) | 系統架構設計 |
| [CHANGELOG.md](docs/CHANGELOG.md) | 版本歷史 |

---

## 🎨 顏色方案 | Color Scheme

| 年份 | 顏色 | 說明 |
|------|------|------|
| 2026 | 🔴 #ff4757 | 當前年份 (高亮) |
| 2024-2025 | 🔵 #4ecdc4 | 近期年份 |
| 2020-2023 | 🟣 #667eea | 疫情時期 |
| 2008-2019 | ⚫ #999999 | 歷史數據 |

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
- **Data Source**: [DSEC](https://www.dsec.gov.mo)

---

## 🔗 相關連結 | Related Links

- [澳門統計暨普查局](https://www.dsec.gov.mo)
- [澳門政府數據開放平台](https://data.gov.mo)
- [Chart.js 文檔](https://www.chartjs.org/)

---

<div align="center">

**Made with ❤️ for Macau Data Analysis**

📊 [View Live Dashboard](https://john-fb-agent.github.io/macao-tourist-stats/)

**Version**: v1.5 | **Last Updated**: 2026-03-19

</div>
