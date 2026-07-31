#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
    long long solve(vector<int> nums) {
        vector<pair<int, int>> ordered;
        ordered.reserve(nums.size());
        for (int index = 0; index < static_cast<int>(nums.size()); ++index) {
            ordered.emplace_back(nums[index], index);
        }
        sort(ordered.begin(), ordered.end());

        vector<bool> marked(nums.size(), false);
        long long score = 0;
        for (const auto& [value, index] : ordered) {
            if (marked[index]) {
                continue;
            }
            score += value;
            marked[index] = true;
            if (index > 0) {
                marked[index - 1] = true;
            }
            if (index + 1 < static_cast<int>(nums.size())) {
                marked[index + 1] = true;
            }
        }
        return score;
    }
};
