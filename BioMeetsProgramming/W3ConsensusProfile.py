def Count(motifs):
    n = len(motifs[0])
    count = {'A': [0] * n, 'T': [0] * n, 'C': [0] * n, 'G': [0] * n}

    for i in range(n):
        for motif in motifs:
            count[motif[i]][i] += 1
    return count

def Profile(motifs):
    n = len(motifs[0])
    
    count = Count(motifs)
    profile = count
    for i in range(n):
        s = 0
        for k in count.keys():
            s += count[k][i]
        for k in count.keys():
            profile[k][i] /= s
    return profile

def Consensus(motifs):
    n = len(motifs[0])
    profile = Profile(motifs)

    consensus = []
    for i in range(n) :
        consensus.append(max([(v[i], k) for k, v in profile.items()])[1])
    return consensus

def Score(motifs):
    n = len(motifs[0]
            )
    count = Count(motifs)
    consensus = Consensus(motifs)

    score = 0
    for i in range(n) :
        for c in count:
            if c != consensus[i] :
                score += count[c][i]
    return score
                
0

def ProfileMostProbablePattern(text, k, profile):
    bestprob = -1
    bestMatching = -1
    for i in range(len(text) - k):
        p = Pr(text[i:i + k], profile)
        if p > bestprob :
            bestprob = p
            bestMatching = i
    return text[bestMatching: bestMatching + k]

if __name__ == "__main__":
    motifs = ['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG']
    # print(Count(['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG']))
    # print(Profile(['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG']))
    # print(Consensus(motifs))
    # print(Score(motifs))

    text = 'ACGGGGATTACC'
    prof = {}
    prof['A'] = [float(i) for i  in '0.2 0.2 0.3 0.2 0.3'.split(' ')]
    prof['C'] = [float(i) for i  in '0.4 0.3 0.1 0.5 0.1'.split(' ')]
    prof['G'] = [float(i) for i  in '0.3 0.3 0.5 0.2 0.4'.split(' ')]
    prof['T'] = [float(i) for i  in '0.1 0.2 0.1 0.1 0.2'.split(' ')]
    
    # print(Pr('ACGGGGATTACC', prof))
    print(ProfileMostProbablePattern('ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT', 5, prof))
