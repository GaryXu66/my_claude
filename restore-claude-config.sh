#!/bin/bash
# Restore Claude config from GitHub repository
# Run this on a new machine to apply your Claude habits

set -e

REPO_URL="git@github.com:GaryXu66/my_claude.git"
REPO_DIR="$HOME/.openclaw/workspace/repos/my_claude"
CLAUDE_DIR="$HOME/.claude"

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
    git pull origin master 2>/dev/null || true
fi

CONFIG_DIR="$REPO_DIR/claude-config"

if [ ! -d "$CONFIG_DIR" ]; then
    log "ERROR: claude-config directory not found in repository"
    exit 1
fi

# Create .claude directory if not exists
mkdir -p "$CLAUDE_DIR"

# Restore settings.json (merge with existing, keep local secrets)
if [ -f "$CONFIG_DIR/settings.json" ]; then
    log "Restoring settings.json..."
    if [ -f "$CLAUDE_DIR/settings.json" ]; then
        # Merge: keep existing env vars (might have local tokens), add new settings
        jq -s '.[0] * .[1]' "$CLAUDE_DIR/settings.json" "$CONFIG_DIR/settings.json" > "$CLAUDE_DIR/settings.json.tmp" 2>/dev/null && \
            mv "$CLAUDE_DIR/settings.json.tmp" "$CLAUDE_DIR/settings.json" || \
            log "  WARNING: Could not merge settings.json, keeping existing"
    else
        cp "$CONFIG_DIR/settings.json" "$CLAUDE_DIR/settings.json"
    fi
    log "  ✓ settings.json restored"
fi

# Restore skills
if [ -d "$CONFIG_DIR/skills" ]; then
    log "Restoring skills..."
    mkdir -p "$CLAUDE_DIR/skills"
    cp -r "$CONFIG_DIR/skills"/* "$CLAUDE_DIR/skills/" 2>/dev/null || true
    log "  ✓ skills/ restored"
fi

# Restore agents
if [ -d "$CONFIG_DIR/agents" ]; then
    log "Restoring agents..."
    mkdir -p "$CLAUDE_DIR/agents"
    cp -r "$CONFIG_DIR/agents"/* "$CLAUDE_DIR/agents/" 2>/dev/null || true
    log "  ✓ agents/ restored"
fi

# Restore project CLAUDE.md files
if [ -d "$CONFIG_DIR/projects" ]; then
    log "Restoring project configs..."
    mkdir -p "$CLAUDE_DIR/projects"
    for proj_dir in "$CONFIG_DIR/projects"/*/; do
        if [ -d "$proj_dir" ]; then
            proj_name=$(basename "$proj_dir")
            mkdir -p "$CLAUDE_DIR/projects/$proj_name"
            [ -f "$proj_dir/CLAUDE.md" ] && cp "$proj_dir/CLAUDE.md" "$CLAUDE_DIR/projects/$proj_name/"
            [ -f "$proj_dir/settings.local.json" ] && cp "$proj_dir/settings.local.json" "$CLAUDE_DIR/projects/$proj_name/"
        fi
    done
    log "  ✓ projects/ restored"
fi

echo ""
log "=========================================="
log "✓ Restore completed!"
log ""
log "IMPORTANT: You need to set your API tokens:"
log "  1. Edit ~/.claude/settings.json"
log "  2. Add ANTHROPIC_AUTH_TOKEN to env section"
log ""
log "Or run: claude config set ANTHROPIC_AUTH_TOKEN <your-token>"
log "=========================================="