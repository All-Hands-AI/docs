# Repository Knowledge

## Repository Structure

The repository is now set up as a monorepo with documentation in a dedicated `docs/` folder:

```
/workspace/docs/              # Root repository
├── .git/                     # Git repository
├── .openhands/               # OpenHands agent memory
│   └── microagents/          # Microagents information
└── docs/                     # Documentation directory (Mintlify content)
    ├── logo/                 # Logo assets
    ├── modules/              # Main documentation content
    │   ├── index.mdx         # Main landing page
    │   ├── usage/            # Core OpenHands documentation
    │   │   ├── about.md      # About OpenHands
    │   │   ├── installation.mdx # Installation guide
    │   │   ├── getting-started.mdx # Getting started guide
    │   │   ├── key-features.md # Feature overview
    │   │   ├── agents.md     # Agents documentation
    │   │   ├── cloud/        # Cloud-specific documentation
    │   │   ├── how-to/       # How-to guides
    │   │   ├── llms/         # LLM configuration
    │   │   ├── prompting/    # Prompting guides
    │   │   ├── runtimes/     # Runtime configuration
    │   │   ├── architecture/ # Architecture documentation
    │   │   ├── customization/ # Customization guides
    │   │   └── troubleshooting/ # Troubleshooting guides
    │   └── python/           # Python-specific documentation
    ├── static/               # Static assets (images, etc.)
    │   └── img/              # Image assets
    ├── docs.json             # Main configuration file (Mintlify)
    ├── favicon.svg           # Favicon
    ├── logo-square.png       # Square logo
    ├── openapi.json          # OpenAPI specification
    ├── README.md             # Repository README
    └── OPENHANDS_MIGRATION.md # Documentation of migration process
```

Key files:
- `docs.json`: Defines the navigation structure and site configuration
- `modules/index.mdx`: Main landing page for the documentation
- `openapi.json`: API specification

## Documentation Format Standards

The documentation uses Mintlify's formatting conventions:

### Frontmatter

Each documentation file should include frontmatter at the top:

```md
---
title: "Page Title"
description: "Brief description of the page content"
---
```

### Components

Common Mintlify components used in the documentation:

1. **Note Component**:
   ```md
   <Note>
   This is a note with important information.
   </Note>
   ```

2. **Warning Component**:
   ```md
   <Warning>
   This is a warning about potential issues.
   </Warning>
   ```

3. **Tip Component**:
   ```md
   <Tip>
   This is a helpful tip for users.
   </Tip>
   ```

4. **Accordion Component**:
   ```md
   <Accordion title="Click to expand">
   This content is hidden by default and expands when clicked.
   </Accordion>
   ```

5. **CodeGroup Component**:
   ```md
   <CodeGroup>
   ```bash
   # Bash code example
   echo "Hello World"
   ```

   ```python
   # Python code example
   print("Hello World")
   ```
   </CodeGroup>
   ```

### Links

Internal links should use absolute paths starting with `/`:

```md
[Link to Installation](/modules/usage/installation)
```

## Navigation Structure

The navigation structure is defined in `docs.json` and organized into the following tabs:

1. **Overview** - General introduction to OpenHands
   - Main landing page
   - About OpenHands

2. **Getting Started** - Installation and basic usage
   - Installation
   - Getting Started
   - Key Features

3. **OpenHands Cloud** - Cloud-specific documentation
   - OpenHands Cloud Overview
   - Installation (GitHub, GitLab)
   - Cloud UI
   - Cloud Issue Resolver
   - Cloud API

4. **Usage Methods** - Different ways to use OpenHands
   - GUI Mode
   - CLI Mode
   - Headless Mode
   - GitHub Action

5. **Customization** - Repository customization and microagents
   - Repository Customization
   - Microagents (Overview, Repo, Keyword, Org, Public)
   - Prompting Best Practices

6. **Advanced Configuration** - LLM and runtime configuration
   - LLM Configuration (Azure, Google, Groq, Local, LiteLLM, OpenAI, OpenRouter)
   - Runtime Configuration (Docker, Remote, Modal, Daytona, Local)
   - Configuration Options
   - Custom Sandbox Guide
   - MCP (Multi-Context Processing)

7. **Developer Resources** - Architecture and development guides
   - Development Overview
   - Architecture (Backend, Runtime)
   - Debugging
   - Evaluation Harness
   - WebSocket Connection

8. **Help & Support** - Troubleshooting and feedback
   - Troubleshooting
   - Feedback

## Common Commands

### Development

To preview documentation changes locally:

1. Install the Mintlify CLI:
   ```bash
   npm i -g mintlify
   ```

2. Run the development server from the root directory (where docs.json is located):
   ```bash
   mintlify dev
   ```

### Troubleshooting

- If Mintlify dev isn't running, reinstall dependencies:
  ```bash
  mintlify install
  ```

- If a page loads as a 404, make sure you are running in a folder with `docs.json`

### Publishing Changes

Changes are automatically deployed to production after pushing to the default branch if the GitHub App is installed. The GitHub App propagates changes from your repository to your deployment.

### Monorepo Configuration

The repository is set up as a monorepo with documentation in a dedicated `docs/` folder. To configure Mintlify to deploy from this folder:

1. Access Git Settings in the Mintlify dashboard: https://dashboard.mintlify.com/settings/deployment/git-settings
2. Enable the "Set up as monorepo" toggle
3. Enter "docs" as the relative path to your docs directory
4. Save the changes

This configuration tells Mintlify to look for documentation files in the `docs/` directory rather than the root of the repository.