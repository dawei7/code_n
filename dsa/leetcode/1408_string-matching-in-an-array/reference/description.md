### 1. Description

Given an array of string `words`, return all strings in* *`words`* *that are a substring of another word. You can return the answer in **any order**.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).

**Return value**

- Returns `List[str]`.

### 3. Examples

#### Example 1

- **Input:** $words = ["mass","as","hero","superhero"]$
- **Output:** `["as","hero"]`
- **Explanation:** "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

#### Example 2

- **Input:** $words = ["leetcode","et","code"]$
- **Output:** `["et","code"]`
- **Explanation:** "et", "code" are substring of "leetcode".

#### Example 3

- **Input:** $words = ["blue","green","bu"]$
- **Output:** `[]`
- **Explanation:** No string of words is substring of another string.

### 4. Constraints

- $1 \le \text{words.length} \le 100$

- $1 \le \text{words}[i].length \le 30$

- $\text{words}[i]$ contains only lowercase English letters.

- All the strings of `words` are **unique**.
