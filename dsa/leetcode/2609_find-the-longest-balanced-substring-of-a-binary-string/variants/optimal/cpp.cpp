#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    int findTheLongestBalancedSubstring(string s) {
        int longest = 0;
        int zeroes = 0;
        int ones = 0;

        for (char character : s) {
            if (character == '0') {
                if (ones > 0) {
                    zeroes = 0;
                    ones = 0;
                }
                ++zeroes;
            } else {
                ++ones;
                longest = max(longest, 2 * min(zeroes, ones));
            }
        }

        return longest;
    }
};
