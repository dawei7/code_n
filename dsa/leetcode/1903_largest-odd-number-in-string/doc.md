# Largest Odd Number in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1903 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string/) |

## Problem Description

### Goal

`num` is the decimal representation of a positive integer that may be too large for ordinary numeric types. Choose a nonempty contiguous substring whose represented integer is odd, and among all such substrings return the one with the greatest numeric value.

Return the chosen digits as a string. If no substring represents an odd integer, return the empty string. The input contains no leading zero, although zeros may appear elsewhere.

### Function Contract

**Inputs**

- `num`: a digit string of length $n$, where $1 \le n \le 10^5$.
- `num` has no leading zero.

**Return value**

Return the largest-valued odd integer obtainable as a nonempty substring of `num`, represented as a string, or `""` when none exists.

### Examples

**Example 1**

- Input: `num = "52"`
- Output: `"5"`
- Explanation: `"5"` is the only odd-valued substring.

**Example 2**

- Input: `num = "4206"`
- Output: `""`
- Explanation: Every digit is even, so every substring ends in an even digit.

**Example 3**

- Input: `num = "35427"`
- Output: `"35427"`
- Explanation: The full input is already odd and is longer than every proper substring.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**An odd substring must end at an odd digit.** Decimal parity depends only on the final digit. Scan `num` from right to left to locate the last occurrence of `1`, `3`, `5`, `7`, or `9`. If none exists, no nonempty odd substring is possible.

**Use the entire prefix through that digit.** For a fixed odd ending position, starting at index zero yields at least as many digits as any later start. Because the original string has no leading zero, a longer decimal representation has a larger numeric value than every shorter one. Among odd ending positions, the rightmost one gives the longest prefix. Therefore `num[:index + 1]` at the first odd digit encountered from the right is globally optimal.

This argument uses only digit positions; converting the potentially $10^5$-digit input to an integer is unnecessary.

#### Complexity detail

The backward scan examines at most $n$ digits, and copying the returned prefix also takes at most $O(n)$ time, so total time is $O(n)$. The scan itself uses $O(1)$ auxiliary space. The returned string can contain $n$ characters, making total output-inclusive space $O(n)$.

#### Alternatives and edge cases

- **Enumerate every substring:** Testing and comparing all candidates requires at least quadratic enumeration and unnecessary large-string work.
- **Convert `num` to an integer:** The input may exceed fixed-width limits, and numeric conversion does not help locate the optimal substring.
- **All digits even:** Return `""`; zero is not odd.
- **Last digit odd:** Return the complete input immediately.
- **Only the first digit odd:** The answer is that one-character prefix.
- **Internal zeros:** They remain ordinary digits inside the selected prefix and do not affect parity unless one is last.

</details>
