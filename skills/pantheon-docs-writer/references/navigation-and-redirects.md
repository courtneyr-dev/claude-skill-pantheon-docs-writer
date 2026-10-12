# Navigation and redirects

> Use when adding a page to the site navigation, or when moving, renaming, or deleting a URL.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Step 11: Adding Pages to Navigation

Site navigation is defined in `src/components/omni-components/`. Each section of the nav has its own TypeScript file. Navigation is not driven by frontmatter — you must explicitly add new pages to the appropriate omni-component file.

### Finding the right nav section

| File | Nav section |
|---|---|
| `get-started.ts` | Get Started |
| `workflows.ts` | Workflows / Develop |
| `go-live.ts` | Go Live |
| `web-infrastructure.ts` | Web Infrastructure / Platform |
| `account-management.ts` | Account Management |
| `terminus.ts` | Terminus |
| `security.ts` | Security |
| `support.ts` | Support |

### Adding a simple link

Use `simpleLink(path, title)` to add a standalone page:

```typescript
simpleLink("/your-doc-slug", "Your Doc Title"),
```

### Adding a guide directory

Use `getGuideDirectory(relativePath, overrideTitle?)` to add an entire multi-page guide. The path is relative to `source/content/`:

```typescript
getGuideDirectory("guides/your-guide-name", "Your Guide Title"),
```

This reads the guide's directory and auto-generates nav entries from the files present. Guide sub-page nav titles come from the `navtitle` frontmatter field if present, otherwise from `subtitle`.

### Adding a link with nested children

```typescript
simpleLink("/parent-path", "Parent Title", [
  simpleLink("/parent-path/child-one", "Child One"),
  simpleLink("/parent-path/child-two", "Child Two"),
]),
```

## Step 12: Creating Redirects

Redirects are required whenever:
- A doc or guide is moved to a new URL
- A doc or guide is deleted (redirect to the nearest related content)
- A URL is restructured

### How to add a redirect

Redirects live in `src/middleware.ts` in the `RedirectMap` object near the top of the file. Add entries as `"/old-path": "/new-path"`:

```typescript
const RedirectMap: Record<string, string> = {
  // ... existing entries ...
  "/old/path/to/doc": "/new/path/to/doc",
};
```

Rules:
- Paths are relative — `/old-path`, not `https://docs.pantheon.io/old-path`
- No trailing slashes on the old path (the file comment is explicit: "Do not add trailing slashes to the old URLs")
- All redirects are 301 permanent
- Add a separate entry for every old URL, including guide sub-pages — not just the parent

### In your PR

When a PR contains redirects:
- Add the **Redirect** label to the PR
- Include a summary table in the PR body so reviewers can verify coverage:

```markdown
| From | To |
|---|---|
| `/old-path` | `/new-path` |
| `/old-path/sub-page` | `/new-path/sub-page` |
```
