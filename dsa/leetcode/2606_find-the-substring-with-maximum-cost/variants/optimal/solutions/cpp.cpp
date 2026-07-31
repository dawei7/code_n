#include <algorithm>
#include <array>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        array<int, 26> values{};
        iota(values.begin(), values.end(), 1);
        for (int index = 0; index < static_cast<int>(chars.size()); ++index) {
            values[chars[index] - 'a'] = vals[index];
        }

        int best = 0;
        int current = 0;
        for (char character : s) {
            current = max(0, current + values[character - 'a']);
            best = max(best, current);
        }
        return best;
    }
};
