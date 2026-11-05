# Inha Cha’s research portfolio

This Jekyll site contains Home and Projects pages.

| To edit | File |
| --- | --- |
| Biography and Home sections | `index.html` |
| News and publications | `_data/news.yml`, `_data/publications.yaml` |
| Projects | `_data/projects.yaml` (entries use `title`, `subtitle`, and `url`) |
| Shared navigation | `_layouts/homepage.html` |
| Typography, spacing, and responsive layout | `assets/css/site.css` |
| Logo, portrait, and CV paths | `_data/files.yml` |

## Updating uploaded files

Store shared images such as the portrait and logo in `assets/images/`. For project images, create a subfolder in `assets/projectimages/` for each project, for example `assets/projectimages/ethics-pathways/cover.jpg`. Store PDFs and other downloadable documents in `assets/documents/`. To replace the portrait, logo, or CV, upload the new file to its folder and change the corresponding path in `_data/files.yml`. Replacing a file under the same name requires no configuration change. Commit the file and its path change together.

Use a repository path starting with `/assets/`. The templates apply Jekyll’s `relative_url` filter so links work in local previews and under the GitHub Pages project URL.

## Local preview

With Jekyll installed, run `jekyll serve` from the repository root.

## Credits

Forked from [Jungsoo Park’s website](https://github.com/JJumSSu/JJumSSu.github.io), based on Martin Saveski’s template. The news layout was inspired by [Donghoon Shin’s website theme](https://github.com/donghoon-io/donghoon-io.github.io).
