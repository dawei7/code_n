## General

**Maintain the longest valid window ending at each position**

Move `right` across the string and count the new `character` inside the current window `[left, right]`. Adding one
character may temporarily introduce a third distinct value.

While the count map has more than two keys, remove `s[left]` and advance `left`. Delete a key exactly when its count
reaches zero; otherwise the map would incorrectly treat a character outside the live window as still present. Stop
as soon as the window is valid again, then update `best` with its length.

The left boundary moves only when validity requires it. After contraction, moving `left` backward would restore the
third character that forced the shrink, so the maintained interval is the longest valid substring ending at the
current `right`. Every candidate substring has some right endpoint, and taking the maximum of these per-endpoint
optima yields the global answer.

Both boundaries move monotonically. A character can enter through `right` once and leave through `left` once, even
when frequent changes among three letters cause several removals in one iteration.

## Complexity detail

Each of the $n$ characters enters and leaves the sliding window at most once, giving $O(n)$ time. The map has at
most three keys before contraction and at most two afterward. Because the source alphabet is fixed to English
letters, this is $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Restart a scan at every position:** is correct but takes $O(n^2)$ time when long suffixes remain valid.
- **Track last positions for two characters:** can also achieve linear time but requires careful selection of the
  character whose most recent occurrence is earlier.
- **Enumerate character pairs:** repeats work across the fixed alphabet and is less direct than one sliding window.
- A one-character string is entirely valid.
- A string containing only one or two distinct characters returns its full length.
- Rapid alternation among three or more characters can trigger repeated contraction, but no left position is removed
  twice.
