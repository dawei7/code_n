### 1. Description

You are given a string array `words` and a **binary** array `groups` both of length `n`.

A subsequence of `words` is **alternating** if for any two *consecutive* strings in the sequence, their corresponding elements at the *same* indices in `groups` are **different** (that is, there *cannot* be consecutive 0 or 1).

Your task is to select the **longest alternating** subsequence from `words`.

Return *the selected subsequence. If there are multiple answers, return **any** of them.*

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).
- `groups`: Input parameter (`List[int]`).

**Return value**

- Returns `List[str]`.

### 3. Note

The elements in `words` are distinct.

### 4. Examples

#### Example 1

- **Input:** words = ["e","a","b"], groups = [0,0,1]

- **Output:** ["e","b"]

- **Explanation:** A subsequence that can be selected is `["e","b"]` because $\text{groups}[0] \neq \text{groups}[2]$. Another subsequence that can be selected is `["a","b"]` because $\text{groups}[1] \neq \text{groups}[2]$. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is `2`.

#### Example 2

- **Input:** words = ["a","b","c","d"], groups = [1,0,1,1]

- **Output:** ["a","b","c"]

- **Explanation:** A subsequence that can be selected is `["a","b","c"]` because $\text{groups}[0] \neq \text{groups}[1]$ and $\text{groups}[1] \neq \text{groups}[2]$. Another subsequence that can be selected is `["a","b","d"]` because $\text{groups}[0] \neq \text{groups}[1]$ and $\text{groups}[1] \neq \text{groups}[3]$. It can be shown that the length of the longest subsequence of indices that satisfies the condition is `3`.

### 5. Constraints

- $1 \le n = \text{words.length} = \text{groups.length} \le 100$

- $1 \le \text{words}[i].length \le 10$

- $\text{groups}[i]$ is either `0` or `1.`

- `words` consists of **distinct** strings.

- $\text{words}[i]$ consists of lowercase English letters.
