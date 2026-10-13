# Navigation and redirects

> Use when adding a page to the site navigation, or when moving, renaming, or deleting a URL. Checked against `pantheon-systems/documentation` main@9b15056.
>
> **Propose, don't apply.** Navigation and redirect changes move readers' URLs and menus. Describe the change and give the coverage table; edit `src/components/omni-components/` or `src/middleware.ts` only when the user asked for that change. A prose edit or a page review never includes one.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Adding pages to navigation

Site navigation is defined in `src/components/omni-components/`. Each section of the nav has its own TypeScript file. Navigation is not driven by frontmatter — you must explicitly add new pages to the appropriate omni-component file. `index.ts` assembles the sections and adds Docs Home and an external Content Publisher link; `helpers.ts` holds `simpleLink` and `getGuideDirectory`.

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
| `learning.ts` | Learning |
| `about.ts` | About |

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

## Creating redirects

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

No test or script validates `RedirectMap`, so check each old path against the file by hand, and check that the new path resolves to a page.

### In your PR

When a PR contains redirects, include a summary table in the PR body so reviewers can verify coverage:

```markdown
| From | To |
|---|---|
| `/old-path` | `/new-path` |
| `/old-path/sub-page` | `/new-path/sub-page` |
```

A **Redirect** label on redirect PRs is unconfirmed: nothing in `.github/`, `CONTRIBUTING.md`, or the workflows of main@9b15056 mentions it (a label can still exist in GitHub). Ask the docs team before you tell anyone to add it.
