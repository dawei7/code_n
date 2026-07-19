# Goat Latin

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 824 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/goat-latin/) |

## Problem Description

### Goal

You are given a string `sentence` consisting of words made only from uppercase and lowercase English letters. The words are separated by one space, and the sentence has no leading or trailing spaces. Convert every word to Goat Latin while preserving the words' order, letter case, and the single spaces between them.

For a word that begins with a vowel (`a`, `e`, `i`, `o`, or `u`, ignoring case), keep all its letters in place and append `"ma"`. For a word that begins with a consonant, move its first letter to the end before appending `"ma"`. Finally, append one `"a"` for the first word, two for the second word, and in general $i$ copies for the word at one-based index $i$. Return the sentence formed by all converted words.

### Function Contract

**Inputs**

- `sentence`: a string of length $n$, where $1 \le n \le 150$; it contains English-letter words separated by single spaces, with no leading or trailing space
- Let $w$ be the number of words. The result length is

  $$
  R = n + 2w + \sum_{i=1}^{w} i
    = n + 2w + \frac{w(w+1)}{2}.
  $$

**Return value**

- The Goat Latin conversion of `sentence`, with the original word order and spacing preserved

### Examples

**Example 1**

- Input: `sentence = "I speak Goat Latin"`
- Output: `"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"`
- Explanation: `I` begins with a vowel, while the other three words begin with consonants and move their first letters to the end. Their index suffixes contain one through four added `"a"` characters.

**Example 2**

- Input: `sentence = "The quick brown fox jumped over the lazy dog"`
- Output: `"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"`
- Explanation: Each word follows its initial-letter rule, then receives an index-length suffix from one through nine `"a"` characters.

**Example 3**

- Input: `sentence = "b A"`
- Output: `"bmaa Amaaa"`
- Explanation: Moving the only letter of `b` leaves that word unchanged, and uppercase `A` is a vowel.
