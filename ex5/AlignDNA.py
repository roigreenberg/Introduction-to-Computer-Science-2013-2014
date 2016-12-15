#############################################################
# FILE: AlingDNA.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex5 2013-2014
# Description: calculate the match between 2 DNA strands 
# and find the best match between two unaligned DNA  strands
#############################################################



def get_alignment_score(dna1,dna2,match=1,mismatch=-1,gap=-2):
    ''' Calculate the match between 2 DNA strands

    A function that calculate the match between 2 given DNA strands
    according to 3 parameters. 'match' for the same DNA, 'mismatch'
    for different letter and 'gap' for 1 letter and gap.

    Args:
    - dna1: first DNA strand. combined with the letters 'A' 'T' 'G' 'C'
            and '-'.
    - dna2: second DNA strand. combined with the letters 'A' 'T' 'G' 'C'
            and '-'.
    - match: score for the same DNA. integer number. default 1.
    - mismatch: score for different letter. integer number. default -1.
    - gap: score for for 1 letter and gap. integer number. default -2.

    return: the score of the match'''
    
    score=0 # start value
    GAP="-"

    # run for the length of the strands
    for dna in range(len(dna1)):
        # check for match
        if dna1[dna]==dna2[dna]:
            score += match
        # check for mismatch and gap
        elif dna1[dna]!=dna2[dna]:
            if dna1[dna]!=GAP and dna2[dna]!="-":
                score += mismatch
            else:
                score += gap
    return score

def get_best_alignment_score(dna_1,dna_2,match=1,mismatch=-1,gap=-2):
    ''' Find the match between two unaligned DNA  strands

    A function that find the best match between 2 given DNA strands
    according to 3 parameters. 'match' for the same DNA, 'mismatch'
    for different letter and 'gap' for 1 letter and gap.

    Args:
    - dna_1: first DNA strand. combined with the letters 'A' 'T' 'G' 'C'
            and '-'.
    - dna_2: second DNA strand. combined with the letters 'A' 'T' 'G' 'C'
            and '-'.
    - match: score for the same DNA. integer number. default 1.
    - mismatch: score for different letter. integer number. default -1.
    - gap: score for for 1 letter and gap. integer number. default -2.

    return: list with the score of the best match and both DNA strands'''
    
    # define a list for all the matches
    store=[]

    def find_matchs(dna_1_src,dna_2_src,dna_1_new="",dna_2_new=""):
        ''' Find all macthes between two unaligned DNA  strands

        A function that find all matches between 2 given DNA strands

        Args:
        - dna_1_src: source of the first DNA strand. combined with the letters
                     'A' 'T' 'G' 'C' and '-'.
        - dna_2_src: source of the second DNA strand. combined with the letters
                     'A' 'T' 'G' 'C' and '-'.
        - dna_1_new: new list build from the first source strands. start with
                    empty sequence
        - dna_1_new: new list build from the second source strands. start with
                    empty sequence
        return: list with lists of every matches'''

        GAP="-"

        # if no DNA left on source strands add the strand
        if len(dna_1_src)==0 and len(dna_2_src)==0:
            store.append([dna_1_new,dna_2_new])

        # add first current letters from both strands
        # if DNA left on source strands
        if len(dna_1_src)!=0 and len(dna_2_src)!=0:
            find_matchs(dna_1_src[1:],dna_2_src[1:],\
              dna_1_new+dna_1_src[0],dna_2_new+dna_2_src[0])

        # add first current letter from first strand and gap to the second
        # if DNA left on first source strand   
        if len(dna_1_src)!=0:
            find_matchs(dna_1_src[1:],dna_2_src,\
              dna_1_new+dna_1_src[0],dna_2_new+GAP)

        # add first current letter from second strand and gap to the first
        # if DNA left on second source strand  
        if len(dna_2_src)!=0:
            find_matchs(dna_1_src,dna_2_src[1:],\
              dna_1_new+GAP,dna_2_new+dna_2_src[0])

    # call the recursive function
    find_matchs(dna_1,dna_2)

    # calculte the score for each dna match
    for dna in store:
        dna1=dna[0]
        dna2=dna[1]
        dna.insert(0,get_alignment_score(dna1,dna2,match,mismatch,gap))

    # return the best match    
    return  max(store)

    


        


                            
