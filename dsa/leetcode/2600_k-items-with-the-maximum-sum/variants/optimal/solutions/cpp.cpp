#include <algorithm>

using namespace std;

class Solution {
public:
    int solve(int numOnes, int numZeros, int numNegOnes, int k) {
        int selected_ones = min(numOnes, k);
        int selected_neg_ones = max(0, k - numOnes - numZeros);
        return selected_ones - selected_neg_ones;
    }
};
