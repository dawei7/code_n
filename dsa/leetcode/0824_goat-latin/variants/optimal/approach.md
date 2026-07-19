## General
**Transform the initial letter without changing case**

Split `sentence` into its words and keep a set containing both lowercase and uppercase vowels. If `word[0]` belongs to that set, the word's letter sequence is already the required base. Otherwise, form the base with `word[1:] + word[0]`. This rotation also handles a one-letter consonant: its empty suffix followed by its first letter reconstructs the same word.

**Attach the suffix belonging to the word's position**

Enumerate the words starting at index `1`. Append `"ma"` and then `"a" * index` to each transformed base. Store the completed words in a list instead of repeatedly rebuilding the whole sentence, then join the list with single spaces.

**Why the assembled sentence follows every Goat Latin rule**

For each word, exactly one of the vowel and consonant cases applies. The selected base therefore either preserves all letters or performs precisely the required first-letter rotation. Adding `"ma"` and the one-based number of `"a"` characters completes that word's conversion. The enumeration visits every original word once in order, and the final join inserts exactly one space between adjacent results, so the returned sentence is the complete conversion and introduces no extra boundary spaces.

## Complexity detail
Let $n$ be the input length, $w$ the number of words, and $R$ the output length defined above. Splitting reads the $n$ input characters. Across all words, slicing and rotating processes the original letters once, while constructing the suffixes writes exactly the additional characters counted in $R$. The final join also writes $R$ characters, so the total time is $O(R)$. The transformed-word list and returned string occupy $O(R)$ space.

## Alternatives and edge cases
- **Repeated whole-sentence concatenation:** Appending each character by rebuilding the accumulated immutable string remains correct, but it can copy earlier output repeatedly and take $O(R^2)$ time.
- **Streaming string builder:** A mutable character buffer can emit the same result in $O(R)$ time and may avoid storing separate word strings, though Python's list-and-join form is clearer.
- **Regular-expression word processing:** Matching words is unnecessary because the contract already guarantees single-space separation and letter-only words.
- **Uppercase vowels:** Membership must treat `A`, `E`, `I`, `O`, and `U` as vowels while preserving their original case.
- **One-letter consonant:** Moving its first character to the end does not remove it; `"b"` becomes `"bmaa"` at index `1`.
- **Indexing convention:** The suffix count starts at one, so even the first converted word receives one extra `"a"` after `"ma"`.
- **Spacing:** The result has one space only between converted words, with no leading or trailing space.
