# Guess the Number Using Bitwise Questions II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3094 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Bit Manipulation, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/) |

## Problem Description

### Goal

An unknown integer $n$ lies in the inclusive interval $[0, 2^{30}-1]$. The task is to recover and return the **initial** value of this 30-bit number through a predefined interactive API, even though every query changes the hidden state.

Calling `commonBits(num)` first counts the bit positions at which the current $n$ and the query value `num` contain the same binary digit. Only the first 30 positions participate in this comparison. The API then performs `n = n XOR num` before returning the count, so later calls observe the mutated value of $n$.

Every query must also satisfy $0 \le \texttt{num} \le 2^{30}-1$; a result obtained with an out-of-range query is not guaranteed to be reliable. Use legal queries and account for every mutation to determine the original hidden number.

### Function Contract

**Inputs**

- `n`: The initial hidden integer, satisfying $0 \le n \le 2^{30}-1$.

In LeetCode's native interactive interface, `findNumber()` receives no explicit parameter. It observes the hidden state only through `commonBits(num)`. The cOde(n) adapter exposes the initial `n` and constructs the explicit stateful `CommonBitsAPI` callable locally.

For each legal query, the oracle counts equal digits across the first 30 bit positions, updates its hidden state with XOR by the query, and returns the count calculated before that update.

**Return value**

Return the value of $n$ from before any API call was made.

### Examples

**Example 1**

- Input: `n = 0`
- Output: `0`
- Explanation: All 30 bits in the initial hidden number are clear.

**Example 2**

- Input: `n = 33`
- Output: `33`
- Explanation: The original number has set bits at positions zero and five, and it must be recovered despite the API's XOR mutations.
