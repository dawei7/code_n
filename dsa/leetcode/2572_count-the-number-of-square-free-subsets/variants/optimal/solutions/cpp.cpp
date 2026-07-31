#include <array>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int solve(std::vector<int> nums) {
        constexpr int mod = 1000000007;
        constexpr std::array<int, 10> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        std::array<int, 31> masks;
        masks.fill(-1);

        for (int value = 2; value <= 30; ++value) {
            int mask = 0;
            bool valid = true;
            for (int bit = 0; bit < 10; ++bit) {
                int prime = primes[bit];
                if (value % (prime * prime) == 0) {
                    valid = false;
                    break;
                }
                if (value % prime == 0) mask |= 1 << bit;
            }
            if (valid) masks[value] = mask;
        }

        std::array<int, 31> counts{};
        for (int value : nums) ++counts[value];
        std::vector<long long> dp(1 << 10, 0);
        dp[0] = 1;

        for (int value = 2; value <= 30; ++value) {
            int frequency = counts[value];
            int value_mask = masks[value];
            if (frequency == 0 || value_mask < 0) continue;
            auto next_dp = dp;
            for (int used_mask = 0; used_mask < (1 << 10); ++used_mask) {
                if ((used_mask & value_mask) == 0) {
                    int combined = used_mask | value_mask;
                    next_dp[combined] = (next_dp[combined] + dp[used_mask] * frequency) % mod;
                }
            }
            dp = std::move(next_dp);
        }

        long long total = 0;
        for (long long ways : dp) total = (total + ways) % mod;
        long long one_choices = 1;
        for (int i = 0; i < counts[1]; ++i) one_choices = one_choices * 2 % mod;
        return static_cast<int>((total * one_choices - 1 + mod) % mod);
    }
};
