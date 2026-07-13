# Reverse Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 190 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Divide and Conquer, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-bits/) |

## Problem Description
### Goal
Given a 32-bit unsigned integer `n`, view it as exactly thirty-two binary positions, including any leading zero bits that are normally omitted from its written representation. Reverse the complete bit sequence so the least significant original bit becomes the most significant result bit and vice versa.

Return the unsigned integer represented by those reversed thirty-two bits. Do not reverse decimal digits or stop at the highest set bit, because leading zeroes can become meaningful trailing positions and trailing zeroes can become high-value bits. An all-zero input remains zero, and applying the same fixed-width reversal twice restores the original value.

### Function Contract
**Inputs**

- `n`: a 32-bit unsigned integer

**Return value**

The unsigned integer represented by the reversed 32-bit sequence.

### Examples
**Example 1**

- Input: `43261596`
- Output: `964176192`

**Example 2**

- Input: `0`
- Output: `0`

**Example 3**

- Input: `1`
- Output: `2147483648`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

The width is part of the value: this is not reversal of the shortest binary spelling, but reversal of exactly 32 bit positions. Begin with result zero and repeat exactly 32 times:

1. Shift the current result left by one position.
2. Copy the input's least-significant bit into the opened position using $n \mathbin{\&} 1$.
3. Shift the input right to expose its next bit.

For input $1$, the first iteration copies the lone set bit. The remaining $31$ iterations append zeroes on the right of the growing result, moving that bit all the way to position $31$ and producing $2^{31}$. Stopping when the input becomes zero would incorrectly return $1$ instead.

After `i` iterations, the low `i` input bits have been consumed, and the result's low `i`-bit sequence is those bits in reverse consumption order. The remaining shifts give that sequence its final placement within the fixed 32-bit output.

At iteration `i` (starting from zero), $n \mathbin{\&} 1$ reads original input bit `i`. The result shift and append make that bit the newest low bit; over the remaining iterations it is shifted left exactly $31 - i$ more times, ending at output position $31 - i$. Thus every input position maps to its required mirrored output position. All 32 positions are processed exactly once, so the final integer is the complete bit reversal.

#### Complexity detail

The loop performs exactly 32 iterations, a constant independent of the numeric value, so time is $O(1)$ under the fixed-width contract. The result, input working value, and counter use $O(1)$ space.

#### Alternatives and edge cases

- Converting to a zero-padded 32-character binary string is readable but allocates additional storage and relies on formatting.
- A sequence of mask-and-swap operations can reverse 16-bit, 8-bit, 4-bit, 2-bit, and 1-bit groups efficiently, which is useful for repeated low-level operations but less transparent.
- Stopping when $n = 0$ loses the fixed-width placement unless the result is shifted for every remaining position.
- Zero and the all-ones 32-bit value are unchanged. Input one becomes `2147483648`.
- Languages with signed right shift must treat the input as unsigned or use a logical shift.

</details>
