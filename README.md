# Inha Cha’s research portfolio

This Jekyll site contains Home and Projects pages.

| To edit | File |
| --- | --- |
| Biography and Home sections | `index.html` |
| News and publications | `_data/news.yml`, `_data/publications.yaml` |
| Projects | `_data/projects.yaml` (gallery titles, links, and thumbnail paths) |
| Shared navigation | `_layouts/homepage.html` |
| Typography, spacing, and responsive layout | `assets/css/site.css` |
| Logo, portrait, and CV paths | `_data/files.yml` |

## Updating uploaded files

Store shared images such as the portrait and logo in `assets/images/`. For project images, create a subfolder in `assets/projectimages/` for each project, for example `assets/projectimages/ethics-pathways/cover.jpg`. Store PDFs and other downloadable documents in `assets/documents/`. To replace the portrait, logo, or CV, upload the new file to its folder and change the corresponding path in `_data/files.yml`. Replacing a file under the same name requires no configuration change. Commit the file and its path change together.

Use a repository path starting with `/assets/`. The templates apply Jekyll’s `relative_url` filter so links work in local previews and under the GitHub Pages project URL.

## Local preview

With Jekyll installed, run `jekyll serve` from the repository root.

## Project pages

Each file in `projects/` contains only a title, role, hero image path, and ordered `blocks`. Project images belong in `assets/projectimages/<project-name>/`. The shared layout is `_layouts/project-detail.html`, block markup is `_includes/project-block.html`, and styling is in `assets/css/site.css`.

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

Forked from [Jungsoo Park’s website](https://github.com/JJumSSu/JJumSSu.github.io), based on Martin Saveski’s template. The news layout was inspired by [Donghoon Shin’s website theme](https://github.com/donghoon-io/donghoon-io.github.io).
