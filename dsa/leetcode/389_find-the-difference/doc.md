# Find the Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 389 |
| Difficulty | Easy |
| Topics | Hash Table, String, Bit Manipulation, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-difference/) |

## Problem Description
### Goal
Given a lowercase string `s`, string `t` was formed by adding exactly one character occurrence to `s` and then shuffling all occurrences. Repeated letters may be present in either string, and the added character may equal a character already present.

Return the extra character occurrence. Comparing only sets is insufficient because multiplicity identifies the difference, while original positions provide no information after shuffling. The guarantee ensures exactly one answer and `len(t) = len(s) + 1`. When `s` is empty, return the sole character of `t`; the function returns a character rather than its index.

### Function Contract
**Inputs**

- `s`: the original lowercase string
- `t`: a permutation of all characters in `s` plus one extra lowercase character

**Return value**

- Return the character occurrence that was added to form `t`.

### Examples
**Example 1**

- Input: `s = "abcd", t = "abcde"`
- Output: `"e"`

**Example 2**

- Input: `s = "", t = "y"`
- Output: `"y"`

**Example 3**

- Input: `s = "aabb", t = "ababa"`
- Output: `"a"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Cancel matching character occurrences**

Initialize an integer accumulator to zero. XOR it with the code point of every character in `s` and every character in `t`. XOR is associative and commutative, so the shuffled order has no effect on the final value.

**Duplicates cancel by multiplicity**

Every occurrence contributed by `s` has one corresponding occurrence in `t`. Pairing equal code points makes each pair vanish because $x \oplus x = 0$. This remains true when a character appears many times: all matched occurrences can be paired independently.

**Why only the added character remains**

After all paired occurrences cancel, the accumulator is `0 ^ extra`, which equals the extra character's code point. Converting that code point back to a character therefore returns exactly the occurrence added to `t`.

#### Complexity detail

If `s` has length `n`, then `t` has length $n + 1$. Scanning both strings takes $O(n)$ time. The accumulator uses $O(1)$ space.

#### Alternatives and edge cases

- **Fixed frequency array:** increment for `s` and decrement for `t`, then locate the unmatched count; it is also linear with constant lowercase-alphabet space.
- **Character-code sum difference:** is linear and concise, but XOR avoids relying on a potentially overflowing numeric sum in fixed-width languages.
- **Sort and compare:** reveals the first mismatch in $O(n \log n)$ time.
- **Match each occurrence by scanning unused positions:** is correct but can take $O(n^2)$ time.
- If `s` is empty, the only character in `t` is the answer.
- The extra character may equal characters already present in `s`.
- The extra occurrence can appear anywhere after shuffling.
- Repeated letters must cancel occurrence by occurrence.

</details>
