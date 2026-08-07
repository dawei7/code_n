### 1. Description

You are given a string `s` consisting of lowercase English letters.

A **substring** of `s` is called **balanced** if all **distinct** characters in the **substring** appear the **same** number of times.

Return the **length** of the **longest balanced substring** of `s`.

### 2. Function Contract

**Inputs**

- `s`: A lowercase English string.

A substring must occupy one contiguous interval of `s`. Only characters present in that interval are compared; absent alphabet letters do not need to have the same frequency.

**Return value**

Return the maximum length among all balanced substrings. Any non-empty one-character substring is balanced, so the result is always at least `1`.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "abbac"

**Output:** 4

**Explanation:**

The longest balanced substring is `"abba"` because both distinct characters `'a'` and `'b'` each appear exactly 2 times.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "zzabccy"

**Output:** 4

**Explanation:**

The longest balanced substring is `"zabc"` because the distinct characters `'z'`, `'a'`, `'b'`, and `'c'` each appear exactly 1 time.​​​​​​​

</div>
#### Example 3

<div class="example-block">
**Input:** s = "aba"

**Output:** 2

**Explanation:**

**​​​​​​​**One of the longest balanced substrings is `"ab"` because both distinct characters `'a'` and `'b'` each appear exactly 1 time. Another longest balanced substring is `"ba"`.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 1000$

- `s` consists of lowercase English letters.