# Queries on a Permutation With Key

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1409 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Indexed Tree, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/queries-on-a-permutation-with-key/) |

## Problem Description

### Goal

Start with the permutation `P = [1, 2, ..., m]`. Process the values in `queries` from left to right. For each query value, find its current zero-based index in `P` and append that index to the answer.

After recording the index, remove that occurrence from its current position and move it to the front of `P`. Each later query observes the permutation produced by every earlier move. Return the recorded indices in query order.

### Function Contract

**Inputs**

- `queries`: an array of $q$ values, where $1 \le q \le 1000$ and every value lies from 1 through `m`.
- `m`: the size and maximum value of the initial permutation, where $1 \le m \le 1000$.

**Return value**

- An array of $q$ zero-based positions, each measured immediately before its queried value moves to the front.

### Examples

**Example 1**

- Input: `queries = [3,1,2,1], m = 5`
- Output: `[2,1,2,1]`

**Example 2**

- Input: `queries = [4,1,2,2], m = 4`
- Output: `[3,1,2,0]`

**Example 3**

- Input: `queries = [7,5,5,8,3], m = 8`
- Output: `[6,5,0,7,5]`

### Required Complexity

- **Time:** $O((m+q)\log(m+q))$
- **Space:** $O(m+q)$

<details>
<summary>Approach</summary>

#### General

**Represent order with occupied positions.** Reserve the first $q$ position numbers for future move-to-front operations. Place initial value `v` at position `q + v`, record that position in a map, and mark every occupied position with one in a Fenwick tree.

For a queried value at position `p`, the Fenwick prefix sum through `p` is the number of permutation elements at or before it. Subtract one to obtain its zero-based index. Remove the old occupancy, assign the next unused reserved position immediately before all current elements, mark it occupied, and decrement the front pointer.

The tree always contains one marker for each permutation value, ordered exactly as the conceptual permutation. Prefix counts therefore give current indices. Reserved positions decrease with query time, so each moved value becomes earlier than every existing position, exactly implementing a move to the front.

#### Complexity detail

Initializing $m$ positions and processing $q$ queries performs $O(m+q)$ Fenwick operations, each costing $O(\log(m+q))$. Total time is $O((m+q)\log(m+q))$. The tree and position map use $O(m+q)$ space.

#### Alternatives and edge cases

- **Direct list simulation:** Use linear search, removal, and front insertion. It is simple and correct but can take $O(qm)$ time.
- **Order-statistics tree:** Store values in a balanced indexed tree with decreasing front keys. It has the same asymptotic behavior but is not built into many languages.
- **Repeated query:** A value queried twice consecutively has index zero on the second query.
- **Value already first:** Removing and reinserting it preserves the permutation order.
- **Maximum value:** It begins at zero-based index `m - 1`.
- **Reserved indexing:** Fenwick indices must remain positive; using initial offset $q$ leaves exactly enough front positions.

</details>
