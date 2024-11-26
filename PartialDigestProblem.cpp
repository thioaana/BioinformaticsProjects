#include <iostream>
#include <list>
#include <set>
#include <vector>
#include <cmath>
#include <bits/stdc++.h>

using namespace std;


void printVector(const vector<int>& L);
void printSet(const set<int>& X);
void PDP(vector<int>&, set<int>&);
int getSizeOfX(const int lenL);
bool checkIfVectorContainsValue(const vector<int>&, int);
void importNewValue(set<int>&, vector<int>&, int, int);

int main(){
    vector <int> L{2, 2, 3, 3, 4, 5, 6, 7, 8, 10};
    set <int> X{};

    printVector(L);
    PDP(L, X);
    printSet(X);

    return 0;
}

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

bool checkIfVectorContainsValue(const vector<int>& v, const int target){
    bool flag = 0;
    for (int i : v) {
        if (i == target) {
            flag = 1;
            break;
        }
    }
    return flag;
}

void importNewValue(set<int>& X, vector<int>& L, int newValue, int maxOfL){
    /*
    Import new value in the set X
    Delete every distance(new value, X) from L  */

    // Delete max of L from the list L 
    L.pop_back();

    /* For each value xv in set X :
        Find distance d(x, newValue)
        Delete d from list L the  */
    for (const int & x : X) {
        int d = abs(x - newValue);
        L.erase(find(L.begin(), L.end(), d));
    }

    // # Add newValue in set X
    // X.add(newValue)
}

void PDP(vector<int>& L, set<int>& X){
    // Sort L in ascending order
    sort(L.begin(), L.end());

     // Calculate the length of X
    int n = getSizeOfX(L.size());
    
    // Get the max value of L
    int maxOfL = L.back();

    // Delete max value of L from L
    L.pop_back();

    // Initialize set X
    X.insert({0, maxOfL});
    printVector(L);
    printSet(X);

    while (L.size() > 0) {
        maxOfL = L.back();
        int newPossibleValue = *max_element(X.begin(), X.end()) - maxOfL;      // It is always positive value

        // Check if the new value can be the leftmost point in X
        int leftMostPoint = true;
        for (const int& x : X) {
            if (checkIfVectorContainsValue(L, x)) {
                leftMostPoint = false;
                break;
            }
        }

        // If the new value is for sure the leftmost point
        if (leftMostPoint) {
            int newValue = newPossibleValue;
            importNewValue(X, L, newValue, maxOfL);
        }
        else {        
            int newValue = maxOfL;              // Typically min(X) + maxOfL, but min(X)=0
            importNewValue(X, L, newValue, maxOfL);
        }
    }
}
    