### 1. Description

You are given two strings `s` and `t`.

Return the **length** of the **longest common prefix** between `s` and `t` after removing **at most** one character from `s`.

### 2. Function Contract

- Refer to method signature.

### 3. Note

`s` can be left without any removal.

### 4. Examples

#### Example 1

- **Input:** s = "madxa", t = "madam"

- **Output:** 4

- **Explanation:** Removing $s[3]$ from `s` results in `"mada"`, which has a longest common prefix of length 4 with `t`.

#### Example 2

- **Input:** s = "leetcode", t = "eetcode"

- **Output:** 7

- **Explanation:** Removing $s[0]$ from `s` results in `"eetcode"`, which matches `t`.

#### Example 3

- **Input:** s = "one", t = "one"

- **Output:** 3

- **Explanation:** No removal is needed.

#### Example 4

- **Input:** s = "a", t = "b"

- **Output:** 0

- **Explanation:** `s` and `t` cannot have a common prefix.

### 5. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $1 \le \text{t.length} \le 10^{5}$

- `s` and `t` contain only lowercase English letters.
