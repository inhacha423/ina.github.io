# Inha Cha’s research portfolio

This Jekyll site contains Home, Projects, and CV pages.

All pages use the Dusty Rose + Warm Paper background in `assets/css/site.css`. The previous Muted Coral + Aged Paper and Faded Lilac + Blush backgrounds are preserved in `assets/css/saved-palettes.css`. That file is not loaded by the site; load it after the page stylesheet to restore those page-specific backgrounds.

| To edit | File |
| --- | --- |
| Biography and Home sections | `index.html` |
| News, publications, and contact links | `_data/news.yml`, `_data/publications.yaml`, `_data/contact.yml` |
| Projects | `_data/projects.yaml` (gallery titles, links, and thumbnail paths) |
| Shared navigation | `_layouts/homepage.html` |
| Shared fonts, colors, and navigation | `assets/css/site.css` |
| Home, Projects, and CV styles | `assets/css/home.css`, `assets/css/projects.css`, `assets/css/cv.css` |
| Logo, portrait, and PDF download paths | `_data/files.yml` |
| CV section order and entries | `_data/cv.yml` (publications come from `_data/publications.yaml`) |

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

Each file in `projects/` starts with a title, role, and hero image path. Until you add project-specific `blocks`, it displays the examples in `_data/project_template.yml`. To replace the examples, add a `blocks` list to that project's file. Project images belong in `assets/projectimages/<project-name>/`. The shared layout is `_layouts/project-detail.html`, block markup is `_includes/project-block.html`, and styling is in `assets/css/projects.css`.

Add blocks to a project page like this:

```yaml
role: "Research, UX design"
hero: /assets/projectimages/everyday-resistance/hero.jpg
hero_alt: "Project overview"
blocks:
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

## Credits

The HTML CV layout adapts the dated-entry structure from [Donghoon Shin’s CV theme](https://github.com/donghoon-io/donghoon-io.github.io).

Forked from [Jungsoo Park’s website](https://github.com/JJumSSu/JJumSSu.github.io), based on Martin Saveski’s template. The news layout was inspired by [Donghoon Shin’s website theme](https://github.com/donghoon-io/donghoon-io.github.io).
