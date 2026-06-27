# Find the Maximum Number of Elements in Subset

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3020 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Enumeration |
| Official Link | [find-the-maximum-number-of-elements-in-subset](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the largest possible subset such that the elements can be arranged in a sequence $[x, x^2, x^4, \dots, x^{2^k}]$ where each element is the square of the previous one. The subset must have an odd number of elements.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the maximum size of a valid subset.

### Examples
**Example 1**

- Input: `nums = [5, 4, 1, 2, 2]`
- Output: `3`
- Explanation: The subset `[2, 4, 2]` forms the sequence `[2, 4, 2]` (or `[2, 4, 2]` is not the sequence, but the subset `[2, 4, 2]` can be ordered as `2, 4, 2`? No, the sequence is `2, 4, 16...`. The subset `[2, 4, 2]` is valid because $2^1=2, 2^2=4, 4^2=16$ is not possible, but $2, 4, 2$ is not the sequence. Wait, the sequence is $x, x^2, x^4...$. For `[2, 4, 2]`, we have $2, 4$. The subset is `[2, 4, 2]`. The sequence is $2, 4$. The size is 3.

**Example 2**

- Input: `nums = [1, 1]`
- Output: `1`

**Example 3**

- Input: `nums = [1, 3, 9, 27]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using a Frequency Map (Hash Table). We count the occurrences of each number. For the number `1`, the subset size is simply the count of `1`s (if odd, use all; if even, use count-1). For other numbers $x > 1$, we simulate the chain $x, x^2, x^4, \dots$ as long as the numbers exist in the frequency map, keeping track of the chain length and ensuring the subset size remains odd.

---

## Complexity Analysis
- **Time Complexity**: $O(N + M \log(\log(\max(nums))))$, where $N$ is the number of elements and $M$ is the number of unique elements. The chain length is logarithmic relative to the maximum value.
- **Space Complexity**: $O(N)$ to store the frequency map of the input array.
