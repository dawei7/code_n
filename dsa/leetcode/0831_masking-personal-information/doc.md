# Masking Personal Information

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 831 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/masking-personal-information/) |

## Problem Description

### Goal

You are given a valid personal-information string `s` representing either an email address or a phone number. Return its masked form according to the rules for the detected format.

An email consists of a name containing at least two English letters, followed by `"@"`, followed by a letter-only domain with one dot that is neither its first nor last character. Convert every uppercase letter in the name and domain to lowercase. Preserve only the first and last name letters, replace everything between them with exactly `"*****"` regardless of the original name length, and keep `"@"` followed by the lowercased domain.

A phone number contains between 10 and 13 digits, possibly separated by characters from `"+"`, `"-"`, `"("`, `")"`, and space. Remove all separators. The final 10 digits are the local number, and any preceding zero to three digits form the country code. Always mask the local number as `"***-***-XXXX"`, where `"XXXX"` is its last four digits. If a country code exists, prepend `"+"`, one asterisk per country-code digit, and `"-"`; omit that entire prefix when there is no country code.

### Function Contract

**Inputs**

- `s`: a valid email of length $8$ through $40$, or a valid formatted phone string of length $10$ through $20$
- Email input contains English letters, exactly one `"@"`, and exactly one `"."`; phone input contains 10 through 13 digits plus only permitted separators.
- Let $n$ be the length of `s`.

**Return value**

- The lowercase email mask or digit-preserving phone mask required by the matching format

### Examples

**Example 1**

- Input: `s = "LeetCode@LeetCode.com"`
- Output: `"l*****e@leetcode.com"`
- Explanation: The email is lowercased, and the middle of the name is replaced by five asterisks.

**Example 2**

- Input: `s = "AB@qq.com"`
- Output: `"a*****b@qq.com"`
- Explanation: A two-letter name still receives exactly five asterisks between its endpoints.

**Example 3**

- Input: `s = "1(234)567-890"`
- Output: `"***-***-7890"`
- Explanation: The input has exactly 10 digits, so there is no country-code prefix.
