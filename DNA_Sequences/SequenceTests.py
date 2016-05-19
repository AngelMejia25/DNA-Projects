

def main():
    """------------------------------------------------------------------------------
    SUMMARY: 
    This code takes a string of DNA and returns different information about the DNA
    sequence such as the starting codon or the gene sequence. 
    
    Programmer: Angel Mejia
    
    INPUT
    No input. A string of DNA is manually set in a variable.
    
    OUTPUT
    To the console (screen):
    A report that shows ....
    ++++++++++++++++++ Upstream and Genic Report +++++++++++++++++


    Starting sequence is: cgccatataatgctcgtccgcgcccta
    Sequence adjusted for uppercase: CGCCATATAATGCTCGTCCGCGCCCTA
    Length of the starting squence is: 27
    ----------------------------------------------------------------
    ATG starting codon begins in position (bp) 10
    Followed by the second codon CTC  in position (bp) 13
    Followed by the third codon GTC  in position (bp) 16
    ---------------------------------------------------------------
    Upstream sequence is: CGCCATATA
    Upstream length (bp): 9
    ---------------------------------------------------------------
    Gene Sequence is: ATGCTCGTCCGCGCCCTA
    Gene length (bp): 18
    ----------------------------------------------------------------
    [+ Strand]: 5' ATGCTCGTCCGCGCCCTA 3'
                   ||||||||||||||||||
    [- Strand]: 3' TACGAGCAGGCGCGGGAT 5'
    
    [- Strand]: 5' TAGGGCGCGGACGAGCAT 3'
    -----------------------------------------------------------------
    Original sequence: cgccatataATGctcgtccgcgcccta
    ----------------------------------------------------------------
    Upstream Direct (+) Strand:
    Number of upstream As: 3
    Number of upstream Ts: 2
    -----------------------------------------------------------------


    ------------------------------------------------------------------------------
    
    """
    
    
    # ----- code starts here ----------------
    
    print ("++++++++++++++++++ Upstream and Genic Report +++++++++++++++++\n\n")
    
    # originalSequence - upstream and start of a gene
    originalSequence	= "cgccatataatgctcgtccgcgcccta"
    # don't forget to test OTHER strings too!
    
    print ("Starting sequence is:", originalSequence)
    
    # next convert all nucleotides to uppercase
    originalSequenceUpper = originalSequence.upper()
    
    print ("Sequence adjusted for uppercase:", originalSequenceUpper)
    print ("Length of the starting squence is:", len(originalSequenceUpper))
    
    print ("----------------------------------------------------------------")
    
    
    # now get the position of the start codon "ATG"
    
    ATGPosition = originalSequenceUpper.find("ATG")
    
    print ("ATG starting codon begins in position (bp)", ATGPosition + 1)
    
    secondCodon = originalSequenceUpper[ATGPosition +3:ATGPosition+6]
    secondCodonPOS = ATGPosition + 3
    
    print ("Followed by the second codon", secondCodon, " in position (bp)", secondCodonPOS + 1)
    
    thirdCodon = originalSequenceUpper[secondCodonPOS+3:secondCodonPOS+6]    
    thirdCodonPOS = secondCodonPOS + 3
    
    print ("Followed by the third codon", thirdCodon, " in position (bp)", thirdCodonPOS + 1)
    
    
    print ("---------------------------------------------------------------")
    
    # upStream - holds the upstream sequence
    
    upStream = originalSequenceUpper[:ATGPosition]
    
    print ("Upstream sequence is:", upStream)
    
    print("Upstream length (bp):", len(upStream) )
    
    
    print ("---------------------------------------------------------------")
    
    # gene - holds actual gene sequence
    
    gene = originalSequenceUpper[ATGPosition:]
    
    print ("Gene Sequence is:", gene)
    print ("Gene length (bp):", len(gene) )
    
    print ("----------------------------------------------------------------")
    
    
    # directStrand - (original) direct strand of the gene sequence
    
    directStrand = gene
    
    # print basepairing notation between strands
    
    changeOriginal = "ACTG"
    toComplement = "TGAC"
    transTable = str.maketrans(changeOriginal, toComplement)
    inDirectStrand = directStrand.translate(transTable)

    # get complementary sequence
    
    print ("[+ Strand]: 5'", directStrand, "3'")
    
    Bars = ""
    geneLen = len(gene)
    while (geneLen > 0):
        Bars = Bars + "|"
        geneLen = geneLen - 1
    
    print ("              ", Bars)
    
    print ("[- Strand]: 3'", inDirectStrand, "5'\n")
    
    # get reversed complementary sequence
    
    print ("[- Strand]: 5'", inDirectStrand[::-1], "3'")
    
    """ 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~NOTE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    I'm not sure if you wanted us to use this method to reverse it or
    the reverseDNA.reverse(inDirectStrand) or another type of method
    that required an abstract way to reverse it.
    I went ahead with the extended slice as it seems relevant and works
    on other tests i did with the program.
    """
    
    print ("-----------------------------------------------------------------")
    
    # now print entire original lowercase sequence with only first codon (ATG) in uppercase
    
    startCodon = "atg"
    startCodonUpper = "ATG"
    
    print ("Original sequence:", originalSequence.replace(startCodon, startCodonUpper))
    
    print ("----------------------------------------------------------------")
    
    # print AT-richness: number of As and number of Ts in the upstream region (only)

    print ("Upstream Direct (+) Strand:")
    
    AsInUpstream = upStream.count('A')
    TsInUpstream = upStream.count('T')
    print ("Number of upstream As:", AsInUpstream)
    print ("Number of upstream Ts:", TsInUpstream)
    
    
    print ("-----------------------------------------------------------------")

# end main()

#-----------------------------------------------------
# Python starts here
if __name__ == '__main__':
    main()
#-----------------------------------------------------  
