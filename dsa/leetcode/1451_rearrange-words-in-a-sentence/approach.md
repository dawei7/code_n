## General

**Normalize the original capitalization before sorting.** The sentence format capitalizes only its first letter; all later letters are lowercase. Once words are rearranged, the original first word may move away from the front. If its capital letter were left unchanged, the output could contain an uppercase letter in the middle.

The code first splits `text` into `words`, then applies `words[0] = words[0].lower()`. Because the original format guarantees that all other words are already lowercase, this makes every word lowercase before rearrangement. Case therefore has no lingering connection to the word's old position.

`text.split()` separates the sentence into word strings. The contract uses exactly one space between words, but calling `split` without an explicit delimiter also safely handles ordinary whitespace and does not retain separator strings. The result is a mutable list, allowing the code to normalize and sort in place.

**Sort by length and rely on stability for ties.** `words.sort(key=len)` asks Python to use each word's length as its only sort key. Shorter words come first. Crucially, Python's list sort is stable: when two words have equal keys, their relative order remains exactly as it was before sorting.

That stability is not merely a convenience; it is the problem's tie-breaking rule. For `"Keep calm and code on"`, after lowercase normalization the four-letter words appear as `keep`, `calm`, `code`. They all have the same key, so stable sorting preserves that order. There is no need to attach original indices or write a two-part key.

Sorting alphabetically within a length group would be incorrect because the requirement is original order, not dictionary order. Likewise, using a set would lose both duplicates and positions.

**Restore sentence capitalization at the new front.** After sorting, `words[0]` is the word that will start the new sentence. The code replaces it with `words[0].title()`. Under the input constraint that words contain lowercase letters, this capitalizes its first letter and keeps its remaining letters lowercase.

Only the new first word is changed. Every other word is already lowercase because the original first word was normalized before sorting and all original later words began lowercase. This restores the required sentence format independently of which word became shortest.

Finally, `" ".join(words)` inserts exactly one space between adjacent words and no space at either end. It reconstructs the required sentence rather than returning the list.

**Walk through a tie-heavy example.** Start with `"Keep calm and code on"`. Splitting produces `["Keep", "calm", "and", "code", "on"]`. Lowercasing the first entry gives `["keep", "calm", "and", "code", "on"]`.

The lengths are four, four, three, four, and two. Stable sorting produces `["on", "and", "keep", "calm", "code"]`. The three length-four words stay in their original relative order. Applying `title` to `on` gives `On`, and joining returns `"On and keep calm code"`.

Consider `"To be or not to be"`. Several two-letter words occur, including a repeated `be`. Stable sorting retains their original sequence `to, be, or, to, be`, followed by `not`. Duplicates remain separate list entries. Capitalizing the first word gives the required result.

**Why lowercasing happens before sorting even though case does not change length.** Length order itself would be the same if the first word were lowercased afterward. The early normalization makes the data invariant clear: every list item is a lowercase content word, and capitalization will later be assigned solely by output position. It also ensures that the old first word is correct whether it ends up first, in the middle, or at the end.

**Why the stable sort solves both ordering requirements.** Let two words have different lengths. Their numeric keys order them increasingly, as required. Let them have equal lengths and suppose the first appeared earlier in the original sentence. Stability keeps it earlier after sorting. These two cases cover every pair of words, so the sorted list satisfies the complete required order.

The capitalization steps do not change word lengths or positions after the sort. Joining preserves the list order. Therefore the final text has all words in increasing length order, stable ties, one capital initial letter, lowercase remaining letters, and single-space separators.

**The nonempty guarantee makes indexing safe.** The sentence length is at least one and the input is a sentence of words, so `split` produces at least one element. Accessing `words[0]` before and after sorting is valid. A general text utility might need to handle an empty string, but the problem does not.

## Complexity detail

Let `N` be the total number of characters in `text` and `W` the number of words. Splitting and lowercasing copy or process `O(N)` characters. Computing length keys requires `O(W)` calls to `len`, which is constant time for Python strings.

Python's comparison sort takes `O(W log W)` key comparisons in the worst-case bound used by the manifest. Because the keys are small integers, each comparison is constant time. Joining the words writes `O(N)` characters. Total time is `O(N + W log W)`.

The split word list and newly produced strings collectively require `O(N)` storage. Python's sort may use `O(W)` temporary references, and the final joined string has `O(N)` characters. Since `W <= N` for nonempty space-separated words, total auxiliary and output storage is `O(N)`.

The algorithm does not compare full word contents during sorting because `key=len` precomputes length keys. Equal-length stability is provided by the sort implementation rather than by additional content comparisons.

## Alternatives and edge cases

- **Attach original indices:** Sort pairs by length and then original index. This explicitly enforces tie order and works even with an unstable sorting algorithm, but Python's stable sort makes the indices redundant.
- **Bucket words by length:** Append each word to a bucket keyed by its length, then concatenate buckets from shortest to longest. This preserves tie order and can run in `O(N + W + L)` where `L` is the maximum length, but it uses a more specialized structure.
- **Sort by length and word text:** A key such as `(len(word), word)` is wrong because it alphabetizes equal-length words instead of preserving their original order.
- **Unstable sort by length:** In a language whose sort is not stable, equal-length words could be rearranged incorrectly. Add original indices or use stable buckets in that environment.
- **One-word sentence:** Splitting gives one word, sorting changes nothing, and the word is returned with its first letter capitalized.
- **Original first word moves later:** Lowercasing it before sorting prevents an uppercase letter from appearing in the middle of the result.
- **A later word becomes first:** `title` gives it the one required initial capital after sorting.
- **Several equal-length words:** Stability retains their complete original relative order, including duplicates.
- **Duplicate words:** They are separate list elements and are all preserved. A set or dictionary keyed only by word would incorrectly collapse them.
- **Already increasing lengths:** Sorting retains that length order; ties also remain stable. Capitalization is still normalized for the possibly unchanged first word.
- **All words the same length:** Stable sorting leaves the word sequence unchanged, and only sentence capitalization is normalized.
- **Single spaces:** `join` guarantees exactly one separator in the returned sentence, matching the format.
- **No leading or trailing spaces:** `join` adds separators only between words, so none are introduced at the ends.
- **Lowercase word guarantee:** `title` is safe for the new first word because the input contains ordinary lowercase-letter words. More complicated punctuation or apostrophes could make title casing affect multiple segments, but such text is outside the contract.
- **Length versus byte count:** Python `len` counts characters in the given strings. The input is constrained to the expected letter format, so this directly represents word length.
- **Empty input outside the contract:** Accessing `words[0]` would fail. The stated sentence constraints guarantee at least one word, so no empty-case branch is needed.
- **Very long sentence:** The sort dominates by word count while splitting and joining remain linear in characters, consistent with `O(N + W log W)`.
