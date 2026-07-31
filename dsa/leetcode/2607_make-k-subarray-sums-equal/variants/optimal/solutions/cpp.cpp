#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
    long long makeSubKSumEqual(vector<int>& arr, int k) {
        const int n = static_cast<int>(arr.size());
        const int group_count = gcd(n, k);
        long long operations = 0;

        for (int start = 0; start < group_count; ++start) {
            vector<int> group;
            for (int index = start; index < n; index += group_count) {
                group.push_back(arr[index]);
            }
            sort(group.begin(), group.end());
            const long long median = group[group.size() / 2];
            for (long long value : group) {
                operations += llabs(value - median);
            }
        }
        return operations;
    }
};
