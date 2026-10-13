# Writing style

> Use when drafting or editing prose: voice, headings, emphasis, code formatting, links, lists, tables, images, and where-the-user-is orientation.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Writing style

### Voice and Person (Pantheon + Google)

- Use **second person** ("you", "your") — not "we", "the user", or "one"
- Use **active voice** — "Click **Save**" not "The button should be clicked"
- Use **present tense** — "Terminus returns a list" not "Terminus will return a list"
- Be direct: skip throat-clearing openers ("In this guide, we will cover...")
- Avoid be-verbs where possible ("the config file controls X" not "the config file is what controls X")

### Headings

- Use **sentence case** for all headings: capitalize only the first word, proper nouns, product names (Terminus, Multidev, WordPress), and acronyms. Applies to docs, guides, and release notes alike
  - ✅ `## Exclude specific pages from caching`
  - ❌ `## Exclude Specific Pages from Caching`
- Much existing content still uses title case. Don't mass-convert headings in files you're not otherwise editing, but do convert headings you add or touch
- The page `title:` in frontmatter renders as the H1 — don't repeat it in the body
- Start body content at `##`
- Don't skip levels (no jumping from `##` to `####`)
- Don't end headings with punctuation

### Emphasis

- **Bold** (`**text**`) — UI elements, navigation paths, and new terms on first introduction only. Not for general emphasis.
- _Italics_ (`*text*`) — emphasis within prose. Used sparingly.
- Never use bold for general emphasis — use italics.

### Code Formatting

- Inline code (`\`backticks\``) — file names, directory paths, variables, commands, and output within sentences
- Code blocks — multi-line commands, config files, code snippets
- Always specify the language in fenced code blocks: ` ```bash `, ` ```php `, ` ```yaml `
- Shell prompts: ` ```bash{promptUser: user} ` — adds the `$` prompt automatically without copying it
- Output lines: ` ```bash{outputLines: 2-6} ` — marks those lines as non-copyable output
- File excerpts: ` ```yaml:title=pantheon.yml `

### Links

- Use **relative paths** for internal links: `[Terminus Guide](/terminus)` not full URLs
- Use **descriptive link text** — never "click here" or bare URLs
- Do not specify target tab/window — leave that to the reader
- Do not repeat the URL as link text

### Lists

- Bulleted lists for non-sequential items
- Numbered lists for sequential steps — use `1.` for every item (the site auto-numbers them)
- Parallel grammatical structure within a list
- End list items with punctuation only if they're full sentences

### Tables

- Use `✓` for yes, `❌` for no
- Use `<Popover>` for column header tooltips if needed

### Images

- Always include descriptive alt text: `![Alt text](../images/...)`
- No screenshots with personal info (name, email, UUIDs)
- No markup (arrows, circles) added in screenshot tools — let the doc text do the directing
- Don't screenshot terminal output — describe it in text or use a code block

### Navigation and Location

Always orient the user before giving instructions. Don't say "Click the Backup tab" — first tell them where they are:

```markdown
1. [Go to the Site Dashboard](/guides/account-mgmt/workspace-sites-teams/sites#site-dashboard).
1. Click the **Backup** tab.
```

Standard navigation links:
- Site Dashboard: `[Go to the Site Dashboard](/guides/account-mgmt/workspace-sites-teams/sites#site-dashboard)`
- My Dashboard: `[Go to My Dashboard](/guides/account-mgmt/workspace-sites-teams/workspaces#switch-between-workspaces)`
- Professional Workspace: `[Go to the workspace](/guides/account-mgmt/workspace-sites-teams/workspaces#switch-between-workspaces)`
