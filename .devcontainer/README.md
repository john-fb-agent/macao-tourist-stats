# Development Container Setup

This dev container provides a consistent development environment for the Macau Tourist Statistics project.

## 🚀 Quick Start

### Option 1: GitHub Codespaces

1. Go to https://github.com/john-fb-agent/macao-tourist-stats
2. Click **Code** → **Codespaces** tab
3. Click **Create codespace on main**
4. Wait for container to build (~2-3 minutes)
5. Start developing!

### Option 2: VS Code Dev Container

**Prerequisites**:
- VS Code installed
- Dev Containers extension installed
- Docker installed and running

**Steps**:
1. Clone the repository
2. Open in VS Code
3. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
4. Select **Dev Containers: Reopen in Container**
5. Wait for container to build
6. Start developing!

## 📦 What's Included

| Tool | Version | Purpose |
|------|---------|---------|
| **Node.js** | 20.x | JavaScript runtime |
| **Python** | 3.11 | Data fetching scripts |
| **http-server** | Latest | Local development server |

## 🛠️ VS Code Extensions

Pre-installed extensions:

- **ESLint** - JavaScript linting
- **Prettier** - Code formatting
- **Live Server** - Local development server
- **Python** - Python support
- **Pylance** - Python language server

## 🌐 Development Server

Once the container is running:

```bash
# Start local server
http-server -p 8000

# Access dashboard at:
# http://localhost:8000
```

The port 8000 is automatically forwarded to your local machine.

## 📁 Workspace Structure

```
macao-tourist-stats/
├── .devcontainer/          # Dev container config
│   └── devcontainer.json
├── data/
│   └── data.json           # Tourist data
├── index.html              # Homepage
├── monthly-trend.html      # Monthly trends
├── yearly-trend.html       # Yearly trends
└── README.md
```

## 🔧 Development Tasks

### Update Data

```bash
# Navigate to workspace
cd /workspaces/macao-tourist-stats

# Run data fetch script (if available)
python3 scripts/fetch_data.py
```

### Test Locally

```bash
# Start server
http-server -p 8000

# Open browser to http://localhost:8000
```

### Commit Changes

```bash
git add .
git commit -m "feat: your changes"
git push origin main
```

## 🎯 Features

- ✅ **Pre-configured environment** - No manual setup
- ✅ **Consistent tooling** - Same versions for all developers
- ✅ **Port forwarding** - Access local server easily
- ✅ **Extension recommendations** - Best tools pre-installed
- ✅ **Python + Node.js** - Both runtimes available

## 🐛 Troubleshooting

### Container won't build

```bash
# Rebuild container
# VS Code: Ctrl+Shift+P → Dev Containers: Rebuild Container
```

### Port not accessible

```bash
# Check if server is running
netstat -tlnp | grep 8000

# Restart server
http-server -p 8000
```

### Extensions not installed

```bash
# Install manually in container
code --install-extension <extension-id>
```

## 📚 Resources

- [Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [GitHub Codespaces](https://github.com/features/codespaces)
- [Container Configuration Reference](https://aka.ms/devcontainer.json)

---

**Happy coding!** 🚀
