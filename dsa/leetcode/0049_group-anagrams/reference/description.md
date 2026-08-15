### 1. Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

### 2. Function Contract

**Inputs**

- `strs`: An array of lowercase strings to classify by their letters.

Let $m = \lvert\texttt{strs}\rvert$ and let $C$ be the total number of characters across all strings.

**Return value**

Return groups in which every pair of strings are anagrams. The group order and the order within each group are unrestricted.

### 3. Examples

#### Example 1

- **Input:** strs = ["eat","tea","tan","ate","nat","bat"]

- **Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

- **Explanation:** 

- There is no string in strs that can be rearranged to form `"bat"`.

- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.

- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

#### Example 2

- **Input:** strs = [""]

- **Output:** [[""]]

#### Example 3

- **Input:** strs = ["a"]

- **Output:** [["a"]]

### 4. Constraints

- $1 \le \text{strs.length} \le 10^{4}$

- $0 \le \text{strs}[i].length \le 100$

- $\text{strs}[i]$ consists of lowercase English letters.
