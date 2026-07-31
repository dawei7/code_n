#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    bool solve(vector<int> nums) {
        int maximum = *max_element(nums.begin(), nums.end());
        vector<bool> is_prime(maximum + 1, true);
        is_prime[0] = false;
        if (maximum >= 1) {
            is_prime[1] = false;
        }

        for (int prime = 2; prime * prime <= maximum; ++prime) {
            if (is_prime[prime]) {
                for (int multiple = prime * prime; multiple <= maximum; multiple += prime) {
                    is_prime[multiple] = false;
                }
            }
        }

        vector<int> primes;
        for (int number = 2; number <= maximum; ++number) {
            if (is_prime[number]) {
                primes.push_back(number);
            }
        }

        int previous = 0;
        for (int number : nums) {
            auto position = lower_bound(primes.begin(), primes.end(), number - previous);
            if (position != primes.begin()) {
                --position;
                number -= *position;
            }
            if (number <= previous) {
                return false;
            }
            previous = number;
        }
        return true;
    }
};
