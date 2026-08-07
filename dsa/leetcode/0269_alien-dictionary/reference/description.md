## Description

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are **sorted lexicographically** by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `"".`

Otherwise, return *a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by the new language's rules**. *If there are multiple solutions, return* **any of them***.
### Function Contract

**Inputs**

- `words`: Dictionary words claimed to be in alien lexicographic order.

Let $c$ be the total number of characters across all words, $a$ the number of distinct letters, and $e$ the number of
distinct precedence edges inferred from adjacent words.

**Return value**

Return any valid order of all distinct letters found in `words`, or `""` if the supplied word order is impossible.

### Examples

#### Example 1

- **Input:** $words = ["wrt","wrf","er","ett","rftt"]$
- **Output:** `"wertf"`
#### Example 2

- **Input:** $words = ["z","x"]$
- **Output:** `"zx"`
#### Example 3

- **Input:** $words = ["z","x","z"]$
- **Output:** `""`
- **Explanation:** The order is invalid, so return "".
### Constraints

- $1 \le \text{words.length} \le 100$

- $1 \le \text{words}[i].length \le 100$

- $\text{words}[i]$ consists of only lowercase English letters.