#include <array>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
    static long long encode(int parent, int child) {
        return (static_cast<long long>(parent) << 32) | static_cast<unsigned int>(child);
    }

public:
    int solve(vector<vector<int>> edges, vector<vector<int>> guesses, int k) {
        const int nodeCount = static_cast<int>(edges.size()) + 1;
        vector<vector<int>> graph(nodeCount);
        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        unordered_set<long long> guessSet;
        for (const auto& guess : guesses) {
            guessSet.insert(encode(guess[0], guess[1]));
        }

        vector<int> parent(nodeCount, -2);
        vector<int> order{0};
        parent[0] = -1;
        for (int index = 0; index < nodeCount; ++index) {
            const int node = order[index];
            for (int neighbor : graph[node]) {
                if (neighbor != parent[node]) {
                    parent[neighbor] = node;
                    order.push_back(neighbor);
                }
            }
        }

        vector<int> correct(nodeCount, 0);
        for (int node = 1; node < nodeCount; ++node) {
            correct[0] += guessSet.count(encode(parent[node], node));
        }

        int answer = correct[0] >= k;
        for (int index = 1; index < nodeCount; ++index) {
            const int node = order[index];
            const int previousRoot = parent[node];
            correct[node] = correct[previousRoot]
                - static_cast<int>(guessSet.count(encode(previousRoot, node)))
                + static_cast<int>(guessSet.count(encode(node, previousRoot)));
            answer += correct[node] >= k;
        }
        return answer;
    }
};
