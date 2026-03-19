# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.2.0] - 2026-03-19

### ✨ Added
- **Real API integration** with Macau DSEC (Statistics and Census Service)
- **Historical data from 2008-2026** (actual government data, not simulated)
- Support for DSEC API Gateway endpoint

### 🔧 Changed
- **API Endpoint**: Changed from `data.gov.mo/api/resource` to `dsec.apigateway.data.gov.mo`
- **Request Method**: Changed from GET to POST
- **Auth Format**: Corrected to `APPCODE xxx` format
- **Data Format**: Parse nested JSON response from DSEC API
- **Data Coverage**: Extended from 15 months to 18+ years (2008-2026)

### 📊 Data Improvements
- Real monthly tourist arrivals data
- Official government statistics
- Automatic updates via GitHub Actions
- No more simulated/estimated data

### 🐛 Fixed
- APPCODE authorization format (now includes "APPCODE " prefix)
- API endpoint URL (now uses correct DSEC gateway)
- Response parsing for nested JSON structure

---

## [Unreleased]

### Planned
- Implement data export (PNG/PDF)
- Add multi-language support (EN/ZH/PT)
- Create automated tests (pytest)

---

## [2.1.0] - 2026-03-18

### ✨ Added
- **Yearly comparison page** (`yearly-comparison.html`)
- **Three chart types** on comparison page:
  1. **Multi-year monthly chart** (2019-2026) - one line per year
  2. **Long-term trend chart** (2002-2026) - yearly totals with area fill
  3. **Full monthly comparison** (2002-2026) - all years as separate lines
- **Current year highlight** (2026) with thicker line (4px vs 1.5-2px)
- **Historical data** from 2002-2018 (estimated from Macau tourism statistics)
- **Navigation** between main dashboard and yearly comparison
- **Hover tooltips** showing exact visitor counts
- **Color-coded legends** for each year
- **Interactive legend** - click to toggle year visibility
- **Smart defaults** - older years (2002-2014) hidden by default to reduce clutter

### 📊 Data Coverage
- 2002-2018: Historical estimates (based on Macau Government Tourism Office data)
- 2019-2023: Simulated trends
- 2024-2025: Sample data
- 2026: Year-to-date projections

### 🔧 Technical
- Extended historical data object (2002-2026)
- Added `createLongTermChart()` function
- Gradient fill for long-term trend chart
- Responsive chart containers (500px height)

---

## [2.0.0] - 2026-03-18

### ✨ Added
- Interactive HTML/JavaScript dashboard using Chart.js
- GitHub Pages hosting for live dashboard
- GitHub Actions workflow for weekly auto-updates
- Three chart types:
  - Line chart (tourist trend over time)
  - Bar chart (visitors by region)
  - Area chart (regional comparison)
- Statistics calculation and display
- Responsive design (mobile + desktop friendly)
- Bilingual labels (Chinese + English)

### 🔄 Changed
- **Breaking**: Replaced Python matplotlib chart generation with Chart.js
- **Breaking**: Removed `scripts/generate_charts.py`
- **Breaking**: Removed `charts/` folder with PNG files
- Simplified `requirements.txt` (removed matplotlib, pandas)
- Updated README with new dashboard instructions
- Created comprehensive design documentation

### 🗑️ Removed
- Python-based chart generation (`scripts/generate_charts.py`)
- Static PNG charts (`charts/tourist_arrivals_line.png`, etc.)
- matplotlib and pandas dependencies

### 📚 Documentation
- Created `docs/DESIGN.md` (system architecture)
- Created `docs/CHANGELOG.md` (this file)
- Updated `README.md` with Chart.js instructions
- Added `WORKFLOW-INSTRUCTIONS.md` for GitHub Actions setup
- Added `SETUP-COMPLETE.md` for final setup steps

### 🔧 Technical
- Enabled GitHub Pages at root directory
- Added `MACAO_DATA_APPCODE` to GitHub Secrets
- Implemented fallback to sample data if API unavailable
- Added error handling for API failures

---

## [1.0.0] - 2026-03-18

### ✨ Added
- Initial release
- Python script to fetch data from data.gov.mo API
- Matplotlib-based chart generation:
  - Line chart (PNG)
  - Regional comparison chart (PNG)
- Sample data for 15 months (42.3M total visitors)
- GitHub repository structure
- MIT License
- `.gitignore` configuration
- Basic `README.md` with setup instructions

### 🔧 Technical
- Python 3.11 environment
- Dependencies: requests, matplotlib, pandas
- GitHub Actions workflow for weekly updates
- API authentication via APPCODE

---

## Version History Summary

| Version | Date | Key Changes |
|---------|------|-------------|
| 2.0.0 | 2026-03-18 | Interactive Chart.js dashboard, GitHub Pages |
| 1.0.0 | 2026-03-18 | Initial release with Python charts |

---

## Migration Guide: v1.0.0 → v2.0.0

### Breaking Changes

1. **Chart Generation**: No longer generates PNG files
   - **Old**: `charts/tourist_arrivals_line.png`
   - **New**: `index.html` (interactive dashboard)

2. **Dependencies**: Removed matplotlib and pandas
   ```bash
   # Old requirements.txt
   requests>=2.31.0
   matplotlib>=3.8.0
   pandas>=2.1.0
   
   # New requirements.txt
   requests>=2.31.0
   ```

3. **Viewing Results**: 
   - **Old**: Open PNG files in image viewer
   - **New**: Open `index.html` in browser or visit GitHub Pages URL

### Non-Breaking

- Data fetching script (`scripts/fetch_data.py`) remains compatible
- API endpoint and authentication unchanged
- GitHub Actions workflow structure similar

---

## Future Versions

### [2.1.0] - Planned
- Add year-over-year comparison
- Export charts as PNG/PDF
- Multi-language support

### [3.0.0] - Under Consideration
- Real-time data updates
- Additional data sources (hotel, casino)
- User authentication for advanced features

---

<div align="center">

**Keep this changelog up to date with every release!** 📝

</div>
