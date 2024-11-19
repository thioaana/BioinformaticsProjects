import BioMeetsProgrammingW1 as bioW1

def SymbolArray(genome, symbol):
    array = {}
    n = len(genome)
    extendedGenome = genome + genome[:n//2]
    array[0] = bioW1.PatternCount(extendedGenome[:n//2], symbol)

    for i in range(1, n):
        # Initialize the new member of array
        array[i] = array[i - 1]

        if extendedGenome[i-1] == symbol :
            array[i] -= 1
        if extendedGenome[i + n//2 - 1] == symbol :
            array[i] += 1

    return array

def SkewArray(genome):
    skew = [0]
    for i, n in enumerate(genome):
        if n == 'G' : skew.append(skew[i] + 1)
        elif n == 'C': skew.append(skew[i] - 1)
        else : skew.append(skew[i])

    return skew

def MinimumSkew(genome):
    skewArray = SkewArray(genome)
    minSkewPositions = []
    m = min(skewArray)
    for i, s in enumerate(skewArray):
        if s == m:
            minSkewPositions.append(i)
    return minSkewPositions

def HammingDistance(text1, text2):
    hamdist = 0
    for i in range(len(text1)):
        if text1[i] !=text2[i]:
            hamdist += 1
    return hamdist

def ApproximatePatternMatching(text, pattern, d):
    startsAt = []
    lenP = len(pattern)
    for i in range(len(text) - lenP + 1) :
        if HammingDistance(text[i:i + lenP], pattern) <= d :
            startsAt.append(i)
    return startsAt

def ApproximatePatternCount(pattern, text, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern or \
           HammingDistance(text[i:i + len(pattern)], pattern) <= d :
            count += 1

    return count

if __name__ == "__main__":
    genome = "AAAAGGGG"
    symb = 'A'
    text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
    # print(SymbolArray(genome, symb))
    # print(SkewArray('CATGGGCATCGGCCATACGCC'))
    # print(MinimumSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'))
    # print(HammingDistance('GGGCCGTTGGT', 'GGACCGTTGAC'))
    # print(ApproximatePatternMatching('CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT', 'ATTCTGGA', 3))
    print(ApproximatePatternCount('GAGG', 'TTTAGAGCCTTCAGAGG', 2))