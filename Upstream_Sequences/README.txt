Use this program to find a TATA box in a sequence and return various
kinds of information about the upstream of the sequence. The program achieves 
this using different methods, particularly regex. The program requires the 
BioDNA.py file to be in the same folder and any files of sequences in your code
need to be in the same folder as well. The program will ask you to input the name
of these files when you run it. Make sure each of the files is of '.fna' format.

The program is currently in a working state but incredibly long sequences may 
cause some issues and cause the program to run for a long time. 

Make sure when inputting the filename into the program you do so without any
quotations or extra characters, and the filename input MUST be case sensitive.

REGEX patters used:

TATA Box:   'TATA[AT]A[AT][AG]'

            used to find an 8-motif for the TATA box in the sequence.

Direct Repeats:         '(.)(.)(.?)\1\2\3'

            Used to find repeats of lengths 4-6bp meaning it will return
            any two letter repeat followed by another two letter repeat, or a
            three letter followed by the same three letters.

Mirror Repeats:         '(.)(.)(.)\3\2\1'
            
            Used to find any nucleotides a that are mirrored on the same 3 bp 
            before it. The total length is 6bp.
            
My Favorite Repeat:     '(A)(T)(A)(T)\1\2\3\4'
            
            Used to find my favorite repeat of 'ATAT'(Reminds me of a certain
            giant quadrapedal robot from a galaxy far away) in the sequence. The
            similar Lettering to the TATA box would lead to expectation that this
            would appear often, especially near the TATA box, but it is not included
            in the upstream meaning it doesn't appear as often as expected.