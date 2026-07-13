# Convert a Number to Hexadecimal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 405 |
| Difficulty | Easy |
| Topics | Math, String, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-a-number-to-hexadecimal/) |

## Problem Description
### Goal
Given a signed 32-bit integer `num`, convert its fixed-width bit pattern to hexadecimal. Positive values use their ordinary magnitude, while negative values must be interpreted through the full 32-bit two's-complement representation rather than prefixed with a minus sign.

Return lowercase hexadecimal digits `0-9` and `a-f` without unnecessary leading zeroes. Return exactly `"0"` for zero. A negative input produces the necessary eight hexadecimal digits representing all thirty-two bits. Do not use a built-in library method to perform the conversion directly; use fixed-width numeric operations so negative values retain the required two's-complement semantics.

### Function Contract
**Inputs**

- `num`: a signed 32-bit integer

**Return value**

- Return the lowercase hexadecimal digits without leading zeroes. Return `"0"` for zero; negative values must contain their full eight-digit two's-complement representation.

### Examples
**Example 1**

- Input: `num = 26`
- Output: `"1a"`

**Example 2**

- Input: `num = -1`
- Output: `"ffffffff"`

**Example 3**

- Input: `num = 0`
- Output: `"0"`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Normalize to the unsigned 32-bit pattern**

Mask `num` with `0xffffffff`. Positive values are unchanged, while a negative Python integer becomes the same finite 32-bit bit pattern used by fixed-width two's-complement arithmetic.

**Translate one low nibble at a time**

The lowest four bits form one hexadecimal digit from zero through fifteen. Use that value to index `"0123456789abcdef"`, append the character, and shift the working value right by four bits.

**Reverse the collected digits**

Low nibbles are extracted from least significant to most significant, so reverse the character list at the end. Stopping when the remaining value is zero omits leading zeroes naturally; handle original zero separately so its representation is not empty.

**Why negative values produce eight digits**

After masking, a negative signed value has a nonzero high bit in a 32-bit unsigned pattern. Exactly eight four-bit extractions consume all 32 bits. Each extraction preserves the remaining higher bits, so their reversed digits are precisely the standard two's-complement hexadecimal form.

#### Complexity detail

A 32-bit value contains at most eight hexadecimal digits, so the loop performs at most eight iterations and uses at most eight temporary characters. Both time and auxiliary space are $O(1)$ for the fixed-width contract.

#### Alternatives and edge cases

- **Repeated division by sixteen:** is equivalent for nonnegative values but still requires explicit two's-complement normalization for negatives.
- **Language formatting helpers:** are concise but bypass the intended bit conversion and may include prefixes or signed formatting.
- **Prepend immutable characters:** is harmless at eight digits but would copy repeatedly for an unbounded-width generalization.
- Zero must return one digit rather than an empty string.
- Values from zero through fifteen produce one hexadecimal digit.
- The minimum signed integer becomes `80000000`.
- No `0x` prefix or uppercase letters belong in the result.

</details>
