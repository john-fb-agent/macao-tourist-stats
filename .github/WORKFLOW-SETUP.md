# ⚙️ GitHub Actions Workflow Setup

**IMPORTANT**: This folder needs to be added manually via GitHub UI due to OAuth scope limitations.

---

## How to Add Workflow File

### Option 1: Via GitHub Website (Recommended)

1. Go to: https://github.com/john-fb-agent/macao-tourist-stats
2. Click **Add file** → **Create new file**
3. Navigate to: `.github/workflows/` (create these folders)
4. Name the file: `update-stats.yml`
5. Copy and paste the content below
6. Click **Commit changes**

### Option 2: Via GitHub CLI (If you have workflow scope)

```bash
# First refresh your token with workflow scope
gh auth refresh -s workflow

# Then push the workflow file
git add .github/workflows/update-stats.yml
git commit -m "Add GitHub Actions workflow"
git push
```

---

## Workflow File Content

Create `.github/workflows/update-stats.yml` with this content:

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

---

## After Adding Workflow

### 1. Add API Secret

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add:
   - **Name**: `MACAO_DATA_APPCODE`
   - **Value**: `09d43a591fba407fb862412970667de4`
4. Click **Add secret**

### 2. Enable GitHub Pages (Optional)

To host the interactive dashboard:

1. Go to **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: Select `main` → `/ (root)`
4. Click **Save**
5. Wait 2-3 minutes
6. Access at: `https://john-fb-agent.github.io/macao-tourist-stats/`

### 3. Test the Workflow

1. Go to **Actions** tab
2. Click **Update Macau Tourist Statistics** workflow
3. Click **Run workflow**
4. Wait for it to complete
5. Check if data was updated

---

## Troubleshooting

### Workflow doesn't run?

- Check **Settings** → **Actions** → **General** → Ensure actions are enabled
- Verify the secret `MACAO_DATA_APPCODE` is set correctly

### Data not updating?

- Check the workflow run logs for errors
- Verify API endpoint is accessible
- Try running locally: `python scripts/fetch_data.py`

### GitHub Pages not working?

- Wait a few minutes after enabling
- Check **Settings** → **Pages** for deployment status
- Ensure `index.html` exists in the root directory

---

**Created**: 2026-03-18  
**Last Updated**: 2026-03-18
