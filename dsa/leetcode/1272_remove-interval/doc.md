# Remove Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1272 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-interval/) |

## Problem Description

### Goal

A set of real numbers is represented by a sorted list of pairwise-disjoint half-open intervals. Each pair `[a, b]` denotes $[a,b)$: it contains every real number $x$ satisfying $a \le x < b$. The right endpoint is excluded, so intervals that only touch at an endpoint do not overlap.

Given this list and another half-open interval `toBeRemoved`, subtract every number in the removal interval from the represented set. Return the remainder as a sorted list of disjoint, nonempty half-open intervals. An input interval may remain unchanged, disappear completely, lose one side, or split into two pieces.

### Function Contract

**Inputs**

- `intervals`: a sorted list of $n$ disjoint pairs `[start, end]`, with $1 \le n \le 10^4$ and $-10^9 \le \texttt{start} < \texttt{end} \le 10^9$.
- `to_be_removed`: a pair `[remove_start, remove_end]` representing the half-open interval to subtract.

**Return value**

- Return the sorted disjoint half-open intervals representing the original union minus `to_be_removed`.

### Examples

**Example 1**

- Input: `intervals = [[0,2],[3,4],[5,7]], to_be_removed = [1,6]`
- Output: `[[0,1],[6,7]]`

**Example 2**

- Input: `intervals = [[0,5]], to_be_removed = [2,3]`
- Output: `[[0,2],[3,5]]`

**Example 3**

- Input: `intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], to_be_removed = [-1,4]`
- Output: `[[-5,-4],[-3,-2],[4,5],[8,9]]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Classify each interval against the removal range**

Process the already sorted input from left to right. For an interval `[start, end]`, there is no overlap when `end <= remove_start` or `start >= remove_end`. The non-strict comparisons are essential for half-open intervals: touching at either endpoint removes no real numbers. Append such an interval unchanged.

When the intervals overlap, preserve a left piece `[start, remove_start]` exactly when `start < remove_start`. Preserve a right piece `[remove_end, end]` exactly when `end > remove_end`. These strict tests prevent empty intervals. If neither condition holds, the input interval lies wholly inside the removal interval and contributes nothing. If both hold, the removal interval sits strictly inside the input and splits it into two pieces.

For every input interval, these retained pieces are exactly the points outside the removal range, so their union is the required set difference. Processing inputs in their original order and emitting each left piece before its right piece preserves sorted order. Subtracting points cannot create overlap between intervals that were initially disjoint.

#### Complexity detail

Each of the $n$ intervals is examined once and emits at most two pieces, so the running time is $O(n)$. The returned list can contain up to $n+1$ intervals and therefore uses $O(n)$ space; excluding the required output, the sweep uses $O(1)$ auxiliary state.

#### Alternatives and edge cases

- **Front insertion followed by reversal:** It can preserve the same final order, but repeatedly shifting an expanding list takes $O(n^2)$ time.
- **Endpoint-event sweep:** Treating all endpoints as events generalizes to many set operations but adds sorting and bookkeeping that the sorted disjoint input does not need.
- **Complete coverage:** An interval entirely inside `to_be_removed` emits no piece.
- **Removal strictly inside one interval:** Both residual sides are nonempty and must be emitted.
- **Touching endpoints:** `[a,b)` and `[b,c)` do not overlap, so the original interval remains unchanged.
- **Removal outside the represented set:** Every interval is copied unchanged.
- **Negative coordinates:** Comparisons work identically across zero; no special arithmetic is required.

</details>
