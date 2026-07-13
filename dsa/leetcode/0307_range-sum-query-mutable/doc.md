# Range Sum Query - Mutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 307 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Design, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problem Description
### Goal
Construct a mutable range-sum structure from an initial integer array. Operations arrive sequentially: `update(index, value)` replaces the current value at one valid position, while `sumRange(left, right)` asks about the current array after all preceding updates.

For every sum query, return the total from `left` through `right`, including both endpoints. Updates produce no output and are assignments rather than increments. Support interleaved operations efficiently, avoiding a full-array rebuild or full-range scan per call. The app contract executes the active operation prefix and returns sum results in order; the native `NumArray` retains state across methods.

### Function Contract
**Inputs**

- `arr`: the initial integer array
- `n`: the active prefix length of `arr`
- `queries`: ordered operations `["update", index, value]` or `["sum", left, right]`
- `q`: the number of operations from `queries` to execute

**Return value**

The results of all executed `sum` operations, in operation order. Updates produce no output.

### Examples
**Example 1**

- Input: `arr = [1,3,5], n = 3, queries = [["sum",0,2],["update",1,2],["sum",0,2]], q = 3`
- Output: `[9,8]`

**Example 2**

- Input: `arr = [4], n = 1, queries = [["sum",0,0],["update",0,7],["sum",0,0]], q = 3`
- Output: `[4,7]`

**Example 3**

- Input: `arr = [2,4,6,8], n = 4, queries = [["sum",1,3],["update",2,1],["sum",0,2]], q = 3`
- Output: `[18,7]`

### Required Complexity

- **Time:** $O((n + q) \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**A Fenwick entry owns one power-of-two suffix**

Use one-based Fenwick indices. Entry `tree[i]` stores the sum of the range ending at `i` whose length is $i \mathbin{\&} - i$. These power-of-two ranges tile prefixes: repeatedly subtracting the lowest set bit walks through disjoint stored ranges whose union is exactly `[1, i]`.

A prefix sum therefore follows parent links `i -= i & -i` while accumulating entries. An inclusive range sum is the difference between the prefix ending at `right` and the prefix ending immediately before `left`.

**Point assignment becomes a propagated delta**

The public update sets a value rather than adding one, so retain the current array values. Compute `delta = new_value - old_value`, store the new value, and add the delta to every Fenwick range containing that index by following `i += i & -i`.

Only those ancestors contain the changed position. Updating them adjusts every affected prefix representation without touching unrelated ranges.

For `[1,3,5]`, the full sum is nine. Assigning index one from three to two propagates delta `-1`; the next full-range query becomes eight.

**Prefix tiles and update ancestors preserve all sums**

During construction, propagating every array value makes each Fenwick entry equal the sum of its defined suffix range. A point update adds the exact value change to precisely the entries whose ranges contain that point, so this representation remains true.

A prefix traversal selects disjoint suffix ranges and removes their lengths until reaching zero; together they cover every index in the prefix exactly once. Prefix subtraction then cancels all positions before `left`, proving every range query exact after any sequence of updates.

#### Complexity detail

Construction through Fenwick additions takes $O(n \log n)$. Both update and range sum traverse $O(\log n)$ tree entries, so `q` operations take $O(q \log n)$ and total time is $O((n + q) \log n)$. The current-value array and Fenwick tree use $O(n)$ space.

#### Alternatives and edge cases

- **Store only the array and sum each range:** makes assignments constant time but wide queries $O(n)$.
- **Rebuild prefix sums after each update:** makes queries constant time but each assignment $O(n)$.
- **Segment tree:** provides the same asymptotic operation bounds and is preferable when richer range aggregates are required.
- Single-element ranges and repeated assignments use the same delta and prefix logic. Negative updates are handled naturally.

</details>
