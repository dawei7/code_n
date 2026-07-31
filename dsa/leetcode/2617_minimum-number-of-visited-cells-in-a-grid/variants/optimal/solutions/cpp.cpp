#include <functional>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
    int minimumVisitedCells(vector<vector<int>>& grid) {
        int rows = static_cast<int>(grid.size());
        int columns = static_cast<int>(grid[0].size());
        using Entry = pair<int, int>;
        using MinHeap = priority_queue<Entry, vector<Entry>, greater<Entry>>;
        vector<MinHeap> rowHeaps(rows);
        vector<MinHeap> columnHeaps(columns);
        int unreachable = rows * columns + 1;
        int distance = unreachable;

        for (int row = 0; row < rows; ++row) {
            for (int column = 0; column < columns; ++column) {
                while (!rowHeaps[row].empty() &&
                       rowHeaps[row].top().second < column) {
                    rowHeaps[row].pop();
                }
                while (!columnHeaps[column].empty() &&
                       columnHeaps[column].top().second < row) {
                    columnHeaps[column].pop();
                }

                if (row == 0 && column == 0) {
                    distance = 1;
                } else {
                    int fromRow = rowHeaps[row].empty()
                        ? unreachable : rowHeaps[row].top().first;
                    int fromColumn = columnHeaps[column].empty()
                        ? unreachable : columnHeaps[column].top().first;
                    distance = min(fromRow, fromColumn) + 1;
                }

                if (distance <= rows * columns) {
                    rowHeaps[row].push(
                        {distance, column + grid[row][column]}
                    );
                    columnHeaps[column].push(
                        {distance, row + grid[row][column]}
                    );
                }
            }
        }

        return distance <= rows * columns ? distance : -1;
    }
};
