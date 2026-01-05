# ECF2 – Company Website

A static, SCSS-powered marketing site. It uses semantic HTML and a modular SCSS architecture to produce a single compiled stylesheet. There is no JavaScript in this project (by design and due to timeline constraints). All interactions and layout are achieved with HTML + CSS.

## Overview
- Purpose: Present services, process, technology stack, and resources in a clean, responsive layout.
- Stack: HTML5 + SCSS (compiled to CSS). No JavaScript.
- Build: `sass` compiles `src/scss/main.scss` → `dist/css/main.css`.
- Assets: Images live under `dist/images/...` and are referenced from HTML and CSS.
 - Responsiveness: Tablet and mobile layouts are handled in `src/scss/responsive.scss` using shared breakpoint tokens.

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
	- Centralized tablet/mobile rules. Uses `$bp-md` (768px) and `$bp-sm` (600px) with `respond-max` mixin.
	- Tablet (≤768px):
		- Header spacing tightened; CTA kept. Desktop menu already hidden.
		- Hero stacks to one column; image centered.
		- Trust becomes single-column; content remains readable.
		- Partners header stacks; logos wrap and center with smaller max-widths.
		- Testimonials hide decorative images/arrows; core content remains.
		- Case studies stack to single column; Way sections stack; Tech tabs spacing reduced; CTA gap adjusted.
	- Mobile (≤600px):
		- Slightly smaller header logo; hero title to 2rem.
		- Service card width reduced (maintains horizontal scroll-snap).
		- Tighter testimonial text padding and avatar gaps; partners logos smaller.
		- Case study padding/gap reduced; Way/CTA headings slightly smaller.

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

### Breakpoints & Mixins
- Breakpoint tokens live in [src/scss/variables.scss](src/scss/variables.scss): `$bp-sm: 600px`, `$bp-md: 768px`, `$bp-lg: 1000px`, `$bp-xl: 1200px`.
- Media helpers are in [src/scss/mixins.scss](src/scss/mixins.scss): `respond-max($bp)` and `respond-min($bp)`.
- A legacy `responsive(tablet)` mixin (max-width: 768px) remains for compatibility; do not remove unless refactoring all call sites.

## Build and Run

You can compile SCSS using the Sass CLI. Example (PowerShell on Windows):

```powershell
Push-Location "C:\Users\nalin\OneDrive\Desktop\ecf2\ECF2"
npx --yes sass src/scss/main.scss:dist/css/main.css --no-source-map --style=expanded
Pop-Location
```

Optional: if you use a live compiler (e.g., VS Code extension), ensure it points to `src/scss/main.scss` and outputs to `dist/css/main.css`.
Tip: If a live compiler emits stray CSS files inside `src/scss/` (e.g., `*.css`, `*.css.map`), delete them to keep sources clean. The only compiled CSS should be `dist/css/main.css`.

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
 - Comments: English-only, ASCII punctuation (avoid smart dashes); section banners use `/* ===== SECTION ===== */` in SCSS and `<!-- ===== SECTION ===== -->` in HTML.
 - Accessibility: Focus-visible rings added via `focus-ring` mixin; decorative elements use `aria-hidden="true"` when appropriate.

## Recent UI Details
- Added vertical accent next to specific quotes using `.how__line--vertical` inside `.way__quote-row`.
- Adjusted Tech logos grid:
	- When 9 logos are present in a 5-column layout, the second row can be centered via grid placement or wrapped in `.tech__secondary` to control alignment (center or left) without altering gaps.
- Footer enhancements: accessible structure, larger social icons, tuned spacing, and PageSpeed badge sizing.
- Responsive pass: added tablet/mobile rules in `responsive.scss` preserving visual intent; hid purely decorative elements on small screens; stacked complex grids (case studies, way, hero) for readability.
- Comment standardization: cleaned and unified English comments in SCSS and `index.html` without altering DOM or output.

## Utility Script: update_process.py
- File: [ECF2/update_process.py](ECF2/update_process.py)
- Purpose: Reads [ECF2/index.html](ECF2/index.html) and replaces any `<section class="process">…</section>` block with a hardcoded HTML template.
- How it works:
	- Opens `index.html` with UTF-8.
	- Uses `re.sub(r'<section class="process">.*?</section>', new_html, flags=re.DOTALL)` to replace matches.
	- Overwrites `index.html` and prints a success message.
- Important for this project:
	- The current site uses the "Way of building" section (`<section class="way">…</section>`), not `process`. As-is, the script will do nothing, or if adapted, it could break styling because its injected markup uses different class names (`process`, `image-wrapper`, etc.) and external images (Unsplash/Pravatar) instead of local assets under `dist/images/...`.
- Risks/limitations:
	- Regex on HTML is brittle; all matches are replaced, and no backup is created.
	- Class names and structure do not align with our SCSS architecture and tokens.
- Recommendations:
	- Prefer not to run this script in the current setup.
	- If automation is required, refactor to use an HTML parser (e.g., BeautifulSoup), create a backup before writing, and inject markup that matches the existing `way` section classes and local image paths.

## Limitations and Future Work
- JavaScript not included due to timeline; may add later for interactive features (tabs, mobile menu, animations).
- Consider extracting assets to a dedicated `assets/` folder and generating `dist/` only on build.
- Add automated linting/formatting and a minimal CI to catch SCSS errors.

---
If you need help extending this project (adding JS interactivity, more pages, or a build pipeline), feel free to open an issue or start a new feature branch.
