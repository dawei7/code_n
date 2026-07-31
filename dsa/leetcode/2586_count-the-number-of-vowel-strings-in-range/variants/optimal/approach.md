## General

Only two characters determine whether a word is a vowel string: its first character and its last character. Every word is guaranteed nonempty, so both positions always exist, including when they refer to the same character in a one-letter word.

Create the fixed vowel set `a`, `e`, `i`, `o`, and `u`. Visit each index from `left` through `right`, inclusive. Add one to the result precisely when both endpoints of that word belong to the vowel set. Words outside this index interval never participate.

This counts every qualifying word exactly once because the scan visits each allowed index once, and the endpoint test is exactly the definition of a vowel string.

## Complexity detail

Let $k = \texttt{right} - \texttt{left} + 1$ be the number of selected words. The scan takes $O(k)$ time. The five-vowel set and counter use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Boolean helper:** A small `isVowel` function with five direct comparisons avoids constructing a set and has the same $O(k)$ time and $O(1)$ space.
- **Scanning every word:** Iterating outside `[left, right]` does unnecessary work and can count words that the contract excludes.
- **One-character words:** The first and last positions coincide, so a single vowel qualifies and a single consonant does not.
- **One-sided matches:** A word contributes only when both endpoint checks succeed; satisfying just one is insufficient.
- **Inclusive right endpoint:** The word at `right` must be inspected, not treated as the excluded endpoint of a half-open slice.
