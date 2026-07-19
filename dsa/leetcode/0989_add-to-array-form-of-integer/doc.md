# Add to Array-Form of Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 989 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/add-to-array-form-of-integer/) |

## Problem Description

### Goal

The array-form of a nonnegative integer stores its decimal digits from left to right. For example, the integer $1321$ has array-form `[1, 3, 2, 1]`.

Given an array-form integer `num` and a positive integer `k`, add `k` to the represented value and return the sum in the same array-form. The input contains no leading zero unless it represents zero itself, and the returned digit list must likewise be the ordinary decimal representation of the exact sum.

### Function Contract

**Inputs**

- `num`: a list of $N$ decimal digits, where $1\le N\le10^4$, each digit is from $0$ through $9$, and there are no unnecessary leading zeros.
- `k`: an integer satisfying $1\le\texttt{k}\le10^4$.

Let $D$ be the number of decimal digits in `k`, and define $L=\max(N,D)$.

**Return value**

- The decimal digits of the represented integer plus `k`, in left-to-right order.

### Examples

**Example 1**

- Input: `num = [1, 2, 0, 0], k = 34`
- Output: `[1, 2, 3, 4]`
- Explanation: $1200+34=1234$.

**Example 2**

- Input: `num = [2, 7, 4], k = 181`
- Output: `[4, 5, 5]`

**Example 3**

- Input: `num = [2, 1, 5], k = 806`
- Output: `[1, 0, 2, 1]`
