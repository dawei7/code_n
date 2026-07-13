# Count Numbers with Unique Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 357 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/count-numbers-with-unique-digits/) |

## Problem Description
### Goal
Given an integer `n` from `0` through `8`, consider every integer `x` in the half-open range $0 \le x < 10^{n}$. An integer has unique digits when no decimal digit repeats in its usual representation.

Return the number of integers in the range that have unique digits. Leading zeroes are not written and therefore are not extra repeated digits, while the integer `0` itself counts as a valid one-digit value. For $n = 0$, the range contains only the conventionally counted zero case and returns `1`. Count numerical values rather than fixed-width strings padded to `n` positions.

### Function Contract
**Inputs**

- `n`: the number of available decimal positions, with $0 \le n \le 8$

**Return value**

- The number of integers below $10^{n}$ with pairwise distinct decimal digits.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `91`

**Example 2**

- Input: `n = 0`
- Output: `1`

**Example 3**

- Input: `n = 1`
- Output: `10`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count numbers by their actual digit length**

Count valid numbers by their actual digit length. Zero is a special one-digit value and is included once. For any positive number of length `length`, the first digit has nine choices (`1` through `9`) because a leading zero is not part of a decimal representation.

For length two, the next digit has nine choices: zero is now allowed, but the chosen first digit is not. Every additional position has one fewer unused digit. The exact-length counts are therefore

- length 1: `9` positive numbers, plus zero;
- length 2: $9 \cdot 9$;
- length 3: $9 \cdot 9 \cdot 8$;
- and so on.

**Carry the permutation product forward**

Maintain the exact count for the current length. Starting at `9` for one-digit positive numbers, multiply by the number of available digits when extending to the next length, and add that exact count to the cumulative answer. This reuses the previous product instead of recomputing it.

**Trace the two-digit count**

For $n = 2$, the ten one-digit values are all valid. There are $9 \cdot 9 = 81$ valid two-digit values, giving $10 + 81 = 91$.

**Why every valid number is counted exactly once**

Every counted construction has a nonzero first digit and chooses each later digit only from unused digits, so it is valid. Conversely, every positive unique-digit number has one of the counted lengths, one of the nine possible leading digits, and exactly one sequence of subsequent unused-digit choices. The length groups are disjoint, so summing them counts every valid number once.

#### Complexity detail

The loop advances through at most `n` digit lengths and performs constant work per length, taking $O(n)$ time and $O(1)$ space. Under the stated bound $n \le 8$, resource use is also absolutely bounded.

#### Alternatives and edge cases

- **Enumerate and inspect every value:** takes exponential time in `n` because the range contains $10^{n}$ integers.
- **Backtrack over unused digits:** avoids invalid constructions but still explicitly visits every valid number.
- **Recompute each permutation product:** takes $O(n^2)$ arithmetic steps instead of extending the previous length's product.
- For $n = 0$, the range contains only zero and the answer is one.
- Zero may occur inside a multi-digit number but cannot be its leading digit.
- A decimal unique-digit number cannot exceed ten positions, although this problem restricts `n` to at most eight.

</details>
