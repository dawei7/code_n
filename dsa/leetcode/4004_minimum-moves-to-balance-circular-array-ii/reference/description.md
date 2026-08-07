## Description

You are given a circular array `balance` of length `n`, where $\text{balance}[i]$ is the net balance of person `i`.

In one move, a person can transfer **exactly** 1 unit of balance to either their left or right neighbor.

Return the **minimum** number of moves required so that every person has a **non-negative** balance. If it is impossible, return -1.
### Function Contract

**Inputs**

- `balance`: An integer array of length $n$ containing the initial net balance of each person in circular order.

Each move transfers exactly one unit across one edge of the circle. Indices are interpreted modulo $n$, so the left neighbor of index `0` is index `n - 1`, and the right neighbor of index `n - 1` is index `0`.

**Return value**

Return the minimum number of unit transfers needed to make every entry non-negative. Return `-1` when no sequence of moves can do so.

### Examples
#### Example 1

<div class="example-block">
**Input:** balance = [-1,2,-1]

**Output:** 2

**Explanation:**

One optimal sequence of moves is:

- Move 1 unit from $i = 1$ to $i = 0$, resulting in $balance = [0, 1, -1]$

- Move 1 unit from $i = 1$ to $i = 2$, resulting in $balance = [0, 0, 0]$

Thus, the minimum number of moves required is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** balance = [4,-1,-2]

**Output:** 3

**Explanation:**

One optimal sequence of moves is:

- Move 1 unit from $i = 0$ to $i = 1$, resulting in $balance = [3, 0, -2]$

- Move 1 unit from $i = 0$ to $i = 2$, resulting in $balance = [2, 0, -1]$

- Move 1 unit from $i = 0$ to $i = 2$, resulting in $balance = [1, 0, 0]$

Thus, the minimum number of moves required is 3.

</div>
#### Example 3

<div class="example-block">
**Input:** balance = [-3,-3,5]

**Output:** -1

**Explanation:**

It is impossible to make all balances non-negative for $balance = [-3, -3, 5]$, so the answer is -1.

</div>
### Constraints

- $1 \le n = \text{balance.length} \le 1000$

- $-10^{5} \le \text{balance}[i] \le 10^{5}$