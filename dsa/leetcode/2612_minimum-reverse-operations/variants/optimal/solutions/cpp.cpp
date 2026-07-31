#include <numeric>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        vector<vector<int>> values(2);
        vector<vector<int>> parent(2);
        for (int parity = 0; parity < 2; ++parity) {
            for (int index = parity; index < n; index += 2) {
                values[parity].push_back(index);
            }
            parent[parity].resize(values[parity].size() + 1);
            iota(parent[parity].begin(), parent[parity].end(), 0);
        }

        auto find = [&](auto&& self, int parity, int index) -> int {
            if (parent[parity][index] != index) {
                parent[parity][index] = self(self, parity, parent[parity][index]);
            }
            return parent[parity][index];
        };

        auto remove = [&](int index) {
            int parity = index & 1;
            int compressed = index / 2;
            parent[parity][compressed] = find(find, parity, compressed + 1);
        };

        for (int index : banned) {
            remove(index);
        }
        remove(p);

        vector<int> answer(n, -1);
        answer[p] = 0;
        queue<int> pending;
        pending.push(p);

        while (!pending.empty()) {
            int current = pending.front();
            pending.pop();
            int leftStart = max(0, current - k + 1);
            int rightStart = min(n - k, current);
            int low = 2 * leftStart + k - 1 - current;
            int high = 2 * rightStart + k - 1 - current;
            int parity = low & 1;
            int first = (low - parity + 1) / 2;
            int last = (high - parity) / 2;

            int cursor = find(find, parity, first);
            while (cursor <= last) {
                int nextPosition = values[parity][cursor];
                answer[nextPosition] = answer[current] + 1;
                pending.push(nextPosition);
                parent[parity][cursor] = find(find, parity, cursor + 1);
                cursor = find(find, parity, cursor);
            }
        }

        return answer;
    }
};
