#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        vector<long long> answer(n);
        unordered_map<int, long long> count;
        unordered_map<int, long long> total;

        for (int i = 0; i < n; ++i) {
            int value = nums[i];
            answer[i] += count[value] * i - total[value];
            ++count[value];
            total[value] += i;
        }

        count.clear();
        total.clear();
        for (int i = n - 1; i >= 0; --i) {
            int value = nums[i];
            answer[i] += total[value] - count[value] * i;
            ++count[value];
            total[value] += i;
        }

        return answer;
    }
};
