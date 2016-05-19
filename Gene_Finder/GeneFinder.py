"""---------------------------------------------------------------------------
Programmer: Angel Mejia

Summary: This program's focus is on the central Dogma for biology relating
to DNA, RNA and proteins, specificially the transcription and translation for 
them that turns DNA into Proteins. After the translation for the DNA this program
will also provide you with addition information about the translated protein 
recieved. This program relies on a helper file "BioDNA.py" and will not run 
without said file. The "BioDNA.py" contains the transcription and translation
functions needed to run the program. There is also a protein table to return the
correct translated values.

Input: This program takes an input of a DNA sequence. Below is a variable 'DNA'
which the program requires to run. Change the DNA to any sequence you wish. Make
sure the sequence you enter is a String and consists only of the nucleotides
that make up a DNA sequence (ACGT) or the program will not work properly. 

output: The program will first output the transcription from the DNA to RNA and 
return to you the mRNA. The program will then translate the mRNA and return to
you a new string of proteins in relation to that mRNA. Afterwards the program 
return to you three reading frames of the protein. The second and third frames
remove the first and second nucleotides of the mRNA respectively and give you 
the new shorter proteins based on the new mRNA. Also the program will provide
you with some information about the proteins such as whether there is a correct
start and stop codon. And if these stop and start codon are found anywhere
else in the sequence. The 3 reading frames will allow you, the user, to find the
best based on the information given about the stop and start codons, but will 
not tell you which reading frame is the best, that is up to you to decide.
---------------------------------------------------------------------------"""

import BioDNA

def main():
    
    print ("\n       ---+++ Mean Gene Machine v0.1 +++---\n")
    
    AAtable = BioDNA.makeAminoAcidTable()
    
    #for (tripleRNA, AAcode) in AAtable.items():
    #    print (tripleRNA, AAcode)

        
    DNA = "ATGTGTACGCAAATGATATCGTATTAG";
    #DNA = "ATGCCGTACAGTATGCCAGTAGCATGGAAGCATTATAG"
    
    
    # --------- TRANSCRIBE --------------------------
    
    #converts the DNA to RNA and returns the RNA
    mRNA = BioDNA.transcribe(DNA)
    
    #prints out new RNA sequence after transcription.
    print("mRNA: 5'", mRNA, "3'")    
    

    print ("\n==============================================================")
    print ("Reading Frame #1")
    # --------- TRANSLATE Reading Frame #1 --------------------------
 
    print("RNA length: ", len(mRNA), " bp")
    
    print("     RNA:      ", mRNA)
    
    #small Loop to to connect the RNA codons to the proteins using '|' bars
    Bars = ""
    RNALen = len(mRNA)
    while (RNALen > 0):
        Bars = Bars + "  |"
        RNALen = RNALen - 3
    print ("              ", Bars) 
    #Definitely not the most efficient way to do it, but it works.
    
    proteins = BioDNA.translate(mRNA, AAtable)
    print("     Protein:  ", proteins, "\n")
    
    #These variables hold the location of specific proteins in the string
    proStart = proteins.find("Met") 
    proEnd = proteins.find("***")
    midMet = proteins[1:].find("Met")
    
    #Comparison of the start protein to see if it is a "Met" protein
    if (proStart == 0):
        print("There is a Met at the start site.")
    else:
        print("There is no Met at the start.")
        
    #A comparison for a stop Protein, checking to see if the sequence ends with a STOP
    if (proEnd == len(proteins) - 3):
        print("There is a stop at the end")
    else:
        print("There is no stop at the end")
    
    #A double check for the "Met" protein anywhere else in the sequence besides start
    #This statement only lets you know that is is there, but not where.
    if (midMet > 1):
        print("There is atleast one Met somewhere other than start.")
    else:
        print("There are no Mets in positions outside of the start site.")
    
    #Similar check as above, but for any STOPS not at end of sequence
    if (proEnd < len(proteins) - 3 and proEnd > 0):
        print("There is at least one stop interrupting the gene.")
    else: 
        print("There are no interrupting stops.")
    
    
    
    print ("==============================================================\n")
    
    
    print ("\n==============================================================")
    print ("Reading Frame #2")
    # --------- TRANSLATE Reading Frame #2 --------------------------
    
    mRNA2 = mRNA[1:] # Used to shift the RNA sequence over by 1 - Gets rid of first Nucleotide
    
    print("RNA length: ", len(mRNA2), " bp")
    
    print("     RNA:      ", mRNA2)
    
    #Same bar loop as above
    Bars = ""
    RNALen = len(mRNA2)
    while (RNALen > 2):
        Bars = Bars + "  |"
        RNALen = RNALen - 3
    print ("              ", Bars) 
    
    #translating for the new mRNA
    proteins = BioDNA.translate(mRNA2, AAtable)
    print("     Protein:  ", proteins, "\n")
    
    
    proStart = proteins.find("Met")
    proEnd = proteins.find("***")
    midMet = proteins[1:].find("Met")
    
    if (proStart == 0):
        print("There is a Met at the start site.")
    else:
        print("There is no Met at the start.")
        
    if (proEnd == len(proteins) - 3):
        print("There is a stop at the end")
    else:
        print("There is no stop at the end")
        
    if (midMet > 1):
        print("There is atleast one Met somewhere other than start.")
    else:
        print("There are no Mets in positions outside of the start site.")
    
    if (proEnd < len(proteins) - 3):
        print("There is at least one stop interrupting the gene.")
    else: 
        print("There are no interrupting stops.")    
    
    
    
    print ("==============================================================\n")
    
    
    print ("\n==============================================================")
    print ("Reading Frame #3")
    # --------- TRANSLATE Reading Frame #3 --------------------------
 
    mRNA3 = mRNA[2:]
    
    print("RNA length: ", len(mRNA3), " bp")
    
    print("     RNA:      ", mRNA3)
    
    Bars = ""
    RNALen = len(mRNA3)
    while (RNALen > 2):
        Bars = Bars + "  |"
        RNALen = RNALen - 3
    print ("              ", Bars) 
    
    proteins = BioDNA.translate(mRNA3, AAtable)
    print("     Protein:  ", proteins, "\n")
    
    proStart = proteins.find("Met")
    
    proEnd = proteins.find("***")
    
    midMet = proteins[1:].find("Met")
    
    if (proStart == 0):
        print("There is a Met at the start site.")
    else:
        print("There is no Met at the start.")
        
    if (proEnd == len(proteins) - 3):
        print("There is a stop at the end")
    else:
        print("There is no stop at the end")
        
    if (midMet > 1):
        print("There is atleast one Met somewhere other than start.")
    else:
        print("There are no Mets in positions outside of the start site.")
    
    if (proEnd < len(proteins) - 3):
        print("There is at least one stop interrupting the gene.")
    else: 
        print("There are no interrupting stops.")     
    
    
    
    print ("==============================================================\n")
    
    

        
# --- end main() ---------


#---------------------------------------------------------
# Python starts here ("call" the main() function at start
if __name__ == '__main__':
    main()
#---------------------------------------------------------  
    