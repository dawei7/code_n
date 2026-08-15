### 1. Description

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string of uppercase English letters.
- `k`: The maximum number of character replacements allowed.

**Return value**

Return the greatest length of a contiguous substring that can be transformed into repetitions of one letter using
at most `k` replacements.

### 3. Examples

#### Example 1

- **Input:** `s = "ABAB", k = 2`
- **Output:** `4`
- **Explanation:** Replace the two 'A's with two 'B's or vice versa.

#### Example 2

- **Input:** `s = "AABABBA", k = 1`
- **Output:** `4`
- **Explanation:** Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of only uppercase English letters.

- $0 \le k \le \text{s.length}$
