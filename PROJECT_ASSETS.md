# Migrated project images

Source: user-provided `old_portfolio-master.zip`, commit `efce36f3cda3572d2bdbd0ebf40e1f40f4ea0398`.

19 original images (30.1 MiB) copied byte-for-byte. Each project folder contains its gallery thumbnail and its detail images. Detail order follows the original HTML pages. Reuse-it keeps its Vimeo hero. Its original overview and six detail images are retained in the repository, but are no longer displayed on the page. Naver Labs has one hero image and no additional detail images in the source.

`P_reuseit/reuseit_6.png` contains JPEG data, so its new filename is `detail-06.jpg`. The image itself has not been re-encoded.

The original 356 × 216 thumbnails are retained for reference. The gallery instead uses the 1920px-wide overview/hero images for sharper display, with `image_position` controlling the crop in `_data/projects.yaml`. The larger images provide a different crop from the old thumbnails.

| Project | Original path | Current path | Dimensions |
| --- | --- | --- | --- |
| reuse-it | `P_reuseit/reuseit_main.png` | `assets/projectimages/reuse-it/overview.png` | 1920 × 608 |
| reuse-it | `P_reuseit/reuseit_1.png` | `assets/projectimages/reuse-it/detail-01.png` | 2512 × 1194 |
| reuse-it | `P_reuseit/reuseit_2.png` | `assets/projectimages/reuse-it/detail-02.png` | 2578 × 1800 |
| reuse-it | `P_reuseit/reuseit_3.png` | `assets/projectimages/reuse-it/detail-03.png` | 2565 × 1800 |
| reuse-it | `P_reuseit/reuseit_4.png` | `assets/projectimages/reuse-it/detail-04.png` | 2589 × 1800 |
| reuse-it | `P_reuseit/reuseit_5.png` | `assets/projectimages/reuse-it/detail-05.png` | 2561 × 1800 |
| reuse-it | `P_reuseit/reuseit_6.png` | `assets/projectimages/reuse-it/detail-06.jpg` | 1626 × 1082 |
| reuse-it | `P_Thumnail/reuseit.png` | `assets/projectimages/reuse-it/thumbnail.png` | 356 × 216 |
| rullen-bandet | `P_rullenbandet/rullenbandet_main.png` | `assets/projectimages/rullen-bandet/hero.png` | 1920 × 608 |
| rullen-bandet | `P_rullenbandet/rullenbandet_1.png` | `assets/projectimages/rullen-bandet/detail-01.png` | 2015 × 638 |
| rullen-bandet | `P_rullenbandet/rullenbandet_2.png` | `assets/projectimages/rullen-bandet/detail-02.png` | 2098 × 893 |
| rullen-bandet | `P_Thumnail/rullenbandet.png` | `assets/projectimages/rullen-bandet/thumbnail.png` | 356 × 216 |
| naver-labs | `P_naverlabs/NAVERLABS_MAIN.png` | `assets/projectimages/naver-labs/interaction-scenarios.png` | 1920 × 608 |
| naver-labs | `P_Thumnail/naverlabs.png` | `assets/projectimages/naver-labs/thumbnail.png` | 356 × 216 |
| shadia-2017 | `P_shadia/SHADIA_main.png` | `assets/projectimages/shadia-2017/hero.png` | 1920 × 608 |
| shadia-2017 | `P_shadia/SHDIA_CON1.png` | `assets/projectimages/shadia-2017/detail-01.png` | 2099 × 1176 |
| shadia-2017 | `P_shadia/SHDIA_CON2.png` | `assets/projectimages/shadia-2017/detail-02.png` | 2098 × 10791 |
| shadia-2017 | `P_shadia/SHDIA_CON3.png` | `assets/projectimages/shadia-2017/detail-03.png` | 2099 × 5242 |
| shadia-2017 | `P_Thumnail/shadia2017.png` | `assets/projectimages/shadia-2017/thumbnail.png` | 356 × 216 |

Page configuration is in `projects/<project-name>.html`. Each image uses an `image` block with a path, alt text, and original dimensions. Images render at their natural aspect ratio; the larger content images load lazily. The original source HTML and scripts are not required by the new pages.

Naver Labs uses its original 1920 × 608 image, `interaction-scenarios.png`, as the hero. It is not duplicated in the body. The temporary person-following robot sketch was removed.

Reuse-it currently displays two user-provided images at full content width, one after the other below the Vimeo hero: `features-summary.png` (1121 × 793), then `prototype-interior.jpg` (2067 × 1537). Their original files are `190613 final presentation (1).png` and `Image 4. 2019 JDA Korea_National Winner_Reuse-it.jpg`.

Following the two full-width images, Reuse-it includes `how-to-use.png` at full width, then the combined `mechanism-blueprint.png` (4584 × 1472, supplied as `Frame 2.png`) at full width. Below these, `team-portrait.jpg` and `team-working.jpg` form a gapless pair. The separate `how-it-works.png` and `blueprint.png` files were replaced by the combined image.
