#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    int solve(int num) {
        string digits = to_string(num);
        sort(digits.begin(), digits.end());

        int first = 0;
        int second = 0;
        for (int index = 0; index < static_cast<int>(digits.size()); ++index) {
            const int digit = digits[index] - '0';
            if (index % 2 == 0) {
                first = first * 10 + digit;
            } else {
                second = second * 10 + digit;
            }
        }
        return first + second;
    }
};
