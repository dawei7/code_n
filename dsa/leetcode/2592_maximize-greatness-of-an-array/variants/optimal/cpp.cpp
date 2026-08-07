#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<int> nums) {
        unordered_map<int, int> frequencies;
        int largestFrequency = 0;
        for (int value : nums) {
            largestFrequency = max(largestFrequency, ++frequencies[value]);
        }
        return static_cast<int>(nums.size()) - largestFrequency;
    }
};
