# FloxGPT

> A custom ChatGPT that stays up-to-date with the latest Flox documentation.

[![Update Documentation](https://github.com/YOUR_USERNAME/floxgpt/actions/workflows/update-docs.yml/badge.svg)](https://github.com/YOUR_USERNAME/floxgpt/actions/workflows/update-docs.yml)

## Overview

FloxGPT is a custom GPT designed to be your expert guide to [Flox](https://flox.dev) - the virtual environment and package manager that makes development environments reproducible, shareable, and delightful.

This repository automates the process of:
1. **Fetching** the latest documentation from [flox/floxdocs](https://github.com/flox/floxdocs)
2. **Consolidating** all documentation into a single, GPT-optimized knowledge file
3. **Updating** daily via GitHub Actions

## Project Structure

```
floxgpt/
├── .flox/                    # Flox environment configuration
├── .github/
│   └── workflows/
│       └── update-docs.yml   # Daily update workflow
├── scripts/
│   └── consolidate-docs.py   # Documentation consolidation script
├── gpt/
│   ├── instructions.md       # GPT system instructions
│   └── conversation-starters.json
├── output/
│   ├── floxgpt-knowledge.md  # Consolidated documentation (auto-generated)
│   └── last-updated.txt      # Update metadata
└── README.md
```

## How It Works

### Daily Updates

A GitHub Action runs every day at 6:00 AM UTC to:
1. Clone the latest `floxdocs` repository
2. Process all markdown documentation files
3. Create a single consolidated knowledge base
4. **Create a GitHub Release** if documentation changed (with the knowledge file attached)

### 🔔 Get Notified of Updates

When the Flox documentation changes, this repo automatically creates a new **GitHub Release** with:
- The updated `floxgpt-knowledge.md` file ready to download
- Step-by-step instructions for updating your GPT
- Document stats and source commit info

**To receive notifications:**
1. Click **Watch** at the top of this repository
2. Select **Custom** → check **Releases**
3. You'll get an email whenever a new knowledge file is available

### Manual Updates

You can trigger an update manually:
- Go to **Actions** → **Update FloxGPT Documentation** → **Run workflow**

Or locally:

```bash
# Using Flox (recommended)
flox activate
python scripts/consolidate-docs.py

# Or directly with Python 3.12+
python3 scripts/consolidate-docs.py
```

## Setting Up Your GPT

### 1. Create a Custom GPT

1. Go to [ChatGPT](https://chat.openai.com) → **Explore GPTs** → **Create**
2. Use the contents of `gpt/instructions.md` for the **Instructions** field
3. Add conversation starters from `gpt/conversation-starters.json`

### 2. Upload the Knowledge Base

1. Go to the [Releases](../../releases) page
2. Download `floxgpt-knowledge.md` from the latest release
3. In your GPT configuration, go to **Knowledge** → **Upload files**
4. Upload the `floxgpt-knowledge.md` file

### 3. Keep It Updated

When you receive a release notification:
1. Download the new `floxgpt-knowledge.md` from the release
2. Go to [ChatGPT](https://chat.openai.com) → Your GPTs → FloxGPT → **Configure**
3. Under **Knowledge**, remove the old file and upload the new one
4. Click **Update** to save

## GPT Configuration

### Name
FloxGPT

### Description
Your expert guide to Flox - the virtual environment and package manager that makes development environments reproducible, shareable, and delightful. Get help with installation, environment creation, package management, team collaboration, and more.

### Capabilities

| Capability | Enabled | Reason |
|------------|---------|--------|
| Web Browsing | ❌ | Knowledge base contains all needed docs |
| DALL·E | ❌ | Not needed for developer assistance |
| Code Interpreter | ✅ | Helpful for analyzing manifests |

### Actions

Currently, this GPT uses only the uploaded knowledge base. Future enhancements could include:
- FloxHub API integration for package search
- Real-time documentation fetching

## Development

### Prerequisites

This project uses Flox for development environment management:

```bash
# Install Flox if you haven't already
curl -fsSL https://install.flox.dev | bash

# Activate the environment
flox activate
```

### Running Locally

```bash
# Run the consolidation script
python scripts/consolidate-docs.py

# Output will be in output/floxgpt-knowledge.md
```

### Testing Changes

After modifying the consolidation script:

```bash
# Test the script
python scripts/consolidate-docs.py

# Check the output
head -100 output/floxgpt-knowledge.md
```

## Contributing

Contributions are welcome! Areas for improvement:
- Better documentation organization/ordering
- Additional metadata extraction
- Support for GPT Actions/API integration
- Improved markdown cleaning for GPT consumption

## License

MIT License - see [LICENSE](LICENSE) for details.

## Related Links

- [Flox](https://flox.dev) - Official Flox website
- [Flox Documentation](https://flox.dev/docs) - Official documentation
- [flox/floxdocs](https://github.com/flox/floxdocs) - Documentation source repository
- [FloxHub](https://hub.flox.dev) - Share and discover Flox environments
