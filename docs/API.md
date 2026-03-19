# API Documentation

**Source**: 澳門統計暨普查局 (DSEC - Statistics and Census Service)  
**Platform**: Macau Government Data Open Platform (data.gov.mo)

---

## 📡 API Endpoint

| Property | Value |
|----------|-------|
| **URL** | `https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals` |
| **Method** | POST |
| **Content-Type** | `application/json` |
| **Authorization** | `APPCODE {your-appcode}` |

---

## 🔐 Authentication

### Request Header

```http
Authorization: APPCODE 09d43a591fba407fb862412970667de4
Content-Type: application/json
Accept: application/json
```

**Important**: The prefix `APPCODE ` (with space) is **required**.

---

## 📤 Request Parameters

### Request Body (JSON)

```json
{
  "from_year": 2008,
  "to_year": 2026,
  "lang": "zh-MO"
}
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `from_year` | INT | No | - | Starting year (min: 2008) |
| `to_year` | INT | No | - | Ending year (max: current year) |
| `lang` | STRING | No | `zh-MO` | Language: `zh-MO`, `zh-CN`, `pt-PT`, `en-US` |

---

## 📥 Response Format

### Success Response (200 OK)

```json
{
  "requestId": "28af8048-e21e-4897-b391-a720517e1677",
  "success": true,
  "errorType": null,
  "errorMessage": null,
  "value": {
    "title": "入境旅客",
    "unit": "人次",
    "minYear": "2008",
    "maxYear": "2026",
    "periodType": "月度",
    "indicatorRemarks": null,
    "values": [
      {
        "value": "1900592",
        "periodString": "2008 年 1 月",
        "remarks": null
      },
      {
        "value": "2000243",
        "periodString": "2008 年 2 月",
        "remarks": null
      }
      // ... more records
    ]
  },
  "responseTime": "2026-03-19T08:53:00"
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `requestId` | STRING | Unique request identifier |
| `success` | BOOLEAN | Request success status |
| `errorType` | INT | Error type code (null if success) |
| `errorMessage` | STRING | Error message (null if success) |
| `value.title` | STRING | Dataset title (e.g., "入境旅客") |
| `value.unit` | STRING | Data unit (e.g., "人次") |
| `value.minYear` | STRING | Minimum available year |
| `value.maxYear` | STRING | Maximum available year |
| `value.periodType` | STRING | Data period type (e.g., "月度") |
| `value.values[]` | ARRAY | Array of data records |
| `value.values[].value` | STRING | Visitor count |
| `value.values[].periodString` | STRING | Period in format "YYYY 年 M 月" |
| `value.values[].remarks` | STRING | Additional notes (null if none) |

---

## ❌ Error Responses

### System Error

```json
{
  "requestId": "166e0df5-a939-4ee8-aa4c-5ce76973a2d3",
  "success": false,
  "errorType": 1,
  "errorMessage": "System error!",
  "value": null,
  "responseTime": "2026-03-19T10:27:12"
}
```

### Invalid APPCODE

```json
{
  "requestId": "...",
  "success": false,
  "errorType": 2,
  "errorMessage": "Invalid authentication",
  "value": null
}
```

---

## 💡 Usage Examples

### cURL

```bash
curl -X POST \
  -H "Authorization: APPCODE 09d43a591fba407fb862412970667de4" \
  -H "Content-Type: application/json" \
  -d '{"from_year":2008,"to_year":2026,"lang":"zh-MO"}' \
  "https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals"
```

### Python

```python
import requests
import json

url = "https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals"

headers = {
    "Authorization": "APPCODE 09d43a591fba407fb862412970667de4",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "from_year": 2008,
    "to_year": 2026,
    "lang": "zh-MO"
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()

if data.get('success'):
    values = data['value']['values']
    print(f"Total records: {len(values)}")
    for item in values[:5]:  # Print first 5 records
        print(f"{item['periodString']}: {item['value']} visitors")
```

### JavaScript (Node.js)

```javascript
const axios = require('axios');

const url = "https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals";

const config = {
  headers: {
    'Authorization': 'APPCODE 09d43a591fba407fb862412970667de4',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
};

const payload = {
  from_year: 2008,
  to_year: 2026,
  lang: 'zh-MO'
};

axios.post(url, payload, config)
  .then(response => {
    if (response.data.success) {
      const values = response.data.value.values;
      console.log(`Total records: ${values.length}`);
      values.slice(0, 5).forEach(item => {
        console.log(`${item.periodString}: ${item.value} visitors`);
      });
    }
  })
  .catch(error => {
    console.error('API Error:', error.response.data);
  });
```

---

## 📊 Data Coverage

| Year Range | Data Availability | Notes |
|------------|-------------------|-------|
| 2008-2019 | ✅ Complete | Pre-pandemic data |
| 2020-2021 | ✅ Complete | Pandemic impact period |
| 2022-2023 | ✅ Complete | Recovery period |
| 2024 | ✅ Complete | Latest full year |
| 2025 | ✅ Partial | Year-to-date |
| 2026 | ✅ Partial | Current year (updates monthly) |

---

## 🔗 Related Resources

| Resource | URL |
|----------|-----|
| **DSEC Website** | https://www.dsec.gov.mo |
| **Data.gov.mo** | https://data.gov.mo |
| **Dataset Page** | https://data.gov.mo/Detail?id=3546225a-2a34-4645-b01e-6752aed03993 |
| **API Gateway** | https://dsec.apigateway.data.gov.mo |

---

## 📝 Notes

1. **Rate Limiting**: Be respectful of API rate limits. This project fetches data once per week.

2. **Data Updates**: New monthly data is typically published within 2-3 weeks after month-end.

3. **APPCODE Validity**: The APPCODE may expire. If you receive authentication errors, register at data.gov.mo to get a new one.

4. **Language Support**:
   - `zh-MO`: Traditional Chinese (Macau)
   - `zh-CN`: Simplified Chinese
   - `pt-PT`: Portuguese
   - `en-US`: English

5. **Historical Data**: Data prior to 2008 is not available through this API endpoint.

---

## 🛠️ Troubleshooting

### Issue: "Invalid authentication"

**Solution**: Ensure the Authorization header includes the `APPCODE ` prefix (with space).

```
✅ Correct: APPCODE 09d43a591fba407fb862412970667de4
❌ Wrong: 09d43a591fba407fb862412970667de4
❌ Wrong: Token 09d43a591fba407fb862412970667de4
```

### Issue: "No data available"

**Solution**: Check that `from_year` and `to_year` are within the valid range (2008-current year).

### Issue: HTML response instead of JSON

**Solution**: Ensure you're using the correct endpoint (`dsec.apigateway.data.gov.mo`) and not the old endpoint.

---

<div align="center">

**API documentation for Macau Tourist Statistics Project**

Last Updated: 2026-03-19 | Version: 2.2.0

</div>
