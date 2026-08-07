### 1. Description

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

### 2. Function Contract

**Inputs**

- `s`: The printable ASCII string whose vowel sequence is to be reversed.

**Return value**

Return `s` with the vowel characters placed in reverse occurrence order and every non-vowel character left in its original position.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "IceCreAm"

**Output:** "AceCreIm"

**Explanation:**

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "leetcode"

**Output:** "leotcede"

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 3 * 10^{5}$

- `s` consist of **printable ASCII** characters.