# Prime Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 866 |
| Difficulty | Medium |
| Topics | Math, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/prime-palindrome/) |

## Problem Description
### Goal
Given an integer `n`, find the smallest integer greater than or equal to `n` that is both prime and a palindrome. A prime has exactly two positive divisors, `1` and itself; in particular, `1` is not prime. A palindrome has the same decimal digit sequence when read from left to right or right to left.

Return the first integer satisfying both properties. The tests guarantee that an answer exists between `2` and $2\cdot10^8$, inclusive, while the input itself satisfies $1 \leq n \leq 10^8$.

### Function Contract
**Inputs**

- `n`: the inclusive lower bound for the search, where $1 \leq n \leq 10^8$.

Let $A$ denote the returned prime palindrome. For `n > 11`, let $P$ be the number of odd-length palindrome candidates generated from the starting decimal prefix through $A$, including any first candidate that falls just below `n`.

**Return value**

Return the smallest prime palindrome $A$ such that $A\geq n$.

### Examples
**Example 1**

- Input: `n = 6`
- Output: `7`

**Example 2**

- Input: `n = 8`
- Output: `11`

**Example 3**

- Input: `n = 13`
- Output: `101`

Every two-digit palindrome after `11` is composite, so the search continues to `101`.

### Required Complexity
- **Time:** $O(P\sqrt{A})$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Skip even-length palindromes after eleven**

The alternating sum of the decimal digits of every even-length palindrome is zero, so the divisibility rule for `11` shows that `11` divides it. The only even-length palindrome that is itself prime is `11`. Handle the small prime palindromes `2`, `3`, `5`, `7`, and `11` directly; for larger lower bounds, only odd-length palindromes need to be generated.

**Generate palindromes from their left half**

An odd-length palindrome is determined by a prefix containing its left half and middle digit. Starting from the leading half of `n` when `n` has odd length—or the smallest prefix of the next odd length when `n` has even length—mirror every prefix except its final digit. For example, prefix `123` becomes `12321`.

Increasing the prefix produces odd-length palindromes in strictly increasing order, including the transition from one odd digit length to the next. Ignore a first generated value below `n`; the first generated candidate at least `n` that is prime must be the smallest possible answer because no intervening odd-length palindrome was skipped and all larger even-length palindromes are composite.

**Test primality only for generated candidates**

Reject values below `2` and even values other than `2`. For an odd candidate, test odd divisors through its square root. If no such divisor exists, any nontrivial factorization would require both factors to exceed the square root, which is impossible; the candidate is prime and can be returned.

#### Complexity detail

For `n > 11`, exactly $P$ generated palindromes are tested. Trial division uses at most $O(\sqrt A)$ checks for any candidate no larger than the answer $A$, giving $O(P\sqrt A)$ time. Decimal digit counting, numeric mirroring, and primality testing retain only a fixed number of integer variables, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Check every integer from `n`:** This is correct, but it wastes work on the overwhelmingly many values that are not palindromes.
- **Restart palindrome prefixes at one:** It avoids non-palindromes but still regenerates every smaller odd-length palindrome instead of jumping to the leading half of `n`.
- **Convert each integer to text before primality testing:** Palindrome recognition is simple, yet scanning the entire numeric gap can dominate the generated-candidate method.
- **Generate both odd- and even-length palindromes:** It is unnecessary after `11` because every longer even-length palindrome has factor `11`.
- **Treat `1` as prime:** This violates the definition; the smallest possible answer is `2`.
- **Input is already a prime palindrome:** The first candidate equals `n` and is returned unchanged.
- **Input has even digit length:** The search begins with the smallest palindrome of the next odd length, except for the separately handled value `11`.
- **Composite palindrome:** Palindromic form alone is insufficient; values such as `121` must fail trial division.
- **Large answer:** Numeric construction avoids building or storing a list of all earlier palindromes.

</details>
