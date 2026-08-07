## Description

You are given a string `s` that consists of lowercase English letters.

Return the string obtained by removing **all** trailing **vowels** from `s`.

The **vowels** consist of the characters `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.
### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

Let $j$ be the largest index whose character is not one of `a`, `e`, `i`, `o`, or `u`. If no such index exists, no character belongs to the retained prefix.

Only the contiguous vowel suffix after $j$ is removed. A vowel at or before a later consonant is not trailing and must remain.

**Return value**

Return $s[:j + 1]$ when a non-vowel exists, or the empty string when all characters are vowels.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "idea"

**Output:** "id"

**Explanation:**

Removing `"id<u>**ea**</u>"`, we obtain the string `"id"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "day"

**Output:** "day"

**Explanation:**

There are no trailing vowels in the string `"day"`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "aeiou"

**Output:** ""

**Explanation:**

Removing `"<u>**aeiou**</u>"`, we obtain the string `""`.

</div>
### Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists of only lowercase English letters.