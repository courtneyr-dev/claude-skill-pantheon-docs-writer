# MDX components and variables

> Use when a page needs callouts, accordions, tabs, partials, popovers, product cards, definitions, or the variables pattern.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Step 6: MDX Components

### Callouts / Alerts

```html
<!-- Info note -->
<Alert title="Note" type="info">

Use notes for important information the reader shouldn't miss.

</Alert>

<!-- Warning -->
<Alert title="Warning" type="danger">

Use warnings for critical info, especially things that can cause data loss.

</Alert>

<!-- Variable export -->
<Alert title="Exports" type="export">

This process uses [Terminus](/terminus) extensively. Set the variables `$site` and `$env`:

```bash{promptUser: user}
export site=yoursitename
export env=dev
```

</Alert>
```

### Accordion (Panel)

Use for extraneous but useful info — troubleshooting details, pro tips, optional steps.

```html
<Accordion title="Panel Title" id="unique-id" icon="wrench">

### Panel content header

Additional context or advanced instructions.

</Accordion>
```

### Tabs (CMS-specific content)

```html
<TabList>

<Tab title="WordPress" id="wp-example" active={true}>

WordPress-specific instructions here.

</Tab>

<Tab title="Drupal" id="d7-example">

Drupal-specific instructions here.

</Tab>

</TabList>
```

### Partials (Reusable Content)

Before writing content that might already exist:
1. Search `src/source/content/partials/` for existing partials on the topic
2. If reusable content exists, include it: `<Partial file="partial-name.md" />`
3. If creating new reusable content, put it in `src/source/content/partials/` and include via `<Partial>`

Partial files don't need frontmatter.

### Popovers (Tooltips)

```markdown
Given two sites with slugs <Popover title="Slugs" content="URL-friendly descriptions for a site." /> `first-site` and `second-site`:
```

### Product Cards

```html
<ProductGroup>

  <Product title="Product Name" link="/product-path">

  Short description of this product.

  </Product>

</ProductGroup>
```

### Definitions

Use `<dfn>` for new terms — they're indexed to the Glossary automatically:

```html
<dfn id="unique-slug">Term</dfn>
```

## Step 7: Variables Pattern

When a guide requires the reader to substitute values (site names, env names, etc.), define them upfront with an export callout in "Before you begin":

```html
<Alert title="Exports" type="export">

Before we begin, set the variables `$site` and `$env` in your terminal:

```bash{promptUser: user}
export site=yoursitename
export env=dev
```

</Alert>
```

Then reference them consistently: `$site`, `$env`, `$uuid`, etc. (lowercase for variables, uppercase for constants).
