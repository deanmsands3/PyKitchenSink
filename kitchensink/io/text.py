__author__ = 'Dean M. Sands, III (deanmsands3@gmail.com)'
import os


def is_text(filename):
    with open(filename) as candidate_text_file:
        s = candidate_text_file.read(512)
    text_characters = "".join(map(chr, range(32, 127))) + "\n\r\t\b"
    _null_trans = str.maketrans("", "", text_characters)
    if not s:
        # Empty files are considered text
        return True
    if "\0" in s:
        # Files with null bytes are likely binary
        return False
    # Get the non-text characters (maps a character to itself then
    # use the 'remove' option to get rid of the text characters.)
    t = s.translate(_null_trans)
    # If more than 30% non-text characters, then
    # this is considered a binary file
    if float(len(t))/float(len(s)) > 0.30:
        return False
    return True


def dos2unix(file):
    # Is it a binary file instead?
    if not is_text(file):
        return
    with open(file, 'rb') as dos_file:
        dos_contents = dos_file.read()
        dos_length = len(dos_contents)
        unix_contents = dos_contents.replace(b'\r\n', b'\n')
        unix_length = len(unix_contents)
    # Is it already unix'ed?
    if dos_length == unix_length:
        return
    # Write the new contents.
    with open(file, 'wb') as unix_file:
        unix_file.write(unix_contents)


def unixify_folder(folder):
    for root, dirs, files in os.walk(folder):
        for name in files:
            dos2unix(os.path.join(root, name))
