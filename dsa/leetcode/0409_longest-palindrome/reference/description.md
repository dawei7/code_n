## Description

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest palindrome** that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.
### Function Contract

**Inputs**

- `s`: The lowercase and uppercase English letter occurrences available for constructing the palindrome.

**Return value**

Return the maximum number of available characters that can be rearranged into a palindrome.

### Examples
#### Example 1

- **Input:** `s = "abccccdd"`
- **Output:** `7`
- **Explanation:** One longest palindrome that can be built is "dccaccd", whose length is 7.
#### Example 2

- **Input:** `s = "a"`
- **Output:** `1`
- **Explanation:** The longest palindrome that can be built is "a", whose length is 1.
### Constraints

- $1 \le \text{s.length} \le 2000$

- `s` consists of lowercase **and/or** uppercase English letters only.