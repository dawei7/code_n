### 1. Description

You are given a string `s` consisting of lowercase English words, each separated by a single space.

Determine how many vowels appear in the **first** word. Then, reverse each following word that has the **same vowel count**. Leave all remaining words unchanged.

Return the resulting string.

Vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

### 2. Function Contract

**Inputs**

- `s`: A nonempty, single-space-separated sequence of lowercase English words.

The string has no leading or trailing spaces. A word's vowel count includes every occurrence of the five lowercase vowels and ignores all consonants.

**Return value**

Return a string with the same words and spacing structure, except that each word after the first is character-reversed exactly when its vowel count matches the first word's count.

### 3. Examples

#### Example 1

- **Input:** s = "cat and mice"

- **Output:** "cat dna mice"

- **Explanation:** 

- The first word `"cat"` has 1 vowel.

- `"and"` has 1 vowel, so it is reversed to form `"dna"`.

- `"mice"` has 2 vowels, so it remains unchanged.

- Thus, the resulting string is `"cat dna mice"`.

#### Example 2

- **Input:** s = "book is nice"

- **Output:** "book is ecin"

- **Explanation:** 

- The first word `"book"` has 2 vowels.

- `"is"` has 1 vowel, so it remains unchanged.

- `"nice"` has 2 vowels, so it is reversed to form `"ecin"`.

- Thus, the resulting string is `"book is ecin"`.

#### Example 3

- **Input:** s = "banana healthy"

- **Output:** "banana healthy"

- **Explanation:** 

- The first word `"banana"` has 3 vowels.

- `"healthy"` has 2 vowels, so it remains unchanged.

- Thus, the resulting string is `"banana healthy"`.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters and spaces.

- Words in `s` are separated by a **single** space.

- `s` does **not** contain leading or trailing spaces.
