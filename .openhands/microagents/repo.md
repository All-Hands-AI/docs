# Repository Knowledge

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

### Links

Internal links should use absolute paths starting with `/`:

```md
[Link to Installation](/modules/usage/installation)
```

## Navigation Structure

The navigation structure is defined in `docs.json`.

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
