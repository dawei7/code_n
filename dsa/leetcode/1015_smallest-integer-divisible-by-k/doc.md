# Smallest Integer Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1015 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/smallest-integer-divisible-by-k/) |

## Problem Description

### Goal

You are given a positive integer `k`. Find the length of the smallest positive integer `n` that is divisible by `k` and whose decimal representation contains only the digit `1`.

Return that length, or return `-1` if no such integer exists. The all-ones integer itself may be far too large for a signed 64-bit type, so the required result is its digit count rather than its numeric value.

### Function Contract

**Inputs**

- `k`: a positive divisor satisfying $1\le k\le10^5$.

**Return value**

- The length of the shortest positive all-ones decimal integer divisible by `k`, or `-1` if none exists.

### Examples

**Example 1**

- Input: `k = 1`
- Output: `1`
- Explanation: The one-digit integer `1` is divisible by `1`.

**Example 2**

- Input: `k = 2`
- Output: `-1`
- Explanation: An all-ones integer is odd and cannot be divisible by `2`.

**Example 3**

- Input: `k = 3`
- Output: `3`
- Explanation: `111` is divisible by `3`, while `1` and `11` are not.

### Required Complexity

- **Time:** $O(k)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reject impossible last digits:** Every positive integer containing only `1` is odd and does not end in `0` or `5`. Therefore, if `k` is divisible by `2` or `5`, no requested integer exists.

**Carry only the remainder:** Appending a digit `1` to a decimal integer transforms its remainder to `(remainder * 10 + 1) % k`. Start from zero and apply this update once per candidate length. When the remainder becomes zero, return the current length without ever constructing the potentially enormous integer.

**Why k iterations are sufficient:** There are only `k` possible remainders. When `k` has no factor `2` or `5`, the sequence of repunit remainders must reach zero within the first `k` lengths; otherwise a nonzero remainder would repeat and create a cycle that can never reach zero. The number-theoretic coprimality condition guarantees the zero remainder exists.

Testing lengths in increasing order makes the first zero remainder the smallest valid all-ones integer. The recurrence is exactly decimal append followed by modular reduction, so it preserves divisibility information at every step.

#### Complexity detail

At most $k$ remainder updates are performed, each using bounded modular arithmetic, for $O(k)$ time. Only the current remainder and length are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Materialize the repunit:** Repeatedly computing `value = value * 10 + 1` is correct in arbitrary-precision languages but makes arithmetic increasingly expensive and stores thousands of digits.
- **Track seen remainders:** A set can detect cycles explicitly, but uses $O(k)$ space even though the iteration bound already suffices.
- **Factor two or five:** Return `-1` immediately.
- **k equals one:** The first one-digit candidate succeeds.
- **Large answer:** Return its length; never serialize or store the full all-ones number.

</details>
