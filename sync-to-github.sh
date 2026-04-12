#!/bin/bash
# Sync AI-generated .md files and Claude config to GitHub repository
# Runs every hour via cron
# NOTE: Excludes sensitive data (API keys, tokens)

set -e

REPO_URL="git@github.com:GaryXu66/my_claude.git"
REPO_DIR="$HOME/.openclaw/workspace/repos/my_claude"
SOURCE_MD_DIR="/data/home/heng_xu/work/program/idea_workhome"
CLAUDE_DIR="$HOME/.claude"
BRANCH="master"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Clone or update repository
if [ ! -d "$REPO_DIR" ]; then
    log "Cloning repository..."
    git clone "$REPO_URL" "$REPO_DIR"
else
    log "Updating repository..."
    cd "$REPO_DIR"
    git pull origin "$BRANCH" 2>/dev/null || true
fi

cd "$REPO_DIR"

# Sync .md files from idea_workhome (root level only)
MD_FILES=$(ls -1 "$SOURCE_MD_DIR"/*.md 2>/dev/null || true)
if [ -n "$MD_FILES" ]; then
    log "Copying .md files from idea_workhome..."
    mkdir -p "$REPO_DIR/idea_workhome"
    cp "$SOURCE_MD_DIR"/*.md "$REPO_DIR/idea_workhome/"
fi

# Sync Claude config files
log "Syncing Claude config files..."

# settings.json - remove sensitive fields
if [ -f "$CLAUDE_DIR/settings.json" ]; then
    mkdir -p "$REPO_DIR/claude-config"
    # Copy settings.json but remove sensitive env vars
    cat "$CLAUDE_DIR/settings.json" | jq 'del(.env.ANTHROPIC_AUTH_TOKEN, .env.ANTHROPIC_API_KEY, .env."ANTHROPIC_AUTH_TOKEN", .env."ANTHROPIC_API_KEY")' > "$REPO_DIR/claude-config/settings.json" 2>/dev/null || cp "$CLAUDE_DIR/settings.json" "$REPO_DIR/claude-config/"
    log "  - settings.json (sanitized)"
fi

# skills directory
if [ -d "$CLAUDE_DIR/skills" ]; then
    mkdir -p "$REPO_DIR/claude-config/skills"
    rm -rf "$REPO_DIR/claude-config/skills"/*
    cp -r "$CLAUDE_DIR/skills"/* "$REPO_DIR/claude-config/skills/" 2>/dev/null || true
    log "  - skills/"
fi

# agents directory
if [ -d "$CLAUDE_DIR/agents" ]; then
    mkdir -p "$REPO_DIR/claude-config/agents"
    rm -rf "$REPO_DIR/claude-config/agents"/*
    cp -r "$CLAUDE_DIR/agents"/* "$REPO_DIR/claude-config/agents/" 2>/dev/null || true
    log "  - agents/"
fi

# projects directory (project-level memories/CLAUDE.md)
if [ -d "$CLAUDE_DIR/projects" ]; then
    mkdir -p "$REPO_DIR/claude-config/projects"
    rm -rf "$REPO_DIR/claude-config/projects"/*
    # Only copy CLAUDE.md files from each project, not session data
    for proj_dir in "$CLAUDE_DIR/projects"/*/; do
        if [ -d "$proj_dir" ]; then
            proj_name=$(basename "$proj_dir")
            mkdir -p "$REPO_DIR/claude-config/projects/$proj_name"
            # Copy CLAUDE.md (project instructions) if exists
            [ -f "$proj_dir/CLAUDE.md" ] && cp "$proj_dir/CLAUDE.md" "$REPO_DIR/claude-config/projects/$proj_name/"
            # Copy settings.local.json if exists (project-specific settings, will sanitize)
            if [ -f "$proj_dir/settings.local.json" ]; then
                cat "$proj_dir/settings.local.json" | jq 'del(.env.ANTHROPIC_AUTH_TOKEN, .env.ANTHROPIC_API_KEY)' > "$REPO_DIR/claude-config/projects/$proj_name/settings.local.json" 2>/dev/null || true
            fi
        fi
    done
    log "  - projects/ (CLAUDE.md only)"
fi

# Check if there are changes
if [ -z "$(git status --porcelain)" ]; then
    log "No changes to commit"
    exit 0
fi

# Commit and push
log "Committing changes..."
git add -A
git commit -m "Auto-sync: Update files [$(date '+%Y-%m-%d %H:%M:%S')]"

log "Pushing to GitHub..."
git push origin "$BRANCH"

log "Sync completed successfully!"