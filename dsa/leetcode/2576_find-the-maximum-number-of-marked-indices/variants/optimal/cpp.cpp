#include <algorithm>
#include <vector>

class Solution {
public:
    int solve(std::vector<int> nums) {
        std::sort(nums.begin(), nums.end());
        int small = 0;
        int large = static_cast<int>(nums.size()) / 2;
        const int small_limit = static_cast<int>(nums.size()) / 2;

        while (small < small_limit && large < static_cast<int>(nums.size())) {
            if (2LL * nums[small] <= nums[large]) {
                ++small;
            }
            ++large;
        }
        return 2 * small;
    }
};
