"""Converts .cbr and .cbz files to .pdf.

Use:  python comic2pdf.py
-- Only works with comicbook files that contain JPG's (for now).
-- The script should be in the same directory the file(s) to convert are in.

Author:  MComas1
Date:  14-09-18

License:  You can do what you want with it.
Mainly based on a script by Bransorem (https://github.com/bransorem/comic2pdf)
"""

import os
import sys
import zipfile
import argparse
import tempfile
import patoolib
from PIL import Image

PACKAGE_NAME = "comic2pdf"
VERSION = "0.0.1"


def extract_cbr(filename, tmpdirname):
    patoolib.extract_archive(filename, outdir=tmpdirname)


def extract_cbz(filename, tmpdirname):
    zip_file = zipfile.ZipFile(filename, "r")
    zip_file.extractall(tmpdirname)
    zip_file.close()


def collect_images(path):
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        if os.path.isdir(itempath):
            yield from collect_images(itempath)
        elif item.lower().endswith(".jpg") or item.lower().endswith(".jpeg"):
            img = Image.open(itempath)
            img.save(itempath, dpi=(96, 96))
            yield img


def to_pdf(filename, tmpdirname):
    images = list(collect_images(tmpdirname))
    images[0].save(filename, "PDF", resolution=100.0, save_all=True, append_images=images[1:])


def process_dir(directory, outdir):
    print(f'processing directory "{directory}"...', file=sys.stdout)
    for filename in os.listdir(directory):
        print(f'processing file "{filename}"...', file=sys.stdout)
        filepath = os.path.join(directory, filename)
        with tempfile.TemporaryDirectory() as tmpdirname:
            if filename[-4:] == ".cbz" or filename[-4:] == ".zip":
                extract_cbz(filepath, tmpdirname)
            elif filename[-4:] == ".cbr" or filename[-4:] == ".rar":
                extract_cbr(filepath, tmpdirname)
            else:
                print(f'skipping "{filename}"', file=sys.stdout)
                continue
            newfilename = filename.replace(filename[-4:], ".pdf")
            newfilepath = os.path.join(outdir, newfilename)
            to_pdf(newfilepath, tmpdirname)
            print(f'"{newfilename}" successfully converted!', file=sys.stdout)


def parse_config():
    parser = argparse.ArgumentParser(description="Converts .cbr and .cbz files to .pdf", prog=PACKAGE_NAME)
    parser.add_argument("directory", help="directory to process")
    parser.add_argument("-o", "--outdir", default=os.getcwd(), help="directory to place generated files")
    parser.add_argument("--version", action="version", version="%(prog)s v" + VERSION)
    return parser.parse_args()


def main():
    config = parse_config()
    process_dir(config.directory, config.outdir)


if __name__ == "__main__":
    main()
