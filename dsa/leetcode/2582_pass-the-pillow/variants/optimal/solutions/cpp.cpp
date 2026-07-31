class Solution {
public:
    int solve(int n, int time) {
        const int traversals = time / (n - 1);
        const int offset = time % (n - 1);
        if (traversals % 2 == 0) {
            return offset + 1;
        }
        return n - offset;
    }
};
