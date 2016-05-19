"""
Programmer: Angel Mejia

Summary: This program will search thru a sequence of DNA and will 
search for the number of Motifs or Lmers that is requested by the user. After
the program has finished the results will be sent to a .csv file.

Input: When you run the program you will be prompted to enter the amount of
Lmers you wish to search for. You will need to enter an input between 4 to 8.
The program will require an "inputDirectory" folder in the current location. 
This folder should contain the sequences you will be using, but they MUST be
stored in a ".fna" file. Do note the DNA in the .fna file must be uppercase
as the program will not do that for you, that said the program is not case 
sensitive and will run the same on lowercase output.

Output: When the program is finished, it will return some output in the console
to tell you which files it has currently searched through and the length of their
DNA sequence. The program will go through these files in alphabetical order.
Afterwards the program will return a ".csv" file in the same location as this
program. The file will contain information on the file and where it is found 
along with the number of motifs in the file, and a table organized to tell you
which motifs appear most frequently and the proportion they take up of the
entire DNA sequence. 
"""

import os
import glob
from math import *
import BioDNA


def main():
        
    COMMA = "," #used as comma placeholder for later insertion for code readability
    Dict = {}
    
    BioDNA.Print_Title() #Start by printing Title from the BioDNA module
    
    inputDirectory = "inputDirectory" #this folder will contain the files.
    
    fullPath = os.path.join(inputDirectory, "*.fna") #Get DNA sequence from file
    
    fileList = glob.glob(fullPath) #get the full path list for files
    
    fileList.sort() #sort the list of files.
    
    Lmer = BioDNA.getLmer()
    
    print("\nWill commence searching for Lmer's of Length: ", Lmer)
    
    #next is getting the Lmers and counting them
    for nextFile in fileList:
        #loop to get the information from all the files in the location
        
        seq = BioDNA.getDNA(nextFile) #get the DNA from current file
        
        print("Currently in file: ", nextFile, "With DNA length: ", len(seq), "bp")
        
        listOfMotifs = BioDNA.breakIntoMotifs(seq, Lmer) #Storing the seq motifs in list
        
        wordCounts = {} #Count the number of times the word appears
        
        #For one word at a time
        for word in listOfMotifs:
            if word in wordCounts: 
                #increase the word count
                wordCounts[word] = wordCounts[word] + 1
                
            else: #for when we first see it
                wordCounts[word] = 1
                
        #sort by the values from most common to least common using a stored tuple     
        wordCounts = sorted(wordCounts.items(), key = lambda x:x[1], reverse=True)
        
        
        Motifsnb = len(seq) - (Lmer - 1) #calculate number of motifs
        
        
        #Next convert results into an excel sheet
        outFile = open("results.csv", 'a') # 'a' will append
        
        outFile.write("%s%s \n" % ("Filename: ", nextFile) )  #file name to .xls 
        outFile.write("%s%s \n" % ("Number of motifs: ", Motifsnb) )  #number of motifs to .xls file
        outFile.write("%s%c%s%c%s%c%s\n" % ("Rank", COMMA, "Motif", COMMA, "Frequency", COMMA, "Proportions" ) )  #headers
           
           
        topMotifs = 1 #will hold the ranks of the motifs
        for nextKey in wordCounts[0:10]:                
            outFile.write("%s%c%s%c%s%c%s\n" % (topMotifs, COMMA, nextKey[0], COMMA, nextKey[1], COMMA, nextKey[1] / Motifsnb )) # output values to .xls
            topMotifs = topMotifs + 1        # increment by 1        
    
    
if __name__ == '__main__':
    main()