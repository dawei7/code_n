#include <vector>

using namespace std;

class Solution {
public:
    vector<int> solve(int n) {
        vector<int> counts(2, 0);
        int index = 0;

        while (n > 0) {
            counts[index & 1] += n & 1;
            n >>= 1;
            ++index;
        }

        return counts;
    }
};
