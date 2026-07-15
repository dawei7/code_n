# Binary String With Substrings Representing 1 To N

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1016 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/) |

## Problem Description

### Goal

You are given a binary string `s` and a positive integer `n`. For every integer in the inclusive range `[1, n]`, write its standard binary representation without leading zeroes.

Return `true` if each of those representations occurs in `s` as a substring; otherwise return `false`. A substring must occupy contiguous character positions, although different required representations may overlap or occur at the same region of `s`.

### Function Contract

**Inputs**

- `s`: a binary string of length $M$, where $1\le M\le1000$.
- `n`: a positive upper bound satisfying $1\le n\le10^9$.

Let $L=\lfloor\log_2 n\rfloor+1$ be the bit length of `n`.

**Return value**

- `True` exactly when every standard binary representation from `1` through `n` is a substring of `s`.

### Examples

**Example 1**

- Input: `s = "0110", n = 3`
- Output: `True`
- Explanation: The representations `1`, `10`, and `11` all occur contiguously.

**Example 2**

- Input: `s = "0110", n = 4`
- Output: `False`
- Explanation: The representation `100` does not occur.

**Example 3**

- Input: `s = "1111000101", n = 5`
- Output: `True`
- Explanation: The string contains `1`, `10`, `11`, `100`, and `101`.

### Required Complexity

- **Time:** $O(ML)$
- **Space:** $O(\min(n,ML))$

<details>
<summary>Approach</summary>

#### General

**Enumerate only relevant substring lengths:** No required representation is longer than $L$. For each start position containing `1`, extend an end position at most $L$ characters, updating `value = value * 2 + bit` instead of reparsing the substring.

**Record required values:** Whenever the accumulated value is at most `n`, add it to a set. Once it exceeds `n`, every longer extension remains too large because appending a bit multiplies the positive value by two and adds zero or one, so that start can stop early.

**Compare coverage with the required count:** The set contains only integers from `1` through `n`. Therefore, all required representations occurred exactly when its size is `n`. Starting only at a `1` respects standard binary representations and avoids treating a leading-zero spelling as a separate candidate.

Every qualifying substring is enumerated from its first through last character, so its value enters the set. Conversely, every stored value comes from a contiguous substring and lies in the required range. The final cardinality test is thus equivalent to complete coverage.

#### Complexity detail

At most $L$ extensions are examined from each of the $M$ starts, giving $O(ML)$ time. At most $ML$ discoveries and no more than $n$ distinct required values can be stored, so space is $O(\min(n,ML))$.

#### Alternatives and edge cases

- **Search for every binary representation:** Testing `bin(value)` for each value through `n` is simple but can take $O(nML)$ time with direct substring matching.
- **Check only the upper half:** If every value above $n/2$ occurs, smaller representations follow as prefixes of doubled values; this reduces the count but still performs many substring searches.
- **Single required value:** For `n == 1`, the answer is whether `s` contains `1`.
- **Leading zeroes:** Required representations never start with zero, even though `s` may contain zeroes.
- **Huge n and short s:** The set cannot reach size `n`, so the method returns false without iterating through the enormous numeric range.

</details>
