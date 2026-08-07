### 1. Description

Given two strings `ransomNote` and `magazine`, return `true`* if *`ransomNote`* can be constructed by using the letters from *`magazine`* and *`false`* otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

### 2. Function Contract

**Inputs**

- `ransomNote`: The lowercase string that must be constructed.
- `magazine`: The lowercase source string whose character occurrences are available.

**Return value**

Return `true` when every required character occurrence can be supplied by `magazine`; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** $ransomNote = "a", magazine = "b"$
- **Output:** `false`
#### Example 2

- **Input:** $ransomNote = "aa", magazine = "ab"$
- **Output:** `false`
#### Example 3

- **Input:** $ransomNote = "aa", magazine = "aab"$
- **Output:** `true`

### 4. Constraints

- $1 \le \text{ransomNote.length}, \text{magazine.length} \le 10^{5}$

- `ransomNote` and `magazine` consist of lowercase English letters.