# Split Array by Prime Indices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3618 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-by-prime-indices/) |

## Problem Description

### Goal

Split `nums` into two arrays according to each element's zero-based position. Place `nums[i]` in array `A` when index $i$ is a prime number. Place every element at a non-prime index in array `B`; in particular, indices 0 and 1 are not prime.

Preserve all values, including negative values and zeros, when computing the two sums. Return the absolute difference between `sum(A)` and `sum(B)`. If either partition is empty, its sum is defined to be zero.

### Function Contract

**Inputs**

- `nums`: The integer array whose elements are classified by their indices.

The constraints are $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return $\lvert\operatorname{sum}(A)-\operatorname{sum}(B)\rvert$ after assigning elements at prime indices to `A` and all remaining elements to `B`.

### Examples

#### Example 1

- **Input:** `nums = [2, 3, 4]`
- **Output:** `1`
- **Explanation:** Only index 2 is prime, so `A` sums to 4 and `B` sums to 5.

#### Example 2

- **Input:** `nums = [-1, 5, 7, 0]`
- **Output:** `3`
- **Explanation:** Prime indices 2 and 3 contribute 7, while indices 0 and 1 contribute 4.

#### Example 3

- **Input:** `nums = [9]`
- **Output:** `9`
- **Explanation:** Index 0 is non-prime, so `A` is empty and `B` sums to 9.
