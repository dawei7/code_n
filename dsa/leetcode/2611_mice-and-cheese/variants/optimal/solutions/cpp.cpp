#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        vector<int> gains;
        gains.reserve(reward1.size());
        for (int index = 0; index < static_cast<int>(reward1.size()); ++index) {
            gains.push_back(reward1[index] - reward2[index]);
        }
        sort(gains.rbegin(), gains.rend());

        int total = accumulate(reward2.begin(), reward2.end(), 0);
        for (int index = 0; index < k; ++index) {
            total += gains[index];
        }
        return total;
    }
};
