'''
The digestion results in a collection of short DNA fragments, and the lengths of these fragments are recorded 
in multiset A. Attempting to reconstruct the locations of the restriction sites in the target DNA molecules 
using multiset A is known as the Partial Digest Problem, PDP.

Given all pairwise distances between points on a line, reconstruct thepositions of those points.
Input: The multiset of pairwise distances L, containing integers (n ana 2).
Output: A set X, of n integers, such that ∆X = L

Steven Skiena brute force algorithm is used.
'''

from math import sqrt

def getSizeOfX(lenL):
    '''
    Having the length of L calculate the n (length of X)
    The equation to be solved is : n * (n-1) / 2 = lenL, 
    ie n^2 - n - 2*lenL = 0 and take the real number solution
    '''
    n = (1 + sqrt(1 + 8 * lenL)) / 2
    return int(n)

def getMaxAndPosition(L):
    m = max(L)
    ind = L.index(m)
    return (ind, m)

def initializeX(n, m):
    X = [-1] * n
    X[0] = 0
    X[-1] = m
    return X

def importNewValue(X, L, newValue, maxOfL):
    '''
    Import new value in the set X
    Delete every distance(new value, X) from L 
    '''
    # Delete max of L from the list L 
    # L.remove(maxOfL)

    # For each value xv in set X :
    #   Find distance d(x, newValue)
    #   Delete d from list L the  
    for x in X :
        d = abs(x - newValue)
        L.remove(d)
    
    # Add newValue in set X
    X.add(newValue)


def PDP(L):
    # Calculate the length of X
    n = getSizeOfX(len(L))
    
    # Get the max value of L
    maxOfL = max(L)

    # Delete max value of L from L
    L.remove(maxOfL)

    # Initialize set X
    X = {0, maxOfL}

    while len(L) > 0 :
        maxOfL = max(L)
        newPossibleValue = max(X) - maxOfL      # It is always positive value
        
        # Check if the new value can be the leftmost point in X
        leftMostPoint = True
        for x in X :
            if abs(x - newPossibleValue) not in L :
                leftMostPoint = False
                break
        
        # If the new value is for sure the leftmost point
        if leftMostPoint :
            newValue = newPossibleValue
            importNewValue(X, L, newValue, maxOfL)
        else :        
            newValue = maxOfL              # Typically min(X) + maxOfL, but min(X)=0
            importNewValue(X, L, newValue, maxOfL)
    return X



if __name__ == "__main__" :
    L = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]
    # L = [9, 30, 100, 170, 293, 302, 393, 402, 462, 562, 632, 732, 855, 864, 945, 954, 975, 984, 1025, 1034, 1247, 1277, 1347, 1377, 1809, 1839, 1979, 2009]
    print(L)
    print(sorted(PDP(L)))