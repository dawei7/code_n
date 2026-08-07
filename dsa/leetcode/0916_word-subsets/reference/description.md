### 1. Description

You are given two string arrays `words1` and `words2`.

A string `b` is a **subset** of string `a` if every letter in `b` occurs in `a` including multiplicity.

- For example, `"wrr"` is a subset of `"warrior"` but is not a subset of `"world"`.

A string `a` from `words1` is **universal** if for every string `b` in `words2`, `b` is a subset of `a`.

Return an array of all the **universal** strings in `words1`. You may return the answer in **any order**.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

**Output:** ["facebook","google","leetcode"]

</div>
#### Example 2

<div class="example-block">
**Input:** words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

**Output:** ["leetcode"]

</div>
#### Example 3

<div class="example-block">
**Input:** words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

**Output:** ["cccbb"]

</div>

### 4. Constraints

- $1 \le \text{words1.length}, \text{words2.length} \le 10^{4}$

- $1 \le \text{words1}[i].length, \text{words2}[i].length \le 10$

- $\text{words1}[i]$ and $\text{words2}[i]$ consist only of lowercase English letters.

- All the strings of `words1` are **unique**.