# Number of 1 Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 191 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Divide and Conquer, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-1-bits/) |

## Problem Description
### Goal
Given a 32-bit unsigned integer, inspect its fixed-width binary representation and count the positions whose bit value is `1`. This count is also known as the population count or Hamming weight of the integer.

Return the number of set bits as an integer between `0` and `32`. Leading zero positions are part of the representation but add nothing, and the task counts bits rather than runs of adjacent ones or decimal digits. Zero therefore returns `0`, while the value with all thirty-two positions set returns `32`; the input is interpreted as unsigned throughout.

### Function Contract
**Inputs**

- `n`: a 32-bit unsigned integer

**Return value**

The number of bit positions containing one.

### Examples
**Example 1**

- Input: `11`
- Output: `3`

**Example 2**

- Input: `128`
- Output: `1`

**Example 3**

- Input: `2147483645`
- Output: `30`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Brian Kernighan's bit trick removes one set bit per iteration:

$n = n \mathbin{\&} (n - 1)$.

To see why, write the suffix of any nonzero value through its least-significant one as `...1000...0`. Subtracting one changes that suffix to `...0111...1`: the lowest one becomes zero and every lower zero becomes one. ANDing with the original clears the changed low region while leaving every higher bit untouched. Exactly the least-significant set bit disappears.

Increment a counter each time this operation is performed and stop when `n` becomes zero. For `11`, whose binary form is `1011`, the values progress `1011 -> 1010 -> 1000 -> 0000`, so the counter reaches three.

Unlike checking every bit position, the loop count depends on the population count. Sparse inputs such as powers of two finish after one iteration, though the fixed 32-bit width makes both strategies constant in the asymptotic notation requested here.

Each iteration clears exactly one set bit and does not change any other set bit. After `c` iterations, exactly `c` original one-bits have been removed, and all remaining one-bits are still present in the working value. The loop terminates precisely when none remain, so the counter equals the original number of set bits.

#### Complexity detail

If the input contains `b` set bits, the loop takes $O(b)$ operations. Because $b \le 32$ under the fixed-width contract, this is $O(1)$ time. The working integer and counter use $O(1)$ space.

#### Alternatives and edge cases

- Testing a mask at all 32 positions is simple and has the same fixed-width asymptotic bound, but always performs 32 checks.
- Binary-string conversion followed by counting is concise but allocates a representation.
- Byte lookup tables can accelerate large batches at the cost of preprocessing or static storage.
- Zero performs no iterations and returns zero; a power of two returns one; $2^{32} - 1$ returns 32.
- Signed-language implementations should preserve the intended unsigned 32-bit representation.

</details>
