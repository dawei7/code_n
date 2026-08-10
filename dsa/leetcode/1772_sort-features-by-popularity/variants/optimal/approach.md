## General

**Popularity counts responses, not word repetitions**

A feature's popularity is the number of separate response strings containing it. If one user repeats a feature word several times in one response, that response still contributes only one.

The exact solution processes each response independently. It splits the response into words, converts those words to a set, and increments a global `Counter` once for every distinct word in that response.

The set is the key detail that aligns counting with the definition.

**Tokenize one response**

`s.split()` separates a response at whitespace. The input guarantees clean single spaces with no leading or trailing space, but calling `split` without an explicit separator is robust to general whitespace as well.

For `"i like cooler cooler"`, splitting produces two occurrences of `"cooler"`. Wrapping the list in `set(...)` collapses those duplicates. The following loop sees `"cooler"` only once and adds one to its counter.

The set also contains non-feature survey words such as `"i"` and `"like"`. The exact source counts them too, but they never appear in the later `features` sort, so they do not affect the result. Filtering to known features could reduce memory without changing output.

**Accumulate across responses**

`cnt` begins as an empty `Counter`. For every distinct word `w` in one response, `cnt[w] += 1` records that one more response contains it.

The per-response set is recreated for each survey string. A feature appearing in two different responses is therefore incremented twice, as required. Deduplication does not leak across users.

After all responses, `cnt[w]` is exactly the number of response sets containing word `w`. A feature never mentioned has the Counter default value zero.

**Sort by negative popularity**

The required popularity order is non-increasing, while Python's `sorted` defaults to increasing key order. The key function:

`lambda w: -cnt[w]`

negates each count. A feature with popularity three receives key minus three, which sorts before a feature with popularity one and key minus one.

Only the numeric popularity appears in the key; no alphabetical secondary key is added.

**Use stable sorting for original-order ties**

Python's sort is stable: when two elements have equal keys, their relative input order is preserved.

`features` is passed to `sorted` in original index order. Therefore features with equal `-cnt[w]` keys remain in the same order as in the original array, exactly satisfying the tie rule.

For the first example, `"cooler"` and `"lock"` both have count one. They receive equal sort keys, so `"cooler"` remains first because its original feature index is smaller.

Adding an explicit original-index map would also work, but stable sorting makes it unnecessary.

**Why substrings do not count as words**

Response words are compared as complete strings. In `"locker like touch"`, the word `"locker"` is not equal to feature `"lock"`, so `cnt["lock"]` is not incremented from that response.

This follows naturally from `split` and dictionary keys. No substring search is performed, avoiding false matches inside longer words.

**Why the returned order is correct**

For every word, the Counter increments once per response containing it because each response is converted to a set. Thus feature counts equal the problem's popularity definition.

Sorting by negative count places every more-popular feature before every less-popular one. When counts tie, stability preserves the original feature order. These two ordering rules exactly define the required result.

The returned list is newly sorted; the input `features` list itself is not modified.

## Complexity detail

Let $W$ be the total number of response-word occurrences after splitting, $U$ the number of distinct words across responses, and $F$ the number of features. Tokenization, per-response set creation, and counter updates take expected $O(W)$ time using hashing.

Sorting $F$ features takes $O(F\log F)$ comparisons or key ordering work. Total time is $O(W+F\log F)$, matching the manifest.

The Counter can store $O(U)$ words, per-response set space is bounded by that response's distinct words, and the sorted result plus sort keys use $O(F)$ space. Peak storage is $O(F+U)$ as stated in the manifest.

Feature and response word lengths are bounded, so string hashing and comparison are treated as constant per word in this notation.

## Alternatives and edge cases

- **Filter response words to features:** Build a feature set and increment only recognized words, reducing Counter entries for irrelevant survey language.
- **Explicit pair sort:** Sort tuples `(-count, original index, feature)`. It makes tie behavior visible but stores an index map or decorated list.
- **Count raw split words:** It is incorrect because repeated words in one response would inflate popularity.
- **Substring search:** It would wrongly count feature `"lock"` inside response word `"locker"`.
- **Feature never mentioned:** Counter returns zero, and stable sorting preserves its order among other zero-popularity features.
- **All features tied:** The returned order is identical to `features`.
- **One response repeats a feature:** Its set contributes exactly one.
- **Feature appears in every response:** Its count is the number of responses and it sorts ahead of lower counts.
- **Non-feature words:** They may occupy Counter entries but never become output elements.
- **No duplicate features:** The constraint makes original-index tie ordering unambiguous.
- **Stable sort:** Correct tie handling relies on Python's documented stability.
- **Negative key:** It reverses only popularity direction without reversing tied elements.
- **Spaces:** `split()` handles the guaranteed formatting and would also tolerate extra whitespace.
- **Input preservation:** `sorted` returns a new list rather than rearranging `features` in place.
