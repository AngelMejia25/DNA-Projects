"""
Angel Mejia
October 23, 2015

This Code checks a sequence and finds the TATA box for that sequence. Once the
code finds the TATA box it will take the upstream and return information on it
using different methods such as regex. The program requires the BioDNA.py file 
the same folder as this file. 

When you run the program it will ask you to input a file, make sure the file is
of a '.fna' extension and that the file is in the same folder as the program.

The program will output information on the TATA box and upstream of the sequence.
You will also be provided with any direct repeats and mirrored repeats for the 
upstream of the sequence. 
"""
import BioDNA
import re

def main():
    
    
    #Code starts here to prompt user for a file
    sequence = input("Please enter the filename where your sequence is stored: ")
    sequence = BioDNA.getDNA(sequence)
    
    print("\n The size of region being searched is: ", len(sequence))
    
    print("====================================================================")
    
    TATA = re.compile(r"TATA[AT]A[AT][AG]")
    
    TATABox = TATA.finditer(sequence)
    
    box = ""
    
    for nextBox in TATABox:
        box = nextBox.group()
        TAstart = nextBox.start()
        TAend = nextBox.end()
        
    if (box == ""):
        print("There is no TATABox. Program Terminating.")
        return     
    
    print(sequence[:TAstart].lower() + sequence[TAstart:TAend] + sequence[TAend:].lower())
    
    indexes = ""
    count = 1
    for index in range(len(sequence)):
        indexes = indexes + str(count)
        count += 1
        if (count > 9):
            count = 0
    
    print(indexes)
    upstream = sequence[:TAstart]
    if (len(upstream) == 0):
        print("Upstream:    None.")
    else:
        print("Upstream:  ", "[ 1 to", TAstart + 1, "bp]")
        
    print("TATA-Box:  ", "[", TAstart + 1, "to", TAend, "bp]")
    
    print("Downstream:  ", "[", TAend + 1, "to", len(sequence), "bp]")
    
    print ("-------------------------------------------------------------------\n")
    
    #----------------------------------------------------------------------------
    print("Upstream of TATA-Box")
    print("----------------------------------------------------------------------")
    
    print(upstream)
    print(indexes[:TAstart+1])
    print(len(upstream), "bp")
    
    percentUP = (len(upstream) / len(sequence)) * 100
    print("Percentage of upstream region is: ", round(percentUP,1) ," %") 
    
    #If upstream has length of 0, the program will end to avoid any further calculation errors
    if (len(upstream) <= 0):
        print("!!!!!!!!")
        print("TATA-Box at beginning, no upstream gene, program terminating.")
        return
    print("---------------------------------------------------------------------\n")
    
    
    #Calls function to find direct repeats in the upstream of the sequence
    print("Searching for direct repeats (DR) in upstream region. \n")
    
    
    directRepeats = BioDNA.findDirectRepeats(upstream)
    
    percentDR = (directRepeats / len(upstream)) * 100
    print("\nPercentage of DRs in upstream region is: ", round(percentDR,1), " %")
    print("--------------------------------------------------------------------\n")
    
    print("--------------------------------------------------------------------")
    
    #Calls function in BioDNA to find mirror repeats in the upstream
    print("Searching for mirror repeats (MR) in upstream region. \n")
    
    mirrorRepeats = BioDNA.findMirrorRepeats(upstream)
    
    percentMR =  (mirrorRepeats / len(upstream)) * 100
    print("\nPercentage of MRs in upstream region is: ", round(percentMR, 1) ," %")
    
    print("---------------------------------------------------------------------")
    
    print("---------------------------------------------------------------------")
    
    print("Searching for AT repeats.")
    
    ATrepeats = BioDNA.findATRepeats(upstream)
    
    percentAT =  (ATrepeats / len(upstream)) * 100
 
    
    print("\nPercentage of ATs in upstream region is: ", round(percentAT, 1) ," %")    
    
    
if __name__ == '__main__':
    main()