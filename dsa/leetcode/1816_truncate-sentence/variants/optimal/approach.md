## General
**Locate the boundary after the retained prefix**

Because every separator is exactly one space, the first word ends at the first space, the second at the second space, and so on. Scan `s` from left to right while counting spaces. When the count reaches `k`, the current space is immediately after the `k`th word. Return the slice before that index so neither the separator nor any later word is included.

**Handle a prefix that is the whole sentence**

A sentence with $w$ words contains exactly $w-1$ spaces. If `k` equals $w$, the scan never encounters a `k`th space. In that case every word is retained, so return `s` unchanged.

**Why the scan returns exactly the requested words**

Before the `k`th separator there are exactly `k` non-empty word regions: one before the first separator and one between every adjacent pair of separators. The input guarantees that no empty regions arise from consecutive spaces. Slicing at that separator therefore returns precisely the first `k` words. If that separator does not exist, validity of `k` means all words were requested.

## Complexity detail
The scan examines at most the $n$ characters of `s` once, and constructing the returned prefix also takes at most $O(n)$ time. The returned string can contain $\Theta(n)$ characters, so total output-inclusive space is $O(n)$; the counter and index require only $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Split and join:** `s.split()` followed by joining the first `k` entries is concise and remains $O(n)$, but it constructs a list and separate word strings that the direct scan does not need.
- **Restart the scan for each boundary:** Finding the first boundary, then rescanning from the beginning for the second, and so on is correct, but it can examine the same prefix repeatedly and take $O(n^2)$ time.
- **Single-word sentence:** The scan finds no spaces and returns the only word, necessarily with `k = 1`.
- **Keep one word:** The first space ends the answer; if there is no space, the entire one-word sentence is returned.
- **Keep every word:** No `k`th space exists, so return `s` without creating a trailing separator.
- **Letter case:** Uppercase and lowercase letters are copied verbatim; they do not affect word boundaries.
