def HammingDistance(text1, text2):
    '''
    Calculates the Hamming distance between 2 texts
    '''
    hamdist = 0
    for i in range(len(text1)):
        if text1[i] !=text2[i]:
            hamdist += 1
    return hamdist

def Count(motifs):
    '''
    Input  : A list of motifs (ie string)
    Return : A dictionary with keys A T C G.
             Each value is a list of length eq to len(motif[0])
             Each element represtents the count of the key in posistion i. 
    '''
    n = len(motifs[0])
    count = {'A': [0] * n, 'T': [0] * n, 'C': [0] * n, 'G': [0] * n}

    for i in range(n):
        for motif in motifs:
            count[motif[i]][i] += 1
    return count

def Profile(motifs):
    '''
    Input  : A list of motifs (ie string)
    Output : Similrs to Count.
             But insteand of counting has the percentage (ie count devided by num of motifs)
    '''
    n = len(motifs[0])
    
    count = Count(motifs)
    profile = count
    for i in range(n):
        s = len(motifs)
        # s = 0
        # for k in count.keys():
        #     s += count[k][i]
        for k in count.keys():
            profile[k][i] /= s
    return profile

def Consensus(motifs):
    '''
    Input  : A list of motifs (ie strings)
    Output : A list. Each element is a character. Its The most possible neucleod based on Profile
    '''
    n = len(motifs[0])
    profile = Profile(motifs)

    consensus = []
    for i in range(n) :
        consensus.append(max([(v[i], k) for k, v in profile.items()])[1])
    return consensus

def Score(motifs):
    '''
    Input  : A list of motifs (ie strings)
    Output : An integer. The addition af all cases where the character is not the relevant concensus character 
    '''
    n = len(motifs[0])
    count = Count(motifs)
    consensus = Consensus(motifs)

    score = 0
    for i in range(n) :
        for c in count:
            if c != consensus[i] :
                score += count[c][i]
    return score

def getMotifsMinDistance(pattern, text) :
    m = len(text)
    for i in range(len(text) - len(pattern) + 1) :
        ham = HammingDistance(pattern, text[i:i + len(pattern)])
        if ham < m :
            m = ham
    return m

def sumMinMotifsDist(pattern, motifs):
    s = 0
    for motif in motifs :
        s += getMotifsMinDistance(pattern, motif)
    return s

def MedianStringProblem(motifs, k):
    finalMotifsDist = 1000
    medianString  = ""

    for motif in motifs :
        for i in range(len(motif) - k + 1) :
            pattern = motif[i:i + k]
            motifsDist = sumMinMotifsDist(pattern, motifs)
            if motifsDist < finalMotifsDist :
                finalMotifsDist = motifsDist
                medianString = pattern
    return medianString

def Pr(text, profile):
    p = 1
    for i, t in enumerate(text):
        p *= profile[t][i]
    return p

def ProfileMostProbable_kMmerProblem(text, k, profile):
    finalPr = 0
    finalStr = ""
    n = len(text)
    for i in range(n - k + 1) :
        pattern = text[i: i + k]
        pr = Pr(pattern, profile)
        if pr > finalPr :
            finalPr = pr
            finalStr = pattern
    return finalStr


if __name__ == "__main__" :
    # motifs = ['TCAGGTTCCGCCTGGCGAATTCTATAAATGTCCTGCGGATGC','GCTCCGGACCTTGGATTCGCAGCGTATATGGTTATTCGCCAC',
    #           'CGAGTATAAATGGCAGTGGCTTGTGAAATGCTGCTTTAAACG', 'TACATGCAATCATTACCTGCCCACAGGGATTCGCTCTCAGAA',
    #           'AGACGATACATGAGGTACAGGCCACGCGTTGCACAAAGATTT', 'GACACATTGGCTGGCGAATTGTCTGGCAGTTACATGTTATGA',
    #           'ATCTGGTACTGGCCCAAATACATGACCCGATAGGGTAATCTT', 'GAAATGGTCCTGGTTGCATACATGCATTAGGGAGTCTCCGAT'
    #           'TCTCTACCTTACTTGGTACTCAAGATCATGTGGTGCTAAATG', 'CCATAAGGGTTCTATATGATAATACGCTGCACAGGAGAGTCC']
    # k = 6
    # print(MedianStringProblem(motifs, k))

    text = 'TCAGGAACGTCGTGAGAACAGCCAGGGGATGTTTGCGAATTGGGTTAGAGCCAAACGGCAATTCCAAGATTGTTGCTATACGACCAAGCATCGCTGCACCAACGCGCCAGGGGGTTTAGGGTTCTATTTCCCGAACCAATGCCTAAATCGACCATGTTATGAGCTCGTGGCAGCTATTTAGACCCGGACCAGTCGACTCGACCCGTGGCAGTTAAGAAACACGCGATTTGTTGAACGTAACCTCTATCATGCCGTACAAGCATTCTGCTCTAGTCCCGGGCAAACTGTCGTGGTGCCCGCCCAAGTGTGAGGTCCCTTAACCTACCTCACTTGACTCTTAAGGGGCAATAGTCTCAAGACCTTAAGACTCTGGGTGCTCTGAACTTGAAGAAAACAAATCCACGCCAACGGCATAACTGCCCCGCCCCCCGCGCGGATCTATGTCAATGCTGTCACATCCCGTCCTCCTGTGTATTCTCGGAAGCCAGACAGCCAATGTCATGGGGCGCGTCAGGGACCCCCAGCGGGGGATTAGATCATCCGTAGATTGGGATACGAGCGTGAGTGGGAAGGCGCTGGGAGGCCTGGCAAAGGCATTACTCGTTATGAATTACGTAAGTGGGAGATCATCCCCGTCCCGGTCCCTGTCCTTAGTGTGCTGGAGCAATCCACTCCCGTGTTGGCCGTGCGAAATGACCGGAGAATCGGAATGTCTACATAACCTAGACCTGTGTACTCCCCGCCGACTGGTCCGGTTTGATTAAGAGCGCGTTAACAACCACCCAATATGAGGGTGTGAGGGCACACGATGGCCATATATGATGTTGGGACCATTCTCTGTCCTGTGGGACGACATGACTGCCCACCTCACTCATGGGAATCCATGCGACGGGCTAGCGAGAAGCGTGTTGTCAGTCCCTTGCGGGACACAAGGTTACGTATACACCTCAGCCTCACTGGTTCCGCCAGGTCATTGTGAGAGTAACCTTTGAGTAATGAT'
    k = 12
    profile = {'A': [0.217, 0.193, 0.253, 0.277, 0.241, 0.205, 0.277, 0.277, 0.229, 0.301, 0.253, 0.241], 
               'C': [0.277, 0.241, 0.229, 0.277, 0.289, 0.265, 0.241, 0.289, 0.277, 0.169, 0.277, 0.277], 
               'G': [0.277, 0.289, 0.277, 0.253, 0.265, 0.277, 0.277, 0.193, 0.241, 0.241, 0.265, 0.265], 
               'T': [0.229, 0.277, 0.241, 0.193, 0.205, 0.253, 0.205, 0.241, 0.253, 0.289, 0.205, 0.217]}   
    print(ProfileMostProbable_kMmerProblem(text, k, profile))