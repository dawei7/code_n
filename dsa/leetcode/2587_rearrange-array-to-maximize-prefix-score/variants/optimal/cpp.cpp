#include <algorithm>
#include <functional>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<int> nums) {
        sort(nums.begin(), nums.end(), greater<int>());

        long long prefixSum = 0;
        int score = 0;
        for (int value : nums) {
            prefixSum += value;
            if (prefixSum <= 0) {
                break;
            }
            ++score;
        }
        return score;
    }
};
