# Richest Customer Wealth

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1672 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/richest-customer-wealth/) |

## Problem Description
### Goal
The rectangular integer matrix `accounts` records bank balances for several customers. Row `i` belongs to one customer, and column `j` gives that customer's balance at bank `j`. Every customer has a balance entry for the same number of banks, and every balance is positive.

A customer's wealth is the sum of every balance in that customer's row. Compute each customer's total and return the greatest such total. If several customers share the greatest wealth, the returned value is still that common total; no customer index needs to be reported.

### Function Contract
**Inputs**

- `accounts`: an $m \times n$ matrix of positive integers, where rows represent customers and columns represent banks.

Let $S = mn$ be the number of balances in the matrix.

**Return value**

Return the maximum row sum, representing the wealth held by the richest customer.

### Examples
**Example 1**

- Input: `accounts = [[1,2,3],[3,2,1]]`
- Output: `6`

**Example 2**

- Input: `accounts = [[1,5],[7,3],[3,5]]`
- Output: `10`

**Example 3**

- Input: `accounts = [[2,8,7],[7,1,3],[1,9,5]]`
- Output: `17`

### Required Complexity
- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Accumulate one customer at a time.** Initialize a running maximum to zero, which is below or equal to every possible positive wealth. For each row, start a fresh total and add every balance in that row exactly once.

**Retain only the best total.** After finishing a row, compare its sum with the running maximum and keep the larger value. The individual row total is no longer needed once that comparison is complete, so totals for all customers do not need to be stored.

**Why the maximum is exact.** The inner scan includes every account belonging to the current customer, so its total is exactly that customer's wealth. After processing the first $k$ rows, the running value is the maximum wealth among precisely those $k$ customers. Extending this fact one row at a time shows that after all rows are processed, the stored value is the richest wealth over the entire matrix.

#### Complexity detail

Every one of the $S=mn$ balances is read and added once, giving $O(S)$ time. Only the current row total and running maximum are stored beyond the input, so auxiliary space is $O(1)$. Inspecting all cells is necessary in the worst case because increasing any unexamined balance can make its customer the richest.

#### Alternatives and edge cases

- **Built-in row sums:** Computing `max(map(sum, accounts))` expresses the same linear scan concisely, though the explicit loops make the constant-space accumulation visible.
- **Store every wealth:** Building a separate array of row sums also works but consumes $O(m)$ avoidable space.
- **Sort row totals:** Sorting can identify the largest total, but it adds $O(m\log m)$ work after the required matrix scan.
- A one-customer, one-bank matrix returns its only balance.
- Multiple customers may tie for the maximum; only the wealth value is returned.
- The richest customer may appear in any row, including the first or last.
- Rectangular matrices need not be square, but every row has the same number of banks.
- Different balance distributions can have the same row sum and are treated as equal wealth.

</details>
