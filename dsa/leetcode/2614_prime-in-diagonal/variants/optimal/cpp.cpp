#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    int diagonalPrime(vector<vector<int>>& nums) {
        auto isPrime = [](int value) {
            if (value < 2) return false;
            if (value == 2) return true;
            if (value % 2 == 0) return false;
            int limit = static_cast<int>(sqrt(value));
            for (int divisor = 3; divisor <= limit; divisor += 2) {
                if (value % divisor == 0) return false;
            }
            return true;
        };

        int n = static_cast<int>(nums.size());
        int answer = 0;
        for (int i = 0; i < n; ++i) {
            int primary = nums[i][i];
            int secondary = nums[i][n - 1 - i];
            if (primary > answer && isPrime(primary)) answer = primary;
            if (secondary > answer && isPrime(secondary)) answer = secondary;
        }
        return answer;
    }
};
