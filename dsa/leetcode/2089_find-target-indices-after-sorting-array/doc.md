# Find Target Indices After Sorting Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2089 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-target-indices-after-sorting-array/) |

## Problem Description

### Goal

You are given a zero-indexed integer array `nums` and an integer `target`. Imagine sorting `nums` in non-decreasing order. An index is a target index when the value at that position in the sorted array equals `target`.

Return every target index in increasing order. Repeated target values produce one index for each occurrence, while a target absent from the array produces an empty list. The original positions of the values do not affect the answer.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 100$.
- `target`: the value to locate after sorting.
- Every element of `nums` and `target` is between $1$ and $100$.

Let $k$ be the number of occurrences of `target` in `nums`.

**Return value**

Return the $k$ indices occupied by `target` after non-decreasing sorting, listed in increasing order.

### Examples

**Example 1**

- Input: `nums = [1, 2, 5, 2, 3]`, `target = 2`
- Output: `[1, 2]`
- Explanation: The sorted array is `[1, 2, 2, 3, 5]`.

**Example 2**

- Input: `nums = [1, 2, 5, 2, 3]`, `target = 3`
- Output: `[3]`

**Example 3**

- Input: `nums = [1, 2, 5, 2, 3]`, `target = 5`
- Output: `[4]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**The target occupies one consecutive block**

In non-decreasing order, every value smaller than `target` appears before every copy of `target`, and every larger value appears afterward. Therefore the target block starts at the number of smaller elements. Its length is exactly the number of elements equal to `target`.

**Recovering indices without constructing the sorted array**

Scan `nums` and count `smaller`, the values below `target`, and `equal`, the values equal to it. The answer is the consecutive range

$$
\{\textit{smaller},\textit{smaller}+1,\ldots,
\textit{smaller}+\textit{equal}-1\}.
$$

If `equal` is zero, this range is empty. Otherwise it is already increasing, so no additional sorting is needed.

**Why the range is exact**

After sorting, precisely `smaller` elements must precede the first target. The next `equal` positions must all contain the indistinguishable target copies, and no other position can contain one. Thus the constructed range contains every target index once and no non-target index.

#### Complexity detail

The counts require one or two linear scans of the $n$ values, so the time is $O(n)$. Apart from the returned list of $k$ indices, the algorithm stores only counters, giving $O(1)$ auxiliary space. The output itself occupies $O(k)$ space.

#### Alternatives and edge cases

- **Sort and scan:** Directly sorting `nums` follows the statement literally but costs $O(n \log n)$ time in general.
- **Counting array over values:** The bounded value range permits a frequency array, but it uses extra fixed storage and is unnecessary for one target.
- **Binary search after sorting:** Lower and upper bounds locate the block quickly only after paying the sorting cost.
- If every value equals `target`, all indices from `0` through `n - 1` are returned.
- If the target is absent, `equal` is zero and the result is empty.
- Values equal to the target are not included in the `smaller` count.

</details>
