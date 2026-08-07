## Description

You are given two strings, `source` and `target`.

You are also given a 2D string array `rules`, where $\text{rules}[i] = [\text{pattern}_{i}, \text{replacement}_{i}]$, and an integer array `costs`, where $\text{costs}[i]$ is the base cost of applying $\text{rules}[i]$. Both arrays have the same length. Additionally, $\text{pattern}_{i}$ and $\text{replacement}_{i}$ have the same length.

You may apply **any** rule **any** number of times. Each rule application works as follows:

- Choose an index `l` such that the range of positions from `l` to $l + \text{pattern}_{i}.length - 1$ exists in the current string and **none** of these positions has been used in a previous rule application.

- For each index `j`, the character $\text{pattern}_{i}[j]$ must either be **equal** to the current character at position $l + j$, or be `'*'`.

- Replace the characters in this range with $\text{replacement}_{i}$. The replacement is used **exactly** as given and does not contain wildcards.

- The cost of this rule application is $\text{costs}[i]$ **plus** the number of `'*'` characters in $\text{pattern}_{i}$.

- Once a character position has been used in a rule application, it **cannot** be used in any **later** rule application.

Since every $\text{pattern}_{i}$ and $\text{replacement}_{i}$ have the same length, character positions are preserved after every rule application.

Return the **minimum** total cost required to transform `source` into `target`. If it is impossible, return -1.
### Function Contract

**Inputs**

- `source`: The original lowercase English string.
- `target`: The desired lowercase English string, with the same length as `source`.
- `rules`: A nonempty array of `[pattern, replacement]` string pairs.
- `costs`: A positive base cost for each rule at the same index.

Each pattern and its replacement have equal length. A pattern contains lowercase English letters and `'*'` wildcards, including at least one letter and at most five wildcards; every replacement contains only lowercase English letters.

Let $n=\lvert\texttt{source}\rvert$, $R=\lvert\texttt{rules}\rvert$, and let $L$ be the maximum pattern length.

**Return value**

Return the minimum sum of application costs that transforms `source` into `target` using pairwise disjoint ranges. Each application's charge is its base cost plus its pattern's wildcard count. Return `-1` if the transformation is impossible.

### Examples
#### Example 1

<div class="example-block">
**Input:** source = "hello", target = "world", rules = [["he","wo"],["llo","rld"]], costs = [3,4]

**Output:** 7

**Explanation:**

- Apply $\text{rules}[0]$ to replace `"he"` with `"wo"` at cost 3, so the string becomes `"wollo"`.

- Apply $\text{rules}[1]$ to replace `"llo"` with `"rld"` at cost 4, so the string becomes `"world"`.

- The total cost is $3 + 4 = 7$.

</div>
#### Example 2

<div class="example-block">
**Input:** source = "cat", target = "dog", rules = [["c*t","dog"]], costs = [2]

**Output:** 3

**Explanation:**

- Apply $\text{rules}[0]$ to replace `"cat"` with `"dog"`. The wildcard `'*'` matches `'a'`, adding 1 to the base cost 2.

- The total cost is $2 + 1 = 3$.

</div>
#### Example 3

<div class="example-block">
**Input:** source = "test", target = "next", rules = [["*e*t","next"]], costs = [4]

**Output:** 6

**Explanation:**

- Apply $\text{rules}[0]$ to replace `"test"` with `"next"`. The first wildcard matches `'t'` and the second wildcard matches `'s'`, adding 2 to the base cost 4.

- The total cost is $4 + 2 = 6$.

</div>
#### Example 4

<div class="example-block">
**Input:** source = "ab", target = "bc", rules = [["a*","bd"]], costs = [9]

**Output:** -1

**Explanation:**

No sequence of rule applications can transform `source` into `target`, so the answer is -1.

</div>
### Constraints

- $1 \le \text{source.length} = \text{target.length} \le 5000$

- `source` and `target` consist of lowercase English letters.

- $1 \le \text{rules.length} = \text{costs.length} \le 200$

- $\text{rules}[i] = [\text{pattern}_{i}, \text{replacement}_{i}]$

- $1 \le \text{pattern}_{i}.length = \text{replacement}_{i}.length \le 20$

- $\text{pattern}_{i}$ contains at least one lowercase English letter and at most 5 `'*'` characters.

- $\text{replacement}_{i}$ contains only lowercase English letters.

- $1 \le \text{costs}[i] \le 1000$