# Minimum Limit of Balls in a Bag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1760 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/) |

## Problem Description

### Goal

You are given several bags, where `nums[i]` is the positive number of balls in the $i$-th bag. In one operation, choose one bag and split all of its balls between two new nonempty bags. The original bag is replaced, and the total number of balls is preserved.

You may perform at most `maxOperations` such splits. The penalty of the final arrangement is the largest number of balls in any remaining bag. Choose the operations to make this penalty as small as possible, and return that minimum achievable value.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive bag sizes, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `maxOperations`: the maximum allowed number of splits, with $1 \le \texttt{maxOperations} \le 10^9$.

Let $M=\max(\texttt{nums})$.

**Return value**

- Return the smallest possible maximum bag size after performing no more than `maxOperations` legal splits.

### Examples

**Example 1**

- Input: `nums = [9], maxOperations = 2`
- Output: `3`
- Explanation: Split nine balls into three bags of three using two operations.

**Example 2**

- Input: `nums = [2, 4, 8, 2], maxOperations = 4`
- Output: `2`
- Explanation: The bags of four and eight can be divided until every bag contains at most two balls.

**Example 3**

- Input: `nums = [7, 17], maxOperations = 2`
- Output: `7`
- Explanation: Split seventeen into parts no larger than seven; a penalty below seven would require too many total splits.

### Required Complexity

- **Time:** $O(n\log M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Search over the possible penalty**

The final maximum is an integer between $1$ and $M$. Instead of constructing bags for every possible sequence of operations, ask whether a proposed penalty $p$ can be achieved within the operation budget.

**Compute the splits required by one bag**

A bag containing $v$ balls must become $\lceil v/p\rceil$ nonempty bags for every part to contain at most $p$. Producing that many parts takes one fewer split, so its minimum required operations are

$$
\left\lceil\frac{v}{p}\right\rceil-1
=
\left\lfloor\frac{v-1}{p}\right\rfloor.
$$

The `(v - 1) // p` form handles exact divisibility correctly: a bag already divisible into size-$p$ parts does not need an extra empty part.

**Use monotonic feasibility**

Sum the required splits over all initial bags. If the sum is at most `maxOperations`, penalty $p$ is feasible. Every larger penalty is also feasible because allowing larger parts can never require more splits; conversely, if $p$ is infeasible, every smaller value is infeasible.

**Find the first feasible value**

Binary-search the monotone range. When the midpoint is feasible, retain it as the upper boundary; otherwise discard it and every smaller penalty. The boundaries meet at the smallest feasible value, which is exactly the minimum attainable penalty.

#### Complexity detail

Each feasibility check scans all $n$ bags in $O(n)$ time. Binary search performs $O(\log M)$ checks over values from $1$ through $M$, giving $O(n\log M)$ time. Only the search boundaries, current split total, and loop values are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Scan penalties in increasing order:** Testing every value from $1$ until one is feasible is correct but takes $O(nM)$ time in the worst case.
- **Repeatedly split the largest bag:** A priority-queue simulation performs one action per operation and is unsuitable when `maxOperations` can reach $10^9$; locally greedy split shapes also require careful balancing.
- **Dynamic programming by operation count:** The operation bound and bag sizes are far too large for a state per split or size.
- **Bag of size one:** It already meets the smallest possible penalty and never needs splitting.
- **Penalty one:** It is feasible exactly when the budget can create one single-ball bag per ball.
- **Exact divisibility:** `(v - 1) // p` avoids counting an unnecessary additional split when $v$ is a multiple of $p$.
- **Unused operations:** The contract permits at most the budget; a feasible arrangement need not spend every operation.
- **Maximum values:** Split totals can exceed 32-bit ranges across $10^5$ bags, so fixed-width implementations need sufficiently wide arithmetic.

</details>
