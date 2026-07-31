class Solution {
public:
    int solve(int n) {
        int operations = 0;

        while (n != 0) {
            int lowest_bit = n & -n;
            if ((n & (lowest_bit << 1)) != 0) {
                n += lowest_bit;
            } else {
                n -= lowest_bit;
            }
            ++operations;
        }

        return operations;
    }
};
