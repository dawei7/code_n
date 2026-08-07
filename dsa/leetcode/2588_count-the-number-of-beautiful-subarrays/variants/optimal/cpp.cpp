#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    long long solve(vector<int> nums) {
        unordered_map<int, long long> prefixCounts{{0, 1}};
        int prefixXor = 0;
        long long answer = 0;

        for (int value : nums) {
            prefixXor ^= value;
            answer += prefixCounts[prefixXor];
            ++prefixCounts[prefixXor];
        }

        return answer;
    }
};
