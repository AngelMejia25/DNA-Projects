"""BioDNA : a module of DNA processing functions """
import re
# ----------------------------------------

def complementDNA_to_DNA( DNA ):
    """Returns the complement strand of DNA"""

    # you need to do the work here
    changeOriginal = "ACTG"
    toComplement = "TGAC"
    transTable = str.maketrans(changeOriginal, toComplement)
    complementaryStrand = DNA.translate(transTable)
    
    return complementaryStrand
# ----------------------------------------

# ----------------------------------------
def complementDNA_to_RNA( DNA ):
    """Returns the complement strand of RNA"""

    # you need to do the work here
    changeOriginal = "T"
    toComplement = "U"
    transTable = str.maketrans(changeOriginal, toComplement)
    complementaryStrand = DNA.translate(transTable)    

    return complementaryStrand
# ----------------------------------------

# ----------------------------------------    
def transcribe( DNA ):
    """Simulates transcription by building template strand and then complementing that to RNA"""
    
    # gene is on the DNA strand
    # but RNA copy is built off the template (or anti-sense) strand

    mRNA = ""   

    # (a) get complement of the DNA strand (that is, make the template strand)
    compDNA = complementDNA_to_DNA(DNA)
    
    # (b) get mRNA complement of the template strand
    # (c) return the mRNA
    
    # you need to do the work here    
    
    complementDNA = complementDNA_to_DNA(DNA)
    
    print (" DNA: 5'", DNA, "3'")
    print (" DNA: 3'", complementDNA, "5'")
    
    Bars = ""
    DNALen = len(DNA)
    while (DNALen > 0):
        Bars = Bars + "|"
        DNALen = DNALen - 1
     
    print ("        ", Bars)    
    
    mRNA = complementDNA_to_RNA(DNA)
        

    
    
    return mRNA
# ----------------------------------------
def getDNA(filename):
    """ Takes a .fna file of a DNA sequence and reads in the lines"""
    
    INFILE = open(filename, 'r')
    
    for filelines in INFILE:
        sequence = filelines
        
    return sequence


#-----------------------------------------
def findDirectRepeats(upstream):
    """Uses regex to search through the file and find direct repeats"""
    DRregex = re.compile(r"(.)(.)(.?)\1\2\3")
    
    DRiterator = DRregex.finditer(upstream)
    DRtotal = 0
    for nextDR in DRiterator: 
        DR = nextDR.group()            
        DRstart = nextDR.start() 
        DRend = nextDR.end() 
        DRtotal = DRtotal + len(DR)
         
        print ("Found DR:", DR, "[", DRstart+1, "to", DRend, "bp]")     
    return DRtotal
    
def findMirrorRepeats(upstream):
    """Uses regex to search through the file and find mirror repeats"""
    
    MRregex = re.compile( r"(.)(.)(.)\3\2\1" ) # build regex for MR of len=4bp
    
    MRiterator = MRregex.finditer(upstream) # find all matches
    MRtotal = 0 #going to be used to find percentile
    for nextMR in MRiterator: # loop thru list of matches
        MR = nextMR.group()      # get the actual regex match      
        MRstart = nextMR.start() # where did it begin
        MRend = nextMR.end()     # location just after the end
        MRtotal = MRtotal + len(MR)
        
        print ("Found MR:", MR, "[", MRstart+1, "to", MRend, "bp]") 
    return MRtotal
#-----------------------------------------
def findATRepeats(upstream):
    """Uses regex to search through the file and find ATAT repeats"""
    
    ATregex = re.compile(r"(A)(T)(A)(T)\1\2\3\4")
    
    ATiterator = ATregex.finditer(upstream)
    ATtotal = 0
    for nextAT in ATiterator: 
        AT = nextAT.group()            
        ATstart = nextAT.start() 
        ATend = nextAT.end() 
        ATtotal = ATtotal + len(AT)
         
        print ("Found AT:", AT, "[", ATstart+1, "to", ATend, "bp]")     
    return ATtotal
#-----------------------------------------
def makeAminoAcidTable( ):
    """Returns a Python Dictionary (hash table) that maps RNA nucleotides to Amino Acid symbols;
    both one letter and three letter symbols are returned; the user will need to parse which of
    these symbols they want to use"""
    
    AAtable = { "UUU":"F|Phe","UUC":"F|Phe","UUA":"L|Leu","UUG":"L|Leu","UCU":"S|Ser","UCC":"S|Ser",
                "UCA":"S|Ser","UCG":"S|Ser","UAU":"Y|Tyr","UAC":"Y|Tyr","UAA":"*|***","UAG":"*|***",
                "UGU":"C|Cys","UGC":"C|Cys","UGA":"*|***","UGG":"W|Trp","CUU":"L|Leu","CUC":"L|Leu",
                "CUA":"L|Leu","CUG":"L|Leu","CCU":"P|Pro","CCC":"P|Pro","CCA":"P|Pro","CCG":"P|Pro",
                "CAU":"H|His","CAC":"H|His","CAA":"Q|Gln","CAG":"Q|Gln","CGU":"R|Arg","CGC":"R|Arg",
                "CGA":"R|Arg","CGG":"R|Arg","AUU":"I|Ile","AUC":"I|Ile","AUA":"I|Ile","AUG":"M|Met",
                "ACU":"T|Thr","ACC":"T|Thr","ACA":"T|Thr","ACG":"T|Thr","AAU":"N|Asn","AAC":"N|Asn",
                "AAA":"K|Lys","AAG":"K|Lys","AGU":"S|Ser","AGC":"S|Ser","AGA":"R|Arg","AGG":"R|Arg",
                "GUU":"V|Val","GUC":"V|Val","GUA":"V|Val","GUG":"V|Val","GCU":"A|Ala","GCC":"A|Ala",
                "GCA":"A|Ala","GCG":"A|Ala","GAU":"D|Asp","GAC":"D|Asp","GAA":"E|Glu",
                "GAG":"E|Glu","GGU":"G|Gly","GGC":"G|Gly","GGA":"G|Gly","GGG":"G|Gly"}
    
    return AAtable
# ------------------------
    

def translate( mRNA, AAtable ):  
    """Returns the 3-letter amino acid string of symbols for the corresponding mRNA"""
    
    protein = ""
    
    startBP = 0
    endBP   = len(mRNA)
    
    nextCodonStart = startBP
    # while we don't run off the end of the sequence of mRNA, snag nucleotide codons
    #       and build a sequence of amino acid symbols (uses the 3-letter symbols)
    while ( nextCodonStart+3 <= endBP):
        
        # slice out the new RNA nucleotide triple
        nextCodon = mRNA[nextCodonStart:nextCodonStart+3]
        
        # play RIBOSOME: convert an RNA nucleotide-triple to an amino acid symbol
        nextAA = AAtable[ nextCodon ]
        
        # amino acid symbols come as two types of symbols (3 letter and 1 letter);
        # in general:  triple:<one letter code>|<three letter code>
        # e.g.,  "GAG":"E|Glu" ... thus we need to parse out which type of symbol we want
        
        # we want the 3-letter 'Glu' version here, so slice out from location 2 to the end
        AAsymbol = nextAA[2:]
        
        # add this AA onto the end of the growing amino-acid (protein) chain
        protein = protein + AAsymbol
        
        # move down to next triple
        nextCodonStart = nextCodonStart + 3
        
    # end while more triples to check
    
    return protein

# ---- end translate() ----------------------------------------