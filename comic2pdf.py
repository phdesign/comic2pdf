"""Converts .cbr and .cbz files to .pdf.
Only works with comicbook files that contain JPG's (for now).
"""

import os
import sys
import zipfile
import argparse
import tempfile
import pkg_resources
import patoolib
from PIL import Image

PACKAGE_NAME = "comic2pdf"
try:
    __version__ = pkg_resources.get_distribution("comic2pdf").version
except pkg_resources.DistributionNotFound:
    __version__ = "0.0.0"


def extract_cbr(filename, tmpdirname):
    patoolib.extract_archive(filename, outdir=tmpdirname)


def extract_cbz(filename, tmpdirname):
    zip_file = zipfile.ZipFile(filename, "r")
    zip_file.extractall(tmpdirname)
    zip_file.close()


def collect_images(path):
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        _, extn = os.path.splitext(item.lower())
        if os.path.isdir(itempath):
            yield from collect_images(itempath)
        elif extn in (".jpg", ".jpeg"):
            img = Image.open(itempath)
            img.save(itempath, dpi=(96, 96))
            yield img


def to_pdf(filename, tmpdirname):
    images = list(collect_images(tmpdirname))
    images[0].save(filename, "PDF", resolution=100.0, save_all=True, append_images=images[1:])


def parse_config():
    parser = argparse.ArgumentParser(description="Converts .cbr and .cbz files to .pdf", prog=PACKAGE_NAME)
    parser.add_argument("path", nargs="+", help="paths to process")
    parser.add_argument("-o", "--outdir", default=os.getcwd(), help="directory to place generated files")
    parser.add_argument("--version", action="version", version="%(prog)s v" + __version__)
    return parser.parse_args()


def main():
    config = parse_config()
    for filename in config.path:
        print(f'processing file "{filename}"...', file=sys.stdout)
        filepath = os.path.join(os.getcwd(), filename)
        with tempfile.TemporaryDirectory() as tmpdirname:
            filename_noextn, extn = os.path.splitext(filename)
            if extn in (".cbz", ".zip"):
                extract_cbz(filepath, tmpdirname)
            elif extn in (".cbr", ".rar"):
                extract_cbr(filepath, tmpdirname)
            else:
                print(f'skipping "{filename}"', file=sys.stdout)
                continue
            newfilename = filename_noextn + ".pdf"
            newfilepath = os.path.join(config.outdir, newfilename)
            to_pdf(newfilepath, tmpdirname)
            print(f'"{newfilename}" successfully converted!', file=sys.stdout)
    print(os.linesep + "we're all done!" + os.linesep, file=sys.stdout)


if __name__ == "__main__":
    main()
