# Russian Doll Envelopes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 354 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/russian-doll-envelopes/) |

## Problem Description
### Goal
Given envelope dimensions `[width, height]`, build a nested chain by placing one envelope strictly inside the next. Envelope `a` fits inside envelope `b` only when both `a.width < b.width` and `a.height < b.height`; rotation is forbidden.

Return the maximum number of envelopes in any valid chain. Equal width or equal height prevents one envelope from containing the other, even when the remaining dimension is larger. Each input envelope occurrence may appear at most once, and the function returns only the optimal chain length rather than the envelopes or their nesting order. A one-envelope input returns `1` because that envelope alone forms a valid chain.

### Function Contract
**Inputs**

- `envelopes`: a list of `[width, height]` pairs

**Return value**

- The maximum length of a strictly nested envelope chain.

### Examples
**Example 1**

- Input: `envelopes = [[5,4],[6,4],[6,7],[2,3]]`
- Output: `3`
- Explanation: `[2,3] -> [5,4] -> [6,7]` is a valid chain.

**Example 2**

- Input: `envelopes = [[1,1],[1,1],[1,1]]`
- Output: `1`

**Example 3**

- Input: `envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]`
- Output: `4`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Prevent equal widths from forming false chains**

If widths are processed in increasing order, any chosen later envelope already has a width at least as large. The remaining task resembles a longest increasing subsequence of heights—but equal widths must never both enter that subsequence.

Sort by width ascending and, crucially, height descending for equal widths. Within one width group, heights now decrease, so a strictly increasing height subsequence can select at most one member. Between different width groups, a height increase means both dimensions increase and therefore represents a legal nesting step.

**Track the best ending height for each length**

Run patience-sorting LIS on the sorted heights. Maintain `tails[length - 1]`, the smallest possible ending height of an increasing subsequence of that length. For each height, binary-search the first tail greater than or equal to it. Replace that tail, or append when the height exceeds every existing tail.

**Why replacing a tail preserves every achievable length**

Replacing a tail does not discard a possible length: it keeps the same subsequence length with an ending height no larger than before, which can only make future extensions easier. Appending proves a longer increasing sequence exists. Consequently, after every height, `tails` represents all achievable lengths with their best ending heights, and its final length is the height LIS.

**Why the sorting reduction is exact**

The sorting reduction is exact. Every height subsequence corresponds to strictly increasing widths because equal-width heights appear in descending order and cannot both be selected. Conversely, every valid envelope chain appears in increasing width order and has increasing heights, so it is a subsequence considered by LIS.

#### Complexity detail

Sorting `n` envelopes costs $O(n \log n)$. Each of the `n` heights performs one $O(\log n)$ binary search, so total time remains $O(n \log n)$. The sorted copy and tails array use $O(n)$ space.

#### Alternatives and edge cases

- **Quadratic dynamic programming:** compares every earlier envelope with every later one, taking $O(n^2)$ time and $O(n)$ space.
- **Sort equal widths by ascending height:** is incorrect because LIS could select multiple envelopes with the same width.
- **Unsorted pairwise chain search:** can be correct but repeatedly explores the same predecessor relationships.
- An empty input has answer zero.
- Duplicate envelopes and envelopes sharing either dimension cannot nest because both dimensions must increase strictly.

</details>
