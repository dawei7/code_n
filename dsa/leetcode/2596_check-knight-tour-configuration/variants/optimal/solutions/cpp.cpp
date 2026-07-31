#include <cstdlib>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
    bool solve(vector<vector<int>> grid) {
        int n = static_cast<int>(grid.size());
        vector<pair<int, int>> positions(n * n);

        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < n; ++col) {
                positions[grid[row][col]] = {row, col};
            }
        }

        if (positions[0] != pair<int, int>{0, 0}) {
            return false;
        }

        for (int move = 1; move < n * n; ++move) {
            int row_change = abs(positions[move].first - positions[move - 1].first);
            int col_change = abs(positions[move].second - positions[move - 1].second);
            if (!((row_change == 1 && col_change == 2) ||
                  (row_change == 2 && col_change == 1))) {
                return false;
            }
        }

        return true;
    }
};
