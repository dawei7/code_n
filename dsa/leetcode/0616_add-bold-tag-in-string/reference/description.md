### 1. Description

You are given a string `s` and an array of strings `words`.

You should add a closed pair of bold tag `<b>` and `</b>` to wrap the substrings in `s` that exist in `words`.

- If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.

- If two substrings wrapped by bold tags are consecutive, you should combine them.

Return `s` *after adding the bold tags*.

### 2. Function Contract

**Inputs**

- `s`: the nonempty source string in which occurrences are located
- `words`: the array of distinct dictionary strings; the array itself may be empty

Let $N = \lvert\texttt{s}\rvert$ and let

$D = \sum_{w \in \texttt{words}} \lvert w \rvert.$

**Return value**

- Return a string containing all characters of `s` in their original order.
- Enclose every maximal span covered by one or more complete dictionary-word occurrences in `<b>` and `</b>`.
- Merge overlapping or consecutive covered spans into one tagged region.
- If no dictionary word occurs, return `s` unchanged.

### 3. Examples

#### Example 1

- **Input:** `s = "abcxyz123", words = ["abc","123"]`
- **Output:** `"**abc**xyz**123**"`
- **Explanation:** The two strings of words are substrings of s as following: "<u>abc</u>xyz<u>123</u>".
We add ** before each substring and ** after each substring.
#### Example 2

- **Input:** `s = "aaabbb", words = ["aa","b"]`
- **Output:** `"**aaabbb**"`
- **Explanation:**
"aa" appears as a substring two times: "<u>aa</u>abbb" and "a<u>aa</u>bbb".
"b" appears as a substring three times: "aaa<u>b</u>bb", "aaab<u>b</u>b", and "aaabb<u>b</u>".
We add ** before each substring and ** after each substring: "**a<b>a**a</b>**b****b****b**".
Since the first two **'s overlap, we merge them: "<b>aaa****b****b****b**".
Since now the four **'s are consecutive, we merge them: "<b>aaabbb**".

### 4. Constraints

- $1 \le \text{s.length} \le 1000$

- $0 \le \text{words.length} \le 100$

- $1 \le \text{words}[i].length \le 1000$

- `s` and $\text{words}[i]$ consist of English letters and digits.

- All the values of `words` are **unique**.

### 5. Note

This question is the same as <a href="https://leetcode.com/problems/bold-words-in-string/description/" target="_blank">758. Bold Words in String</a>.