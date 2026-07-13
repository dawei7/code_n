# Add Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 258 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/add-digits/) |

## Problem Description
### Goal
Given a nonnegative integer `num`, repeatedly replace it with the sum of its decimal digits. Continue applying the same transformation to each multi-digit result until the value lies between `0` and `9`.

Return that final one-digit value, known as the digital root. The input `0` remains `0`, and no intermediate decimal digit may be omitted. Meet the constant-time, loop-free follow-up by using the number's modular pattern rather than constructing every intermediate digit sum, while still handling positive multiples of nine correctly as `9` rather than `0`.

### Function Contract
**Inputs**

- `num`: a nonnegative integer

**Return value**

The final one-digit digital root.

### Examples
**Example 1**

- Input: `num = 38`
- Output: `2`

**Example 2**

- Input: `num = 0`
- Output: `0`

**Example 3**

- Input: `num = 9999`
- Output: `9`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Decimal place values collapse modulo nine**

Because every decimal place value is congruent to one modulo nine, an integer and the sum of its digits have the same remainder modulo nine. Repeating the operation preserves that remainder.

The final digit is congruent to `num` modulo nine. For positive inputs it lies in `1..9`, so remainder zero maps to nine; zero remains the special result zero.

**The residue identifies one positive digit**

Digit summation preserves the value modulo nine until a single digit remains. For a positive input, exactly one value in `1..9` has the same residue: residue one through eight maps directly, while residue zero maps to nine. This is expressed uniformly as `1 + (num - 1) % 9`; zero is handled separately because it never enters the positive range.

#### Complexity detail

One comparison and constant-count arithmetic operations take $O(1)$ time and space.

#### Alternatives and edge cases

- **Simulate digit sums:** is correct but processes digits repeatedly rather than using the number-theoretic invariant.
- Zero must not be mapped to nine; positive multiples of nine must be.

</details>
