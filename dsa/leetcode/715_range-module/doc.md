# Range Module

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 715 |
| Difficulty | Hard |
| Topics | Design, Segment Tree, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/range-module/) |

## Problem Description
### Goal
A `RangeModule` tracks portions of the real-number line using half-open intervals. Interval `[left, right)` contains every real number `x` satisfying `left <= x < right`, including the left endpoint but excluding the right.

Implement `addRange(left, right)` to track every point in the interval, `removeRange(left, right)` to stop tracking those points, and `queryRange(left, right)` to return whether every point in the requested interval is currently tracked. Overlapping operations combine according to coverage, and a query is false when even one portion is missing.

### Function Contract
**Inputs**

- `operations`: ordered `addRange(left, right)`, `removeRange(left, right)`, or `queryRange(left, right)` calls with `left < right`

**Return value**

- A list containing each query result in operation order; a query is true only when every point in `[left, right)` is currently tracked

### Examples
**Example 1**

- Input: `operations = [["addRange",10,20],["removeRange",14,16],["queryRange",10,14],["queryRange",13,15],["queryRange",16,17]]`
- Output: `[true,false,true]`

**Example 2**

- Input: `operations = [["queryRange",1,2],["addRange",1,2],["queryRange",1,2]]`
- Output: `[false,true]`

**Example 3**

- Input: `operations = [["addRange",5,10],["addRange",10,15],["queryRange",5,15]]`
- Output: `[true]`

### Required Complexity

- **Time:** $O(q \log C)$
- **Space:** $O(q \log C)$

<details>
<summary>Approach</summary>

#### General

**Represent uniform coordinate regions lazily**

Use a dynamic segment tree over the integer unit intervals in the published coordinate domain. A node state is untracked, tracked, or mixed. Uniform nodes need no children, so the enormous untouched domain consumes only one node.

**Assign a complete half-open range**

Convert `[left, right)` to inclusive unit indices `[left, right - 1]`. Adding assigns tracked state and removing assigns untracked state. A fully covered tree node adopts the state and discards any children because their older distinctions are overwritten.

**Descend only at assignment boundaries**

For partial overlap, create children inheriting the parent's uniform state, recurse into the intersected sides, and then collapse them back into their parent when both become uniformly equal. Only paths near range boundaries remain expanded.

**Query complete coverage**

If a queried region reaches a uniform node, that state answers the whole overlap immediately. A mixed node delegates to the necessary children, and a query spanning both halves is tracked only when both recursive results are true.

**Why assignments and queries match interval semantics**

Every leaf unit interval records exactly the latest covering add or remove operation. Range assignment changes precisely the leaves in its half-open input and preserves all others. The query returns true exactly when every covered leaf is tracked; because all operation endpoints are integers, those unit intervals partition the requested real interval without gaps.

#### Complexity detail

The coordinate bound `C` has logarithmic tree height. A range assignment or query follows at most a constant number of boundary paths and takes $O(\log C)$ time. Across `q` operations, at most $O(q \log C)$ dynamic nodes are created, giving the stated total time and space bounds.

#### Alternatives and edge cases

- **Sorted disjoint intervals:** merge additions, split removals, and binary-search queries; it can be compact, though array-backed insertion and deletion may shift $O(n)$ intervals.
- **Fixed full segment tree:** range assignment and query are logarithmic but allocating proportional to `C` is infeasible for the large coordinate domain.
- **Rescan every stored interval:** it is straightforward and correct but can take $O(q^2)$ total time.
- Intervals are half-open, so touching at one endpoint creates no overlap but adjacent tracked intervals jointly cover their union.
- Removing an untracked region has no effect on other coordinates.
- Re-adding a removed subrange restores its coverage.
- A query is false if even one interior unit interval is untracked.

</details>
