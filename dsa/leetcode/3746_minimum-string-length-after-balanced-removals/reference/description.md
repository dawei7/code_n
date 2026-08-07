### 1. Description

You are given a string `s` consisting only of the characters `'a'` and `'b'`.

You are allowed to repeatedly remove **any substring** where the number of `'a'` characters is equal to the number of `'b'` characters. After each removal, the remaining parts of the string are concatenated together without gaps.

Return an integer denoting the **minimum possible length** of the string after performing any number of such operations.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string containing only `a` and `b` characters.

A removable selection must be a contiguous substring of the current string and must contain equal counts of the two characters. After a removal, the surviving prefix and suffix become adjacent.

**Return value**

Return the smallest possible length of the string after any number of valid removals.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = `"aabbab"`

**Output:** 0

**Explanation:**

The substring `"aabbab"` has three `'a'` and three `'b'`. Since their counts are equal, we can remove the entire string directly. The minimum length is 0.

</div>
#### Example 2

<div class="example-block">
**Input:** s = `"aaaa"`

**Output:** 4

**Explanation:**

Every substring of `"aaaa"` contains only `'a'` characters. No substring can be removed as a result, so the minimum length remains 4.

</div>
#### Example 3

<div class="example-block">
**Input:** s = `"aaabb"`

**Output:** 1

**Explanation:**

First, remove the substring `"ab"`, leaving `"aab"`. Next, remove the new substring `"ab"`, leaving `"a"`. No further removals are possible, so the minimum length is 1.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $s[i]$ is either `'a'` or `'b'`.