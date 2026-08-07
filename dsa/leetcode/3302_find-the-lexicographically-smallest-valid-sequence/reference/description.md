## Description

You are given two strings `word1` and `word2`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it *identical* to `y`.

A sequence of indices `seq` is called **valid** if:

- The indices are sorted in **ascending** order.

- *Concatenating* the characters at these indices in `word1` in **the same** order results in a string that is **almost equal** to `word2`.

Return an array of size `word2.length` representing the lexicographically smallest **valid** sequence of indices. If no such sequence of indices exists, return an **empty** array.

**Note** that the answer must represent the *lexicographically smallest array*, **not** the corresponding string formed by those indices.<!-- notionvc: 2ff8e782-bd6f-4813-a421-ec25f7e84c1e -->
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** word1 = "vbcca", word2 = "abc"

**Output:** [0,1,2]

**Explanation:**

The lexicographically smallest valid sequence of indices is `[0, 1, 2]`:

- Change $\text{word1}[0]$ to `'a'`.

- $\text{word1}[1]$ is already `'b'`.

- $\text{word1}[2]$ is already `'c'`.

</div>
#### Example 2

<div class="example-block">
**Input:** word1 = "bacdc", word2 = "abc"

**Output:** [1,2,4]

**Explanation:**

The lexicographically smallest valid sequence of indices is `[1, 2, 4]`:

- $\text{word1}[1]$ is already `'a'`.

- Change $\text{word1}[2]$ to `'b'`.

- $\text{word1}[4]$ is already `'c'`.

</div>
#### Example 3

<div class="example-block">
**Input:** word1 = "aaaaaa", word2 = "aaabc"

**Output:** []

**Explanation:**

There is no valid sequence of indices.

</div>
#### Example 4

<div class="example-block">
**Input:** word1 = "abc", word2 = "ab"

**Output:** [0,1]

</div>
### Constraints

- $1 \le \text{word2.length} < \text{word1.length} \le 3 * 10^{5}$

- `word1` and `word2` consist only of lowercase English letters.