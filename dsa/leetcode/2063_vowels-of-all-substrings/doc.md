# Vowels of All Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2063 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/vowels-of-all-substrings/) |

## Problem Description

### Goal

For every nonempty contiguous substring of a lowercase English string `word`, count how many of its characters are vowels: `a`, `e`, `i`, `o`, or `u`. Return the sum of those counts over all substrings. If one vowel occurrence belongs to several index ranges, include it once for each such substring.

The result can exceed the range of a signed 32-bit integer, so calculations must preserve the full integer value.

### Function Contract

**Inputs**

- `word`: a lowercase English string of length $n$, where $1 \le n \le 10^5$.

**Return value**

- Return the total number of vowel occurrences counted across every nonempty substring of `word`.

### Examples

**Example 1**

- Input: `word = "aba"`
- Output: `6`
- Explanation: Across `"a"`, `"ab"`, `"aba"`, `"b"`, `"ba"`, and `"a"`, the vowel counts sum to $6$.

**Example 2**

- Input: `word = "abc"`
- Output: `3`
- Explanation: The first `a` occurs in `"a"`, `"ab"`, and `"abc"`.

**Example 3**

- Input: `word = "ltcd"`
- Output: `0`
- Explanation: No substring contains a vowel because the string has none.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reverse the order of counting**

Enumerating substrings repeats the same work. Instead, consider one vowel occurrence at index $i$ and count how many substrings include that position. The left endpoint has $i+1$ choices, from index $0$ through $i$, while the right endpoint has $n-i$ choices, from $i$ through index $n-1$.

**Add each occurrence's contribution**

The vowel at index $i$ therefore contributes

$$
(i+1)(n-i)
$$

to the requested sum. Scan the string and add this product only when the current character is a vowel.

Each pair of substring boundaries contributes once for every vowel position it encloses. The contribution formula counts exactly those boundary pairs for one position, so summing it over vowel positions counts the same `(substring, vowel occurrence)` pairs as the original definition, without constructing any substring.

#### Complexity detail

The algorithm inspects each of the $n$ characters once and performs constant work per character, for $O(n)$ time. The vowel membership test and accumulated total require $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate all substrings:** Maintaining a running vowel count for each start avoids recounting characters, but still requires $O(n^2)$ time.
- **Ending-at dynamic total:** Track the vowel count summed over all substrings ending at each index and add those totals; this also achieves $O(n)$ time.
- A vowel at either endpoint still participates in many substrings; its contribution is not merely one.
- Repeated vowels are distinct occurrences and each makes its own contribution.
- A string with no vowels returns zero, while a one-character vowel returns one.
- The maximum result requires an integer type wider than signed 32 bits in languages with fixed-width integers.

</details>
