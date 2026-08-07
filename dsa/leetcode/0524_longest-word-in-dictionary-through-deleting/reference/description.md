### 1. Description

Given a string `s` and a string array `dictionary`, return *the longest string in the dictionary that can be formed by deleting some of the given string characters*. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]`
- **Output:** `"apple"`
#### Example 2

- **Input:** `s = "abpcplea", dictionary = ["a","b","c"]`
- **Output:** `"a"`

### 4. Constraints

- $1 \le \text{s.length} \le 1000$

- $1 \le \text{dictionary.length} \le 1000$

- $1 \le \text{dictionary}[i].length \le 1000$

- `s` and $\text{dictionary}[i]$ consist of lowercase English letters.