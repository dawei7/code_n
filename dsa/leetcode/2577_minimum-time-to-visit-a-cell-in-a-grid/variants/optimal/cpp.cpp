#include <functional>
#include <limits>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<vector<int>> grid) {
        const int rows = static_cast<int>(grid.size());
        const int cols = static_cast<int>(grid[0].size());
        if (grid[0][1] > 1 && grid[1][0] > 1) {
            return -1;
        }

        using State = tuple<int, int, int>;
        const int infinity = numeric_limits<int>::max();
        vector<vector<int>> earliest(rows, vector<int>(cols, infinity));
        priority_queue<State, vector<State>, greater<State>> heap;
        earliest[0][0] = 0;
        heap.emplace(0, 0, 0);

        constexpr int directions[4][2] = {
            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };

        while (!heap.empty()) {
            auto [time, row, col] = heap.top();
            heap.pop();
            if (time != earliest[row][col]) {
                continue;
            }
            if (row == rows - 1 && col == cols - 1) {
                return time;
            }

            for (const auto& direction : directions) {
                const int nextRow = row + direction[0];
                const int nextCol = col + direction[1];
                if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols) {
                    continue;
                }

                int nextTime = time + 1;
                const int required = grid[nextRow][nextCol];
                if (nextTime < required) {
                    nextTime = required + ((required - nextTime) & 1);
                }

                if (nextTime < earliest[nextRow][nextCol]) {
                    earliest[nextRow][nextCol] = nextTime;
                    heap.emplace(nextTime, nextRow, nextCol);
                }
            }
        }

        return -1;
    }
};
