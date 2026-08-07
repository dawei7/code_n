### 1. Description

You are given a string `s` consisting only of the characters `'a'`, `'b'`, and `'c'`.

A **substring** of `s` is called **balanced** if all **distinct** characters in the **substring** appear the **same** number of times.

Return the **length of the longest balanced substring** of `s`.

### 2. Function Contract

**Inputs**

- `s`: A string over the three-character alphabet `{a, b, c}`.

Only positive frequencies inside the chosen contiguous interval are compared. A balanced substring may contain one, two, or all three allowed characters.

**Return value**

Return the maximum length of a balanced substring. At least one character can always be chosen, so the answer is at least `1`.

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
**Input:** s = "aabcc"

**Output:** 3

**Explanation:**

The longest balanced substring is `"abc"` because all distinct characters `'a'`, `'b'` and `'c'` each appear exactly 1 time.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "aba"

**Output:** 2

**Explanation:**

One of the longest balanced substrings is `"ab"` because both distinct characters `'a'` and `'b'` each appear exactly 1 time. Another longest balanced substring is `"ba"`.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` contains only the characters `'a'`, `'b'`, and `'c'`.