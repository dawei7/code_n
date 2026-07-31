#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<int> nums) {
        if (nums.size() < 2) {
            return -1;
        }

        const int limit = *max_element(nums.begin(), nums.end());
        vector<int> smallest(limit + 1);
        for (int value = 0; value <= limit; ++value) {
            smallest[value] = value;
        }
        for (int prime = 2; prime * prime <= limit; ++prime) {
            if (smallest[prime] == prime) {
                for (int multiple = prime * prime; multiple <= limit; multiple += prime) {
                    if (smallest[multiple] == multiple) {
                        smallest[multiple] = prime;
                    }
                }
            }
        }

        auto factors = [&](int value) {
            vector<int> result;
            while (value > 1) {
                const int prime = smallest[value];
                result.push_back(prime);
                while (value % prime == 0) {
                    value /= prime;
                }
            }
            return result;
        };

        unordered_map<int, int> last;
        for (int index = 0; index < static_cast<int>(nums.size()); ++index) {
            for (int prime : factors(nums[index])) {
                last[prime] = index;
            }
        }

        int rightmost = 0;
        for (int index = 0; index + 1 < static_cast<int>(nums.size()); ++index) {
            for (int prime : factors(nums[index])) {
                rightmost = max(rightmost, last[prime]);
            }
            if (rightmost == index) {
                return index;
            }
        }
        return -1;
    }
};
