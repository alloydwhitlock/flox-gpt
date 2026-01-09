#!/usr/bin/env python3
"""
FloxGPT Documentation Consolidator

This script fetches the latest Flox documentation from GitHub and consolidates
it into a single, well-organized document optimized for use with a custom GPT.
"""

import os
import subprocess
import shutil
from datetime import datetime, timezone
from pathlib import Path
import re


# Configuration
REPO_URL = "https://github.com/flox/floxdocs.git"
REPO_DIR = "floxdocs-temp"
DOCS_SUBDIR = "docs"
OUTPUT_FILE = "output/floxgpt-knowledge.md"
LAST_UPDATED_FILE = "output/last-updated.txt"

# File ordering for logical documentation flow
PRIORITY_ORDER = [
    "index",
    "install",
    "getting-started",
    "quick-start",
    "tutorial",
    "concepts",
    "environments",
    "packages",
    "commands",
    "manifest",
    "services",
    "sharing",
    "collaboration",
    "teams",
    "reference",
    "faq",
    "troubleshooting",
]


def get_script_dir():
    """Get the directory containing this script."""
    return Path(__file__).parent.absolute()


def get_project_root():
    """Get the project root directory."""
    return get_script_dir().parent


def clone_or_update_repo():
    """Clone the floxdocs repository or update if it exists."""
    project_root = get_project_root()
    repo_path = project_root / REPO_DIR
    
    if repo_path.exists():
        print(f"Removing existing temp directory: {repo_path}")
        shutil.rmtree(repo_path)
    
    print(f"Cloning {REPO_URL}...")
    subprocess.run(
        ["git", "clone", "--depth", "1", REPO_URL, str(repo_path)],
        check=True,
        capture_output=True
    )
    
    # Get the latest commit info
    result = subprocess.run(
        ["git", "-C", str(repo_path), "log", "-1", "--format=%H|%ci|%s"],
        capture_output=True,
        text=True,
        check=True
    )
    commit_hash, commit_date, commit_msg = result.stdout.strip().split("|", 2)
    
    return repo_path, commit_hash, commit_date, commit_msg


def get_file_priority(filepath: Path) -> int:
    """
    Get the sort priority for a file based on its name.
    Lower numbers = higher priority (appear earlier in output).
    """
    filename = filepath.stem.lower()
    
    for i, keyword in enumerate(PRIORITY_ORDER):
        if keyword in filename:
            return i
    
    return len(PRIORITY_ORDER)


def find_markdown_files(docs_path: Path) -> list[Path]:
    """Find all markdown files in the docs directory."""
    md_files = list(docs_path.rglob("*.md"))
    
    # Sort by priority, then alphabetically
    md_files.sort(key=lambda f: (get_file_priority(f), f.name.lower()))
    
    return md_files


def clean_markdown_content(content: str, filepath: Path) -> str:
    """
    Clean and normalize markdown content for GPT consumption.
    """
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Remove admonition syntax that GPT doesn't need (mkdocs specific)
    content = re.sub(r'!!! \w+.*?\n', '', content)
    content = re.sub(r'\?\?\? \w+.*?\n', '', content)
    
    # Clean up excessive whitespace
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # Remove trailing whitespace
    content = '\n'.join(line.rstrip() for line in content.split('\n'))
    
    return content.strip()


def extract_title(content: str, filepath: Path) -> str:
    """Extract the title from markdown content or generate from filename."""
    # Look for a top-level heading
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    
    # Fall back to filename
    return filepath.stem.replace("-", " ").replace("_", " ").title()


def create_consolidated_document(md_files: list[Path], docs_path: Path) -> str:
    """
    Create a single consolidated markdown document from all source files.
    """
    sections = []
    toc_entries = []
    
    for filepath in md_files:
        try:
            content = filepath.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Warning: Could not read {filepath}: {e}")
            continue
        
        if not content.strip():
            continue
        
        # Get relative path for context
        rel_path = filepath.relative_to(docs_path)
        
        # Extract and clean
        title = extract_title(content, filepath)
        cleaned_content = clean_markdown_content(content, filepath)
        
        # Remove the title from content if it exists (we'll add our own header)
        cleaned_content = re.sub(r'^#\s+.+\n*', '', cleaned_content, count=1)
        
        # Create section anchor
        anchor = title.lower().replace(" ", "-").replace(".", "")
        anchor = re.sub(r'[^a-z0-9-]', '', anchor)
        
        toc_entries.append(f"- [{title}](#{anchor})")
        
        section = f"""
## {title}

> Source: `{rel_path}`

{cleaned_content}

---
"""
        sections.append(section)
    
    # Build the final document
    toc = "\n".join(toc_entries)
    content = "\n".join(sections)
    
    return toc, content


def generate_document(commit_hash: str, commit_date: str, commit_msg: str, 
                      toc: str, content: str) -> str:
    """Generate the final consolidated document with metadata."""
    
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    document = f"""# Flox Documentation - Complete Knowledge Base

> **Purpose**: This document contains the complete Flox documentation, consolidated for use by FloxGPT, a custom GPT assistant.

## Metadata

- **Last Updated**: {now}
- **Source Repository**: https://github.com/flox/floxdocs
- **Source Commit**: `{commit_hash[:8]}`
- **Source Commit Date**: {commit_date}
- **Source Commit Message**: {commit_msg}

## About Flox

Flox is a virtual environment and package manager all in one. With Flox you can:

- Create reproducible development environments that work across Linux and macOS
- Install packages from the largest open-source package repository (Nixpkgs)
- Share environments with your team using FloxHub or Git
- Run services and background processes within your environment
- Build and publish your own packages

Flox provides a friendly CLI that abstracts away the complexity of Nix while giving you access to its powerful features.

## Table of Contents

{toc}

---

# Documentation Content

{content}

---

# End of Documentation

This document was automatically generated from the official Flox documentation repository.
For the most current information, visit https://flox.dev/docs/
"""
    
    return document


def save_update_info(commit_hash: str, commit_date: str):
    """Save the last update information."""
    project_root = get_project_root()
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)
    
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    info = f"""Last Updated: {now}
Source Commit: {commit_hash}
Source Commit Date: {commit_date}
"""
    
    (output_dir / "last-updated.txt").write_text(info)


def main():
    """Main entry point."""
    print("=" * 60)
    print("FloxGPT Documentation Consolidator")
    print("=" * 60)
    
    project_root = get_project_root()
    
    # Clone/update the repository
    print("\n[1/4] Fetching latest documentation...")
    repo_path, commit_hash, commit_date, commit_msg = clone_or_update_repo()
    print(f"  Commit: {commit_hash[:8]}")
    print(f"  Date: {commit_date}")
    print(f"  Message: {commit_msg[:50]}...")
    
    # Find markdown files
    print("\n[2/4] Finding documentation files...")
    docs_path = repo_path / DOCS_SUBDIR
    if not docs_path.exists():
        print(f"Error: Docs directory not found at {docs_path}")
        return 1
    
    md_files = find_markdown_files(docs_path)
    print(f"  Found {len(md_files)} markdown files")
    
    # Create consolidated document
    print("\n[3/4] Consolidating documentation...")
    toc, content = create_consolidated_document(md_files, docs_path)
    document = generate_document(commit_hash, commit_date, commit_msg, toc, content)
    
    # Save output
    print("\n[4/4] Saving output...")
    output_path = project_root / OUTPUT_FILE
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(document, encoding='utf-8')
    print(f"  Saved to: {output_path}")
    
    # Save update info
    save_update_info(commit_hash, commit_date)
    
    # Cleanup
    print("\nCleaning up...")
    shutil.rmtree(repo_path)
    
    # Stats
    doc_size = len(document)
    word_count = len(document.split())
    print(f"\n{'=' * 60}")
    print("Complete!")
    print(f"  Document size: {doc_size:,} characters")
    print(f"  Word count: ~{word_count:,} words")
    print(f"  Estimated tokens: ~{word_count * 1.3:.0f}")
    print(f"{'=' * 60}")
    
    return 0


if __name__ == "__main__":
    exit(main())
