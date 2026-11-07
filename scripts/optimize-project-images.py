"""Create responsive WebP copies; leave source images unchanged.

Usage: python3 scripts/optimize-project-images.py path/to/photo.jpg [...]
Requires Pillow with WebP support.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageOps


def optimize(source):
    destination = source.parent / 'optimized'
    destination.mkdir(exist_ok=True)
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert('RGB')
        for width in (800, 1200, 1600):
            if width > image.width:
                continue
            height = round(image.height * width / image.width)
            output = destination / f'{source.stem}-{width}.webp'
            image.resize((width, height), Image.Resampling.LANCZOS).save(
                output, 'WEBP', quality=88, method=6, icc_profile=original.info.get('icc_profile')
            )
            print(f'{output}: {width}×{height}, {output.stat().st_size / 1024:.0f} KB')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('images', type=Path, nargs='+')
    for source in parser.parse_args().images:
        optimize(source)
