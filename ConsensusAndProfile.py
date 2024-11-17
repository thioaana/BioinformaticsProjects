'''
Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j
 represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the j
th position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the j
th symbol of c therefore corresponds to the symbol having the maximum value in the j
-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
'''

def getFormalDNA(s):
    formal = s.split('\n')
    formal = formal[:len(formal)-1]
    
    for i in range(len(formal)):
        formal[i] = formal[i].replace(" ", "")
    
    return formal;

def getProfile(dna):
    pr = []


    for col in range(len(dna[0])) :
        dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        
        for row in range(len(dna)) :
            dict[dna[row][col]] += 1
        pr.append(dict)
    return pr
        

if __name__ == "__main__":
    DNAStrings = '''A T C C A G C T
                    G G G C A A C T
                    A T G G A T C T
                    A A G C A A C C
                    T T G G A A C T
                    A T G C C A T T
                    A T G G C A C T
                    '''

    DNAFormal = getFormalDNA(DNAStrings)
    print(DNAFormal)

    profile = getProfile(DNAFormal)
    print(profile)
    
    consensus = [max(zip(p.values(), p.keys()))[1] for p in profile]
    print(consensus)
