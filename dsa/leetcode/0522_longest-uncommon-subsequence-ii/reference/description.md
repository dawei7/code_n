### 1. Description

Given an array of strings `strs`, return *the length of the **longest uncommon subsequence** between them*. If the longest uncommon subsequence does not exist, return `-1`.

An **uncommon subsequence** between an array of strings is a string that is a **subsequence of one string but not the others**.

A **subsequence** of a string `s` is a string that can be obtained after deleting any number of characters from `s`.

- For example, `"abc"` is a subsequence of `"aebdc"` because you can delete the underlined characters in `"a<u>e</u>b<u>d</u>c"` to get `"abc"`. Other subsequences of `"aebdc"` include `"aebdc"`, `"aeb"`, and `""` (empty string).

### 2. Function Contract

**Inputs**

- `strs`: Input parameter (`List[str]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $strs = ["aba","cdc","eae"]$
- **Output:** `3`

#### Example 2

- **Input:** $strs = ["aaa","aaa","aa"]$
- **Output:** `-1`

### 4. Constraints

- $2 \le \text{strs.length} \le 50$

- $1 \le \text{strs}[i].length \le 10$

- $\text{strs}[i]$ consists of lowercase English letters.
