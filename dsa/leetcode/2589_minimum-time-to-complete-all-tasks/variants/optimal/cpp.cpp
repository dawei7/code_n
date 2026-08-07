#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(vector<vector<int>> tasks) {
        sort(tasks.begin(), tasks.end(), [](const auto& left, const auto& right) {
            return left[1] < right[1];
        });
        const int limit = tasks.back()[1];
        vector<int> bit(limit + 2);
        vector<int> parent(limit + 1);
        iota(parent.begin(), parent.end(), 0);

        auto prefix = [&](int time) {
            int total = 0;
            while (time > 0) {
                total += bit[time];
                time -= time & -time;
            }
            return total;
        };
        auto activate = [&](int time) {
            while (time <= limit) {
                ++bit[time];
                time += time & -time;
            }
        };
        auto find = [&](int time) {
            int root = time;
            while (parent[root] != root) {
                root = parent[root];
            }
            while (parent[time] != time) {
                const int nextTime = parent[time];
                parent[time] = root;
                time = nextTime;
            }
            return root;
        };

        int active = 0;
        for (const auto& task : tasks) {
            const int start = task[0];
            const int end = task[1];
            int needed = task[2] - (prefix(end) - prefix(start - 1));
            int time = find(end);
            while (needed > 0) {
                activate(time);
                ++active;
                --needed;
                parent[time] = find(time - 1);
                time = find(time);
            }
        }
        return active;
    }
};
