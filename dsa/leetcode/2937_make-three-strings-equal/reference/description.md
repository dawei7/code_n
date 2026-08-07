### 1. Description

You are given three strings: `s1`, `s2`, and `s3`. In one operation you can choose one of these strings and delete its **rightmost** character. Note that you **cannot** completely empty a string.

Return the *minimum number of operations* required to make the strings equal*. *If it is impossible to make them equal, return `-1`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **s1 = "abc", s2 = "abb", s3 = "ab"

**Output: **2

**Explanation: **Deleting the rightmost character from both `s1` and `s2` will result in three equal strings.

</div>
#### Example 2

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **s1 = "dac", s2 = "bac", s3 = "cac"

**Output: **-1

**Explanation:** Since the first letters of `s1` and `s2` differ, they cannot be made equal.

</div>

### 4. Constraints

- $1 \le \text{s1.length}, \text{s2.length}, \text{s3.length} \le 100$

- `s1`, `s2` and `s3` consist only of lowercase English letters.