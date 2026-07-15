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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Choose the format from the email delimiter**

A valid email contains exactly one `"@"`, while a valid phone number contains none. Test for that delimiter once and apply only the corresponding masking rules. The validity guarantee means no further format disambiguation or error recovery is necessary.

**Normalize and mask an email**

Lowercase the complete input, then split it into `name` and `domain` at `"@"`. Build the result from `name[0]`, the fixed string `"*****"`, `name[-1]`, `"@"`, and the unchanged lowercased domain. Selecting the endpoint letters after lowercasing preserves exactly the allowed name information; inserting the fixed mask hides every possible middle regardless of whether the original name had two or many letters.

**Extract digits before formatting a phone number**

Scan `s` and retain only characters for which `character.isdigit()` is true. If the resulting digit string has length $d$, then `country_length = d - 10`. The suffix `digits[-4:]` is always the visible local ending. Construct `"***-***-" + digits[-4:]`, and prepend `"+" + "*" * country_length + "-"` exactly when `country_length` is positive.

For email input, every output letter and delimiter follows directly from the two valid parts. For phone input, digit extraction preserves order while discarding exactly the permitted separators, so the last 10 digits and country-code length match the contract. The construction reveals only the four allowed local digits and emits the required number of country asterisks, proving that either branch returns its exact mask.

#### Complexity detail

Let $n$ be the input length. Lowercasing and splitting an email, or filtering the characters of a phone number, scans $n$ characters once. Constructing the result is also linear in its length, so the time is $O(n)$. The normalized email or extracted digit string and the returned mask use $O(n)$ space.

#### Alternatives and edge cases

- **Regular expressions:** A substitution can normalize either format, but separate string operations make the fixed output rules easier to audit.
- **Manual ASCII conversion:** Testing and converting uppercase letters without `lower()` remains linear but adds unnecessary character arithmetic.
- **Repeated immutable-prefix rebuilding:** Appending one normalized character by copying the accumulated string each time is correct but can take $O(n^2)$ time.
- **Two-letter email name:** Output five asterisks even though the original name has no middle letters.
- **Mixed email case:** Lowercase both the name endpoints and the entire domain.
- **No country code:** A 10-digit phone begins directly with `"***-***-"` and has no leading plus sign.
- **One to three country digits:** Emit exactly the same number of leading asterisks after `"+"`.
- **Phone separators:** Their kind and placement do not affect digit order or the result.
- **Visible phone suffix:** Preserve only the last four digits, including any leading zero among those four.

</details>
