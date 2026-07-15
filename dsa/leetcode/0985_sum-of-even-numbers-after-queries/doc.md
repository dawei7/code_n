# Sum of Even Numbers After Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 985 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/sum-of-even-numbers-after-queries/) |

## Problem Description

### Goal

You are given an integer array `nums` and a sequence `queries`, where each query is `[val_i, index_i]`.

Process the queries in their given order. For query `i`, first perform the executable update `nums[index_i] = nums[index_i] + val_i`. Then compute the sum of every even value currently in `nums`. Return an array `answer` whose entry `answer[i]` is that even-value sum after the corresponding update. Updates persist, so every later query observes all earlier changes.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers with $1\le N\le10^4$ and $-10^4\le\texttt{nums[i]}\le10^4$.
- `queries`: a list of $Q$ pairs `[val_i, index_i]`, where $1\le Q\le10^4$, $-10^4\le\texttt{val_i}\le10^4$, and $0\le\texttt{index_i}<N$.

**Return value**

- A length-$Q$ list containing the sum of the current even array values after each query.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4], queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]`
- Output: `[8, 6, 2, 4]`
- Explanation: the successive arrays are `[2, 2, 3, 4]`, `[2, -1, 3, 4]`, `[-2, -1, 3, 4]`, and `[-2, -1, 3, 6]`.

**Example 2**

- Input: `nums = [1], queries = [[4, 0]]`
- Output: `[0]`
- Explanation: the updated value is `5`, which is odd.

### Required Complexity

- **Time:** $O(N+Q)$
- **Space:** $O(Q)$

<details>
<summary>Approach</summary>

#### General

**Maintain the aggregate instead of rebuilding it:** Compute the initial sum of even values once. A query changes only one array position, so every other contribution remains unchanged.

**Remove the old contribution before updating:** Let `index` be the queried position. If `nums[index]` is even, subtract it from the running sum. Perform `nums[index] += value`. If the updated value is even, add it to the running sum. Append the resulting aggregate to the answer.

Before each query, the running value equals the sum of all current even entries. Removing the old indexed value when necessary leaves exactly the contribution of all unchanged positions. Adding the new indexed value when necessary restores the complete even sum for the updated array. This maintains the invariant after every query and produces each required answer in order.

#### Complexity detail

The initial aggregate scans $N$ values. Each of the $Q$ queries then performs constant work, giving $O(N+Q)$ time. The returned list uses $O(Q)$ space; excluding output, the running sum and in-place array updates use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Rescan after every query:** Summing all even values from scratch is correct but costs $O(NQ)$ time.
- **Fenwick tree:** A tree of even contributions supports point updates and total queries in $O(\log N)$ time, but a single maintained total already supports this exact whole-array query in $O(1)$.
- **Even-to-odd transition:** Remove the old even contribution and add nothing after the update.
- **Odd-to-even transition:** The old value contributes nothing, while the new even value is added.
- **Negative even values:** They contribute their signed value to the sum, just like positive even values.

</details>
