# Repository Knowledge

## Repository Structure

The documentation repository follows the Mintlify structure:

```
docs/
├── .openhands/                # OpenHands agent memory
├── modules/                   # Main documentation content
│   ├── index.mdx              # Main landing page
│   ├── usage/                 # Core OpenHands documentation
│   │   ├── about.md           # About OpenHands
│   │   ├── installation.mdx   # Installation guide
│   │   ├── getting-started.mdx # Getting started guide
│   │   ├── key-features.md    # Feature overview
│   │   ├── cloud/             # Cloud-specific documentation
│   │   ├── how-to/            # How-to guides
│   │   ├── llms/              # LLM configuration
│   │   ├── prompting/         # Prompting guides
│   │   ├── runtimes/          # Runtime configuration
│   │   ├── architecture/      # Architecture documentation
│   │   ├── customization/     # Customization guides
│   │   └── troubleshooting/   # Troubleshooting guides
│   └── python/                # Python-specific documentation
├── static/                    # Static assets (images, etc.)
├── docs.json                  # Main configuration file
├── mint.json                  # Mintlify configuration
├── README.md                  # Repository README
└── OPENHANDS_MIGRATION.md     # Documentation of migration process
```

Key files:
- `docs.json`: Defines the navigation structure and site configuration
- `mint.json`: Contains Mintlify-specific settings
- `modules/index.mdx`: Main landing page for the documentation

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
   - About
   - Key Features

2. **Getting Started** - Installation and basic usage
   - Installation
   - Getting Started

3. **OpenHands Cloud** - Cloud-specific documentation
   - Overview
   - GitHub Installation
   - GitLab Installation
   - Cloud UI
   - Cloud API
   - Issue Resolver

4. **Usage Methods** - Different ways to use OpenHands
   - CLI Mode
   - GUI Mode
   - Headless Mode
   - GitHub Action
   - Evaluation Harness
   - WebSocket Connection

5. **Customization** - Repository customization and microagents
   - Repository Customization
   - Microagents Overview
   - Microagents Repo
   - Microagents Org
   - Microagents Public
   - Microagents Keyword

6. **Advanced Configuration** - LLM and runtime configuration
   - LLM Backends
   - Runtime Options
   - Configuration Options

7. **Developer Resources** - Architecture and development guides
   - Development Overview
   - Backend Architecture
   - Runtime Architecture
   - Custom Sandbox Guide
   - Debugging

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

2. Run the development server:
   ```bash
   mintlify dev
   ```

### Troubleshooting

- If Mintlify dev isn't running:
  ```bash
  mintlify install
  ```

- If a page loads as a 404, make sure you are running in a folder with `docs.json`

### Publishing Changes

Changes are automatically deployed to production after pushing to the default branch if the GitHub App is installed.