# Make Array Empty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2659 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Binary Indexed Tree, Segment Tree, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-array-empty/) |

## Problem Description

### Goal

You are given an integer array `nums` whose values are distinct. Repeatedly inspect the first element until the array becomes empty. If that element is currently the smallest value in the array, remove it; otherwise move it from the front to the end. Either action counts as one operation.

Return the total number of operations required to empty the array. Because every value is distinct, each removal target is unambiguous, and targets are necessarily removed in strictly increasing value order even though rotations continually change which surviving element is at the front.

### Function Contract

**Inputs**

- `nums`: An array of $n$ distinct integers, where $1 \le n \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- Return the number of front removals and front-to-back rotations performed before the array is empty.

### Examples

#### Example 1

- **Input:** `nums = [3,4,-1]`
- **Output:** `5`
- **Explanation:** Rotate `3` and `4`, remove `-1`, then remove `3` and `4`.

#### Example 2

- **Input:** `nums = [1,2,4,3]`
- **Output:** `5`
- **Explanation:** Remove `1` and `2`, rotate `4`, then remove `3` and `4`.

#### Example 3

- **Input:** `nums = [1,2,3]`
- **Output:** `3`
- **Explanation:** The front is always the current minimum, so every operation removes an element.
