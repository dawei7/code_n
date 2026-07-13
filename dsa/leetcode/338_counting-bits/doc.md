# Counting Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 338 |
| Difficulty | Easy |
| Topics | Dynamic Programming, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/counting-bits/) |

## Problem Description
### Goal
Given a nonnegative integer `n`, consider every integer from `0` through `n` in increasing order. For each value, count the positions containing `1` in its ordinary binary representation.

Return a list of length $n + 1$ whose entry at index `i` is the set-bit count for `i`. Thus the first entry is always zero, and each input value contributes exactly one output count. Compute the full list in linear time $O(n)$, possibly in a single pass, without using a built-in bit-count function. Reuse relationships among smaller binary values instead of independently inspecting every bit of every integer.

### Function Contract
**Inputs**

- `n`: a non-negative integer

**Return value**

- A list of $n + 1$ integers where result index `i` contains the number of `1` bits in `i`.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `[0, 1, 1]`
- Explanation: `0`, `1`, and `2` are `0`, `1`, and `10` in binary.

**Example 2**

- Input: `n = 5`
- Output: `[0, 1, 1, 2, 1, 2]`

**Example 3**

- Input: `n = 0`
- Output: `[0]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Remove one bit to reuse an earlier answer**

Counting the bits of each number independently repeats almost the same work. Consecutive integers share no convenient binary prefix, but every positive integer can be reduced to a smaller integer whose answer has already been computed.

Right-shifting `i` once removes its least-significant bit. The remaining bits are exactly the binary representation of $i \gg 1$, while $i \mathbin{\&} 1$ tells whether the removed bit was a `0` or a `1`. This gives the recurrence

`bits[i] = bits[i >> 1] + (i & 1)`.

**Why the forward recurrence is valid**

Start with `bits[0] = 0` and fill the list from left to right. For every positive `i`, $i \gg 1$ is smaller than `i`, so its count is already available. The useful invariant is local to this construction: before computing index `i`, all indices below `i` contain their correct popcounts. The recurrence adds precisely the contribution of the bit that was removed, which makes index `i` correct and preserves the invariant.

**Trace the values through five**

For $n = 5$, the transitions are:

- `1`: reuse `bits[0]` and add `1`, giving `1`.
- `2` (`10`): reuse `bits[1]` and add `0`, giving `1`.
- `3` (`11`): reuse `bits[1]` and add `1`, giving `2`.
- `4` (`100`): reuse `bits[2]` and add `0`, giving `1`.
- `5` (`101`): reuse `bits[2]` and add `1`, giving `2`.

This produces every required value in a single forward pass without performing a separate bit scan for each integer.

#### Complexity detail

The loop computes each of the `n` positive indices once with constant-time shifts, masks, lookups, and additions, so the running time is $O(n)$. The returned list contains $n + 1$ values and therefore uses $O(n)$ space. Aside from that required output, the algorithm uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Clear the lowest set bit:** the recurrence `bits[i] = bits[i & (i - 1)] + 1` is also linear because it always reuses a smaller index.
- **Copy power-of-two blocks:** reusing the block below the latest power of two has the same complexity but needs more bookkeeping.
- **Independent popcount calls:** are concise and may be fast on fixed-width hardware, but scanning up to $O(\log i)$ bits per value costs $O(n \log n)$ in the bit-operation model.
- When $n = 0$, the initialized list `[0]` is already the complete answer.
- At a power of two, the count resets to `1` because its binary representation contains one leading `1` followed only by zeros.

</details>
