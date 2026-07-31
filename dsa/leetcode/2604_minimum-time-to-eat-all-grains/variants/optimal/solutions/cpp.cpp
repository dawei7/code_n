#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int minimumTime(vector<int>& hens, vector<int>& grains) {
        sort(hens.begin(), hens.end());
        sort(grains.begin(), grains.end());
        const int grain_count = static_cast<int>(grains.size());

        auto can_eat_all = [&](long long time) {
            int grain = 0;
            for (long long hen : hens) {
                if (grain == grain_count) return true;

                long long right_reach;
                if (grains[grain] < hen) {
                    const long long left_distance = hen - grains[grain];
                    if (left_distance > time) return false;
                    right_reach = max(
                        hen + time - 2 * left_distance,
                        hen + (time - left_distance) / 2
                    );
                } else {
                    right_reach = hen + time;
                }

                while (grain < grain_count && grains[grain] <= right_reach) {
                    ++grain;
                }
            }
            return grain == grain_count;
        };

        long long low = -1;
        long long high = 2000000000LL;
        while (high - low > 1) {
            const long long middle = low + (high - low) / 2;
            if (can_eat_all(middle)) high = middle;
            else low = middle;
        }
        return static_cast<int>(high);
    }
};
