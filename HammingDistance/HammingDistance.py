'''
Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
Given two strings s and t of equal length, the Hamming rdistance between s and t, denoted dH(s,t), 
is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
'''

if __name__ == "__main__":
    aStrand = "GAGCCTACTAACGGGAT"
    bStrand = "CATCGTAATGACGGCCT"

    HamDist = 0

    if len(aStrand) != len(bStrand):
        print("Hamming distance cannot be computed.\nThe strands length diffes")
    else:
        for i in range(len(aStrand)):
            if aStrand[i] != bStrand[i]:
                HamDist += 1

    print("Hamming Diastance : ", HamDist)