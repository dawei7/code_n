# Find Pattern in Infinite Stream I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3023 |
| Difficulty | Medium |
| Topics | Array, Sliding Window, Rolling Hash, String Matching, Interactive, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/find-pattern-in-infinite-stream-i/) |

## Problem Description
### Goal
You are given a binary array `pattern` and an `InfiniteStream` representing a 0-indexed, unending sequence of bits. The stream exposes only `next()`, which consumes and returns the next bit; it does not support indexing or rewinding.

Return the first index at which the complete `pattern` begins in the stream. The input guarantees that such a starting position exists among the first $10^5$ stream indices, so a correct sequential search eventually finds it.

### Function Contract
**Inputs**

- `stream`: An `InfiniteStream` whose `next()` method returns the next `0` or `1`. App-local fixtures provide a finite authored prefix containing the guaranteed first match, but the solution receives only the sequential interface.
- `pattern`: A binary list of length $M$, where $1 \le M \le 100$.

Let $S$ be the number of stream bits consumed through the end of the first match.

**Return value**

The 0-indexed starting position of the first occurrence of `pattern` in `stream`.

### Examples
**Example 1**

- Input: `stream = [1, 1, 1, 0, 1, 1, 1, ...], pattern = [0, 1]`
- Output: `3`

The first matching pair is the `0, 1` beginning at index `3`.

**Example 2**

- Input: `stream = [0, 0, 0, 0, ...], pattern = [0]`
- Output: `0`

The first bit already matches the one-bit pattern.

**Example 3**

- Input: `stream = [1, 0, 1, 1, 0, 1, 1, 0, 1, ...], pattern = [1, 1, 0, 1]`
- Output: `2`

The first four-bit match starts at index `2`.
