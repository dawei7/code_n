#include <vector>

using namespace std;

class Solution {
public:
    int solve(int target, vector<vector<int>> types) {
        constexpr int modulus = 1'000'000'007;
        vector<int> ways(target + 1);
        ways[0] = 1;

        for (const vector<int>& type : types) {
            const int count = type[0];
            const int marks = type[1];
            const int expiredDistance = (count + 1) * marks;
            vector<int> nextWays(target + 1);

            for (int score = 0; score <= target; ++score) {
                long long value = ways[score];
                if (score >= marks) {
                    value += nextWays[score - marks];
                }
                if (score >= expiredDistance) {
                    value -= ways[score - expiredDistance];
                }
                value %= modulus;
                if (value < 0) {
                    value += modulus;
                }
                nextWays[score] = static_cast<int>(value);
            }

            ways = move(nextWays);
        }

        return ways[target];
    }
};
