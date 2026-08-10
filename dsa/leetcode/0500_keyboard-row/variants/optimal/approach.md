## General

A word is valid when every distinct letter it uses belongs to one keyboard row. Repeated letters do not change that condition: if `"a"` is on the middle row, using it five times still uses only the middle row. This makes set containment a natural representation.

The solution creates three constant keyboard-row sets:

- `s1 = set('qwertyuiop')`;
- `s2 = set('asdfghjkl')`;
- `s3 = set('zxcvbnm')`.

Each set supports expected constant-time membership tests and exactly captures the lowercase letters allowed on that row.

**Normalize case without changing the returned word.** For each original word `w`, the code computes `w.lower()` before making its letter set. This treats uppercase and lowercase forms as the same keyboard key, as the contract requires. The original `w` itself is not replaced or modified; when a word is valid, the source appends `w` to `ans`, preserving its original capitalization.

For example, `"Alaska"` becomes lowercase `"alaska"` for testing. Its distinct-letter set is `{'a', 'l', 's', 'k'}`, and all four letters belong to `s2`. The returned result still contains `"Alaska"` rather than `"alaska"`.

**Discard multiplicity and test containment.** `s = set(w.lower())` keeps one copy of every letter used by the word. The expression `s <= s1` is Python's subset test: it is true exactly when every element of `s` is contained in `s1`. The same test is applied to the other two row sets.

The three conditions are joined with `or` because belonging wholly to any one row is sufficient:

`s <= s1 or s <= s2 or s <= s3`.

If the condition succeeds, the original word is appended. Otherwise at least two of its letters come from different rows, and the word is skipped.

Consider `"Hello"`. Its lowercase distinct letters include `h` and `l` from the middle row but also `e` and `o` from the top row. Its set is not a subset of any one keyboard row, so it is rejected. For `"Dad"`, lowercase distinct letters are `d` and `a`, both in the middle row, so it is accepted.

**Why checking distinct letters is sufficient.** Suppose the set of letters in a word is a subset of one keyboard row. Every position in the word contains one of those set members, so every character can be typed on that row. Conversely, if the word uses only one row, every distinct letter extracted from it must belong to that row, making the subset test true. The set transformation therefore preserves exactly the property being decided.

Correctness follows independently for every word. Lowercasing maps each English letter to the row of its case-insensitive key. Set construction records every key the word needs. The three subset checks accept exactly when one row contains all those keys. Appending only accepted original words produces precisely the required filtered list and keeps input order.

The constraints guarantee every word is nonempty and contains only English letters. Therefore the letter set is never empty, and characters such as punctuation or digits do not need a policy. If empty words were allowed, the empty set would be a subset of every row and this code would accept them vacuously.

The keyboard layout is fixed, so building the three row sets is constant work despite being done when the method is called. Their total size is twenty-six letters.

## Complexity detail

Let $c$ be the total number of characters across all input words. Lowercasing and building the set for one word takes time proportional to its length. Subset checks inspect at most the distinct letters of that word, at most twenty-six under the English alphabet. Across all words, total time is $O(c)$.

The three keyboard sets use $O(1)$ space because their contents are fixed. The temporary set for one word contains at most twenty-six letters, also $O(1)$ under the stated alphabet; if measured against an unrestricted alphabet, it is bounded by that word's length. The result holds references to accepted words and can contain total content $O(c)$ if output storage is included, matching the manifest's $O(c)$ bound.

## Alternatives and edge cases

- **Character-by-character row lookup:** Map each letter to a row number, use the first letter's row as the target, and reject any mismatch. This avoids constructing a per-word set and has the same linear time.
- **Regular expressions:** Three case-insensitive patterns can test the rows, but set containment states the condition more directly and avoids regex overhead.
- **Convert row strings repeatedly:** Testing every letter with `in` on short fixed strings is still effectively linear, but prebuilt sets make membership intent explicit.
- **Mixed capitalization:** Lowercasing is used only for validation, so output spelling and capitalization remain unchanged.
- **Repeated letters:** Set construction removes duplicates because multiplicity cannot introduce a new keyboard row.
- **One-letter word:** Its singleton set belongs to exactly one row, so it is always accepted.
- **Input order:** Words are considered once from left to right and appended immediately, so accepted words retain their original order.
- **English-letter guarantee:** The row sets cover all lowercase English letters. Unexpected symbols would make every subset check fail.
