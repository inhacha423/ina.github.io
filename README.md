# Inha Cha’s research portfolio

This Jekyll site contains Home, Projects, and CV pages.

Design system: see [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) for fonts, color tokens, layout rules, and editing locations. Open `/design-system.html` in the local preview to inspect colors, typography, and live components.

All pages use the Dusty Rose + Warm Paper background in `assets/css/site.css`. The previous Muted Coral + Aged Paper and Faded Lilac + Blush backgrounds are preserved in `assets/css/saved-palettes.css`. That file is not loaded by the site; load it after the page stylesheet to restore those page-specific backgrounds.

| To edit | File |
| --- | --- |
| Biography and Home sections | `index.html` |
| News, publications, and contact links | `_data/news.yml`, `_data/publications.yaml`, `_data/contact.yml` |
| Projects | `_data/projects.yaml` (gallery titles, links, and thumbnail paths) |
| New project starter | `_templates/project.html` (copy into `projects/`) |
| Shared project header and blocks | `_includes/project-header.html`, `_includes/project-block.html` |
| Shared navigation | `_layouts/homepage.html` |
| Shared fonts, colors, and navigation | `assets/css/site.css` |
| Home, Projects, and CV styles | `assets/css/home.css`, `assets/css/projects.css`, `assets/css/cv.css` |
| Logo, portrait, and PDF download paths | `_data/files.yml` |
| CV section order and entries | `_data/cv.yml` (publications come from `_data/publications.yaml`) |


## File structure

```text
_templates/
  project.html              # Copy to start a new project page
_layouts/
  homepage.html             # Shared page shell and navigation
  project-detail.html       # Header → hero image/video → content → note
_includes/
  project-header.html       # Title, subtitle, credit, and Role
  project-hero.html         # Hero image, video, or PDF
  link-arrow.html           # Shared SVG arrows (external, down, left)
  project-block.html        # Image, video, and text blocks
  cv-date.html              # CV date-range formatting
_data/                      # Projects, publications, CV, news, and file paths
projects/
  upstage.html              # Each project's content and metadata
  reuse-it.html
  ...
assets/
  css/                      # Shared tokens and page styles
  projectimages/            # One image folder per project
  images/                   # Shared logo and portrait
  documents/                # Downloadable documents
index.html                  # Home
cv/index.html               # CV
projects.html               # Project gallery
design-system.html          # Design reference
```

## Updating uploaded files

Store shared images such as the portrait and logo in `assets/images/`. For project images, create a subfolder in `assets/projectimages/` for each project, for example `assets/projectimages/ethics-pathways/cover.jpg`. Store PDFs and other downloadable documents in `assets/documents/`. To replace the portrait, logo, or CV, upload the new file to its folder and change the corresponding path in `_data/files.yml`. Replacing a file under the same name requires no configuration change. Commit the file and its path change together.

Use a repository path starting with `/assets/`. The templates apply Jekyll’s `relative_url` filter so links work in local previews and under the GitHub Pages project URL.

## Local preview

With Jekyll installed, run `jekyll serve` from the repository root. The shared layout loads `site.css` and the stylesheet that matches each page's `nav_item`.

## CV entries

Edit entries and the order of the dated sections in `_data/cv.yml`. The `section_order` list controls their headings and order. Publications are shared with Home through `_data/publications.yaml`, and Academic Services appears below them in `cv/index.html`.

For a publication, `venue` is the full CV label. `venue_short` is the abbreviated Home label, and optional `venue_url` makes that abbreviation clickable.
Add a `links` item with `label: bibtex` and a `url` to activate the BibTeX button beside PDF. Until then, it appears as a disabled placeholder.

## Project pages

For a new project, copy `_templates/project.html` into `projects/<project-name>.html`, then add its gallery entry to `_data/projects.yaml`. Every detail page uses `_includes/project-header.html` for the same heading order: `title` → `subtitle` → `role` → hero image or video. Empty subtitles and roles are hidden without reserving blank space.

Header styling is shared in `assets/css/projects.css`: title 32–44px, subtitle 16px, Role label 12px and value 13px. Title-to-subtitle spacing is 16px, subtitle-to-Role spacing is 6px, and the header-to-hero gap is 24px.

All project detail pages and the starter template use the shared `.project-body` style: Inter 17px / weight 300 / line-height 1.6, with .8em between paragraphs. This applies to text-only, image-with-text, and video-with-text blocks. Change this style once in `assets/css/projects.css` to update every project; no per-page font settings are needed.

Set `subtitle_url` to turn the subtitle into an external link. The template adds the SVG arrow automatically; keep the subtitle text free of arrow characters. Use optional `credit` for a team or project credit below it; leave `role` empty when no role label is needed.

To crop a hero without changing the original image file, set `hero_width`, `hero_height`, and `hero_crop: {top: 4, right: 80, bottom: 4, left: 80}`. Crop values are pixels in the original image, and the same crop scales to every viewport.

Reuse-it, Rullen Bandet, Naver Labs, and Shadia 2017 use images migrated from the old portfolio. See [PROJECT_ASSETS.md](PROJECT_ASSETS.md) for the original-to-current filename mapping. Their blocks are configured directly in each project page.

Each file in `projects/` starts with a title, role, and hero image path. Until you add project-specific `blocks`, it displays the examples in `_data/project_template.yml`. To replace the examples, add a `blocks` list to that project's file. Project images belong in `assets/projectimages/<project-name>/`. The shared layout is `_layouts/project-detail.html`, block markup is `_includes/project-block.html`, and styling is in `assets/css/projects.css`.

Gallery crop settings live in `_data/projects.yaml`: `image_position` sets the focal point (for example `left center` or `14% center`), and optional `image_scale` makes a small fixed zoom from the left edge. These only affect gallery thumbnails; source files and detail images retain their original composition. Gallery titles are left-aligned.
For a logo thumbnail, set `image_style: logo` to use a white background, 24px padding, and an uncropped image.

Add blocks to a project page like this:

Optional front-matter fields: `subtitle` adds supporting text under the title, `hero_caption` adds a small caption below the hero image, `content_width: reading` limits full-width text blocks to 68ch, and `note` adds a smaller italic note after the content. The gallery title remains separately editable in `_data/projects.yaml`.

```yaml
role: "Research, UX design"
hero: /assets/projectimages/everyday-resistance/hero.jpg
hero_alt: "Project overview"
blocks:
  - type: image
    image: /assets/projectimages/reuse-it/detail-01.png
    alt: "Describe the image"
    # caption: "Location or image description"
    # width: 2512  # Optional original dimensions reserve space while loading
    # height: 1194
  - type: image_text
    image: /assets/projectimages/everyday-resistance/process.jpg
    alt: "Design process"
    text: |
      Describe the process here.
  - type: text
    title: Findings
    text: |
      Write a full-width paragraph here.
  - type: two_images
    image_left: /assets/projectimages/everyday-resistance/one.jpg
    alt_left: "First view"
    image_right: /assets/projectimages/everyday-resistance/two.jpg
    alt_right: "Second view"
  - type: image_left
    image: /assets/projectimages/everyday-resistance/left.jpg
    alt: "Left view"
    title: Approach
    text: "Write beside the image."
  - type: image_right
    image: /assets/projectimages/everyday-resistance/right.jpg
    alt: "Right view"
    title: Outcome
    text: "Write beside the image."
```

Copy, remove, or reorder blocks as needed. Use `hero` for the full-width image below the title. An empty `hero` displays a placeholder until an image is added.

For a `two_images` block, add `gap: none` to remove the gap between the images. Optional `width_left`, `height_left`, `width_right`, and `height_right` reserve each image's original proportions while loading. These pairs stack vertically on screens 700px wide or narrower.

### YouTube and Vimeo

Add a `video` block to a project's `blocks` list. Use the video's ID, not its full watch URL. Both players use a responsive 16:9 frame, lazy loading, playback controls, and fullscreen support. They do not autoplay. The video's hosting settings must allow embedding.

```yaml
  - type: video
    provider: youtube
    video_id: "YOUR_YOUTUBE_ID"
    video_title: "Project demonstration"
    # title: Demo          # Optional heading
    # text: "Description"  # Optional paragraph below the video

  - type: video
    provider: vimeo
    video_id: "YOUR_VIMEO_ID"
    video_title: "Project walkthrough"
```

For YouTube, copy the ID after `watch?v=` or `youtu.be/`. For Vimeo, copy the numeric video ID. `video_title` is the accessible name of the player. Empty IDs or unsupported providers do not render a player.

To replace a project's top hero image with a video, add `hero_video` to its front matter (outside `blocks`):

```yaml
hero_video:
  type: video
  provider: vimeo
  video_id: "345037607"
  video_title: "Reuse-it project video"
```

`hero_video` takes precedence over `hero`. The hero video loads immediately; videos inside content blocks load lazily.

Provider references: [YouTube embedded players](https://developers.google.com/youtube/player_parameters), [Vimeo player parameters](https://help.vimeo.com/hc/en-us/articles/12426260232977-About-Player-Parameters).

### PDF reader

Save project PDFs in `assets/documents/<project-name>/`. To show a PDF reader below the project header, use:

```yaml
hero_pdf:
  type: pdf
  file: /assets/documents/why-phd-is-so-hard/zine.pdf
  pdf_title: "Why PhD is SO Hard zine"
blocks: []
```

The same `type: pdf` block can be placed inside `blocks`. It uses the browser's built-in PDF viewer, so controls and mobile support depend on the browser. Open and download links are always shown outside the viewer. `hero_pdf` takes precedence over image/video heroes; `blocks: []` suppresses sample content.

Why PhD is SO Hard shows PNG exports of each PDF page in `assets/projectimages/why-phd-is-so-hard/pages/` after a PDF reader block. The page order is listed explicitly in its project HTML. `hide_hero: true` omits the empty hero placeholder so the PDF reader follows the header directly. Each PNG preserves the full PDF page or spread, with a longest edge of 2000px. The source PDF is unchanged; regenerate the PNGs when replacing it.

Image blocks accept an optional `caption`, using the same centered, muted `.project-caption` style as `hero_caption`. Link arrows are rendered by `_includes/link-arrow.html` with explicit em-based dimensions to keep their appearance consistent even before CSS loads. Local stylesheet URLs include a build version so browsers refresh cached styles after deployment.

## Credits

The HTML CV layout adapts the dated-entry structure from [Donghoon Shin’s CV theme](https://github.com/donghoon-io/donghoon-io.github.io).

Forked from [Jungsoo Park’s website](https://github.com/JJumSSu/JJumSSu.github.io), based on Martin Saveski’s template. The news layout was inspired by [Donghoon Shin’s website theme](https://github.com/donghoon-io/donghoon-io.github.io).

### Responsive project photographs

Everyday Resistance preserves original JPEGs and serves WebP copies from its `optimized/` folder at 800, 1200, and 1600px widths. Image blocks accept a `sources` list of `image` paths and numeric `width` values plus a `sizes` string. The shared image block builds `srcset` with deployment-aware URLs. Keep `image` as the largest fallback and specify its `width` and `height` to reserve space.

To regenerate variants after replacing a source, run `python3 scripts/optimize-project-images.py path/to/photo.jpg` with Pillow installed. The script respects EXIF orientation, preserves embedded color profiles, and leaves originals unchanged. It generates WebP at quality 88 and removes unnecessary photo metadata. Existing blocks without `sources` continue to use a single image.

Google Drive videos also use the shared `video` block: set `provider: google_drive` and `video_id` to the file ID between `/d/` and `/view` in its sharing URL. The block embeds Drive's `/preview` player. The owner must allow visitors to view the file in Drive's sharing settings.
