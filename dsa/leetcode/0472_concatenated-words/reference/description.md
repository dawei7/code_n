### 1. Description

Given an array of strings `words` (**without duplicates**), return *all the **concatenated words** in the given list of* `words`.

A **concatenated word** is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.

### 2. Function Contract

**Inputs**

- `words`: the array of distinct, nonempty lowercase English words

**Return value**

- Return every input word that is a concatenation of at least two shorter input words. Result order is not
  semantically significant.

Each component must consume one or more characters, components may be reused, and their joined text must equal the
candidate without gaps or leftover characters.

### 3. Examples

#### Example 1

- **Input:** $words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]$
- **Output:** `["catsdogcats","dogcatsdog","ratcatdogcat"]`
- **Explanation:** "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
#### Example 2

- **Input:** $words = ["cat","dog","catdog"]$
- **Output:** `["catdog"]`

### 4. Constraints

- $1 \le \text{words.length} \le 10^{4}$

- $1 \le \text{words}[i].length \le 30$

- $\text{words}[i]$ consists of only lowercase English letters.

- All the strings of `words` are **unique**.

- $1 \le sum(\text{words}[i].length) \le 10^{5}$