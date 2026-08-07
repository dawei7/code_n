## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.
### Function Contract

**Inputs**

- `strs`: The array of lowercase strings to compare.

**Return value**

Return the longest common prefix, or `""` when no non-empty prefix is shared.

### Examples
#### Example 1

- **Input:** $strs = ["flower","flow","flight"]$
- **Output:** `"fl"`
#### Example 2

- **Input:** $strs = ["dog","racecar","car"]$
- **Output:** `""`
- **Explanation:** There is no common prefix among the input strings.
### Constraints

- $1 \le \text{strs.length} \le 200$

- $0 \le \text{strs}[i].length \le 200$

- $\text{strs}[i]$ consists of only lowercase English letters if it is non-empty.