'''
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, 
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT
'''

if __name__ == "__main__":
    DNAStrand = "AAAACCCGGT"
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverseCompl = ""

    reversedDNA = ''.join(reversed(DNAStrand))
    print(reversedDNA)
    for d in reversedDNA:
        reverseCompl +=complements[d]

    print (reverseCompl)