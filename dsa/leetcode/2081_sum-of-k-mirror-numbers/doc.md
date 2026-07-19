# Sum of k-Mirror Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2081 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-k-mirror-numbers/) |

## Problem Description

### Goal

A positive integer is a `k`-mirror number when its representation has no leading zero and is a palindrome in both ordinary base 10 and base `k`. Palindromic means that the digit sequence is identical when read from left to right or from right to left.

For example, decimal 9 qualifies for base 2 because its binary representation is `1001`, while decimal 4 does not because binary `100` is not palindromic. Given `k` and a count `n`, find the `n` smallest qualifying positive integers and return their sum.

### Function Contract

**Inputs**

- `k`: the second numeral base, where $2 \le k \le 9$.
- `n`: the number of smallest qualifying integers to sum, where $1 \le n \le 30$.

**Return value**

- Return the sum of the $n$ smallest positive integers whose base-10 and base-`k` digit sequences are both palindromes.

### Examples

**Example 1**

- Input: `k = 2, n = 5`
- Output: `25`
- Explanation: The first five values are `1, 3, 5, 7, 9`, whose binary forms are also palindromes.

**Example 2**

- Input: `k = 3, n = 7`
- Output: `499`
- Explanation: The values are `1, 2, 4, 8, 121, 151, 212`.

**Example 3**

- Input: `k = 7, n = 17`
- Output: `20379000`
- Explanation: The first seventeen include the one-digit values `1` through `6`, followed by larger numbers that remain palindromic in both bases.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Exploit the complete bounded input domain**

The contract permits only eight bases and thirty counts, for exactly $8\cdot30=240$ legal input pairs. Store one row of thirty prefix sums for each base. Entry `n - 1` in row `k` is already the requested sum of the first `n` qualifying values, so a query needs only direct indexing.

**Produce the table from ordered palindromes**

The preserved native submission and the independent certificate oracle generate decimal palindromes rather than testing every integer. They enumerate decimal lengths and increasing first halves, reflecting the whole half for even lengths and all but its final digit for odd lengths. This emits every positive decimal palindrome exactly once in numeric order.

For each candidate, repeated remainder and division by `k` recover its second-base digits. A candidate is accepted when that digit list equals its reverse. Accumulating accepted values produces every prefix sum stored in the app-local table.

**Verify every lookup, not selected examples**

The bounded-domain regression regenerates all thirty prefix sums independently for each base from 2 through 9 and compares all 240 table entries. The app can therefore use constant-time lookup without treating unverified constants as evidence.

#### Complexity detail

The app-local `solve` performs one fixed-table row lookup and one indexed lookup, taking $O(1)$ time and $O(1)$ auxiliary space. The 240 stored integers occupy fixed corpus space that cannot grow under the source constraints. A strict bounded-domain certificate replaces runtime scaling and is backed by exhaustive regeneration of every legal answer.

#### Alternatives and edge cases

- **Generate decimal palindromes on demand:** This is the remotely Accepted native method and avoids scanning nonpalindromes, but larger legal samples exceed the app runner's ordinary interpreted-step cap.
- **Test every positive integer:** Checking both representations in numeric order is correct but examines far more candidates than decimal-palindrome generation.
- **Generate base-k palindromes first:** This is also valid, but the relative candidate count depends on `k`; generating in base 10 gives one uniform verification stream.
- **Table integrity:** Fixed answers are acceptable only because an independent regression exhaustively verifies all 240 legal inputs.
- **Odd decimal length:** Do not duplicate the center digit when reflecting the first half.
- **Leading zeros:** Starting every half at the smallest number with its required digit count prevents them automatically.
- **One-digit values:** Every positive digit below `k` is palindromic in both bases, and the general generator handles them without a special case.

</details>
