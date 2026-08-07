#include <cstdlib>
#include <numeric>
#include <vector>

class Solution {
public:
    std::vector<int> solve(std::vector<int> nums) {
        long long left_sum = 0;
        long long right_sum = std::accumulate(nums.begin(), nums.end(), 0LL);
        std::vector<int> answer;
        answer.reserve(nums.size());

        for (int value : nums) {
            right_sum -= value;
            answer.push_back(static_cast<int>(std::llabs(left_sum - right_sum)));
            left_sum += value;
        }
        return answer;
    }
};
