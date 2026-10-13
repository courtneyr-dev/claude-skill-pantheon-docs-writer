# Document structure

> Use when laying out a page: intro, Before you begin, content sections, Troubleshooting, More resources.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Document structure

### Standard section order

1. **Introductory paragraph** — one paragraph explaining what this doc covers and what the reader will accomplish. No heading.
2. **Before you begin** (`## Before you begin`) — prerequisites only. Use a bulleted list.
3. **Content sections** — `##` for major steps, `###` for subsections. Don't go deeper than `###` unless unavoidable.
4. **Troubleshooting** (`## Troubleshooting`) — if applicable. Error messages as `###` headers, verbatim.
5. **More resources** (`## More resources`) — 3–5 links. Last section. Always present.

### Before you begin

```markdown
## Before you begin

Be sure that you have:

- An existing WordPress site on Pantheon, or [create](https://dashboard.pantheon.io/sites/create) one.
- [Terminus](/terminus) installed on your local computer.
- A [local clone](/guides/git/git-config#clone-your-site-codebase) of your site's codebase.
```

If the guide uses shell variables, add the export callout here (see Variables section below).

### Troubleshooting

Error message headers are `###`, written verbatim as they appear in the UI/terminal. This makes them findable by search.

```markdown
### RedisException: Redis server went away
```

### More resources

```markdown
## More resources

- [Getting Started with Terminus](/terminus)
- [Git on Pantheon Guide](/guides/git)
```
