# Guess the Number Using Bitwise Questions I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3064 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Bit Manipulation, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/) |

## Problem Description

### Goal

An unknown positive integer $n$ must be recovered through a predefined interactive API. The hidden number fits in 30 bits.

Calling `commonSetBits(num)` returns how many bit positions contain `1` in both $n$ and the query value `num`. Equivalently, the response is the number of set bits in `n & num`. Every query value must remain between $0$ and $2^{30}-1$; results for values outside that interval are not guaranteed to be reliable.

Determine and return the exact hidden number $n$ using the information supplied by this API.

### Function Contract

**Inputs**

- `n`: The hidden integer, satisfying $1 \le n \le 2^{30}-1$.

In LeetCode's native interactive interface, `findNumber()` receives no explicit parameter. It learns about $n$ only by calling `commonSetBits(num)`. The cOde(n) adapter exposes `n` and constructs the explicit `CommonSetBitsAPI` callable so the same deterministic oracle is available locally.

For every legal query $0 \le \texttt{num} \le 2^{30}-1$, the oracle returns the population count of `n & num`.

**Return value**

Return the exact hidden integer $n$.

### Examples

**Example 1**

- Input: `n = 31`
- Output: `31`
- Explanation: The API responses contain enough information to recover the five low set bits of `31`.

**Example 2**

- Input: `n = 33`
- Output: `33`
- Explanation: The recovered number has set bits at positions zero and five.
