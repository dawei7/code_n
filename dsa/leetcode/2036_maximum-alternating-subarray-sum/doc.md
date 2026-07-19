# Maximum Alternating Subarray Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2036 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-alternating-subarray-sum/) |

## Problem Description

### Goal

A subarray is a nonempty contiguous segment of the 0-indexed integer array
`nums`. For a subarray beginning at index $i$, form its alternating sum by
adding `nums[i]`, subtracting the next element, adding the following element,
and continuing with alternating signs through the chosen endpoint.

Consider every possible nonempty subarray. Return the greatest alternating sum
among them. The sign pattern always restarts with addition at the subarray's
left boundary; elements cannot be skipped, and the selected segment may have
either odd or even length.

### Function Contract

Let $N$ be the length of `nums`.

**Inputs**

- `nums`: an integer array with $1 \le N \le 10^5$ and
  $-10^5 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- The maximum alternating sum of any nonempty contiguous subarray of `nums`.

### Examples

**Example 1**

- Input: `nums = [3, -1, 1, 2]`
- Output: `5`
- Explanation: Subarray `[3, -1, 1]` contributes `3 - (-1) + 1 = 5`.

**Example 2**

- Input: `nums = [2, 2, 2, 2, 2]`
- Output: `2`
- Explanation: A one-element subarray has sum `2`; odd-length alternating
  segments also have sum `2`.

**Example 3**

- Input: `nums = [1]`
- Output: `1`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Classify subarrays by the sign of their final element**

For each index $i$, let $A_i$ be the greatest alternating sum of a subarray
ending at $i$ in which `nums[i]` has a positive sign. Such a subarray has odd
length. Let $S_i$ describe an ending subarray in which `nums[i]` is
subtracted, so its length is even.

These two states retain exactly the information needed to append the next
contiguous element. Keeping only one generic best sum would lose the next sign.

**Either restart with addition or extend the opposite state**

An added state can start a new one-element subarray or extend the previous
subtracted state. A subtracted state must extend the previous added state:

$$
A_i = \max\left(\texttt{nums[i]}, S_{i-1}+\texttt{nums[i]}\right),
$$

$$
S_i = A_{i-1}-\texttt{nums[i]}.
$$

There is no restart option for $S_i$ because the first element of every
subarray is added. Compute both new values from the previous pair before
overwriting either state.

**Take the best endpoint and parity**

Every nonempty subarray ends at some index and has either odd length or even
length, so it belongs to exactly one of these states. The transitions consider
all valid ways to produce each state: restart when allowed, or extend the only
opposite-sign predecessor. Induction on the endpoint therefore makes each
state optimal for its class. The maximum state seen across all endpoints is
the required answer.

#### Complexity detail

Each of the $N$ elements performs a constant number of arithmetic operations
and comparisons, for $O(N)$ time. Only the two previous states and the running
answer are retained, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Enumerate all starts and ends:** Maintaining an alternating sum while
  extending every start is correct but takes $O(N^2)$ time.
- **Recompute every subarray sum:** A third loop that sums each selected segment
  raises the cost to $O(N^3)$ and is unnecessary.
- A single element is a valid subarray and is always treated as positive.
- With all negative values, an even-length segment may still be positive
  because subtracting a negative value increases the sum.
- The problem asks for a subarray, not a subsequence; no interior element may
  be skipped.
- A new subarray resets the sign to positive regardless of the absolute index's
  parity.
- The result can exceed the individual value bounds, so fixed-width
  implementations need a sufficiently wide integer type.

</details>
