#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    int findShortestCycle(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        int shortest = n + 1;
        for (int start = 0; start < n; ++start) {
            vector<int> distance(n, -1);
            vector<int> parent(n, -1);
            queue<int> pending;
            distance[start] = 0;
            pending.push(start);

            while (!pending.empty()) {
                const int node = pending.front();
                pending.pop();
                for (int neighbor : graph[node]) {
                    if (distance[neighbor] == -1) {
                        distance[neighbor] = distance[node] + 1;
                        parent[neighbor] = node;
                        pending.push(neighbor);
                    } else if (parent[node] != neighbor) {
                        shortest = min(
                            shortest,
                            distance[node] + distance[neighbor] + 1
                        );
                    }
                }
            }
        }
        return shortest == n + 1 ? -1 : shortest;
    }
};
