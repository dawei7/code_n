# Find Pattern in Infinite Stream II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3037 |
| Difficulty | Hard |
| Topics | Array, Sliding Window, Rolling Hash, String Matching, Interactive, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/) |

## Problem Description

### Goal

You are given a binary array `pattern` and an `InfiniteStream` representing a 0-indexed, unending sequence of bits. The stream exposes only `next()`, which consumes and returns one bit. Earlier bits cannot be indexed, requested again, or recovered by rewinding the stream.

Return the first index at which all entries of `pattern` occur consecutively in the same order. The input guarantees that a matching start exists among the first $10^5$ stream positions, so a sequential algorithm will eventually reach the end of the first occurrence.

### Function Contract

Let $M=\lvert\texttt{pattern}\rvert$, and let $S$ be the number of stream bits consumed through the end of the first match.

**Inputs**

- `stream`: An `InfiniteStream` whose `next()` method consumes and returns the next `0` or `1`. App-local fixtures provide a finite authored prefix containing the guaranteed first match while preserving this sequential interface.
- `pattern`: A binary array of length $1 \le M \le 10^4$.

The first matching start index is guaranteed to be less than $10^5$.

**Return value**

Return the 0-indexed starting position of the earliest complete occurrence of `pattern` in the stream.

### Examples

#### Example 1

- **Input:** `stream = [1,1,1,0,1,1,1,...], pattern = [0,1]`
- **Output:** `3`
- **Explanation:** The first `[0,1]` begins with the bit at index `3`.

#### Example 2

- **Input:** `stream = [0,0,0,0,...], pattern = [0]`
- **Output:** `0`
- **Explanation:** The first stream bit already matches the one-bit pattern.

#### Example 3

- **Input:** `stream = [1,0,1,1,0,1,1,0,1,...], pattern = [1,1,0,1]`
- **Output:** `2`
- **Explanation:** The first complete `[1,1,0,1]` occupies indices `2` through `5`.
