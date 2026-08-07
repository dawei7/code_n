## Description

A **valid encoding** of an array of `words` is any reference string `s` and array of indices `indices` such that:

- $\text{words.length} = \text{indices.length}$

- The reference string `s` ends with the `'#'` character.

- For each index $\text{indices}[i]$, the **substring** of `s` starting from $\text{indices}[i]$ and up to (but not including) the next `'#'` character is equal to $\text{words}[i]$.

Given an array of `words`, return *the **length of the shortest reference string** *`s`* possible of any **valid encoding** of *`words`*.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $words = ["time", "me", "bell"]$
- **Output:** `10`
- **Explanation:** A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "<u>time</u>#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "ti<u>me</u>#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#<u>bell</u>#"
#### Example 2

- **Input:** $words = ["t"]$
- **Output:** `2`
- **Explanation:** A valid encoding would be s = "t#" and indices = [0].
### Constraints

- $1 \le \text{words.length} \le 2000$

- $1 \le \text{words}[i].length \le 7$

- $\text{words}[i]$ consists of only lowercase letters.