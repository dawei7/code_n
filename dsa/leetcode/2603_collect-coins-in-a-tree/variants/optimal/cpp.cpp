#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    int collectTheCoins(vector<int>& coins, vector<vector<int>>& edges) {
        const int n = static_cast<int>(coins.size());
        vector<vector<int>> graph(n);
        vector<int> degree(n, 0);
        for (const auto& edge : edges) {
            const int first = edge[0];
            const int second = edge[1];
            graph[first].push_back(second);
            graph[second].push_back(first);
            ++degree[first];
            ++degree[second];
        }

        int remaining_edges = n - 1;
        queue<int> leaves;
        for (int node = 0; node < n; ++node) {
            if (degree[node] == 1 && coins[node] == 0) {
                leaves.push(node);
            }
        }
        while (!leaves.empty()) {
            const int leaf = leaves.front();
            leaves.pop();
            degree[leaf] = 0;
            for (int neighbor : graph[leaf]) {
                if (degree[neighbor] == 0) continue;
                --degree[neighbor];
                --remaining_edges;
                if (degree[neighbor] == 1 && coins[neighbor] == 0) {
                    leaves.push(neighbor);
                }
            }
        }

        for (int node = 0; node < n; ++node) {
            if (degree[node] == 1) leaves.push(node);
        }
        for (int round = 0; round < 2; ++round) {
            int layer_size = static_cast<int>(leaves.size());
            while (layer_size-- > 0) {
                const int leaf = leaves.front();
                leaves.pop();
                degree[leaf] = 0;
                for (int neighbor : graph[leaf]) {
                    if (degree[neighbor] == 0) continue;
                    --degree[neighbor];
                    --remaining_edges;
                    if (degree[neighbor] == 1) leaves.push(neighbor);
                }
            }
        }
        return max(0, 2 * remaining_edges);
    }
};
