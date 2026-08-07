## Description

A string can be **abbreviated** by replacing any number of **non-adjacent**, **non-empty** substrings with their lengths. The lengths **should not** have leading zeros.

For example, a string such as `"substitution"` could be abbreviated as (but not limited to):

- `"s10n"` (`"s <u>ubstitutio</u> n"`)

- `"sub4u4"` (`"sub <u>stit</u> u <u>tion</u>"`)

- `"12"` (`"<u>substitution</u>"`)

- `"su3i1u2on"` (`"su <u>bst</u> i <u>t</u> u <u>ti</u> on"`)

- `"substitution"` (no substrings replaced)

The following are **not valid** abbreviations:

- `"s55n"` (`"s <u>ubsti</u> <u>tutio</u> n"`, the replaced substrings are adjacent)

- `"s010n"` (has leading zeros)

- `"s0ubstitution"` (replaces an empty substring)

Given a string `word` and an abbreviation `abbr`, return *whether the string **matches** the given abbreviation*.

A **substring** is a contiguous **non-empty** sequence of characters within a string.
### Function Contract

**Inputs**

- `word`: The lowercase English word that the abbreviation must represent.
- `abbr`: A string of lowercase English letters and decimal digits to interpret as an abbreviation.

**Return value**

Return `true` exactly when every literal and replacement length in `abbr` consumes all of `word` under the valid
abbreviation rules; otherwise, return `false`.

### Examples

#### Example 1

- **Input:** $word = "internationalization", abbr = "i12iz4n"$
- **Output:** `true`
- **Explanation:** The word "internationalization" can be abbreviated as "i12iz4n" ("i <u>nternational</u> iz <u>atio</u> n").
#### Example 2

- **Input:** $word = "apple", abbr = "a2e"$
- **Output:** `false`
- **Explanation:** The word "apple" cannot be abbreviated as "a2e".
### Constraints

- $1 \le \text{word.length} \le 20$

- `word` consists of only lowercase English letters.

- $1 \le \text{abbr.length} \le 10$

- `abbr` consists of lowercase English letters and digits.

- All the integers in `abbr` will fit in a 32-bit integer.