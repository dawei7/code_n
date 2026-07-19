# Guess the Majority in a Hidden Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1538 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/) |

## Problem Description
### Goal
A hidden array `nums` contains only `0` and `1`. You cannot read its entries directly. Instead, an `ArrayReader` exposes its length and lets you query four distinct indices in strictly increasing order.

For indices $a < b < c < d$, `reader.query(a, b, c, d)` reports only the distribution of the four hidden bits: it returns `4` when all four are equal, `2` when one bit differs from the other three, and `0` when the group contains two zeros and two ones. At most $2n$ calls to `query` are allowed, where $n$ is the hidden-array length.

Return any index containing the more frequent bit. If zeros and ones occur equally often, return `-1`.

### Function Contract
**Inputs**

- `reader`: an `ArrayReader` for a hidden binary array of length $n$, where $5 \le n \le 10^5$.
- `reader.length()` returns $n$.
- `reader.query(a, b, c, d)` requires $0 \le a < b < c < d < n$ and returns `4`, `2`, or `0` according to the four-bit distribution above.

**Return value**

Any valid index of the majority bit, or `-1` when the two bit counts tie. The solution may make at most $2n$ queries.

### Examples
**Example 1**

- Hidden input: `nums = [0, 0, 1, 0, 1, 1, 1, 1]`
- Output: `5`
- Explanation: Ones are more frequent, so any index containing `1`, including `2`, `4`, `5`, `6`, or `7`, is valid.

**Example 2**

- Hidden input: `nums = [0, 0, 1, 1, 0]`
- Output: `0`
- Explanation: Zeros form the majority, and index zero contains a zero.

**Example 3**

- Hidden input: `nums = [1, 0, 1, 0, 1, 0, 1, 0]`
- Output: `-1`
- Explanation: Each bit occurs four times.
