# RLE Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 900 |
| Difficulty | Medium |
| Topics | Array, Design, Counting, Iterator |
| Official Link | [LeetCode](https://leetcode.com/problems/rle-iterator/) |

## Problem Description
### Goal
Run-length encoding represents an integer sequence with an even-length, 0-indexed array `encoding`. At every even index `i`, `encoding[i]` is the number of consecutive copies of the non-negative value `encoding[i + 1]`. A count may be zero, and adjacent runs may contain the same value, so one decoded sequence can have several valid encodings.

Design an iterator over the represented sequence without requiring it to be expanded.

Construct `RLEIterator` from `encoding`. Each call `next(n)` exhausts the next `n` decoded elements and returns the last element exhausted. If fewer than `n` elements remain, exhaust everything that is left and return `-1`.

### Function Contract
Let $m$ be the number of encoded runs and $q$ be the number of `next` calls.

**Operations**

- `RLEIterator(encoding)`: initialize the iterator from $m$ count-value pairs.
- `next(n)`: consume the next $n$ represented elements, where $1 \leq n \leq 10^9$, and return the final consumed value or `-1` if the request passes the end.
- `encoding` has even length between `2` and `1000`, and every entry is between `0` and $10^9$.
- At most `1000` calls are made to `next`.

**App-local input**

- `encoding`: the alternating count-value array.
- `operations`: calls encoded as `["next", n]`.

**Return value**

Return the integer result of each `next` call in order.

### Examples
**Example 1**

- Input: `encoding = [3,8,0,9,2,5], operations = [["next",2],["next",1],["next",1],["next",2]]`
- Output: `[8,8,5,-1]`

The encoding represents `[8,8,8,5,5]`. The final request asks for two elements when only one remains, so it returns `-1`.

**Example 2**

- Input: `encoding = [1,4], operations = [["next",1]]`
- Output: `[4]`

**Example 3**

- Input: `encoding = [0,7,2,3], operations = [["next",1],["next",1]]`
- Output: `[3,3]`
