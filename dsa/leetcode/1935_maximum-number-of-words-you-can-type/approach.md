## General

**Reduce each word to a membership test**

A word can be fully typed exactly when none of its characters belongs to `brokenLetters`. The solution first converts the broken-letter string to a set:

`s = set(brokenLetters)`.

Set membership is expected $O(1)$, so each keyboard check becomes the direct question `c not in s`. The contract says broken letters are distinct, but using a set would also harmlessly remove duplicates.

Next, `text.split()` produces the words in order. The input guarantees single spaces with no leading or trailing space, so this yields exactly the intended words and no empty strings. The no-argument form of `split` would also tolerate runs of whitespace, though that extra behavior is not needed here.

For a word `w`, the expression

`all(c not in s for c in w)`

is true only when every character passes the working-key test. Python's `all` short-circuits: as soon as one broken character is found, the remaining characters of that word need not be inspected because the word is already impossible to type.

**Convert Boolean results into the answer**

The outer generator produces one Boolean per word. In Python, `True` has integer value one and `False` has integer value zero when summed. Therefore

`sum(all(...) for w in text.split())`

counts exactly the words for which every character is typeable.

For `text = "hello world"` and `brokenLetters = "ad"`, the set is `{"a", "d"}`. Every letter of `"hello"` is outside it, so `all` returns true and contributes one. The scan of `"world"` eventually reaches `d`, returns false, and contributes zero. The result is one.

**Why checking every character is necessary**

A word must be typed in full. Finding one working character says nothing about its other letters, so `any` would express the wrong rule. Conversely, one broken occurrence is enough to reject the whole word, even when every other occurrence is typeable.

Repeated letters need no special counting. If a repeated character is broken, the first occurrence makes `all` false. If it works, all occurrences pass the same constant-time membership check.

**Why the result is correct**

Take any word from `text`. If the generator for that word returns true, every character is absent from the broken-key set, so all required keys work and the whole word can be typed. If it returns false, some character belongs to the broken set, so at least one required keystroke is impossible and the word cannot be fully typed. Thus the Boolean produced for each word exactly represents its eligibility.

Summing those Booleans adds one for every and only typeable word. Since `split` enumerates all input words once, the returned count is correct.

**Why a set is the right lookup structure**

One could search the short `brokenLetters` string for every text character. Since there are at most 26 lowercase letters, that would still be linear in `text` under a fixed-alphabet analysis. A set states the intent clearly and gives expected constant-time membership even if the alphabet restriction changes.

The broken set is built once rather than once per word. Building it inside the generator would repeat identical work and allocate many temporary sets.

## Complexity detail

Let $N$ be the length of `text` and $B$ the length of `brokenLetters`.

Building the set costs $O(B)$ expected time. Splitting scans `text` in $O(N)$ time. Across all words, `all` examines each letter at most once; short-circuiting may examine fewer, but the worst case is $O(N)$. Total expected time is $O(N+B)$, which is $O(N)$ here because $B\le26$.

The broken set uses $O(B)$ space, which is $O(1)$ under the fixed 26-letter alphabet. However, the exact Python call `text.split()` creates a list of word strings whose combined size is $O(N)$. Therefore the concrete implementation has $O(N)$ peak auxiliary allocation, not strict $O(1)$. A single streaming scan over `text` could achieve the manifest's constant-space bound.

The generator expressions themselves are lazy and use only constant iteration state. The materialized list returned by `split` is the source of the linear temporary space.

## Alternatives and edge cases

- **Streaming character scan:** Track whether the current word has encountered a broken key, count it at each space, and handle the final word afterward. This gives $O(N+B)$ time and $O(B)$ space without materializing word substrings.
- **Set intersection per word:** `set(w).isdisjoint(s)` is expressive but allocates another set for every word. The exact `all` approach can short-circuit and avoids those sets.
- **Search the broken string directly:** Testing `c not in brokenLetters` avoids building a set but costs $O(B)$ per tested character; with $B\le26$ it is still asymptotically linear but has a less robust bound.
- **No broken letters:** The set is empty, every membership test succeeds, and all words are counted.
- **Every word contains a broken letter:** Every inner `all` is false and the result is zero.
- **A broken letter repeated in one word:** The first encountered occurrence rejects the word; later occurrences need not be scanned.
- **Single word:** `split` returns a one-element list, and the method returns either zero or one.
- **Single-character word:** It is typeable exactly when that character is absent from the broken set.
- **Shared broken character across words:** Each affected word is rejected independently, as required.
- **Spaces are not keys being tested:** Splitting removes separators before character checks, so a space can never make a word fail.
- **Input formatting guarantee:** Single separators and no outer spaces ensure no empty words. The chosen `split()` would also ignore extra whitespace if it appeared.
- **Exact-space caveat:** Although the fixed broken-letter set is constant-sized, the word list and substring objects created by `split` make this source $O(N)$ in peak auxiliary space.
