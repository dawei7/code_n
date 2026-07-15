# Complement of Base 10 Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1009 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/complement-of-base-10-integer/) |

## Problem Description

### Goal

The complement of an integer is obtained from its binary representation by changing every `0` bit to `1` and every `1` bit to `0`. Only the written representation is complemented; leading zeroes outside its significant bits are not included.

Given a nonnegative integer `n`, return the base-10 value of its complement. For example, `5` is written as `101`, whose complement is `010`, representing `2`. The representation of zero is the single bit `0`, so its complement is `1`.

### Function Contract

**Inputs**

- `n`: an integer satisfying $0\le n<10^9$.

Let $B$ be the number of bits in the standard binary representation of `n`, taking $B=1$ when `n == 0`.

**Return value**

- The integer represented after flipping all $B$ bits of `n`.

### Examples

**Example 1**

- Input: `n = 5`
- Output: `2`
- Explanation: `101` becomes `010`.

**Example 2**

- Input: `n = 7`
- Output: `0`
- Explanation: `111` becomes `000`.

**Example 3**

- Input: `n = 10`
- Output: `5`
- Explanation: `1010` becomes `0101`.

### Required Complexity

- **Time:** $O(B)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Build a mask over exactly the significant bits:** Start with `mask = 1` and repeatedly shift it left while it is no greater than `n`. When the loop stops, `mask` is the first power of two larger than `n`; subtracting one produces $B$ consecutive `1` bits.

**Flip only the represented positions:** XOR `n` with `mask - 1`. A `1` in every mask position toggles the corresponding significant bit, while no higher position is touched. Thus `1010 XOR 1111` becomes `0101`.

**Give zero its one-bit representation:** For `n == 0`, the shifting loop would leave `mask - 1` equal to zero. Return `1` directly because the source representation is `0`, not an empty bit string.

The mask contains a `1` in precisely every position written in `n` and nowhere else. XOR therefore flips every required bit exactly once without introducing a leading complemented bit.

#### Complexity detail

The mask advances once per significant bit, taking $O(B)$ time. A constant number of integer variables gives $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Use the bit length directly:** `(1 << n.bit_length()) - 1` forms the mask compactly when the language exposes that operation.
- **Convert to a binary string:** Replacing characters is straightforward but allocates $O(B)$ additional space.
- **Recompute every positional power:** Building each complemented bit's value from scratch is correct but can take $O(B^2)$ time.
- **Zero:** Its one displayed bit flips from `0` to `1`.
- **All bits are one:** The complement is zero, as with `n = 7`.

</details>
