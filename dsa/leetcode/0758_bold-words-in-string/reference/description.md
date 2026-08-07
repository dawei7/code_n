### 1. Description

Given an array of keywords `words` and a string `s`, make all appearances of all keywords $\text{words}[i]$ in `s` bold. Any letters between `<b>` and `</b>` tags become bold.

Return `s` *after adding the bold tags*. The returned string should use the least number of tags possible, and the tags should form a valid combination.

### 2. Function Contract

$solve(words: \text{list}[str], s: str) -> str$

Let $n$ be the length of `s`.

**Inputs**

- `words`: an array of lowercase keywords whose appearances must be bolded.
- `s`: the lowercase source string to annotate.

**Return value**

Return `s` with each maximal consecutive range covered by at least one complete keyword appearance enclosed in `<b>` and `</b>`. The tags must be properly paired and ordered, and the result must use the minimum possible number of tags.

### 3. Examples

#### Example 1

- **Input:** $words = ["ab","bc"], s = "aabcd"$
- **Output:** `"a**abc**d"`
- **Explanation:** Note that returning "a**a<b>b**c</b>d" would use more tags, so it is incorrect.
#### Example 2

- **Input:** $words = ["ab","cb"], s = "aabcd"$
- **Output:** `"a**ab**cd"`

### 4. Constraints

- $1 \le \text{s.length} \le 500$

- $0 \le \text{words.length} \le 50$

- $1 \le \text{words}[i].length \le 10$

- `s` and $\text{words}[i]$ consist of lowercase English letters.

### 5. Note

This question is the same as <a href="https://leetcode.com/problems/add-bold-tag-in-string/description/" target="_blank">616. Add Bold Tag in String</a>.