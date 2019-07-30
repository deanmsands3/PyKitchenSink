__author__ = 'Dean M. Sands, III (deanmsands3@gmail.com)'
import os
import gzip
import lzma
import bz2


extension_compressor_table = [
    ("", open),
    (".gz", gzip.open),
    (".xz", lzma.open),
    (".bz2", bz2.open)
]


def find_file_in_any_compressed_form(file):
    base_file_name = os.path.abspath(file)
    for extension, reader in extension_compressor_table:
        this_file_name = base_file_name + extension
        if not os.path.exists(this_file_name) or os.path.isfile(this_file_name):
            continue
        with reader(this_file_name, 'rb') as this_file:
            return this_file.read()
    return None


def create_file_in_every_compressed_form(file, contents):
    base_file_name = os.path.abspath(file)
    for extension, writer in extension_compressor_table:
        this_file_name = base_file_name + extension
        with writer(this_file_name, 'wb') as this_file:
            this_file.write(contents)


