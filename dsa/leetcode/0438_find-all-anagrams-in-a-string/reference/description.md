### 1. Description

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in **any order**.

### 2. Function Contract

**Inputs**

- `s`: The lowercase English text to search.
- `p`: The lowercase English pattern whose anagrams are required.

**Return value**

Return all zero-based start positions where the length-`len(p)` substring has exactly the same character
multiplicities as `p`. Any order is valid; the reviewed implementation produces increasing positions.

### 3. Examples

#### Example 1

- **Input:** `s = "cbaebabacd", p = "abc"`
- **Output:** `[0,6]`
- **Explanation:** The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

#### Example 2

- **Input:** `s = "abab", p = "ab"`
- **Output:** `[0,1,2]`
- **Explanation:** The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

### 4. Constraints

- $1 \le \text{s.length}, \text{p.length} \le 3 * 10^{4}$

- `s` and `p` consist of lowercase English letters.
