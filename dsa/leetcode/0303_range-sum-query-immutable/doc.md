# Range Sum Query - Immutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 303 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Design, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-query-immutable/) |

## Problem Description
### Goal
Construct a `NumArray` from a nonempty integer array that will not change after construction. The object receives repeated `sumRange(left, right)` queries using valid zero-based endpoints with `left <= right`.

For each query, return the sum of all array values from index `left` through index `right`, including both endpoints. Negative values and repeated queries must be handled normally. Perform preprocessing once so each later query is answered in constant time rather than resumming its interval. The app adapter returns all query results in order, while the native class preserves the immutable array state between method calls.

### Function Contract
**Inputs**

- `nums`: a nonempty immutable list of integers
- `queries`: a list of pairs `[left, right]` with valid inclusive indices

**Return value**

A list containing `nums[left] + ... + nums[right]` for each query in the original query order.

### Examples
**Example 1**

- Input: `nums = [-2,0,3,-5,2,-1], queries = [[0,2],[2,5],[0,5]]`
- Output: `[1,-1,-3]`

**Example 2**

- Input: `nums = [1,2], queries = [[0,0],[1,1]]`
- Output: `[1,2]`

**Example 3**

- Input: `nums = [5], queries = [[0,0]]`
- Output: `[5]`

### Required Complexity

- **Time:** $O(n + q)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Store sums at boundaries, not at elements**

Build `prefix` with one leading zero, where `prefix[i]` equals the sum of the first `i` array elements. The extra entry makes every array boundary—including the boundary before index zero—addressable without a special case.

For an inclusive query `[left, right]`, `prefix[right + 1]` contains the desired range plus everything before `left`. Subtracting `prefix[left]` cancels that earlier prefix and leaves exactly the requested sum.

**Immutability makes one preprocessing pass reusable**

Because `nums` never changes, every prefix value remains correct for the lifetime of the query object. Construction performs the only element-by-element accumulation. Each later query needs two reads and one subtraction, regardless of range width.

For `[-2,0,3,-5,2,-1]`, the prefix array is `[0,-2,-2,1,-4,-2,-3]`. Query `[2,5]` returns `prefix[6] - prefix[2] = - 3 - ( - 2) = - 1`.

**Prefix subtraction includes every requested index exactly once**

By definition,
`prefix[right + 1] = nums[0] + ... + nums[right]`
and
`prefix[left] = nums[0] + ... + nums[left - 1]`.
Their difference cancels precisely the indices before `left`, while indices `left` through `right` occur only in the first sum. Thus every returned value equals its inclusive range sum.

#### Complexity detail

Building $n + 1$ prefix entries takes $O(n)$ time. Each of the `q` queries takes $O(1)$, for $O(n + q)$ total time. The prefix array uses $O(n)$ auxiliary space; the returned query results are output storage.

#### Alternatives and edge cases

- **Sum each requested slice directly:** uses no preprocessing but costs $O(range length)$ per query and can reach $O(nq)$.
- **Segment tree or Fenwick tree:** supports updates, but immutability makes its logarithmic query cost and additional machinery unnecessary.
- Single-element and full-array queries follow the same subtraction formula. Negative values and zero totals require no special handling.

</details>
