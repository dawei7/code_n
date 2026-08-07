#include <functional>
#include <optional>
#include <queue>
#include <vector>

using namespace std;

class Solution {
    struct Node {
        int value;
        int left = -1;
        int right = -1;
    };

public:
    long long solve(vector<int> root, int k) {
        vector<optional<int>> converted;
        converted.reserve(root.size());
        for (int value : root) {
            converted.push_back(value);
        }
        return solve(converted, k);
    }

    long long solve(vector<optional<int>> root, int k) {
        vector<Node> tree;
        tree.reserve(root.size());
        tree.push_back(Node{*root[0]});

        queue<int> parents;
        parents.push(0);
        size_t inputIndex = 1;
        while (!parents.empty() && inputIndex < root.size()) {
            const int parent = parents.front();
            parents.pop();

            if (root[inputIndex].has_value()) {
                tree[parent].left = static_cast<int>(tree.size());
                tree.push_back(Node{*root[inputIndex]});
                parents.push(tree[parent].left);
            }
            ++inputIndex;

            if (inputIndex < root.size() && root[inputIndex].has_value()) {
                tree[parent].right = static_cast<int>(tree.size());
                tree.push_back(Node{*root[inputIndex]});
                parents.push(tree[parent].right);
            }
            ++inputIndex;
        }

        priority_queue<long long, vector<long long>, greater<long long>> largest;
        queue<int> nodes;
        nodes.push(0);
        while (!nodes.empty()) {
            const int levelSize = static_cast<int>(nodes.size());
            long long levelSum = 0;
            for (int i = 0; i < levelSize; ++i) {
                const int node = nodes.front();
                nodes.pop();
                levelSum += tree[node].value;
                if (tree[node].left != -1) {
                    nodes.push(tree[node].left);
                }
                if (tree[node].right != -1) {
                    nodes.push(tree[node].right);
                }
            }

            largest.push(levelSum);
            if (static_cast<int>(largest.size()) > k) {
                largest.pop();
            }
        }

        return static_cast<int>(largest.size()) == k ? largest.top() : -1;
    }
};
