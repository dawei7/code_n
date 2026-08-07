## Description

You are given an array of strings `message` and an array of strings `bannedWords`.

An array of words is considered **spam** if there are **at least** two words in it that **exactly** match any word in `bannedWords`.

Return `true` if the array `message` is spam, and `false` otherwise.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** message = ["hello","world","leetcode"], bannedWords = ["world","hello"]

**Output:** true

**Explanation:**

The words `"hello"` and `"world"` from the `message` array both appear in the `bannedWords` array.

</div>
#### Example 2

<div class="example-block">
**Input:** message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]

**Output:** false

**Explanation:**

Only one word from the `message` array (`"programming"`) appears in the `bannedWords` array.

</div>
### Constraints

- $1 \le \text{message.length}, \text{bannedWords.length} \le 10^{5}$

- $1 \le \text{message}[i].length, \text{bannedWords}[i].length \le 15$

- $\text{message}[i]$ and $\text{bannedWords}[i]$ consist only of lowercase English letters.