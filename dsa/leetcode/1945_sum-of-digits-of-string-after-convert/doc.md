# Sum of Digits of String After Convert

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1945 |
| Difficulty | Easy |
| Topics | String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/) |

## Problem Description
### Goal
You are given a lowercase English string `s` and an integer `k`. First replace
each letter by its one-based alphabet position: `a` becomes `1`, `b` becomes
`2`, and so on through `z`, which becomes `26`. Concatenate those decimal
representations to form the converted integer.

A transform replaces the current integer with the sum of its decimal digits.
Apply this transform exactly `k` times in total and return the resulting
integer. The first transform therefore sums every digit contributed by the
alphabet positions; each later transform sums the digits of the preceding
result.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $N$, where
  $1 \le N \le 100$.
- `k`: the number of digit-sum transforms, where $1 \le k \le 10$.

**Return value**

- The integer remaining after converting `s` and applying the digit-sum
  transform exactly `k` times.

### Examples
**Example 1**

- Input: `s = "iiii", k = 1`
- Output: `36`
- Explanation: The conversion is `9999`, whose digits sum to 36.

**Example 2**

- Input: `s = "leetcode", k = 2`
- Output: `6`
- Explanation: The first digit sum is 33, and the second is 6.

**Example 3**

- Input: `s = "zbax", k = 2`
- Output: `8`
- Explanation: The converted digits sum to 17, then to 8.

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Combine conversion with the first transform**

The converted decimal string never needs to be built. For a letter with
alphabet position $p$, its contribution to the first transform is the sum of
the decimal digits of $p$. Since $1 \le p \le 26$, that contribution is
`p // 10 + p % 10`. Add this value for every character in `s`.

This produces exactly the value after transform one: digit summation is
additive across the concatenated decimal representations, so treating each
letter's digits separately cannot change the total.

**Perform the remaining transforms**

Repeat a standard integer digit sum `k - 1` more times. At each step, extract
the last digit with `% 10`, add it, and remove it with `// 10`. Because the
first transform has already been included during the string scan, this loop
performs exactly the requested total of `k` transforms.

#### Complexity detail

The initial scan visits all $N$ characters once. Its result is at most $18N$,
so each of the at most nine remaining transforms examines only
$O(\log N)$ digits. Under the contract's fixed bound $k \le 10$, the total time
is $O(N)$ and the algorithm uses only a few integer variables, or $O(1)$
auxiliary space.

#### Alternatives and edge cases

- **Build the converted string:** Concatenate every alphabet position, convert
  the result to an integer, and sum its digits. This mirrors the statement but
  stores an unnecessary intermediate representation.
- **Repeated string conversion:** Convert the numeric result to text for every
  transform and sum its characters. It is concise, though integer arithmetic
  avoids repeated temporary strings.
- `k = 1` returns the per-letter digit total directly; no later transform
  should run.
- A position from 1 through 9 contributes one digit, while positions 10
  through 26 contribute the sum of two digits.
- Once a value is a single digit, any remaining transforms leave it unchanged.
- The input is nonempty, so the first transformed value is always positive.

</details>
