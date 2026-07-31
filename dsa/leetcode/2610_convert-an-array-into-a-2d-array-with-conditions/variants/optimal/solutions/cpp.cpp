#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        unordered_map<int, int> frequency;
        vector<vector<int>> rows;

        for (int number : nums) {
            int occurrence = frequency[number]++;
            if (occurrence == static_cast<int>(rows.size())) {
                rows.push_back({});
            }
            rows[occurrence].push_back(number);
        }

        return rows;
    }
};
