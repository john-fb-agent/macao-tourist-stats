# GitHub Actions Workflow for Macao Tourist Stats

**File**: `.github/workflows/update-stats.yml`

**Note**: This file needs to be added manually via GitHub UI due to OAuth scope limitations.

## How to Add:

### Option 1: Via GitHub Website

1. Go to: https://github.com/john-fb-agent/macao-tourist-stats
2. Click **Add file** → **Create new file**
3. Name: `.github/workflows/update-stats.yml`
4. Paste the content below
5. Click **Commit changes**

### Option 2: Via GitHub Codespaces

1. Open the repo in Codespaces
2. Create the file locally
3. Commit and push

---

## Workflow Content:

```yaml
name: Update Macau Tourist Statistics

on:
  schedule:
    # Run every Monday at 00:00 UTC (8:00 AM Asia/Shanghai)
    - cron: '0 0 * * 1'
  workflow_dispatch:  # Allow manual trigger

permissions:
  contents: write  # Allow pushing data and charts

jobs:
  update-stats:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Configure Git
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
      
      - name: Fetch tourist data
        env:
          MACAO_DATA_APPCODE: ${{ secrets.MACAO_DATA_APPCODE }}
        run: |
          echo "📊 Fetching Macau tourist data..."
          python scripts/fetch_data.py
      
      - name: Generate charts
        run: |
          echo "📈 Generating charts..."
          python scripts/generate_charts.py
      
      - name: Commit and push changes
        run: |
          git add data/ charts/
          if git diff --staged --quiet; then
            echo "No changes to commit"
          else
            git commit -m "📊 Update tourist statistics $(date +%Y-%m-%d)"
            git push
            echo "✅ Changes pushed successfully"
          fi
      
      - name: Upload charts as artifacts
        uses: actions/upload-artifact@v4
        with:
          name: tourist-charts
          path: charts/
          retention-days: 30
```

---

## After Adding:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Add repository secret:
   - **Name**: `MACAO_DATA_APPCODE`
   - **Value**: `09d43a591fba407fb862412970667de4` (or your own)
3. Go to **Actions** tab and click **Run workflow** to test

---

**Created**: 2026-03-18
