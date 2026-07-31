#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        if (p == 0) return 0;

        vector<int> values = nums;
        sort(values.begin(), values.end());

        auto feasible = [&](int limit) {
            int pairs = 0;
            int i = 0;
            while (i + 1 < static_cast<int>(values.size())) {
                if (values[i + 1] - values[i] <= limit) {
                    ++pairs;
                    i += 2;
                    if (pairs == p) return true;
                } else {
                    ++i;
                }
            }
            return false;
        };

        int low = 0;
        int high = values.back() - values.front();
        while (low < high) {
            int middle = low + (high - low) / 2;
            if (feasible(middle)) {
                high = middle;
            } else {
                low = middle + 1;
            }
        }
        return low;
    }
};
