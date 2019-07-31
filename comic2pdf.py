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
import PIL.ExifTags

PACKAGE_NAME = "comic2pdf"
VERSION = "0.0.1"


def extract_cbr(filename, tmpdirname):
    patoolib.extract_archive(filename, outdir=tmpdirname)


def extract_cbz(filename, tmpdirname):
    zip_file = zipfile.ZipFile(filename, "r")
    zip_file.extractall(tmpdirname)
    zip_file.close()


def to_pdf(filename, tmpdirname):
    filelist = os.listdir(tmpdirname)
    if len(filelist) == 1:
        to_pdf(filename, os.path.join(tmpdirname, filelist[0], ""))
    else:
        # imagelist is the list with all image filenames
        im_list = list()
        firstP = True
        im = None
        for image in filelist:
            if image.endswith(".jpg") or image.endswith(".JPG") or image.endswith(".jpeg") or image.endswith(".JPEG"):
                im1 = Image.open(os.path.join(tmpdirname, image))
                try:
                    im1.save(os.path.join(tmpdirname, image), dpi=(96, 96))
                except:
                    aaaaa = 4

                if firstP:
                    im = im1
                    firstP = False
                else:
                    im_list.append(im1)
            else:
                continue
        # print(exif)
        im.save(filename, "PDF", resolution=100.0, save_all=True, append_images=im_list)
    # print("OK")


def process_dir(directory):
    # look at all files in directory
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
            newfilepath = os.path.join(directory, newfilename)
            to_pdf(newfilepath, tmpdirname)
            print(f'"{newfilename}" successfully converted!', file=sys.stdout)


def parse_config():
    parser = argparse.ArgumentParser(description="Converts .cbr and .cbz files to .pdf", prog=PACKAGE_NAME)
    parser.add_argument("directory", help="directory to process")
    parser.add_argument("--version", action="version", version="%(prog)s v" + VERSION)
    return parser.parse_args()


def main():
    config = parse_config()
    process_dir(config.directory)


if __name__ == "__main__":
    main()
