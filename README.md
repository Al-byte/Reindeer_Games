# The Reindeer Lock

A standalone Christmas picture keypad using Bootstrap 5.3.8 for responsive layout. Bootstrap CSS is loaded from the official jsDelivr CDN (internet required for the full Bootstrap styles); built-in fallback styles keep the puzzle functional and responsive during offline local preview. No account, build step, tracking, fonts, or paid services. All eight supplied reindeer PNG icons are included in the `images/` directory and used by the puzzle.

## Responsive Bootstrap layout

- The keypad displays **2 columns on phones** (below 576px) and **4 columns on larger screens**.
- The eight answer slots display **two rows of four on phones** and **one row of eight** at 576px and wider.
- Bootstrap containers, responsive spacing utilities, grid columns, and buttons are used on both `index.html` and `next.html`. The Christmas theme and image treatment are preserved.
- Bootstrap CSS uses the official CDN link with Subresource Integrity. Its JavaScript is not needed because the puzzle is controlled by the existing vanilla JavaScript.

## Run and configure

1. Open `index.html` in a browser. Select eight symbols; the eighth selection checks the order automatically.
2. Edit `LOCK_CONFIG` near the start of the script in `index.html` using a text editor.
3. Set `sequence` to exactly eight image IDs in your intended order. Repeated IDs are supported. The demo answer is **Comet → Dasher → Cupid → Vixen → Blitzen → Dancer → Donner → Prancer**. Keep this README away from players if you don't want to give away the answer.
4. The eight reindeer images are already configured as `images/dasher.png` through `images/blitzen.png`. Keep the entire `images/` folder when uploading the website. The original black-on-transparent PNGs are displayed in a light gold tone using CSS filters to remain visible against the dark green interface. Broken images show a letter fallback rather than an SVG placeholder. To change an icon later, update its `src` in the `images` configuration.
5. Set `nextUrl` to your next webpage, e.g. `https://example.com/christmas/room-two/`. It defaults to the included `next.html` sample. Use an empty string for success without a destination.
6. Optional: set `autoRedirect: true` and adjust `redirectDelayMs`. Reset cancels a pending redirect. No progress is saved; refreshing starts a new game.

Undo removes the last selection, Clear empties a current attempt, and Reset puzzle returns to the start even after success. Incorrect attempts remain visible for correction. Keyboard users can Tab through controls and activate with Enter or Space. Status updates are announced to screen readers. No flashing effects or time limit.

## Host on GitHub Pages

Upload `index.html`, `next.html`, and the entire `images/` folder to the root of a GitHub repository. Enable GitHub Pages for its main branch and root folder under the repository's Pages settings. Open the published address shown there. This static project requires no build step; use a public repository for GitHub Free. See the [official GitHub Pages setup guide](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site). You can also upload the same files to any static web host.

## Embed with an iframe

Replace the source with your hosted puzzle address:

```html
<iframe
  src="https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/"
  title="Christmas reindeer sequence puzzle"
  width="100%"
  height="1050"
  style="display:block; width:100%; border:0; border-radius:16px;"
  loading="lazy">
</iframe>
```

The content responds to the iframe width, not the outer browser window width. Allow **at least 1000px of iframe height on phones** for the two-column keypad, or enable scrolling. On larger screens, approximately 750–900px is often enough. Adjust for your site, fonts, and zoom levels. Your website builder must permit custom HTML/iframe embeds, and your host must allow framing.

By default `redirectTarget: '_self'` opens the next page **inside the iframe**. Use `'_top'` to navigate the whole parent page when the player clicks Continue. Browsers may block automatic top-level navigation from an iframe, especially across origins; the visible Continue link lets players navigate with a click. If your site adds a sandbox, allow scripts; top navigation additionally needs `allow-top-navigation-by-user-activation` for the link. Avoid sandboxing for a normal trusted self-hosted embed unless your site requires it. An automatic top redirect may still be blocked by the browser. Some next pages refuse to load in an iframe; use `_top` and the Continue link for those pages.

## Embed directly in an existing HTML page

Include the Bootstrap 5.3.8 CSS link in your host page first (unless it already uses compatible Bootstrap 5). Then copy the two `<style>` blocks, the entire `<main class="reindeer-lock">…</main>` block, and the `<script>…</script>` block, in that order. Keep the `<div class="container-fluid page-shell">` wrapper too if you want the same responsive page padding. Place the script after the puzzle markup. If embedding the puzzle directly on a page, omit the `.reindeer-page` body styling to preserve your site's colors. Bootstrap might affect other elements on that page, so iframe embedding is usually safer. Keep only one lock per page; its IDs must be unique. Relative image and destination paths then resolve against your existing page's address. A restrictive Content Security Policy may require moving the inline styles/script into allowed local files or adding approved nonces.

## Gameplay only

This is a client-side gameplay lock, **not access control**. The answer and destination are visible in page source, and anyone with the destination URL can visit it directly. Use server-side authentication if the destination needs actual protection. The puzzle sends no data and stores nothing.

