################################################################
# FILE: hzlib.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex9 2013-2014
# Description: implement some function about Huffman tree and
# compress and decompress data
################################################################

import collections
from bisect import bisect
'''
This module contains several function for compress and decompress data, using
the Huffman code algorithm.
'''

MAGIC = b"i2cshcfv1"
LEFT_TREE = 0
RIGHT_TREE = 1

def symbol_count(data):
    """the function return dictionary from item to number of returns in data
    Args: data - a data
    """
    return collections.Counter(data)


def make_huffman_tree(counter):
    """the function create a huffman tree of a given dictionary from item to
    number of returns
    Return tree of tuple of tuples represent the tree or None if dictionary
    is empty
    Args: counter - a dictionary (output of symbol_data)
    """
    # create a list from the dictonary and sorted it from low repeats to high
    # and high value to low
    sort_list = sorted([(tuple0, counter[tuple0]) for tuple0 in counter], \
                       reverse=True )
    sort_list.sort(key=lambda leaf: leaf[1])

    # run until have only 1 tuple
    while len(sort_list) > 1:
        # take the first 2 tuples
        tuple1 = sort_list.pop(0)
        tuple2 = sort_list.pop(0)

        # calculate the combined repeats
        count = tuple1[1] + tuple2[1]

        #create new tuple of both tuple
        parent = ((tuple2[0], tuple1[0]), count)

        #create a list of all the reapets
        counts = [repeats[1] for repeats in sort_list]

        #insert the new tuple to the list in the right place
        sort_list.insert(bisect(counts, count), parent)

    return sort_list[0][0] if sort_list else None


def build_codebook(huff_tree):
    """create a codebook of the Huffman tree
    the function recieve a huffman tree and return a dictionary from item
    to tuple of length and decimal value of the binary code represent the item
    Args:
    huff_tree - a coded tree of a recursive tuple structure
    (same structure of output of privious function).
    bin_item - a string. default is "".
    codebook - a dictionary. default is {}.
    """
    new_codebook = {}
    def codebook(huff_tree, n=""):
        # return empty dictionary in tree is empty
        if not huff_tree:
            return {}
        # return the dictionary in case tree is only 1 leaf
        elif type(huff_tree) is not tuple:
            return {huff_tree: (1, 0)}

        # the left branch
        left=huff_tree[LEFT_TREE]
        # the right branch
        right=huff_tree[RIGHT_TREE]

        # if got to leaf, add it to the dictionary
        # if not check the left branch in recursive way
        if type(left) is not tuple:
            binary_info = (len(n + "0"), int(n + "0", 2))
            new_codebook[left] = binary_info
        else:
            codebook(left, n + "0")
            
        # if got to leaf, add it to the dictionary
        # if not check the right branch in recursive way
        if type(right) is not tuple:
            binary_info = (len(n + "1"), int(n + "1", 2))
            new_codebook[right] = binary_info 
        else:
            codebook(right, n + "1")
    
        return new_codebook
    return codebook(huff_tree)

    

def build_canonical_codebook(codebook):
    """create a canonical codebook of the Huffman tree
    the function recieve a huffman codebook and return a dictionary from item
    to tuple of length and decimal value of the binary code represent the item
    in canonical way
    Args:
    codebook - a dictionary - table of char: code pairs."""
    # create a list from the codebook and sorted it from low value to high and
    # low binary length to high 
    new_list = sorted([[leaf,codebook[leaf][0]] for leaf in codebook])
    new_list.sort(key=lambda x: x[1])
    
    # return empty codebook if tree is empty
    if not new_list:
        return {}
    # take the length of the first item
    length=new_list[0][1]
    # calculate a new binary code the first item 
    code = "0" + ''.join("0" for i in range(length - 1))
    # create  new dictonary with the first item with new values
    canonical_codebook={new_list[0][0]: (length,int(code,2))}
    # run for every item from the second one
    for item in new_list[1:]:
        # calculate a new binary code the item 
        code = bin(int(code,2)+1)[2:]
        # add 0 to the end of the new code if it's length smaller then
        # the previus item code's
        if len(code) < length:
               code=code.zfill(length)
        # take the current length
        length=item[1]
        # add 0 to the begining of the new code if it's length smaller then
        # the original item code's
        code=code+"".join("0" for i in range(length-len(code)))
        # add the new dictionary the item with new values
        canonical_codebook[item[0]] = (length, int(code, 2))
        
    return canonical_codebook

                   
def build_decodebook(codebook):
    ''' return a dictionary from tuple of length and decimal value of the
    binary code to item built from a dictionary of item to tuple of length
    and decimal value of the binary code
    rgs:
    codebook - a dictionary - table of char: code pairs."""
    '''
    # new dictionary
    decodebook = {}
    # add the new dictionary the value as key and key as value
    for item in codebook:
        decodebook[codebook[item]]=item
    return decodebook

def compress(corpus, codebook):
    """the function create an iterator of 0 or 1 as ints, after iterating on
    corpus input.

    Args:
    corpus - a sequence of chars by a iterator.
    codebook - a dictionary - table of char: code pairs. """

    # run for every item in corpus
    for item in corpus:
        # take the length and decimal values according to the codebook
        length = codebook[item][0]
        num = codebook[item][1]
        # convert to binary
        binary = bin(num)[2:].zfill(length)
        # iterator?????
        for char in binary:
            yield  int(char)

def decompress(bits, decodebook):
    """the function run over the decoding bits of coded bits input
    and create an iterator of 0 or 1 as an int.

    Args:
    bits - an iterable, a sequence of coded bits each is an int 0 or 1.
    decodebook - a dictionary, a decoded one"""
    # set a new binary code
    binary = ""
    # run for every bit
    for bit in bits:
        # add the current binary code the next bit
        binary = binary + str(bit)
        # create a tuple of length and decimal value of the binary code
        decode = (len(binary), int(binary, 2))
        # if the binary code is in the decodebook return his value and reset
        # the binary code
        if decode in decodebook:
            yield decodebook[decode]
            binary = ""


def pad(bits):
    """the function run over each eight sequence bits out of the input,
    adds the 1 as a final bit and appends zeros for the total length be
    divided by 8. the function create an iterator of 0 or 1 as an ints.

    Args:
    bits - an iterable, a sequence of coded bits each is an int 0 or 1."""
    # set a new binary code
    binary = ""
    # run for every bit
    for bit in bits:
        binary = binary + str(bit)
        # when binary code have length of 8 return the decimal value and reset
        # the binary code
        if len(binary) == 8:
            yield int(binary, 2)
            binary = ""
    # for the last bits, add single 1 and zeros until binary have length of 8
    binary = binary + "1"
    while len(binary) != 8:
        binary = binary + "0"
    # return the last binary code
    yield int(binary, 2)

def unpad(byteseq):
    """the function run over all bytes of input, taking off the '0' and '1'
    on top of it and create an iterator of 0 or 1 as ints.

    Args:
    byteseq - an iterator, a sequence of bytes."""
    # set a boolin for the first byte
    first = True
    # run for every byte
    for byte in byteseq:
        # for the first byte get his binary value and finish the corrent loop
        if first:
            binary = bin(byte)[2:].zfill(8)
            first = False
            continue
        
        # return every single bit as iterator
        for bit in binary:
            yield int(bit)
        # get the next byte binary value
        binary = bin(byte)[2:].zfill(8)
    # for the last byte, find the last "1" digit index
    index = -1
    bit = binary[index]
    while bit != "1":
        index -= 1
        bit = binary[index]
    # return the bits up to the last "1" digit
    for bit in binary[:index]:
            yield int(bit)

def join(data, codebook):
    """the function run over the bytes of input (first codebook then data)
    and create an iterator of the codebook vals which appear, then  the
    data items.

    Args:
    data - an iterator, a sequence of bytes.
    codebook - a canonical code table, the output of
    build_canonical_codebook."""
    for key in range(256):
        if key in codebook:
            yield codebook[key][0]
        else:
            yield 0
    for data_0 in data:
        yield data_0

def split(byteseq):
    """that function split the output of the function join to data and codebook
    the function return a tuple which is consist of a dictionary - canonical
    coding table and an iterator which iterate over rest of byteseq as
    byte sequent.

    Args:
    byteseq - an iterator, a sequence of bytes."""
    index = 0
    codebook = {}
    data = []
    for byte in byteseq:
        if index < 256:
            if byte != 0:
                codebook[index] = (byte, 0)
            index += 1
        else:
           data.append(byte)
    codebook = build_canonical_codebook(codebook)
    return iter(data), codebook
    
