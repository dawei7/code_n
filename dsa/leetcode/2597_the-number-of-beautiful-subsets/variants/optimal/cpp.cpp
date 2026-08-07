#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<int> nums, int k) {
        map<int, map<int, int>> groups;
        for (int value : nums) {
            ++groups[value % k][value];
        }

        int answer = 1;
        for (const auto& [remainder, group] : groups) {
            int not_taken = 1;
            int taken = 0;
            int previous_value = -k;

            for (const auto& [value, frequency] : group) {
                int choices = (1 << frequency) - 1;
                int total = not_taken + taken;
                int next_taken = value - previous_value == k
                    ? not_taken * choices
                    : total * choices;

                not_taken = total;
                taken = next_taken;
                previous_value = value;
            }

            answer *= not_taken + taken;
        }

        return answer - 1;
    }
};
