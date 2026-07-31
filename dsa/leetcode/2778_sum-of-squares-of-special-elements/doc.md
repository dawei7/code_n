# Sum of Squares of Special Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2778 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-squares-of-special-elements/) |

## Problem Description

### Goal

You are given a 1-indexed integer array `nums` of length $n$. An element at index $i$ is special when $i$ divides $n$ exactly, meaning $n \bmod i = 0$.

Return the sum of the squares of every special element. The divisibility test applies to the element's 1-based index, while the squared quantity is the element value stored at that index. Every qualifying index contributes independently to the total.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 50$ and every value is between $1$ and $50$ inclusive.

Although programming-language lists are normally 0-indexed, the problem's index $i$ refers to `nums[i - 1]`.

**Return value**

Return

$$
\sum_{\substack{1 \le i \le n \\ i \mid n}} \texttt{nums}[i-1]^2,
$$

the integer sum of the squared values at all 1-based indices that divide $n$.

### Examples

**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `21`
- Explanation: The special indices are $1$, $2$, and $4$, so the result is $1^2 + 2^2 + 4^2 = 21$.

**Example 2**

- Input: `nums = [2,7,1,19,18,3]`
- Output: `63`
- Explanation: The divisors of $6$ are $1$, $2$, $3$, and $6$. Their values contribute $2^2 + 7^2 + 1^2 + 3^2 = 63$.

**Example 3**

- Input: `nums = [9]`
- Output: `81`
- Explanation: Index $1$ divides the array length $1$, so the only value is special.
