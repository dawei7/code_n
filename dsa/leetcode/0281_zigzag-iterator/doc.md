# Zigzag Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 281 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Design, Queue, Iterator |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/zigzag-iterator/) |

## Problem Description
### Goal
Design an iterator over two integer vectors that emits their values in zigzag order. Begin with the first vector, then take one value from the second, and continue alternating while both vectors still contain unconsumed elements.

If one vector is empty initially or becomes exhausted first, continue through the remaining values of the other vector in their original order. `next()` returns and consumes the next scheduled integer, while `hasNext()` reports whether any value remains. The app adapter collects the complete emitted sequence; the native iterator must preserve incremental state without eagerly rearranging the input vectors.

### Function Contract
**Inputs**

- `v1`: the first integer vector
- `v2`: the second integer vector

**Return value**

The local batch adapter returns the full sequence produced by native `ZigzagIterator.next()` calls until `hasNext()` is false.

### Examples
**Example 1**

- Input: `v1 = [1,2], v2 = [3,4,5,6]`
- Output: `[1,3,2,4,5,6]`

**Example 2**

- Input: `v1 = [1], v2 = []`
- Output: `[1]`

**Example 3**

- Input: `v1 = [], v2 = [7,8]`
- Output: `[7,8]`
