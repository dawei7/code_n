#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        const int n = static_cast<int>(nums.size());
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        vector<long long> answer;
        answer.reserve(queries.size());
        for (int query : queries) {
            const int split = static_cast<int>(
                lower_bound(nums.begin(), nums.end(), query) - nums.begin()
            );
            const long long left_cost =
                1LL * query * split - prefix[split];
            const long long right_cost =
                prefix[n] - prefix[split] - 1LL * query * (n - split);
            answer.push_back(left_cost + right_cost);
        }
        return answer;
    }
};

