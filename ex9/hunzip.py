#!/usr/bin/env python3
'''
usage: hunzip.py [-h] [-o OUTFILE] [-s SUFFIX] [-S OUTSUFFIX] [-f] infile

Decompress files using the hzlib module.

positional arguments:
  infile

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        Name of output file
  -s SUFFIX, --suffix SUFFIX
                        Default suffix to remove instead of .hz
  -S OUTSUFFIX, --outsuffix OUTSUFFIX
                        Default suffix to add if instead of .out
  -f, --force           Force decompression and overwrite output file if it
                        exists
'''
import hzlib
import struct
import os.path

DEFAULT_IN_EXTENSION = '.hz'
DEFAULT_OUT_EXTENSION = '.out'
MEGIC_LENGTH = len(hzlib.MAGIC)

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Decompress files using the hzlib module.')
    parser.add_argument("infile")
    parser.add_argument("-o", "--outfile", type=str, default=None, 
                        help='Name of output file')
    parser.add_argument("-s", "--suffix", type=str,
                        default=DEFAULT_IN_EXTENSION,
                        help=('Default suffix to remove instead of ' +
                              DEFAULT_IN_EXTENSION))
    parser.add_argument("-S", "--outsuffix", type=str,
                        default=DEFAULT_OUT_EXTENSION,
                        help=('Default suffix to add if instead of ' +
                              DEFAULT_OUT_EXTENSION))
    parser.add_argument("-f", "--force", action='store_true',
                        help=('Force decompression and overwrite output ' +
                              'file if it exists'))
    args = parser.parse_args()
 
    # create the output file name
    source_file = args.infile
    out_file_name = args.outfile
    suffixin = args.suffix
    suffixout = args.outsuffix
    if not out_file_name:
        new_file = source_file[:-len(suffixin)] + suffixout
    else:
        new_file = out_file_name
    source_file = args.infile

    # open and read the file
    file = open(source_file, "rb", 1)
    file.seek(MEGIC_LENGTH,0)
    level = struct.unpack('1b',file.read(1))[0]
    text = file.read()
    file.close()

    # decompress the data
    for i in range(level):
        splited = hzlib.split(text)
        can_codebook = splited[1]
        decode = hzlib.build_decodebook(can_codebook)
        text= list(splited[0])
        unpaded = list(hzlib.unpad(text))
        text = list(hzlib.decompress(unpaded,decode))

    # create the new file if possible
    if os.path.isfile(out_file_name) and not args.force:
        raise FileExistsError
    else:       
        new_file = open(new_file,'wb')
        for bit in text:
            new_file.write(struct.pack('1B',bit))
    
if __name__ == '__main__':
    main()
