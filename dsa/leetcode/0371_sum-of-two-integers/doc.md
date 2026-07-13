# Sum of Two Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 371 |
| Difficulty | Medium |
| Topics | Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-two-integers/) |

## Problem Description
### Goal
Given two signed integers `a` and `b`, compute their arithmetic sum under the problem's 32-bit two's-complement model. Positive and negative operands, zero, carries, and sign-bit behavior must all be handled consistently with that fixed width.

Return the signed integer result without using the arithmetic `+` or `-` operators to perform the addition. Combine bitwise sum and carry information until no carry remains, then interpret the fixed-width pattern as signed when its high bit is set. The task returns the sum only and does not require exposing intermediate binary representations.

### Function Contract
**Inputs**

- `a`: a signed integer
- `b`: a signed integer

**Return value**

- Their signed integer sum under the problem's 32-bit two's-complement model.

### Examples
**Example 1**

- Input: `a = 1, b = 2`
- Output: `3`

**Example 2**

- Input: `a = -1, b = 47`
- Output: `46`

**Example 3**

- Input: `a = -33, b = 22`
- Output: `-11`

### Required Complexity

- **Time:** $O(w)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate addition without carry from carry generation**

For each bit position, XOR produces the sum bit when no incoming carry is applied: equal bits become zero and different bits become one. AND identifies positions where both operands have one and therefore generate a carry; shifting that mask left moves each carry into the position where it must be added.

Replace the operands with `partial = a ^ b` and `carry = (a AND b) << 1`. Repeat until the carry is zero. Each round incorporates one layer of carries, so the remaining operand is then the complete sum.

**Constrain Python to 32-bit two's complement**

Python negative integers conceptually have infinitely many leading one bits, which would keep shifted carries alive. Mask both partial sums and carries with `0xFFFFFFFF` so every iteration operates on exactly 32 bits.

After carry propagation, values at most `0x7FFFFFFF` are already non-negative Python integers. A larger bit pattern represents a negative signed value. Invert its lower 32 bits with `~(value ^ mask)` to recover the corresponding Python negative integer.

**Why the loop preserves the intended sum**

At every bit position, XOR plus the shifted AND carry represents exactly the same binary total as the two previous operands; it merely separates non-carry bits from carry bits. Masking discards only overflow beyond the fixed 32-bit model. When no carry remains, the partial pattern is therefore the correct 32-bit sum, and the final conversion changes only its representation, not its bits.

#### Complexity detail

Let `w` be the fixed word width. A carry can move left through at most `w` positions, so the loop takes $O(w)$ time. For LeetCode's 32-bit integers, $w = 32$ is constant. Only a fixed number of integer masks is stored, giving $O(1)$ space.

#### Alternatives and edge cases

- **Bit-by-bit full adder:** explicitly tracks one carry through all 32 positions and has the same $O(w)$ bound.
- **Repeated bitwise increment or decrement:** avoids forbidden arithmetic operators but can take $O(|b|w)$ time.
- **Convert through strings or decimal digits:** adds representation overhead and avoids the intended bitwise reasoning.
- Adding zero leaves the other operand's bit pattern unchanged.
- Opposite signs may cancel to zero or leave either sign.
- Two negative operands require the final unsigned-to-signed conversion.
- Masking is essential in Python; fixed-width languages naturally discard bits beyond their integer width.

</details>
