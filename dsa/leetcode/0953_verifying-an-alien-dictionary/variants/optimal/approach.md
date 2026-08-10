## General

**Translate alien letters into numeric ranks**

The dictionary comprehension `{c: i for i, c in enumerate(order)}` maps each alien character to its position in the supplied alphabet. A smaller rank means the character comes earlier.

The checked-in solution then scans character positions from zero through nineteen, matching the maximum word length in the contract. At each position it converts every word's character to a rank. If a word has already ended, it uses sentinel `-1`, which is smaller than every real rank. This sentinel is intended to encode the rule that a shorter prefix comes before a longer word.

**What the implementation checks at one position**

For a fixed character index `i`:

- `prev` stores the previous word's rank at this position;
- `curr` is the current word's rank or `-1` when it has ended;
- if `prev > curr`, the function immediately returns false;
- if `prev == curr`, `valid` becomes false.

If the entire column is non-decreasing and contains no equal adjacent ranks, `valid` remains true and the method returns true.

If some adjacent words tie at this position, the scan continues to the next character position.

**The intended lexicographic idea**

For any one adjacent pair of words, lexicographic comparison should ignore equal prefix characters, then decide the pair using its first differing position. If no differing position exists, the shorter word must come first.

A correct linear approach normally compares adjacent word pairs independently. Once a pair is decided by an earlier character, later characters of that pair are irrelevant.

The rank map and ended-word sentinel are useful ingredients for this comparison.

**Why the exact implementation is not generally correct**

This solution scans an entire character column across all words and does not remember which adjacent pairs were already decided by earlier characters.

Consider alien order equal to the ordinary alphabet and:

`words = ["aa", "ab", "ba"]`.

This list is correctly sorted:

- `"aa" < "ab"` because their first characters tie and `a < b` at the second position;
- `"ab" < "ba"` because `a < b` at the first position. Their second characters no longer matter.

At position zero, ranks are `a, a, b`. They are non-decreasing, but the first pair ties, so `valid` becomes false and the code continues.

At position one, ranks are `a, b, a`. The transition from `b` to `a` makes `prev > curr`, so the method returns false. That comparison belongs to `"ab"` versus `"ba"`, but this pair was already correctly ordered at position zero. The later reversal should have been ignored.

Therefore, a correctness proof for the stated problem cannot be given for the exact checked-in code. The approach is a column-wise heuristic rather than a correct general lexicographic verifier.

**Cases it does handle**

The code correctly detects a direct descending rank at the earliest column when all earlier adjacent relationships remain tied. It also detects the prefix violation `["apple", "app"]`: once the shorter word ends, its sentinel `-1` follows a real rank from the longer word, triggering `prev > curr`.

It returns true early when one position strictly increases across every adjacent pair, because all pairs are then decided at that position or earlier.

These successful cases do not repair the missing per-pair resolved state.

**How the optimal logic should work**

For each adjacent pair `a = words[k]` and `b = words[k + 1]`:

1. scan positions only up to the shorter length;
2. skip equal characters;
3. at the first difference, require `rank[a[i]] < rank[b[i]]` and stop comparing that pair;
4. if every shared position ties, require `len(a) <= len(b)`.

If every adjacent pair passes, transitivity proves the whole list is sorted.

This corrected structure processes each character only until its pair is decided and uses `O(S)` time, where `S` is total input characters.

## Complexity detail

The exact code performs at most twenty position scans over every word. Because maximum word length is fixed at twenty by the contract, its time is `O(S)` or equivalently `O(20N) = O(N)` for `N` words.

The rank map has exactly twenty-six entries, and all other state is scalar, so auxiliary space is `O(1)`.

These complexity bounds describe execution cost, not correctness. A fast algorithm can still implement the wrong comparison rule.

## Alternatives and edge cases

- **Adjacent-pair comparison:** This is the correct optimal approach. Preserve the first-difference rule separately for each neighboring pair.
- **Transform whole words into rank arrays:** Python can compare transformed sequences lexicographically, but constructing all arrays uses `O(S)` extra space.
- **Already ordered by first characters:** The exact implementation returns true when that column is strictly increasing across all words.
- **Proper prefix:** `"app"` must come before `"apple"`; the ended sentinel represents this direction.
- **Longer word before its prefix:** `"apple"` before `"app"` must return false.
- **Single word:** It is always sorted. The exact code eventually returns true, though it scans more positions than necessary.
- **Repeated identical words:** They are lexicographically equal and valid. The exact loop continues through all positions and returns true.
- **Previously decided pairs:** Later characters must be ignored for those pairs; failure to track this is the checked-in defect.
- **Twenty-character bound:** The hard-coded `range(20)` depends on the current constraint and would be wrong if longer words were allowed.
- **Rank map:** Native English character order must not be used because the alien alphabet may be any permutation.
