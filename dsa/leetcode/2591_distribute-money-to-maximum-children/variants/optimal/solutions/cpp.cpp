#include <algorithm>

using namespace std;

class Solution {
public:
    int solve(int money, int children) {
        money -= children;
        if (money < 0) {
            return -1;
        }

        int eightDollarChildren = min(money / 7, children);
        money -= eightDollarChildren * 7;

        if (eightDollarChildren == children && money > 0) {
            --eightDollarChildren;
        } else if (eightDollarChildren == children - 1 && money == 3) {
            --eightDollarChildren;
        }
        return eightDollarChildren;
    }
};
