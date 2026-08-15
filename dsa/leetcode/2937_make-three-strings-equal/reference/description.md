### 1. Description

You are given three strings: `s1`, `s2`, and `s3`. In one operation you can choose one of these strings and delete its **rightmost** character. Note that you **cannot** completely empty a string.

Return the *minimum number of operations* required to make the strings equal*. *If it is impossible to make them equal, return `-1`.

### 2. Function Contract

**Inputs**

- `s1`: Input parameter (`str`).
- `s2`: Input parameter (`str`).
- `s3`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** s1 = "abc", s2 = "abb", s3 = "ab"

- **Output:** 2

- **Explanation:** Deleting the rightmost character from both `s1` and `s2` will result in three equal strings.

#### Example 2

- **Input:** s1 = "dac", s2 = "bac", s3 = "cac"

- **Output:** -1

- **Explanation:** Since the first letters of `s1` and `s2` differ, they cannot be made equal.

### 4. Constraints

- $1 \le \text{s1.length}, \text{s2.length}, \text{s3.length} \le 100$

- `s1`, `s2` and `s3` consist only of lowercase English letters.
