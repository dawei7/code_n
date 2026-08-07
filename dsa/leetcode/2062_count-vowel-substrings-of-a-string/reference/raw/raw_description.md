## Description

A **substring** is a contiguous (non-empty) sequence of characters within a string.

A **vowel substring** is a substring that **only** consists of vowels (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) and has **all five** vowels present in it.

Given a string `word`, return *the number of **vowel substrings** in* `word`.

**Example 1:**

```
**Input:** word = "aeiouu"
**Output:** 2
**Explanation:** The vowel substrings of word are as follows (underlined):
- "**<u>aeiou</u>**u"
- "**<u>aeiouu</u>**"
```

**Example 2:**

```
**Input:** word = "unicornarihan"
**Output:** 0
**Explanation:** Not all 5 vowels are present, so there are no vowel substrings.
```

**Example 3:**

```
**Input:** word = "cuaieuouac"
**Output:** 7
**Explanation:** The vowel substrings of word are as follows (underlined):
- "c**<u>uaieuo</u>**uac"
- "c**<u>uaieuou</u>**ac"
- "c**<u>uaieuoua</u>**c"
- "cu**<u>aieuo</u>**uac"
- "cu**<u>aieuou</u>**ac"
- "cu**<u>aieuoua</u>**c"
- "cua**<u>ieuoua</u>**c"
```

**Constraints:**

	- `1 <= word.length <= 100`

	- `word` consists of lowercase English letters only.
