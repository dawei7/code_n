## Function Contract

**Inputs**

- `balance`: An integer array of net balances in circular person order.

Let $N=\lvert\texttt{balance}\rvert$. Indices `0` and `N - 1` are neighbors because the arrangement is circular. Each move changes two adjacent entries by exactly one unit: the sender loses one and the receiver gains one.

**Return value**

Return the least number of adjacent one-unit transfers that leaves every entry at least zero, or `-1` if this is impossible.
