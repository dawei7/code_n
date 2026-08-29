## General

**The final digit tells each word’s destination.** Every shuffled token consists of its original letters followed by one digit from one through nine. Because there are at most nine words, the position always occupies exactly the last character; no multi-digit parsing is required.

The algorithm splits the sentence, allocates an output slot for every word, places each stripped word at its encoded position, and joins the slots.

**Split into shuffled tokens.** `ws = s.split()` separates on whitespace. Under the contract, words are separated by one space with no leading or trailing spaces, so it produces exactly the shuffled word tokens. Using `split()` without an explicit separator is also robust to extra whitespace, although that is not needed here.

**Allocate the exact number of positions.** `ans = [None] * len(ws)` creates one slot for each original word. The encoded positions are one through the number of words, so every valid digit maps to one of these indices after subtracting one.

The temporary `None` values are placeholders only. The input construction guarantees one position suffix for every word and a valid shuffled sentence, so all slots are replaced by strings before `join`.

**Decode one token.** For token `w`:

- `w[-1]` is the final digit character.
- `int(w[-1]) - 1` converts its one-based position to a zero-based list index.
- `w[:-1]` is the original word with the position digit removed.

The assignment

`ans[int(w[-1]) - 1] = w[:-1]`

puts the word directly where it belongs. The input order no longer matters because destinations come from the suffixes.

**Trace the first sample.** Splitting `"is2 sentence4 This1 a3"` produces four tokens. `"is2"` places `"is"` at index one, `"sentence4"` places `"sentence"` at index three, `"This1"` fills index zero, and `"a3"` fills index two. The completed list is `["This", "is", "a", "sentence"]`.

**Reconstruct spacing with join.** `" ".join(ans)` concatenates the ordered words with exactly one space between adjacent entries and no leading or trailing space. That recreates the sentence format required by the definition.

**Why no comparison sort is necessary.** The digits already provide direct array positions. Sorting tokens by their last character would also work for at most nine words, but direct placement avoids comparison logic and expresses the one-to-one position mapping more clearly.
Each shuffled token carries the unique one-based position of its word in the original sentence. The loop converts that to the corresponding zero-based slot and removes only the suffix digit. Therefore, after every token is processed, slot `p - 1` contains exactly the original word from position `p`. Joining slots from zero upward returns all original words in their original order with correct spacing.

**Case is preserved.** `w[:-1]` copies the word’s letters without altering them, so uppercase and lowercase characters remain exactly as supplied. Only the final numeric marker is removed.

**Why the one-character suffix assumption is safe.** The sentence has no more than nine words, and positions are from one through nine. If ten or more words were allowed, taking only `w[-1]` would misread a suffix such as `10`. The explicit constraint makes the current parsing exact.

## Complexity detail

Let `S` be the total character length of the shuffled sentence. Splitting copies or references all token characters in `O(S)` time. Slicing all word bodies and joining them also process `O(S)` characters in total. Direct assignments are constant time per word, so total time is `O(S)`.

`ws`, `ans`, the sliced word strings, and the returned sentence collectively use `O(S)` space. The number of list entries is at most nine, but the word character storage still scales with input length.

## Alternatives and edge cases

- **Sort tokens by suffix:** Sorting at most nine tokens is simple, but direct placement is linear and avoids comparisons.
- **Dictionary from position to word:** It works but a fixed list naturally represents the complete consecutive positions.
- **One word:** Its suffix is one, it fills the only slot, and joining returns the word without the digit.
- **Nine words:** Every suffix is still one character, so `w[-1]` remains sufficient.
- **Mixed uppercase and lowercase:** Slicing preserves exact case.
- **Single-letter word:** Removing the last digit leaves its one letter correctly.
- **Shuffled order already correct:** Direct placement reproduces the same order without relying on that coincidence.
- **No leading or trailing spaces:** `join` guarantees the reconstructed sentence also has none.
- **Unique positions:** Correct input must supply each original position once; otherwise a slot could be overwritten or remain `None`.
- **Position range validity:** Every encoded digit must fall between one and the number of tokens. This guarantee keeps every converted zero-based index inside `ans` and ensures that successful placement fills a real sentence position rather than extending or indexing outside the list.
- **More than nine words outside constraints:** Multi-digit positions would require separating the full numeric suffix rather than reading one character.
- **Whitespace robustness:** `split()` tolerates repeated whitespace even though the contract uses single spaces.
- **No input mutation:** The source string is immutable; reconstruction uses new lists and strings.
