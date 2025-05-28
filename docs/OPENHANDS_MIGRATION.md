# OpenHands Documentation Migration

This document describes the process of migrating the OpenHands documentation from the original Docusaurus format to Mintlify.

## Migration Process

1. **Initial Setup**
   - Created a new branch `openhands-docs-migration` for the migration work
   - Cloned the OpenHands repository to access the original documentation

2. **Content Migration**
   - Copied all documentation files from OpenHands/docs/modules to docs/modules
   - Copied static assets (images, etc.) from OpenHands/docs/static to docs/static
   - Updated docs.json to include the new content structure based on OpenHands sidebars.ts

3. **Format Conversion**
   - Added frontmatter to all markdown files
   - Converted Docusaurus-specific syntax to Mintlify format:
     - `:::note` blocks to `<Note>` components
     - `:::tip` blocks to `<Tip>` components
     - `:::warning` blocks to `<Warning>` components
     - `<details><summary>` to `<Accordion>` components
     - Blockquotes to `<CodeGroup>` components
   - Updated relative links to absolute paths
   - Fixed image references

4. **Quality Assurance**
   - Fixed conversion issues with a cleanup script
   - Manually reviewed and fixed problematic files
   - Tested documentation with Mintlify CLI

## File Structure

The migrated documentation follows this structure:

```
modules/
├── index.mdx                  # Main landing page
├── usage/                     # Core documentation
│   ├── about.md               # About OpenHands
│   ├── installation.mdx       # Installation guide
│   ├── getting-started.mdx    # Getting started guide
│   ├── key-features.md        # Feature overview
│   ├── cloud/                 # Cloud-specific documentation
│   ├── how-to/                # How-to guides
│   ├── llms/                  # LLM configuration
│   ├── prompting/             # Prompting guides
│   ├── runtimes/              # Runtime configuration
│   ├── architecture/          # Architecture documentation
│   ├── customization/         # Customization guides
│   └── troubleshooting/       # Troubleshooting guides
└── python/                    # Python-specific documentation
```

## Navigation Structure

The navigation structure in docs.json is organized into the following tabs:

1. **Overview** - General introduction to OpenHands
2. **Getting Started** - Installation and basic usage
3. **OpenHands Cloud** - Cloud-specific documentation
4. **Usage Methods** - Different ways to use OpenHands
5. **Customization** - Repository customization and microagents
6. **Advanced Configuration** - LLM and runtime configuration
7. **Developer Resources** - Architecture and development guides
8. **Help & Support** - Troubleshooting and feedback

## Future Improvements

Some potential improvements for the future:

1. Add more code examples and interactive components
2. Create a dedicated API reference section
3. Add more diagrams to explain complex concepts
4. Improve search functionality with better metadata
5. Add version selector for different OpenHands versions