#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<int> nums, int value) {
        unordered_map<int, int> remainder_counts;
        for (int number : nums) {
            int remainder = ((number % value) + value) % value;
            ++remainder_counts[remainder];
        }

        int mex = 0;
        while (remainder_counts[mex % value] > 0) {
            --remainder_counts[mex % value];
            ++mex;
        }
        return mex;
    }
};
