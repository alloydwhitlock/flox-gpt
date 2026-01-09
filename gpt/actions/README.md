# Flox Package Search GPT Actions

This directory contains OpenAPI specifications for ChatGPT custom GPT actions that enable searching for packages compatible with Flox environments.

## Available Actions

### `floxhub-search.json` ✅ (Recommended)

A working action that searches for Nix packages via the Nixhub API. Since Flox uses Nixpkgs as its package source, these are the same packages available via `flox search` and `flox install`.

**Endpoints:**
- `searchPackages` (`/v2/search`) - Search packages by name
- `getPackageVersions` (`/v2/pkg`) - Get version history for a package
- `resolvePackageVersion` (`/v2/resolve`) - Resolve a specific version

### `package-search.json` ⚠️ (Deprecated)

Original action targeting hub.flox.dev API. The FloxHub API (`api.flox.dev`) is not publicly accessible - it requires authentication from the hub.flox.dev frontend. Use `floxhub-search.json` instead.

## Adding to a Custom GPT

### Step 1: Create or Edit Your GPT

1. Go to [ChatGPT](https://chat.openai.com)
2. Click your profile → **My GPTs** → **Create a GPT** (or edit existing)
3. Go to the **Configure** tab

### Step 2: Add the Action

1. Scroll down to **Actions** and click **Create new action**
2. Copy the entire contents of `floxhub-search.json`
3. Paste into the **Schema** field (replace any existing content)
4. Set **Authentication** to **None**
5. Click **Save**

### Step 3: Configure Privacy Policy

Add this URL to the Privacy Policy field:
```
https://github.com/alloydwhitlock/flox-gpt/blob/main/PRIVACY.md
```

### Step 4: Test the Action

In the GPT preview, try:
- "Search for python packages"
- "Show me nodejs versions"
- "What postgresql versions are available?"

## Usage Examples

Once added, your GPT can:

### Search for Packages
> "Search for postgresql"

Returns packages matching "postgresql" with their name and description.

### Get Version History
> "Show me all available versions of nodejs"

Returns the complete version history for the nodejs package.

### Resolve Specific Versions
> "What's the latest nodejs 20.x version?"

Resolves version constraints to find available versions.

## How Results Map to Flox Manifests

Search results provide package names that go directly into your `manifest.toml`:

```toml
[install]
# From search result: name = "nodejs"
nodejs.pkg-path = "nodejs"

# From search result: name = "python311"  
python.pkg-path = "python311"

# With version constraint
nodejs.pkg-path = "nodejs"
nodejs.version = "^20.0"
```

## API Details

The action uses the [Nixhub API](https://www.jetify.com/docs/nixhub/) by Jetify:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v2/search?q={query}` | GET | Search packages by name |
| `/v2/pkg?name={name}` | GET | Get package details and versions |
| `/v2/resolve?name={name}&version={ver}` | GET | Resolve specific version |

**Rate Limits:**
- 1,000 requests per IP address pool
- Replenishes at 5 requests/minute
- Returns 429 if exhausted

## Why Nixhub Instead of FloxHub?

Flox uses Nixpkgs as its package source. The FloxHub web API (`api.flox.dev`) requires authentication and isn't publicly accessible for third-party integrations. The Nixhub API provides the same package data that `flox search` uses, making it a suitable alternative for GPT actions.

## Related Resources

- [FloxHub](https://hub.flox.dev/packages) - Browse packages in the web UI
- [Flox Documentation](https://flox.dev/docs) - Official Flox docs
- [Nixhub API Docs](https://www.jetify.com/docs/nixhub/) - API documentation
- [flox-agentic](https://github.com/flox/flox-agentic) - Flox agent instructions
