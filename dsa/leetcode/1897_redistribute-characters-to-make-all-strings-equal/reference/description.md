## Description

You are given an array of strings `words` (**0-indexed**).

In one operation, pick two **distinct** indices `i` and `j`, where $\text{words}[i]$ is a non-empty string, and move **any** character from $\text{words}[i]$ to **any** position in $\text{words}[j]$.

Return `true` *if you can make** every** string in *`words`* **equal **using **any** number of operations*,* and *`false` *otherwise*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $words = ["abc","aabc","bc"]$
- **Output:** `true`
- **Explanation:** Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.
#### Example 2

- **Input:** $words = ["ab","a"]$
- **Output:** `false`
- **Explanation:** It is impossible to make all the strings equal using the operation.
### Constraints

- $1 \le \text{words.length} \le 100$

- $1 \le \text{words}[i].length \le 100$

- $\text{words}[i]$ consists of lowercase English letters.