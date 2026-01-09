# FloxHub GPT Actions

This directory contains OpenAPI specifications for ChatGPT custom GPT actions that enable searching the FloxHub package catalog.

## Available Actions

### `floxhub-search.json` (Recommended)

A comprehensive action for searching and exploring FloxHub packages:

- **searchPackages**: Search for packages by name, keyword, or description
- **getPackageDetails**: Get detailed info and version history for a specific package

### `package-search.json` (Legacy)

The original search-only action. Use `floxhub-search.json` instead for full functionality.

## Adding to a Custom GPT

### Step 1: Create or Edit Your GPT

1. Go to [ChatGPT](https://chat.openai.com)
2. Click your profile → **My GPTs** → **Create a GPT** (or edit existing)
3. Go to the **Configure** tab

### Step 2: Add the Action

1. Scroll down to **Actions** and click **Create new action**
2. Copy the entire contents of `floxhub-search.json`
3. Paste into the **Schema** field (replace any existing content)
4. Set **Authentication** to **None** (FloxHub's public API doesn't require auth)
5. Click **Save**

### Step 3: Configure Privacy Policy (Optional)

If publishing your GPT, add a privacy policy URL. You can use:
```
https://flox.dev/privacy
```

### Step 4: Test the Action

In the GPT preview, try:
- "Search for python packages"
- "Find nodejs versions"
- "What CUDA packages are available?"

## Usage Examples

Once added, your GPT can:

### Search for Packages
> "Search FloxHub for postgresql"

Returns packages matching "postgresql" with their pkg_path, version, description, and supported systems.

### Find Specific Versions
> "Show me all available versions of nodejs"

Returns version history for the nodejs package.

### Platform-Specific Search
> "Find Python packages available on aarch64-darwin (Apple Silicon)"

Filters results to packages supporting the specified architecture.

## How Results Map to Flox Manifests

Search results provide `pkg_path` values that go directly into your `manifest.toml`:

```toml
[install]
# From search result: pkg_path = "nodejs"
nodejs.pkg-path = "nodejs"

# From search result: pkg_path = "python311Packages.pip"
pip.pkg-path = "python311Packages.pip"

# With version constraint
nodejs.pkg-path = "nodejs"
nodejs.version = "^20.0"
```

## Troubleshooting

### No Results Found
- Search is case-sensitive; try different casing
- Use broader search terms
- Increase the `limit` parameter

### Package Details Not Found
- Ensure you're using the exact `pkg_path` from search results
- Some nested packages require full paths (e.g., `python311Packages.requests`)

### System Not Supported
- Check if the package supports your target architecture
- CUDA packages only support Linux: `x86_64-linux`, `aarch64-linux`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/catalog/search?q={query}` | GET | Search packages |
| `/api/v1/catalog/packages/{pkg_path}` | GET | Get package details |

## Related Resources

- [FloxHub](https://hub.flox.dev/packages) - Browse packages in the web UI
- [Flox Documentation](https://flox.dev/docs) - Official Flox docs
- [flox-agentic](https://github.com/flox/flox-agentic) - Flox agent instructions and knowledge
