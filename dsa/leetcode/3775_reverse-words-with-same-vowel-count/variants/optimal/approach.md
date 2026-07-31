## General

Split the sentence at its guaranteed single-space separators. Count members of `{a, e, i, o, u}` in the first word once and retain that number as the target.

Examine every remaining word independently. Count its vowels; if the count equals the target, replace that word by its character reversal. Otherwise retain it verbatim. Finally join the word list with single spaces.

The first word is never modified. Every later word is tested against exactly the count specified by the problem, so it is reversed if and only if the rule requires it. Splitting and rejoining preserve word order and the guaranteed separator format, proving that the constructed string is the requested result.

## Complexity detail

Let $N=\lvert s\rvert$. Across all words, vowel counting and reversal inspect or copy each character only a constant number of times, so the running time is $O(N)$. The word list, reversed strings, and returned string require $O(N)$ space.

## Alternatives and edge cases

- **Scan character ranges in place:** Tracking word boundaries in a character buffer can reverse matching regions without a split list, but is more intricate and still requires mutable output storage.
- **Repeated string prepending:** Building a reversal by inserting each character at the front repeatedly can copy an ever-growing string and approach quadratic time for a long word.
- **First word:** It defines the vowel target but remains unchanged even though its count necessarily matches itself.
- **Zero-vowel target:** If the first word contains no vowels, every later consonant-only word is reversed.
- **One-word sentence:** No later word exists, so the input is returned unchanged.
- **Palindromic matching word:** Reversal is still required conceptually, although its visible spelling may not change.
- **Single spaces:** Joining with one space exactly restores the source-guaranteed spacing format.
