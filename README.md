# ECF2 – Company Website

A static, SCSS-powered marketing site. It uses semantic HTML and a modular SCSS architecture to produce a single compiled stylesheet. There is no JavaScript in this project (by design and due to timeline constraints). All interactions and layout are achieved with HTML + CSS.

## Overview
- Purpose: Present services, process, technology stack, and resources in a clean, responsive layout.
- Stack: HTML5 + SCSS (compiled to CSS). No JavaScript.
- Build: `sass` compiles `src/scss/main.scss` → `dist/css/main.css`.
- Assets: Images live under `dist/images/...` and are referenced from HTML and CSS.

## How It Works (No JavaScript)
There is no JavaScript bundle or runtime. The site relies on:
- Semantic HTML sections for content structure
- CSS Grid/Flexbox for layout and responsiveness
- SCSS variables, mixins, and partials for maintainability

Examples of CSS-only behaviors used:
- Decorative lines and separators (e.g., `.how__line`, `.how__line--vertical`)
- Grid alignment tweaks (e.g., centering or shifting second-row logos)
- Responsive breakpoints for layout changes

## Project Structure

```
ECF2/
	index.html                 # Main HTML page
	README.md                  # This file
	src/
		scss/
			base.scss              # Base/element resets and typography foundations
			body.scss              # Main page sections + component styles
			footer.scss            # Footer-specific styles
			header.scss            # Header-specific styles
			main.scss              # SCSS entry point that @uses all partials
			mixins.scss            # Reusable SCSS mixins (helpers/shortcuts)
			responsive.scss        # Media queries and responsive helpers
			variables.scss         # Design tokens: colors, spacing, sizes
	dist/
		css/
			main.css              # Compiled CSS output (generated)
		images/                 # Image assets used by the site
```

Notes:
- `dist/` is build output (compiled CSS, images). It is typically ignored by Git (see Git section).
- Some assets include partner logos and icons referenced in `index.html` and component styles.

## HTML Structure (index.html)
Key sections and notable elements:
- Header: global branding and navigation (styles in `header.scss`).
- Hero/Intro: top-of-page content establishing value props (styles in `body.scss`).
- “Tech Stack” (`.tech`):
	- Uses a 5-column CSS Grid for logos (`.tech__logos`).
	- When there are 9 logos (1 short of a full 10-slot grid), a wrapper (`.tech__secondary`) can align the second row as needed (center or left) without changing gaps.
- “How (Timeline)” (`.how`):
	- Decorative horizontal rail (`.how__rail`) with positioned trophy icon.
	- Cards for steps arranged across two grid rows.
	- `.how__line` is a short horizontal accent under the section title.
	- `.how__line--vertical` is a vertical pill used beside highlighted quotes.
- “Way of building” quotes:
	- Highlighted with `.way__quote` and optionally wrapped by `.way__quote-row` to add a vertical accent using `.how__line--vertical`.
- “Resources” (`.resources`):
	- Horizontal scrolling cards using CSS only (no JS), with snap alignment.
- CTA section (`.cta`): a gradient button and illustrative graphic.
- Footer: accessible layout for brand, navigation, contact details, and social links (styles in `footer.scss`).

Accessibility considerations:
- Semantic elements (`section`, `article`, `h1`–`h3`) with logical heading order.
- Decorative elements marked with `aria-hidden="true"` where appropriate.
- Sufficient color contrast via tokenized variables.

## SCSS Architecture
- `main.scss`
	- Entry point; uses/imports other partials. Compile this file to generate the site CSS.

- `variables.scss`
	- Central design tokens: color palette (e.g., `$primary-color`, `$text-color`, `$text-muted`, `$second`), spacing scales, breakpoints, etc.

- `mixins.scss`
	- Reusable helpers (e.g., clearfix, visually-hidden, media query wrappers, gradient/text utilities) to keep selectors concise and DRY.

- `base.scss`
	- Normalize/base styles: box-sizing, default typography rules, links, lists, and basic element resets.

- `responsive.scss`
	- Centralized media queries and breakpoint utilities used across sections.

- `header.scss`
	- Styles for the site header (branding, nav alignment, spacing, responsive tweaks).

- `footer.scss`
	- Footer grid layout, social icons sizing, badges, and responsive behavior.
	- Social icons sized for comfortable tap targets; spacing tuned per design updates.

- `body.scss`
	- Main section styles. Examples of notable selectors:
		- `.tech`, `.tech__container`, `.tech__logos` (5-col grid), and `.tech__secondary` (wrap for second-row logos).
		- `.how`, `.how__rail`, `.how-card` variants, `.how__line`, `.how__line--vertical`.
		- `.resources` cards with scroll-snap.
		- `.cta` button and layout.
		- `.text-highlight`, `.way__quote`, `.way__quote-row`.

## Build and Run

You can compile SCSS using the Sass CLI. Example (PowerShell on Windows):

```powershell
Push-Location "C:\Users\nalin\OneDrive\Desktop\ecf2\ECF2"
npx --yes sass src/scss/main.scss:dist/css/main.css --no-source-map --style=expanded
Pop-Location
```

Optional: if you use a live compiler (e.g., VS Code extension), ensure it points to `src/scss/main.scss` and outputs to `dist/css/main.css`.

## Version Control (Git)
- Repository: standard Git project; work should be done on feature branches and merged via pull requests.
- Branching: an example branch used during development is `feature_footer` for footer and related UI changes.
- Pushing policy: compiled assets are generally not pushed; keep pushes on hold until explicitly approved if that’s part of your workflow.
- `.gitignore`: typically excludes build artifacts like `dist/` (e.g., `dist/css/main.css`). If you ever need to commit build output, you can force add: `git add -f dist/css/main.css`.

Suggested workflow:
1. Create a branch: `git checkout -b feature/<name>`
2. Make changes; compile SCSS
3. Commit: `git add -A && git commit -m "Describe your change"`
4. Push when approved: `git push -u origin feature/<name>`

## Conventions and Notes
- Naming: BEM-style class names (e.g., `.tech__logos`, `.how-card__title`).
- Layout: CSS Grid for section layouts; Flexbox for alignment.
- No JS: there is intentionally no `*.js` file; interactions are purely CSS/HTML.
- Images: stored in `dist/images/...` and referenced directly; prefer transparent PNG/SVG where appropriate.

## Recent UI Details
- Added vertical accent next to specific quotes using `.how__line--vertical` inside `.way__quote-row`.
- Adjusted Tech logos grid:
	- When 9 logos are present in a 5-column layout, the second row can be centered via grid placement or wrapped in `.tech__secondary` to control alignment (center or left) without altering gaps.
- Footer enhancements: accessible structure, larger social icons, tuned spacing, and PageSpeed badge sizing.

## Limitations and Future Work
- JavaScript not included due to timeline; may add later for interactive features (tabs, mobile menu, animations).
- Consider extracting assets to a dedicated `assets/` folder and generating `dist/` only on build.
- Add automated linting/formatting and a minimal CI to catch SCSS errors.

---
If you need help extending this project (adding JS interactivity, more pages, or a build pipeline), feel free to open an issue or start a new feature branch.
