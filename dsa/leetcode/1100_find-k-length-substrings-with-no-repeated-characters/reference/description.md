### 1. Description

Given a string `s` and an integer `k`, return *the number of substrings in *`s`* of length *`k`* with no repeated characters*.

### 2. Function Contract

**Inputs**

- `s`: a string of lowercase English letters.
- `k`: the exact required substring length.

For every start position where $s[start:start + k]$ has length `k`, test whether its $k$ characters are pairwise distinct. Overlapping substrings are separate candidates, and the same text occurring at different starts contributes once per occurrence.

**Return value**

Return the number of length-`k` substrings with no repeated character. Return zero if no complete window exists or if every complete window contains a repetition.

### 3. Examples

#### Example 1

- **Input:** `s = "havefunonleetcode", k = 5`
- **Output:** `6`
- **Explanation:** There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.

#### Example 2

- **Input:** `s = "home", k = 5`
- **Output:** `0`
- **Explanation:** Notice k can be larger than the length of s. In this case, it is not possible to find any substring.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of lowercase English letters.

- $1 \le k \le 10^{4}$
