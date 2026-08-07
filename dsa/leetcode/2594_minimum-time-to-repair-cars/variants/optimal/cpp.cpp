#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    long long solve(vector<int> ranks, int cars) {
        long long low = 0;
        long long high = 1LL * *min_element(ranks.begin(), ranks.end()) * cars * cars;

        while (low < high) {
            long long time = low + (high - low) / 2;
            long long repaired = 0;
            for (int rank : ranks) {
                long long quotient = time / rank;
                long long count = static_cast<long long>(sqrtl(quotient));
                while ((count + 1) * (count + 1) <= quotient) {
                    ++count;
                }
                while (count * count > quotient) {
                    --count;
                }
                repaired += count;
                if (repaired >= cars) {
                    break;
                }
            }

            if (repaired >= cars) {
                high = time;
            } else {
                low = time + 1;
            }
        }

        return low;
    }
};
