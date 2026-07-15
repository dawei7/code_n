# Peak Index in a Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 852 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/) |

## Problem Description
### Goal
You are given an integer mountain array `arr`. Its values are strictly increasing up to one interior peak element and strictly decreasing after that peak, so the peak index is unique. The guarantee excludes flat adjacent values and peaks at either array boundary.

Return the index of the peak element. The solution must exploit the mountain shape and run in logarithmic time rather than scanning the entire array.

### Function Contract
**Inputs**

- `arr`: a guaranteed mountain array of length $n$, where $3 \leq n \leq 10^5$ and $0 \leq \texttt{arr[i]} \leq 10^6$.

**Return value**

Return the unique index at which the strictly increasing prefix changes to the strictly decreasing suffix.

### Examples
**Example 1**

- Input: `arr = [0,1,0]`
- Output: `1`

**Example 2**

- Input: `arr = [0,2,1,0]`
- Output: `1`

**Example 3**

- Input: `arr = [0,10,5,2]`
- Output: `1`

### Required Complexity
- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**An adjacent comparison reveals the side of the peak**

Maintain an inclusive search interval `[left, right]` known to contain the peak. Choose `middle = (left + right) // 2` and compare `arr[middle]` with `arr[middle + 1]`. The latter index is safe while `left < right`, because then `middle < right`.

If `arr[middle] < arr[middle + 1]`, the slope is rising. The peak must lie strictly to the right of `middle`, so assign `left = middle + 1`. Otherwise the slope is falling, or `middle` itself is the peak; keep `middle` by assigning `right = middle`.

**The interval cannot discard the unique peak**

On the increasing side every adjacent comparison rises, and on the decreasing side every adjacent comparison falls. Each update therefore removes only indices that cannot be the change point while retaining the peak. The interval shrinks on every iteration. When `left == right`, the invariant leaves that sole index as the unique peak.

#### Complexity detail

Each comparison reduces the search interval by roughly half, so the algorithm takes $O(\log n)$ time. It stores only three indices, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Linear maximum scan:** The peak is also the array's maximum, so scanning all values is correct but takes $O(n)$ time and misses the required logarithmic bound.
- **Linear slope scan:** Returning the first index whose next value is smaller is also correct for a mountain array, but remains linear.
- **Peak near the left boundary:** The peak may be index `1`; retaining `middle` on a falling comparison prevents skipping it.
- **Peak near the right boundary:** The peak may be index `n - 2`; a rising comparison advances the left boundary toward it.
- **Minimum length:** A three-element mountain is handled by the same comparison and interval invariant.
- **No plateaus:** Strict increase and strict decrease guarantee that equality never needs a branch.
- **No validation step:** The input is guaranteed to be a mountain array, so the algorithm need not detect malformed shapes.

</details>
