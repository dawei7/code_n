# Array Transformation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1243 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/array-transformation/) |

## Problem Description

### Goal

You are given an integer array `arr`. Repeatedly transform all interior elements simultaneously. If an element is strictly smaller than both immediate neighbors, increase it by one; if it is strictly larger than both neighbors, decrease it by one. Every other element remains unchanged.

The first and last elements never change. Each round must use the values from the beginning of that round, so an update cannot influence another update until the next round. Continue until an entire round makes no change, then return the resulting stable array.

### Function Contract

**Inputs**

- `arr`: A list of $n$ integers, where $3\le n\le100$ and $1\le\texttt{arr[i]}\le100$.

Let $C$ be the total number of individual element updates made before the array stabilizes.

**Return value**

- The stable array obtained after applying the simultaneous transformation until no element changes.

### Examples

**Example 1**

- Input: `arr = [6,2,3,4]`
- Output: `[6,3,3,4]`

The value `2` is a strict valley and rises once; the next round makes no change.

**Example 2**

- Input: `arr = [1,6,3,4,3,5]`
- Output: `[1,4,4,4,4,5]`

Several peaks and valleys change across multiple simultaneous rounds.

**Example 3**

- Input: `arr = [1,2,3,4]`
- Output: `[1,2,3,4]`

A monotone array has no strict interior extremum and is already stable.

### Required Complexity

- **Time:** $O(n+C)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Start with every interior index active.** On the first round, any interior position might be a strict peak or valley. Evaluate all of them against the unchanged current array and collect their signed updates without applying any update early.

**Apply one simultaneous batch.** After every active position has been evaluated, add the collected `+1` or `-1` changes. This preserves the rule that all decisions in a round use the same prior values. The endpoints are never active and therefore never change.

**Restrict the next frontier.** If a position did not change and neither neighbor changed, its complete three-value neighborhood is identical on the next round, so it still cannot change. Consequently, only a changed index and its immediate interior neighbors need reevaluation. Build the next active set from those positions. When a batch contains no updates, the array is stable everywhere: every omitted position has an unchanged neighborhood, and every active position was just shown not to be a strict extremum.

#### Complexity detail

The initial frontier contains $O(n)$ indices. Each of the $C$ actual updates contributes at most three positions to the following frontier, so the total number of evaluations is $O(n+C)$. The current array, update batch, and active-index sets use $O(n)$ space.

#### Alternatives and edge cases

- **Rescan the full array each round:** It is straightforward and correct but can spend $O(n)$ work per day even when only one local extremum is changing.
- **Update in place during the scan:** This is incorrect because later decisions would observe values from the current round rather than its beginning.
- **Copy the entire array per round:** It preserves simultaneity but still performs unnecessary full-array work on a sparse frontier.
- **Already stable array:** The first evaluation produces no updates and returns the input values unchanged.
- **Equal neighbor:** The comparison is strict; equality with either neighbor prevents an update in that direction.
- **Endpoint:** Positions `0` and `n - 1` remain fixed even if they would be extrema.
- **Direction reversal:** An element may change in different directions on later rounds, so frontier membership—not a permanent per-index direction—is tracked.

</details>
