### 1. Description

Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The **frequency** of a character is the number of times it appears in the string.

Return *the sorted string*. If there are multiple answers, return *any of them*.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string of uppercase English letters, lowercase English letters, and digits.

**Return value**

- Return a permutation of `s` whose character groups appear in nonincreasing order of frequency. Groups with equal frequencies may appear in any relative order.

Uppercase and lowercase forms are distinct characters.

### 3. Examples

#### Example 1

- **Input:** `s = "tree"`
- **Output:** `"eert"`
- **Explanation:** 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

#### Example 2

- **Input:** `s = "cccaaa"`
- **Output:** `"aaaccc"`
- **Explanation:** Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

#### Example 3

- **Input:** `s = "Aabb"`
- **Output:** `"bbAa"`
- **Explanation:** "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

### 4. Constraints

- $1 \le \text{s.length} \le 5 * 10^{5}$

- `s` consists of uppercase and lowercase English letters and digits.
