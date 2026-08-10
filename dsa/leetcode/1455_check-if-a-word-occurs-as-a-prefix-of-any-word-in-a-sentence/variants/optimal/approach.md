## General

**Turn the sentence into words in original order.** `sentence.split()` produces a list of its words from left to right. The input guarantees single spaces and lowercase letters, so tokenization is straightforward. Calling `split` without an explicit delimiter also ignores surrounding or repeated whitespace, although that extra tolerance is not needed by the contract.

The code passes this list to `enumerate(..., 1)`. The second argument makes the first produced index one rather than Python's usual zero. Each loop iteration therefore receives exactly the word position required by the problem and the corresponding word `s`.

**Use the language's exact prefix operation.** `s.startswith(searchWord)` is true when the first characters of `s` equal all of `searchWord`. It also returns false when `searchWord` is longer than `s`, so there is no need for a separate length check or slicing boundary logic.

A prefix must begin at character zero. A match later inside the word does not count. For example, `"burg"` is a prefix of `"burger"`, while `"urge"` is only an internal substring and `startswith` correctly rejects it.

The complete word is also one of its prefixes. If `s == searchWord`, `startswith` returns true, which matches the mathematical definition of a leading substring.

**Return immediately on the first match.** Words are scanned in increasing sentence order. The first time the condition is true, its one-based index is necessarily the minimum matching index. Returning immediately both satisfies the tie rule and avoids testing later words.

If the loop ends normally, every word has failed the prefix test. The function then returns `-1`, the required sentinel for absence.

**Trace a sentence with multiple matches.** For `sentence = "this problem is an easy problem"` and `searchWord = "pro"`, splitting yields six words. The first word `this` does not start with `pro`. The second word `problem` does, so the function returns two immediately. The later word `problem` at position six is also a match, but it must not replace the earlier answer.

For `"i love eating burger"` and `"burg"`, the first three checks fail and `"burger".startswith("burg")` succeeds at enumerated index four. For `"i am tired"` and `"you"`, all three fail and the function reaches `-1`.

**The loop invariant.** Before examining word position `i`, none of the earlier positions is a match. This is true initially because there are no earlier words. If the current word fails, the statement becomes true for the next position. If it succeeds, returning `i` is correct because the invariant proves no smaller index could have matched.

If every iteration fails, the invariant at loop completion says no word in the sentence has the requested prefix, justifying `-1`.

**Why startswith is preferable to manual slicing here.** Testing `s[:len(searchWord)] == searchWord` can also work, but it creates a new substring in Python. `startswith` can compare directly against the original word and clearly states the intended relation. It also handles a search word longer than the candidate naturally.

**Case and punctuation need no special policy.** Both inputs consist of lowercase English letters, and words are separated by spaces. Prefix comparison is therefore an ordinary case-sensitive character comparison. No conversion, punctuation stripping, or locale handling is appropriate.

**Be precise about the stored source's memory use.** The manifest advertises `O(1)` space, which is achievable by scanning word boundaries directly in the original sentence. The exact stored code calls `sentence.split()` before the loop. In Python, that creates a list and word strings whose total size is linear in the sentence length. The exact source therefore uses `O(N)` auxiliary space, not `O(1)`.

Its time remains linear overall. Splitting scans the sentence, and prefix checks inspect initial characters of words. Across all words, the amount inspected is bounded by their total character content in the worst case, so the full operation is `O(N)`.

## Complexity detail

Let `N` be the number of characters in `sentence` and `M` the length of `searchWord`. Splitting the sentence takes `O(N)` time and creates words with `O(N)` total characters.

For a candidate word of length `w`, `startswith` examines at most `min(w, M)` characters. Summed across all words reached by the loop, this is at most the total word characters, hence `O(N)`. Even though one might write the looser expression `O(WM)` for `W` words, the comparisons cannot inspect more than each candidate word's available prefix, and the total available word length is bounded by `N`. Overall time is `O(N)`.

Because `split()` materializes the complete list before iteration begins, early return does not avoid tokenizing the rest of the sentence. The list and its word strings use `O(N)` auxiliary space. The enumerator and scalar loop variables use only constant additional storage.

The manifest's `O(1)` space describes the manual in-place scan alternative, not this exact implementation. For this file, report `O(N)` time and `O(N)` auxiliary space.

## Alternatives and edge cases

- **Manual character scan:** Walk the original sentence, identify each word start, and compare `searchWord` without creating word strings. This achieves the manifest's `O(N)` time and `O(1)` auxiliary space.
- **Explicit split list variable:** Assign `words = sentence.split()` before looping. It behaves exactly like the inline stored expression and can be easier to inspect, with the same linear allocation.
- **Prefix slicing:** Compare `s[:len(searchWord)]` with `searchWord`. It is correct but allocates a substring for each checked word.
- **Regular expression:** A word-boundary pattern can locate a prefix, but translating its character position back to a one-based word index adds complexity for this simple scan.
- **Trie:** Building a prefix tree can help answer many prefix queries against the same sentence. For one query it uses unnecessary `O(N)` construction and storage.
- **Search as an arbitrary substring:** Using `searchWord in s` is wrong because occurrences away from the first character are not prefixes.
- **Several matching words:** Immediate return gives the minimum one-based index.
- **Whole-word equality:** A word starts with itself, so it is a valid match.
- **Search word longer than a word:** `startswith` returns false safely.
- **First word matches:** `enumerate` begins at one, so the function returns one without examining later words.
- **Last word matches:** Earlier failures do not prevent reaching it, and its correct one-based position is returned.
- **No match:** Exhausting the loop produces `-1`.
- **One-word sentence:** The single prefix test decides between one and `-1`.
- **Repeated words:** Each occurrence has its own position. The first matching occurrence wins.
- **Lowercase guarantee:** Direct comparison is correct; converting case could change a problem with case-sensitive semantics and is unnecessary.
- **Single-space guarantee:** `split` preserves word order and produces no empty tokens. Its broader whitespace behavior does not affect valid inputs.
- **Empty search word outside the contract:** Every string starts with the empty string, but the input guarantees at least one search character.
- **Memory accounting:** The generator-like `enumerate` is constant-space, but the underlying split list is not. Include that list when analyzing this exact source.
