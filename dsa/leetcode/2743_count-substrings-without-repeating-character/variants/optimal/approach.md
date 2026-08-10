## General

**Count valid substrings by their right endpoint**

Instead of listing all substrings, process each position `i` as a right endpoint. Maintain the longest suffix ending at `i` that has no repeated character.

If that suffix begins at `j`, then every substring ending at `i` and starting at any position from `j` through `i` is also repetition-free. There are:

$$
i-j+1
$$

such substrings. Adding this number for every right endpoint counts each special substring exactly once.

**Maintain character frequencies in the current window**

`cnt` is a Counter for characters inside window `s[j:i+1]`. When new character `c=s[i]` enters, its count increases.

Before insertion, the previous window contains no duplicate. Therefore the only character that can now violate uniqueness is the newly added `c`. Testing `cnt[c] > 1` is enough; no other frequency changed.

**Shrink until c is unique again**

While `cnt[c] > 1`, remove the leftmost character:

- decrement `cnt[s[j]]`;
- increment `j`.

If the removed character is not `c`, the duplicate remains and shrinking continues. When the older occurrence of `c` is removed, `cnt[c]` becomes one and the window is valid again.

Counts of removed characters may become zero, but leaving zero entries in the Counter does not affect future increments or comparisons.

**Why the window is the longest valid suffix**

The loop moves `j` only while the current window is invalid and stops immediately once it becomes valid. At that moment, moving `j` one position back would reintroduce the older duplicate `c`. Hence no valid suffix ending at `i` can start earlier.

The maintained window is therefore not just some valid window; it is the longest distinct-character window ending at the current position.

**Why all suffixes of a valid window are valid**

Removing characters from a string cannot create a duplicate. Thus if `s[j:i+1]` has all distinct characters, every suffix `s[p:i+1]` for `j <= p <= i` is also distinct.

Starts before `j` are invalid by the minimal-left argument. This proves there are exactly `i-j+1` valid substrings ending at `i`.

**Trace s equal to abab**

At index zero, window `"a"` contributes one.

At index one, `"ab"` is distinct and contributes two: `"b"` and `"ab"`. Running total is three.

At index two, adding `'a'` duplicates the earlier `'a'`. Remove index zero, leaving `"ba"`. It contributes two, total five.

At index three, adding `'b'` duplicates the older `'b'`. Remove index one, leaving `"ab"`. It contributes two, total seven.

Every special substring from the example appears in exactly one of these endpoint groups.

**Trace all equal characters**

For `"ooo"`, each new `'o'` makes its count two. The loop removes the previous one immediately, keeping window length one. Each position contributes one, so the answer is three.

**Why the two pointers are linear**

The right pointer `i` advances once per character. The left pointer `j` never retreats and can advance at most $n$ times over the entire algorithm. Although a while loop is nested syntactically, its total iterations across all right endpoints are linear.

**Fixed alphabet and Counter storage**

The input contains only lowercase English letters, so at most 26 keys can have appeared. The Counter's size is therefore bounded independently of $n$.


After each shrink phase, the window contains no duplicate and has the smallest possible left endpoint among valid windows ending at `i`. Exactly its `i-j+1` suffixes are valid substrings ending there, and no earlier start is valid. Every substring has one unique right endpoint, so summing these exact endpoint counts counts all special substrings once and only once.

## Complexity detail

Let $n$ be the string length. Each character enters the window once through the outer loop and leaves at most once through the moving left pointer. Expected Counter operations are $O(1)$, so total time is $O(n)$.

The Counter stores at most 26 lowercase-character keys, giving $O(1)$ auxiliary space under the fixed alphabet. Scalars `ans`, `i`, `j`, and `c` are constant space.

The algorithm never creates substring copies; it represents the active substring only with indices and counts.

## Alternatives and edge cases

- **Enumerate every substring:** There are $O(n^2)$ substrings, and checking each separately adds further work.
- **Last-seen index array:** Set `j = max(j, last[c] + 1)` for another $O(n)$ solution without a shrink loop.
- **Boolean set window:** Works by deleting left characters until the duplicate disappears, with the same complexity.
- **Single character:** Contributes exactly one substring.
- **All characters distinct:** Every substring is special, producing $n(n+1)/2$.
- **All characters equal:** Only length-one substrings count, producing $n$.
- **Duplicate just outside window:** Does not matter because only current-window frequencies are tracked.
- **Zero Counter entries:** Harmless even though the exact code does not delete them.
- **Large answer:** Python integers hold the $O(n^2)$ count without overflow.
- **Lowercase guarantee:** Limits Counter space to 26 keys and justifies $O(1)$ space.
