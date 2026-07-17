# Check if Array Is Sorted and Rotated

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1752 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) |

## Problem Description

### Goal

Given an integer array `nums`, determine whether it can be obtained from an array sorted in non-decreasing order by rotating that sorted array by some number of positions. A rotation by zero positions is permitted, so an already sorted array qualifies.

Duplicates are allowed. Rotating an array `A` by $x$ positions produces an array `B` of the same length where `B[i]` equals `A[(i+x) % n]` for every valid index. Return `true` exactly when some sorted original array and some legal rotation amount produce `nums`.

### Function Contract

**Inputs**

- `nums`: a nonempty list with $1 \le \lvert\texttt{nums}\rvert \le 100$ and $1 \le \texttt{nums[i]} \le 100$.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- Return `True` if `nums` is a rotation, possibly by zero, of a non-decreasing array; otherwise return `False`.

### Examples

**Example 1**

- Input: `nums = [3, 4, 5, 1, 2]`
- Output: `True`
- Explanation: Rotating `[1, 2, 3, 4, 5]` to begin at `3` produces the input.

**Example 2**

- Input: `nums = [2, 1, 3, 4]`
- Output: `False`
- Explanation: No single rotation cut makes all values non-decreasing.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `True`
- Explanation: The array is already non-decreasing, corresponding to a zero-position rotation.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**View adjacent comparisons on a circle**

Compare every element with its successor, using the first element as the successor of the last. Call an index a descent when `nums[i] > nums[(i + 1) % n]`. Equal adjacent values are not descents because the original order is non-decreasing rather than strictly increasing.

**Allow only the single rotation boundary**

Within each unchanged portion of a sorted array, values cannot decrease. A rotation can introduce only one circular descent: the boundary where the sorted array's largest trailing region is followed by its smallest leading region. More than one descent therefore proves that no single rotation created the input.

**Use the descent as a sufficient cut**

If exactly one descent exists, cutting immediately after it produces a sequence with no internal decrease and therefore a non-decreasing original array. If there is no descent, all circular neighbors are equal or the one-element array is already valid. Thus at most one circular descent is both necessary and sufficient.

#### Complexity detail

The algorithm performs one circular comparison per element and can stop after the second descent, taking $O(n)$ time. It stores only the descent count and current index, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Try every rotation:** Sorting a copy and comparing all $n$ rotations is straightforward but requires $O(n^2)$ comparison work after sorting.
- **Find the minimum first:** Choosing one minimum as a presumed cut can fail with duplicates when the same minimum appears in several positions; the circular descent criterion avoids that ambiguity.
- **Zero-position rotation:** An already non-decreasing array must return `True`.
- **Duplicates:** Equal neighbors never count as a descent.
- **All equal:** There are zero descents, so the array is valid.
- **One element:** Its circular comparison is equal and the array is valid.
- **Two elements:** Either ordering is a rotation of the sorted pair.
- **Wraparound comparison:** Omitting the last-to-first pair can accept arrays with two effective rotation boundaries.

</details>
