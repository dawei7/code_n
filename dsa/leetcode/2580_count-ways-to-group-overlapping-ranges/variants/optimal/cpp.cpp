#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<vector<int>> ranges) {
        constexpr int modulus = 1'000'000'007;
        sort(ranges.begin(), ranges.end());

        int ways = 1;
        int currentEnd = -1;
        for (const auto& range : ranges) {
            if (range[0] > currentEnd) {
                ways = static_cast<int>(2LL * ways % modulus);
            }
            currentEnd = max(currentEnd, range[1]);
        }
        return ways;
    }
};
