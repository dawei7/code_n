# Valid Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 941 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-mountain-array/) |

## Problem Description

### Goal

Given an integer array `arr`, decide whether it is a valid mountain array. A mountain must contain at least three elements and have an interior peak: some index strictly between the first and last positions.

All values before that peak must be strictly increasing, and all values after it must be strictly decreasing. Thus both slopes must contain at least one step, equal adjacent values are forbidden, and neither endpoint can serve as the peak. Return whether the whole array satisfies this shape.

### Function Contract

Let $n$ be the length of `arr`, and let $a_i$ denote the value at index $i$.

**Inputs**

- `arr`: an integer array with $1 \le n \le 10^4$ and $0 \le a_i \le 10^4$ for every valid index $i$.

**Return value**

Return `true` exactly when there is an index $p$ with $0<p<n-1$ such that the values are strictly increasing through $p$ and strictly decreasing after $p$; otherwise return `false`.

### Examples

**Example 1**

- Input: `arr = [2,1]`
- Output: `false`

**Example 2**

- Input: `arr = [3,5,5]`
- Output: `false`

**Example 3**

- Input: `arr = [0,3,2,1]`
- Output: `true`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Climb the strictly increasing slope.** Start at the first index and move right while each next value is greater. When this loop stops, the current index is the only possible peak: any earlier choice would leave an increasing step on the required descending side.

**Require an interior peak.** Reject if no increasing step occurred or if the climb reached the final element. These checks enforce both the minimum shape and the existence of a descending side.

**Descend without plateaus or reversals.** From the peak, move right while each next value is strictly smaller. The array is a mountain exactly when this descent reaches the final index. If it stops early, the blocking pair is equal or rises again, either of which violates strict decrease.

The climb covers the complete required prefix and fixes the only possible turning point. The descent then verifies the entire remaining suffix. Passing both phases therefore proves the exact mountain definition, and every valid mountain necessarily passes them.

#### Complexity detail

The pointer moves only forward and examines each adjacent pair at most once. Total time is $O(n)$ and the index uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Try every possible peak:** Validate both sides separately for each interior index. This is correct but can repeat prefix comparisons and take $O(n^2)$ time.
- **Direction-state scan:** Track whether the traversal is climbing or descending and reject any forbidden transition. It also runs in $O(n)$ time but requires careful endpoint checks.
- **Fewer than three elements:** No interior peak can exist, so return `false`.
- **Plateau:** Any equal adjacent values invalidate the array, including equality at the apparent peak.
- **Peak at an endpoint:** A wholly increasing or wholly decreasing array is not a mountain.
- **Second rise:** Once descent begins, any later increase makes the whole array invalid.

</details>
