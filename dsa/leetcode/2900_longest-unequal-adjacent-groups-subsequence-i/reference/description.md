## Description

You are given a string array `words` and a **binary** array `groups` both of length `n`.

A subsequence of `words` is **alternating** if for any two *consecutive* strings in the sequence, their corresponding elements at the *same* indices in `groups` are **different** (that is, there *cannot* be consecutive 0 or 1).

Your task is to select the **longest alternating** subsequence from `words`.

Return *the selected subsequence. If there are multiple answers, return **any** of them.*

**Note:** The elements in `words` are distinct.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
**Input:** words = ["e","a","b"], groups = [0,0,1]

**Output:** ["e","b"]

**Explanation:** A subsequence that can be selected is `["e","b"]` because $\text{groups}[0] \neq \text{groups}[2]$. Another subsequence that can be selected is `["a","b"]` because $\text{groups}[1] \neq \text{groups}[2]$. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is `2`.

</div>
#### Example 2

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
**Input:** words = ["a","b","c","d"], groups = [1,0,1,1]

**Output:** ["a","b","c"]

**Explanation:** A subsequence that can be selected is `["a","b","c"]` because $\text{groups}[0] \neq \text{groups}[1]$ and $\text{groups}[1] \neq \text{groups}[2]$. Another subsequence that can be selected is `["a","b","d"]` because $\text{groups}[0] \neq \text{groups}[1]$ and $\text{groups}[1] \neq \text{groups}[3]$. It can be shown that the length of the longest subsequence of indices that satisfies the condition is `3`.

</div>
### Constraints

- $1 \le n = \text{words.length} = \text{groups.length} \le 100$

- $1 \le \text{words}[i].length \le 10$

- $\text{groups}[i]$ is either `0` or `1.`

- `words` consists of **distinct** strings.

- $\text{words}[i]$ consists of lowercase English letters.