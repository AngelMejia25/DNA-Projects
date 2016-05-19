            -+-+-+_Motif & Frequency Finder v0.3_+-+-+-


    -._    _.--'"`'--._    _.--'"`'--._    _.--'"`'--._    _  
    '-:`.'|`|"':-.  '-:`.'|`|"':-.  '-:`.'|`|"':-.  '.` : '.   
  '.  '.  | |  | |'.  '.  | |  | |'.  '.  | |  | |'.  '.:   '.  '.
  : '.  '.| |  | |  '.  '.| |  | |  '.  '.| |  | |  '.  '.  : '.  `.
  '   '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.'   `.
         `-..,..-'       `-..,..-'       `-..,..-'       `         `
         

             -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
             
Program to search through DNA Sequences and find Motifs and how often they 
appear in the DNA Sequence.

Documentation
----------------

This program was written in Python 3.4.3 and uses the following modules:
-Python os module
-Python glob module
-Python math module
-BioDNA.py module file that accompanies this program.

Running this program
------------------------

Before running the program place all DNA sequences in the "inputDirectory" folder
that comes in the main folder for this program. All files in the "inputDirectory"
folder must be of '.fna' extension, the program will ignore any files of a different
extension. 

Open the "Mejia_A5.py" in any Python editor that is capable of USER INPUT 
(for instance this program was built and tested in Wing IDE v5) and then 
run the program from there. The program will prompt you for the Lmer size
you wish to search for, any integer between 4 to 8, and will run from there.

The program will output some information to the console, but will also produce
a "results.csv" file which will neatly organize the information from the files
into tables for each file it is given. The file will contain information about
the frequency of the motif size given, what the motif is and the proportion of
the motif in the sequence. The program will only return the top 10 motifs with
the most frequent being ranked 1 in the table, descending to 10. 

NOTE: The program will always output a "results.csv" and if ran multiple times
will append the new results onto the file. PLEASE rename the filename if you 
wish for different files holding seperate results!!!!!

-------------------------------------------------------------------------------

This program is part of a project for COMP 242 - DNA, at Wheaton College.
-Angel Mejia 16'