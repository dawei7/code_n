# Construct the Lexicographically Largest Valid Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1718 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/) |

## Problem Description

### Goal

Given an integer `n`, construct a sequence whose elements lie in the range from $1$ through $n$. The value $1$ must occur exactly once. Every value $i$ with $2 \le i \le n$ must occur exactly twice, and the absolute difference between the indices of its two occurrences must equal $i$. These multiplicities make the sequence length $2n - 1$.

Among all sequences satisfying those distance rules, return the lexicographically largest one. Two equal-length sequences are compared at their first differing position, where the sequence containing the larger value ranks higher. A valid sequence is guaranteed to exist for every legal `n`.

### Function Contract

**Inputs**

- `n`: the largest value in the sequence, with $1 \le n \le 20$.

**Return value**

- Return the lexicographically largest valid integer sequence of length $2n - 1$.

### Examples

**Example 1**

- Input: `n = 3`
- Output: `[3,1,2,3,2]`
- Explanation: Both copies of $2$ and $3$ are separated by their values, and no valid sequence begins with a larger lexicographic prefix.

**Example 2**

- Input: `n = 5`
- Output: `[5,3,1,4,3,5,2,4,2]`
- Explanation: Each value above $1$ appears at indices whose difference equals that value.

**Example 3**

- Input: `n = 1`
- Output: `[1]`
- Explanation: The sole required value is also the complete sequence.
