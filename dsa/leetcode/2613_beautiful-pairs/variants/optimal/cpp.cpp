#include <algorithm>
#include <array>
#include <climits>
#include <numeric>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> beautifulPair(vector<int>& nums1, vector<int>& nums2) {
        int n = static_cast<int>(nums1.size());
        int width = *max_element(nums2.begin(), nums2.end()) + 1;
        array<vector<int>, 2> trees{
            vector<int>(2 * width, -1),
            vector<int>(2 * width, -1)
        };

        auto slot = [](int sign) { return sign == -1 ? 0 : 1; };
        auto better = [&](int i, int j, int sign) {
            if (i < 0) return j;
            if (j < 0) return i;
            pair<int, int> keyI{-nums1[i] + sign * nums2[i], i};
            pair<int, int> keyJ{-nums1[j] + sign * nums2[j], j};
            return keyI <= keyJ ? i : j;
        };

        auto update = [&](int position, int index, int sign) {
            vector<int>& tree = trees[slot(sign)];
            position += width;
            tree[position] = better(tree[position], index, sign);
            for (position /= 2; position; position /= 2) {
                tree[position] = better(
                    tree[2 * position], tree[2 * position + 1], sign
                );
            }
        };

        auto query = [&](int left, int right, int sign) {
            vector<int>& tree = trees[slot(sign)];
            left += width;
            right += width;
            int result = -1;
            while (left <= right) {
                if (left & 1) result = better(result, tree[left++], sign);
                if (!(right & 1)) result = better(result, tree[right--], sign);
                left /= 2;
                right /= 2;
            }
            return result;
        };

        vector<int> order(n);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int i, int j) {
            return pair<int, int>{nums1[i], i} < pair<int, int>{nums1[j], j};
        });

        pair<long long, pair<int, int>> best{LLONG_MAX, {n, n}};
        for (int i : order) {
            int y = nums2[i];
            array<int, 2> candidates{
                query(0, y, -1),
                query(y, width - 1, 1)
            };
            for (int j : candidates) {
                if (j < 0) continue;
                pair<int, int> indices{min(i, j), max(i, j)};
                long long distance =
                    abs(nums1[i] - nums1[j]) + abs(nums2[i] - nums2[j]);
                best = min(best, make_pair(distance, indices));
            }
            update(y, i, -1);
            update(y, i, 1);
        }

        return {best.second.first, best.second.second};
    }
};
