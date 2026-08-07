#include <algorithm>
#include <array>
#include <vector>

using namespace std;

class Solution {
public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        array<bool, 10> present{};
        for (int digit : nums1) {
            present[digit] = true;
        }

        int common = 10;
        for (int digit : nums2) {
            if (present[digit]) {
                common = min(common, digit);
            }
        }
        if (common < 10) {
            return common;
        }

        const int first = *min_element(nums1.begin(), nums1.end());
        const int second = *min_element(nums2.begin(), nums2.end());
        return min(10 * first + second, 10 * second + first);
    }
};
