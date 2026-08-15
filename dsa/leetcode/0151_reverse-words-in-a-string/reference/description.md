### 1. Description

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return *a string of the words in reverse order concatenated by a single space.*

### 2. Function Contract

**Inputs**

- `s`: A string containing at least one word, with words separated by one or more spaces.

**Return value**

Return the words in reverse order with one space between adjacent words and no spaces at either end.

### 3. Note

that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

### 4. Examples

#### Example 1

- **Input:** `s = "the sky is blue"`
- **Output:** `"blue is sky the"`

#### Example 2

- **Input:** `s = "  hello world  "`
- **Output:** `"world hello"`
- **Explanation:** Your reversed string should not contain leading or trailing spaces.

#### Example 3

- **Input:** `s = "a good   example"`
- **Output:** `"example good a"`
- **Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

### 5. Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.

- There is **at least one** word in `s`.

### 6. Follow-up

If the string data type is mutable in your language, can you solve it **in-place** with `O(1)` extra space?
