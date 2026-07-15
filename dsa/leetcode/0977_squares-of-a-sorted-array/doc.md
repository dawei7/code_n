# Squares of a Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 977 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/squares-of-a-sorted-array/) |

## Problem Description

### Goal

An integer array `nums` is already sorted in non-decreasing order. Square every number and return the resulting values, also sorted in non-decreasing order.

Negative inputs require care because squaring reverses their magnitude order: a value farther below zero can produce a larger square than a later positive value. Preserve every occurrence, including duplicate values and duplicate squares, and produce an output with exactly the same length as the input. The requested solution should exploit the input ordering to run in linear time rather than sorting all squares again.

### Function Contract

**Inputs**

- `nums`: a non-decreasing list of $N$ integers, where $1 \le N \le 10^4$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- A list containing each value `nums[i] * nums[i]`, sorted in non-decreasing order.

### Examples

**Example 1**

- Input: `nums = [-4, -1, 0, 3, 10]`
- Output: `[0, 1, 9, 16, 100]`
- Explanation: direct squaring gives `[16, 1, 0, 9, 100]`; ordering those values gives the output.

**Example 2**

- Input: `nums = [-7, -3, 2, 3, 11]`
- Output: `[4, 9, 9, 49, 121]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Find the largest remaining magnitude at an endpoint:** Because `nums` is non-decreasing, the value with greatest absolute magnitude among an unprocessed interval must be at its left or right boundary. Interior values lie numerically between those endpoints and cannot have a larger magnitude than both.

**Fill the answer from right to left:** Maintain `left` and `right` at the current boundaries and an output position starting at `N - 1`. Compare `abs(nums[left])` with `abs(nums[right])`. Square the larger magnitude into the current output position, move that boundary inward, and decrement the output position. Equal magnitudes may be taken from either end because their squares are identical.

Each step places the largest square that has not yet been written. Therefore everything placed to its right is at least as large, and the remaining unwritten positions need only receive smaller or equal squares. When the pointers cross, every input occurrence has been consumed once and the output is in non-decreasing order.

#### Complexity detail

The two pointers move inward a total of $N$ times, and each iteration performs constant work, so time is $O(N)$. The returned array contains $N$ squares and uses $O(N)$ space; aside from that result, the algorithm uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Square and sort:** Applying a comparison sort after squaring is concise but costs $O(N\log N)$ time and ignores the useful input ordering.
- **Insert squares into order:** Repeated insertion is correct but can take $O(N^2)$ time when the squared sequence arrives in descending order.
- **All-negative input:** The squares appear in reverse order, which the endpoint comparison handles without a special branch.
- **All-nonnegative input:** The right endpoint wins each comparison, reproducing the naturally ordered squares.
- **Equal magnitudes:** Values such as `-3` and `3` produce duplicate squares, and both occurrences must remain in the result.

</details>
