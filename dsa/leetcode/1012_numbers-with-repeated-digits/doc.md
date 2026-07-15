# Numbers With Repeated Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1012 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/numbers-with-repeated-digits/) |

## Problem Description

### Goal

You are given a positive integer `n`. Consider every positive integer in the inclusive range `[1, n]` and its ordinary base-10 representation, without leading zeroes.

Return how many of those integers contain at least one repeated digit. A number qualifies when any decimal digit occurs in two or more positions; other digits may occur once or not at all. Count numbers, not the number of repeated positions within each number.

### Function Contract

**Inputs**

- `n`: the inclusive upper bound, where $1\le n\le10^9$.

Let $D$ be the number of decimal digits in `n`.

**Return value**

- The number of positive integers no greater than `n` that have at least one repeated decimal digit.

### Examples

**Example 1**

- Input: `n = 20`
- Output: `1`
- Explanation: Only `11` has a repeated digit.

**Example 2**

- Input: `n = 100`
- Output: `10`
- Explanation: The qualifying values are `11`, `22`, through `99`, plus `100`.

**Example 3**

- Input: `n = 1000`
- Output: `262`

### Required Complexity

- **Time:** $O(D^2)$
- **Space:** $O(D)$

<details>
<summary>Approach</summary>

#### General

**Count the complementary set:** Every positive integer either has a repeated digit or has all distinct digits. Count distinct-digit values no greater than `n`, then subtract that count from `n`.

**Count shorter lengths with permutations:** For a length $L<D$, the first digit has nine choices because it cannot be zero. Each later position chooses a different digit from the remaining pool, giving `9 * permutations(9, L - 1)` distinct-digit numbers.

**Follow the prefix of n:** Scan `n` left to right. At position `i`, try every smaller digit that is legal there and has not appeared in the fixed prefix. After choosing it, fill the remaining positions with ordered selections from unused digits. Then add the actual digit of `n` to the used set and continue. If that digit is already used, stop because no number with the exact prefix can remain distinct; if the entire scan succeeds, include `n` itself.

Every distinct-digit number is counted either in a shorter-length group or at the first position where it is smaller than `n`. These groups are disjoint, and the permutation factor fills every legal suffix exactly once. Subtracting their total therefore leaves precisely the numbers with a repeated digit.

#### Complexity detail

There are $D$ positions, at most ten candidate digits per position, and a permutation product over at most $D$ factors, giving $O(D^2)$ time. The used-digit set stores at most $D$ entries, so auxiliary space is $O(D)$.

#### Alternatives and edge cases

- **Digit dynamic programming:** Memoizing position, used-digit mask, and tightness is a general solution with $O(D2^{10})$ states.
- **Enumerate every integer:** Testing each decimal representation is correct but costs $O(nD)$ time.
- **Single-digit bound:** No positive one-digit number contains a repeated digit.
- **Repeated digit in n:** Stop the equal-prefix scan at its first repetition; smaller branches were already counted.
- **Leading zeroes:** They are not digits of a shorter number and must not consume the digit zero.

</details>
