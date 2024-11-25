#include <iostream>
#include <list>
#include <set>
#include <vector>
#include <cmath>
#include <bits/stdc++.h>

using namespace std;


void printVector(const vector<int>& L);
void printSet(const set<int>& X);
void PDP(vector<int>& k);
int getSizeOfX(const int lenL);

int main(){

    
    vector <int> * L = new vector({2, 2, 3, 3, 4, 5, 6, 7, 8, 10});
    set <int> * X = new set({0});
    printVector(*L);
    printSet(*X);

    PDP(*L);

    return 0;
}
    // set <ind> X s // print(PDP(L))

void printVector(const vector <int>& L) {
    for (int num : L) {
        cout << num << " ";
    }
    cout << endl;
}

void printSet(const set <int>& L) {
    for (int num : L) {
        cout << num << " ";
    }
    cout << endl;
}

int getSizeOfX(const int lenL){
    /*
    Having the length of L calculate the n (length of X)
    The equation to be solved is : n * (n-1) / 2 = lenL, 
    ie n^2 - n - 2*lenL = 0 and take the real number solution
    */
    int n = (1 + sqrt(1 + 8 * lenL)) / 2;
    return int(n);
}

void PDP(vector<int>& L){
    // Sort L in ascending order
    sort(L.begin(), L.end());

     // Calculate the length of X
    int n = getSizeOfX(L.size());
    
    // Get the max value of L
    int maxOfL = *max_element(L.begin(), L.end());

    // Delete max value of L from L
    L.pop_back();

    // Initialize set X
    set <int > X = {0, maxOfL};

    while (L.size() > 0) {
        maxOfL = *max_element(L.begin(), L.end());
        int newPossibleValue = *max_element(X.begin(), X.end()) - maxOfL;      // It is always positive value
        
        // Check if the new value can be the leftmost point in X
        bool leftMostPoint = true;
        for (int x : X) {
            cout << x << "-->";
            cout << X.count(10) << " -- " << X.count(50) << endl;
            //  if (abs(x - newPossibleValue) not in L) :
            //     leftMostPoint = False
            //     break        
        }
    }
}
    


        
//         # If the new value is for sure the leftmost point
//         if leftMostPoint :
//             newValue = newPossibleValue
//             importNewValue(X, L, newValue, maxOfL)
//         else :        
//             newValue = maxOfL              # Typically min(X) + maxOfL, but min(X)=0
//             importNewValue(X, L, newValue, maxOfL)
//     return X