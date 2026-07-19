## General
**Recognize pattern suffixes incrementally**

Build the KMP prefix table for `part`. At each pattern position, the table records the longest proper prefix of `part` that is also a suffix ending there. This lets a mismatch fall back to the next possible prefix without rescanning characters already processed.

Process `s` from left to right and append each character to a result stack. Beside every retained character, store the KMP match length after that character. The current match length therefore describes how much of `part` matches the suffix of the current retained string.

**Delete a match and restore the exposed boundary**

When the match length reaches $M$, the top $M$ stack characters are exactly one completed occurrence of `part`, so remove them together with their saved states. The KMP state preceding that occurrence is now again at the top of the state stack; restoring it makes the next input character continue matching across the deletion boundary.

Immediate deletion while scanning is equivalent to repeatedly removing the leftmost occurrence. A match is removed at the first position where its final character becomes available, before any later-starting occurrence can finish. Restoring the earlier state also detects every occurrence created by joining the surviving prefix to later characters.

## Complexity detail
Constructing the prefix table takes $O(M)$ time and space. Each of the $N$ source characters is pushed once and removed at most once; KMP fallback over the whole scan is amortized $O(N)$. The total time is $O(N + M)$ and the result, state stack, and prefix table use $O(N + M)$ space.

## Alternatives and edge cases
- **Repeated `find` and slicing:** This directly mirrors the statement, but rebuilding the string after every deletion can take $O(N^2)$ time.
- **Stack plus suffix comparison:** Checking the last $M$ characters after every push is easy to implement but takes $O(NM)$ time in the worst case.
- **No occurrence:** Every input character remains in its original order.
- **Pattern longer than the source:** No match is possible, so return `s` unchanged.
- **Overlapping occurrences:** `"aaaaa"` with `"aa"` removes the leftmost pairs successively and leaves `"a"`.
- **Boundary-created occurrence:** In `"aabcbc"` with `"abc"`, deleting the first match can expose another match spanning the joined boundary.
- **Complete deletion:** If every retained character belongs to a removed occurrence, return the empty string.
