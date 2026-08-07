### 1. Description

Given a string `s`, return *the number of **distinct** substrings of* `s`.

A **substring** of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

### 2. Function Contract

**Inputs**

- `s`: A string of lowercase English letters ($1 \le \text{s.length} \le 500$).

**Return value**

Return an integer representing the number of distinct nonempty substrings in `s`.

### 3. Examples

#### Example 1

- **Input:** `s = "aabbaba"`
- **Output:** `21`
- **Explanation:** The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
#### Example 2

- **Input:** `s = "abcdefg"`
- **Output:** `28`

### 4. Constraints

- $1 \le \text{s.length} \le 500$

- `s` consists of lowercase English letters.

**Follow up:** Can you solve this problem in `O(n)` time complexity?