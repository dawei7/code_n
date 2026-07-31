#include <functional>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<int> nums) {
        long long prefix_sum = 0;
        int operations = 0;
        priority_queue<int, vector<int>, greater<int>> negatives;

        for (int number : nums) {
            prefix_sum += number;
            if (number < 0) {
                negatives.push(number);
            }

            if (prefix_sum < 0) {
                prefix_sum -= negatives.top();
                negatives.pop();
                ++operations;
            }
        }

        return operations;
    }
};
