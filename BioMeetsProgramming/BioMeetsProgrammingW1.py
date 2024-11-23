def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern :
            count += 1
    return count

def FrequencyMap(text, k):
    freq = {}
    for i in range(len(text) - k + 1):
        freq[text[i:i+k]] = freq.get(text[i:i+k], 0) +1
    return freq

def FrequentWords(text, k):
    words = []
    freq = FrequencyMap(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m :
            words.append(key)
    return words

def Reverse(pattern):
    return pattern[::-1]

def getComplement(pattern):
    dirCompl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement = ""
    for p in pattern:
        complement += dirCompl[p]
    return complement

def ReverseComplement(pattern):
    return getComplement(Reverse(pattern))

def PatternMatching(pattern, genome):
    startsAt = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i + len(pattern)] == pattern :
            startsAt.append(i)
    return startsAt


if __name__ == '__main__':
    Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
    k = 9
    # print(FrequencyMap(Text, 4))
    # print(FrequentWords(Text, k))
    # print('\nAAAACCCGGT\n', ReverseComplement('AAAACCCGGT'))
    print(PatternMatching('ATAT', 'GATATATGCATATACTT'))