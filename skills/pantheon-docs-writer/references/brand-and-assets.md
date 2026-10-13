# Brand colors, logos, and icons

> Use when a page, image, diagram, or Google Doc shows Pantheon branding: a cover, a diagram, a status table, a share image. Not needed for plain prose.
> Part of the `pantheon-docs-writer` skill. Return to `../SKILL.md`.
> Adapted from the Pantheon brand reference in `pantheon-skills:pantheon-docs` (v0.6.4, copied 2026-10-12). That skill makes branded business documents; this file keeps what a docs author needs. The assets are in `../assets/`.

## Which palette applies

| Work | Palette | Where it's defined |
|---|---|---|
| Branded Google Docs, diagrams, status tables, covers | The brand palette below | This file |
| Screenshot annotations in Figma | The Annotation kit (Pantheon Design System tokens: purple `#7952A8`, gold `#FFCA28`) | The `screenshots-to-docs` skill, `docs/reference/annotation-kit.md` |
| Pages on docs.pantheon.io | The site's own theme and components. Don't set colors or fonts in page content. | `components-and-variables.md` |

The two palettes differ on purpose. Don't mix them in one image: a diagram uses the brand palette, an annotated screenshot uses the kit.

## Identity

- Write "Pantheon", never "pantheon" or "PANTHEON", in body text. All caps is fine for a wordmark in a heading or display context.
- Don't put the marketing tagline ("The Platform for Extraordinary Websites") or sub-tagline ("Secure. Fast. Reliable.") in docs pages. The style guide bans hyperbole and unverifiable claims, and the taglines are marketing copy.

## Colors

| Name | Hex | Use |
|---|---|---|
| Black | `#23232D` | Body text, titles, dark backgrounds |
| Yellow | `#FFDC28` | Links on dark backgrounds, highlights, warning status |
| White | `#FFFFFF` | Text on dark backgrounds, table header text |
| Dark purple | `#3017A1` | Table label columns, subtitles, section dividers |
| Medium purple | `#5F41E5` | Subheadings, calls to action, captions |
| Light purple | `#D0C6FF` | Divider backgrounds, accent fills |
| Pink | `#DE0093` | Highlights, fail status |
| Green | `#218C5F` | Pass status |
| Medium gray | `#DFDFEC` | Section backgrounds, unknown status, rules |
| Light gray | `#F4F4FC` | Table row fills, page backgrounds |
| Blue | `#0F62FE` | Links on light backgrounds |

### Status colors

Use these for any status, result, or health indicator, and pair the color with a word or symbol so the meaning doesn't depend on color alone (accessibility):

| Status | Color | Hex |
|---|---|---|
| Pass, approved, positive | Green | `#218C5F` |
| Warning, neutral, in progress | Yellow | `#FFDC28` |
| Fail, negative, blocked | Pink | `#DE0093` |
| Not started, unknown | Medium gray | `#DFDFEC` |

Check contrast before you put text on a fill. Contrast ratios computed 2026-10-12 against WCAG AA (4.5:1 for normal text, 3:1 for large text):

| Fill | White text | Black `#23232D` text |
|---|---|---|
| Black, dark purple, medium purple, blue | 5.0 to 15.6: passes | too low |
| Pink `#DE0093` | 4.64: passes, narrowly | 3.35: large text only |
| Green `#218C5F` | **4.22: fails for normal text**; passes only for large text (18 pt, or 14 pt bold) | 3.69: large text only |
| Yellow, light purple, medium gray, light gray | too low | 9.8 to 14.2: passes |

Green is the one trap: a pass badge with small white text on `#218C5F` misses AA. Use large text (18 pt, or 14 pt bold), or put dark text and a symbol beside a green swatch instead. Captions in medium purple `#5F41E5` pass on white (6.22) and on light gray (5.69).

## Fonts (Google Docs deliverables only)

Poppins for headings and tables, Aleo Italic for cover subtitles, Inter for body text. All three are free Google Fonts, already in Google Docs. Never substitute another typeface. Pages on docs.pantheon.io use the site's fonts, so don't apply these there.

| Style | Font | Size | Color |
|---|---|---|---|
| Title (cover) | Poppins Bold | 24 pt | `#23232D` |
| Subtitle (cover) | Aleo Italic | 20 pt | `#6D6D78` |
| Heading 1, 2, 3 | Poppins SemiBold | 18, 14, 12 pt | `#23232D` |
| Heading 4 | Poppins Italic | 11 pt | `#23232D` |
| Body | Inter Regular | 11 pt | `#23232D` |
| Table header, horizontal | Poppins SemiBold 10 pt | white on `#23232D` | |
| Table header, vertical | Poppins SemiBold 10 pt | white on `#3017A1` | |
| Table body | Poppins Regular | 10 pt on `#F4F4FC` | |
| Caption, footnote | Poppins Regular | 9 pt | `#5F41E5` |

Tables: a 1.5 pt white border between cells, 0.069 in padding on all four sides, full width.

For slides: Poppins Bold 28 pt titles, Aleo Italic 16 pt subtitles, Poppins Bold 14 pt subheads, Inter 10 pt body.

## Logos and icons

Files are in `../assets/`: `pantheon-logo/logo-black` and `logo-white` (PNG and SVG), `pantheon-icon/logo-fist-black` and `logo-fist-white` (PNG and SVG). See `../assets/README.md` for sizes and where they came from.

- Black version on white or light backgrounds. White version on dark or colored backgrounds.
- Clear space on all sides at least the height of the "P" in the wordmark.
- Never distort, rotate, recolor, or add a shadow. Never place on a pattern or photo without a solid backing.
- A partner logo next to Pantheon's uses the black or white version only.
- Cover page of a branded Doc: top left, about 1.5 in wide and 0.54 in tall. Not needed in the footer. Optional on internal memos, cover only.
- Give every logo or icon image alt text: "Pantheon logo", or "Pantheon" for an icon used as a decoration with text beside it.
- Don't add logos to docs.pantheon.io pages without asking the docs team. A search of `src/source/content` (main @ 9b15056) found no Pantheon logo images in page content, and the site template carries the brand.

## Google Doc layout

Margins: 1 in top and bottom, 1.25 in left and right. Footer on every page except the cover: page number centered, "© [YEAR] Pantheon Systems, Inc." on the right, a 0.5 pt `#DFDFEC` rule above it. The cover has no page number; the first body page starts at 1.

## Voice

The brand reference describes a direct, data-driven, structured tone. The docs style guide and `voice-rules.md` govern docs pages and win on any conflict: no be verbs, no hyperbole, sentence-case headings. Use the brand tone only for branded business documents, and keep numbers over adjectives there too ("TTFB fell 42%", not "performance improved").

## For a full branded business document

A report, SOW, memo, or project plan needs more than this file: cover, document-type structure, and Google Doc creation. Use the `pantheon-skills:pantheon-docs` skill for those. This file covers the brand pieces a docs author reaches for.
