# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Add data export feature (PNG/PDF)
- Add multi-language support (EN/ZH/PT)
- Add automated testing

---

## [1.5.0] - 2026-03-19

### ✨ Added
- **Recent Years Comparison Chart** (2019-2026) on monthly-trend.html
- Shows last 8 years for easier recent trend comparison
- Current year (2026) highlighted in bold red

### 📊 Chart Structure
- Chart 1: All Monthly Data (2008-2026)
- Chart 2: **Recent Years (2019-2026)** ← NEW
- Chart 3: All Years Comparison (2008-2026)

---

## [1.4.0] - 2026-03-19

### 🔧 Changed
- Removed debug box from monthly-trend.html
- Cleaned up all debug logging
- Production-ready UI

---

## [1.3.0] - 2026-03-19

### ✨ Added
- **Current year (2026) highlighting**
  - Bright red color (#ff4757)
  - 6px bold line (vs 2px normal)
  - 8px points (vs 3px normal)
  - 🔴 Emoji in legend
  - Drawn on top of other lines

### 🎨 Color Scheme
- 2026: 🔴 Red (current year)
- 2024-2025: Teal
- 2020-2023: Purple
- 2008-2019: Gray

---

## [1.2.0] - 2026-03-19

### 🐛 Fixed
- **Fixed data parsing issue**
  - Changed from regex to manual string parsing
  - Correctly parses "2008 年 1 月" format (no space)
  - All 217 records now display correctly

### 🔍 Added
- Version number display in debug box
- Better error messages for parsing failures

---

## [1.1.0] - 2026-03-19

### ✨ Added
- **monthly-trend.html** - Monthly trend page
  - Chart 1: All monthly data (2008-2026)
  - Chart 2: Year-by-year comparison (one line per year)
  - Current year shown with bold line
- Navigation links between pages

### 📊 Features
- Interactive Chart.js charts
- Hover tooltips with exact values
- Responsive design
- Legend with year toggles

---

## [1.0.0] - 2026-03-19

### ✨ Added
- **Real API integration** with Macau DSEC
  - Endpoint: `https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals`
  - Data range: 2008-2026 (217 monthly records)
  - Authentication: APPCODE

- **index.html** - Homepage with yearly trend
  - Yearly bar chart
  - Statistics cards (Total, Peak Year, Lowest Year)

- **yearly-trend.html** - Yearly trend analysis
  - Yearly bar chart with gradient colors
  - Year-over-Year growth rate chart
  - Green = positive growth, Red = negative growth

- **data/data.json** - Real API data
  - 217 monthly records
  - ~500M total visitors (2008-2026)

- **Documentation**
  - docs/API.md - Complete API documentation
  - docs/DATA_WORKFLOW.md - Data processing workflow
  - docs/DESIGN.md - System architecture
  - docs/CHANGELOG.md - Version history

### 🔧 Technical
- Chart.js 4.4.0 for visualization
- GitHub Pages hosting
- Responsive design (mobile + desktop)
- Clean, minimal codebase

---

## Version History Summary

| Version | Date | Key Changes |
|---------|------|-------------|
| 1.5.0 | 2026-03-19 | Added Recent Years (2019-2026) chart |
| 1.4.0 | 2026-03-19 | Removed debug box |
| 1.3.0 | 2026-03-19 | Current year highlighting (red, bold) |
| 1.2.0 | 2026-03-19 | Fixed data parsing (regex → manual) |
| 1.1.0 | 2026-03-19 | Added monthly-trend.html |
| 1.0.0 | 2026-03-19 | Initial release with real DSEC API data |

---

## Migration Guide

### From v1.0 to v1.5

No breaking changes. All updates are additive:

- v1.1.0: Added monthly-trend.html
- v1.2.0: Fixed data parsing (transparent fix)
- v1.3.0: Enhanced current year styling
- v1.4.0: Removed debug box (UI cleanup)
- v1.5.0: Added Recent Years chart

All existing pages remain functional.

---

## Future Versions

### [2.0.0] - Under Consideration
- Add data export (PNG/PDF)
- Add multi-language support
- Add automated data updates
- Add more chart types (area, pie)

---

<div align="center">

**Keep this changelog up to date with every release!** 📝

**Latest Version**: v1.5 | **Last Updated**: 2026-03-19

</div>
