# Placeholders, embeds, and other guide sections

> Use for sample values, videos, icons, file downloads, DNS provider lists, tables of contents, and review dates. Each section restates the matching section of the style guide (`src/source/content/style-guide.md`). If they differ, the style guide wins.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md` for the workflow.

## Placeholder text

Use these sample values so docs stay consistent and never point at a real account or address.

- Organization: `Anita Agency`
- Site name: `Anita Drupal`
- IP addresses: the range reserved for documentation, `203.0.113.0–203.0.113.255`

For other sample values, make them obviously fake. Define repeated values once in "Before you begin" (see the variables pattern in `components-and-variables.md`) and reuse them.

## Videos

Use the `Youtube` and `Wistia` components.

- **YouTube:** set both `title` and `src`.
  ```markdown
  <Youtube src="AcL-v1j_XX0" title="Installing Drupal with demo content for Front-End Sites" />
  ```
- **Wistia:** set only `src`, without `title`.
  ```markdown
  <Wistia src="7gn1g3ljz6">

  </Wistia>
  ```
- Landing pages can set a `video_id` attribute in `src/source/data/landings.yaml`. Check the style guide's Videos section for the details.
- Pair every video with written steps. Don't put essential information only in a video.

## Icons

Use the `Icon` component. The list of available icons is in the style guide's Icons section. A few legacy icons are deprecated but still available for the site dashboard.

```markdown
<Icon icon="userPlus" text="Add user" />
```

## File downloads and DNS provider lists

- Link a downloadable file with `<Download file="pantheon-backup-to-s3.sh" />`. Store files in `source/scripts`.
- `<DNSProviderDocs />` builds a bulleted list of the DNS provider docs in `source/content/dns-providers`. It skips docs with `draft: true`.

## Table of contents

Add a table of contents on the right side of a doc with `showtoc: true` in frontmatter.

## Review dates

Review dates record the last time a member of the documentation team reviewed a doc. Two ways to set one:

- Frontmatter: `reviewed: "YYYY-MM-DD"` (the usual way; set it to today when you create or review a doc).
- A section-level component:
  ```markdown
  ### Section title
  <ReviewDate date="YYYY-MM-DD" />
  ```
