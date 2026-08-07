## Description

You are given two integers `m` and `n` representing the number of rows and columns of a grid. Your goal is to reach cell $(m - 1, n - 1)$. You are also given a 2D integer array `penalty`.

The cost to enter cell `(i, j)` is $(i + 1) * (j + 1)$.

You begin at cell `(0, 0)` and initially pay its entrance cost. Actions performed after entering `(0, 0)` are numbered starting from 1.

On each action, you may move to an **adjacent** cell or wait in the current cell. A move follows the parity rule if:

- On an **odd-numbered** action, you move **right** or **down**.

- On an **even-numbered** action, you move **left** or **up**.

The cost of an action is determined as follows:

- If you move according to the parity rule, pay only the entrance cost of the destination cell.

- If you move in a direction that **violates** the parity rule, pay the entrance cost of the destination cell plus $\text{penalty}[i][j]$, where `(i, j)` is the cell you move from.

- If you **wait** in cell `(i, j)`, pay $\text{penalty}[i][j]$.

After every move or wait, the action number increases by 1. Therefore, the required parity alternates after every action, regardless of whether a penalty was paid.

Return the **minimum** total cost required to reach $(m - 1, n - 1)$.
### Function Contract

**Inputs**

- `m`: The number of grid rows.
- `n`: The number of grid columns.
- `penalty`: An $m \times n$ matrix where `penalty[i][j]` is the extra cost of waiting in zero-based cell `(i, j)` or leaving it in a direction not permitted at the current second.

Let $N=mn$ denote the number of cells in the grid. The initial state is cell `(0, 0)` at odd second $1$, and its entrance cost is already included. A move must remain inside the grid. Both moving and waiting advance time by exactly one second.

**Return value**

Return the minimum total cost of reaching cell `(m - 1, n - 1)`. Arrival ends the journey immediately; no action or penalty is required at the destination.

### Examples
#### Example 1

<div class="example-block">
**Input:** m = 2, n = 2, penalty = [[5,3],[1,4]]

**Output:** 8

**Explanation:**

The optimal path is:

- Start at cell `(0, 0)` with entry cost $(0 + 1) * (0 + 1) = 1$.

- **Move 1**: Move down to cell `(1, 0)` with entry cost $(1 + 1) * (0 + 1) = 2$.

- **Move 2**: Move right to cell `(1, 1)` with entry cost $(1 + 1) * (1 + 1) = 4$ and an extra cost of $\text{penalty}[1][0] = 1$ for violating the even parity rule.

Thus, the total cost is $1 + 2 + 4 + 1 = 8$.

</div>
#### Example 2

<div class="example-block">
**Input:** m = 2, n = 2, penalty = [[0,7],[3,2]]

**Output:** 7

**Explanation:**

The optimal path is:

- Start at cell `(0, 0)` with entry cost $(0 + 1) * (0 + 1) = 1$.

- **Move 1**: Wait at cell `(0, 0)` with an extra cost of $\text{penalty}[0][0] = 0$ to flip to even parity.

- **Move 2**: Move right to cell `(0, 1)` with entry cost $(0 + 1) * (1 + 1) = 2$ and an extra cost of $\text{penalty}[0][0] = 0$ for violating the even parity rule.

- **Move 3**: Move down to cell `(1, 1)` with entry cost $(1 + 1) * (1 + 1) = 4$.

Thus, the total cost is $1 + 0 + 2 + 0 + 4 = 7$.

</div>
#### Example 3

<div class="example-block">
**Input:** m = 2, n = 3, penalty = [[8,0,9],[7,4,1]]

**Output:** 12

**Explanation:**

The optimal path is:

- Start at cell `(0, 0)` with entry cost $(0 + 1) * (0 + 1) = 1$.

- **Move 1**: Move right to cell `(0, 1)` with entry cost $(0 + 1) * (1 + 1) = 2$.

- **Move 2**: Move right to cell `(0, 2)` with entry cost $(0 + 1) * (2 + 1) = 3$ and an extra cost of $\text{penalty}[0][1] = 0$ for violating the even parity rule.

- **Move 3**: Move down to cell `(1, 2)` with entry cost $(1 + 1) * (2 + 1) = 6$.

Thus, the total cost is $1 + 2 + 3 + 0 + 6 = 12$.

</div>
### Constraints

- $1 \le m, n \le 10^{5}$

- $2 \le m * n \le 10^{5}$

- $\text{penalty.length} = m$

- $\text{penalty}[i].length = n$

- $0 \le \text{penalty}[i][j] \le 10^{5}$