### 1. Description

Given an array of strings `words`, return *the first **palindromic** string in the array*. If there is no such string, return *an **empty string** *`""`.

A string is **palindromic** if it reads the same forward and backward.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** $words = ["abc","car","ada","racecar","cool"]$
- **Output:** `"ada"`
- **Explanation:** The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

#### Example 2

- **Input:** $words = ["notapalindrome","racecar"]$
- **Output:** `"racecar"`
- **Explanation:** The first and only string that is palindromic is "racecar".

#### Example 3

- **Input:** $words = ["def","ghi"]$
- **Output:** `""`
- **Explanation:** There are no palindromic strings, so the empty string is returned.

### 4. Constraints

- $1 \le \text{words.length} \le 100$

- $1 \le \text{words}[i].length \le 100$

- $\text{words}[i]$ consists only of lowercase English letters.
