# ✅ Almost Done! One Manual Step Required

**Completed** (2026-03-18 15:00 GMT+8):

- ✅ GitHub Pages enabled: https://john-fb-agent.github.io/macao-tourist-stats/
- ✅ API secret added: `MACAO_DATA_APPCODE`
- ✅ Workflow file created locally
- ⏳ **TODO**: Add workflow file via GitHub UI (requires OAuth workflow scope)

---

## 📋 Final Step: Add Workflow File

### Option 1: Via GitHub Website (2 minutes)

1. **Go to**: https://github.com/john-fb-agent/macao-tourist-stats/new/main

2. **Name the file**:
   ```
   .github/workflows/update-stats.yml
   ```

3. **Paste this content**:
   ```yaml
   name: Update Macau Tourist Statistics

   on:
     schedule:
       # Run every Monday at 00:00 UTC (8:00 AM Asia/Shanghai)
       - cron: '0 0 * * 1'
     workflow_dispatch:  # Allow manual trigger

   permissions:
     contents: write

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
         
         - name: Commit and push changes
           run: |
             git add data/
             if git diff --staged --quiet; then
               echo "No changes to commit"
             else
               git commit -m "📊 Update tourist statistics $(date +%Y-%m-%d)"
               git push
               echo "✅ Changes pushed successfully"
             fi
   ```

4. **Click**: "Commit changes"

---

### Option 2: Test Workflow Immediately

After adding the workflow file:

1. Go to **Actions** tab: https://github.com/john-fb-agent/macao-tourist-stats/actions
2. Click **"Update Macau Tourist Statistics"** workflow
3. Click **"Run workflow"** dropdown
4. Click **"Run workflow"** button
5. Wait 1-2 minutes for it to complete

---

## ✅ What's Already Done

| Task | Status |
|------|--------|
| GitHub Pages | ✅ Enabled |
| Dashboard URL | ✅ https://john-fb-agent.github.io/macao-tourist-stats/ |
| API Secret | ✅ `MACAO_DATA_APPCODE` added |
| Workflow file | ⏳ Needs manual addition |
| First workflow run | ⏳ After adding workflow file |

---

## 🎉 After Completion

Your Macau Tourist Statistics will:
- Auto-update every Monday at 8:00 AM (Macau time)
- Fetch latest data from data.gov.mo
- Update the interactive dashboard automatically
- Keep charts and data in sync

---

**Created**: 2026-03-18 15:00 GMT+8
