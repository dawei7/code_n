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

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Transform the initial letter without changing case**

Split `sentence` into its words and keep a set containing both lowercase and uppercase vowels. If `word[0]` belongs to that set, the word's letter sequence is already the required base. Otherwise, form the base with `word[1:] + word[0]`. This rotation also handles a one-letter consonant: its empty suffix followed by its first letter reconstructs the same word.

**Attach the suffix belonging to the word's position**

Enumerate the words starting at index `1`. Append `"ma"` and then `"a" * index` to each transformed base. Store the completed words in a list instead of repeatedly rebuilding the whole sentence, then join the list with single spaces.

**Why the assembled sentence follows every Goat Latin rule**

For each word, exactly one of the vowel and consonant cases applies. The selected base therefore either preserves all letters or performs precisely the required first-letter rotation. Adding `"ma"` and the one-based number of `"a"` characters completes that word's conversion. The enumeration visits every original word once in order, and the final join inserts exactly one space between adjacent results, so the returned sentence is the complete conversion and introduces no extra boundary spaces.

#### Complexity detail

Let $n$ be the input length, $w$ the number of words, and $R$ the output length defined above. Splitting reads the $n$ input characters. Across all words, slicing and rotating processes the original letters once, while constructing the suffixes writes exactly the additional characters counted in $R$. The final join also writes $R$ characters, so the total time is $O(R)$. The transformed-word list and returned string occupy $O(R)$ space.

#### Alternatives and edge cases

- **Repeated whole-sentence concatenation:** Appending each character by rebuilding the accumulated immutable string remains correct, but it can copy earlier output repeatedly and take $O(R^2)$ time.
- **Streaming string builder:** A mutable character buffer can emit the same result in $O(R)$ time and may avoid storing separate word strings, though Python's list-and-join form is clearer.
- **Regular-expression word processing:** Matching words is unnecessary because the contract already guarantees single-space separation and letter-only words.
- **Uppercase vowels:** Membership must treat `A`, `E`, `I`, `O`, and `U` as vowels while preserving their original case.
- **One-letter consonant:** Moving its first character to the end does not remove it; `"b"` becomes `"bmaa"` at index `1`.
- **Indexing convention:** The suffix count starts at one, so even the first converted word receives one extra `"a"` after `"ma"`.
- **Spacing:** The result has one space only between converted words, with no leading or trailing space.

</details>
