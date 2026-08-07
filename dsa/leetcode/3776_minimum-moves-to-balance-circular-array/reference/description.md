## Description

You are given a **circular** array `balance` of length `n`, where $\text{balance}[i]$ is the net balance of person `i`.

In one move, a person can transfer **exactly** 1 unit of balance to either their left or right neighbor.

Return the **minimum** number of moves required so that every person has a **non-negative** balance. If it is impossible, return `-1`.

**Note**: You are guaranteed that **at most** 1 index has a **negative** balance initially.
### Function Contract

**Inputs**

- `balance`: An integer array of net balances in circular person order.

Let $N=\lvert\texttt{balance}\rvert$. Indices `0` and `N - 1` are neighbors because the arrangement is circular. Each move changes two adjacent entries by exactly one unit: the sender loses one and the receiver gains one.

**Return value**

Return the least number of adjacent one-unit transfers that leaves every entry at least zero, or `-1` if this is impossible.

### Examples
#### Example 1

<div class="example-block">
**Input:** balance = [5,1,-4]

**Output:** 4

**Explanation:**

One optimal sequence of moves is:

- Move 1 unit from $i = 1$ to $i = 2$, resulting in $balance = [5, 0, -3]$

- Move 1 unit from $i = 0$ to $i = 2$, resulting in $balance = [4, 0, -2]$

- Move 1 unit from $i = 0$ to $i = 2$, resulting in $balance = [3, 0, -1]$

- Move 1 unit from $i = 0$ to $i = 2$, resulting in $balance = [2, 0, 0]$

Thus, the minimum number of moves required is 4.

</div>
#### Example 2

<div class="example-block">
**Input:** balance = [1,2,-5,2]

**Output:** 6

**Explanation:**

One optimal sequence of moves is:

- Move 1 unit from $i = 1$ to $i = 2$, resulting in $balance = [1, 1, -4, 2]$

- Move 1 unit from $i = 1$ to $i = 2$, resulting in $balance = [1, 0, -3, 2]$

- Move 1 unit from $i = 3$ to $i = 2$, resulting in $balance = [1, 0, -2, 1]$

- Move 1 unit from $i = 3$ to $i = 2$, resulting in $balance = [1, 0, -1, 0]$

- Move 1 unit from $i = 0$ to $i = 1$, resulting in $balance = [0, 1, -1, 0]$

- Move 1 unit from $i = 1$ to $i = 2$, resulting in $balance = [0, 0, 0, 0]$

Thus, the minimum number of moves required is 6.​​​

</div>
#### Example 3

<div class="example-block">
**Input:** balance = [-3,2]

**Output:** -1

**Explanation:**

**​​​​​​​**It is impossible to make all balances non-negative for $balance = [-3, 2]$, so the answer is -1.

</div>
### Constraints

- $1 \le n = \text{balance.length} \le 10^{5}$

- $-10^{9} \le \text{balance}[i] \le 10^{9}$

- There is at most one negative value in `balance` initially.