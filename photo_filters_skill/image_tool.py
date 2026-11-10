#!/usr/bin/env python3
"""image_tool.py — фотофильтры на Pillow: негатив и чёрно-белое.

Использование:
    python image_tool.py negative <input> <output>
    python image_tool.py bw       <input> <output>
"""
import argparse
import sys

from PIL import Image, ImageOps


def apply_negative(input_path, output_path):
    """Накладывает эффект негатива (ImageOps.invert)."""
    with Image.open(input_path) as img:
        result = ImageOps.invert(img.convert("RGB"))
        result.save(output_path)
    return output_path


def apply_black_and_white(input_path, output_path):
    """Делает фотографию чёрно-белой (ImageOps.grayscale)."""
    with Image.open(input_path) as img:
        result = ImageOps.grayscale(img)
        result.save(output_path)
    return output_path


def main(argv=None):
    parser = argparse.ArgumentParser(description="Фотофильтры: negative / bw")
    parser.add_argument("mode", choices=["negative", "bw"], help="режим обработки")
    parser.add_argument("input", help="путь к исходному изображению")
    parser.add_argument("output", help="путь для сохранения результата")
    args = parser.parse_args(argv)

    try:
        if args.mode == "negative":
            apply_negative(args.input, args.output)
        else:
            apply_black_and_white(args.input, args.output)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}", file=sys.stderr)
        return 1
    print(f"OK: режим '{args.mode}' -> {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
