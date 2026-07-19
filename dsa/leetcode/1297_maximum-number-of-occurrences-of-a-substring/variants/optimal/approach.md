## General
**Why only the shortest permitted length is needed**

Suppose a valid substring of length greater than `minSize` occurs $f$ times. Its length-`minSize` prefix appears at each of those same starting positions, cannot contain more distinct characters than the longer substring, and is therefore also valid. That prefix occurs at least $f$ times. Consequently, no longer candidate can produce an answer larger than the best valid substring of the minimum length.

**Count fixed windows**

Slide one window of length `minSize` across `s`. Maintain the frequency of each letter and a distinct-letter counter as the right edge enters and the left edge leaves. Whenever the full window uses at most `maxLetters` distinct characters, increment that exact window string in a frequency map and update the maximum.

Every eligible starting position is examined once. The prefix argument proves that restricting the scan to `minSize` does not discard a potentially better answer, while the map counts overlapping occurrences naturally.

## Complexity detail
There are $O(n)$ fixed-length windows. Updating the 26-letter frequency table is constant time, and materializing a window costs at most 26 character operations because `minSize` is bounded by 26. Thus the total time is $O(n)$. The substring-frequency map can contain $O(n)$ keys and uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every allowed length:** This is correct, but repeats work for lengths that cannot improve on their minimum-length prefixes.
- **Compare every pair of windows:** Directly recounting each candidate's occurrences can take $O(n^2)$ time.
- **No valid window:** If every minimum-length window exceeds `maxLetters`, the frequency map stays empty and the answer is $0$.
- **Overlapping occurrences:** Advancing the window by one position ensures overlaps are counted.
- **`minSize = maxSize`:** The same fixed-window scan applies without special handling.
- **Repeated single character:** With `minSize = 1`, every matching position contributes to that character's frequency.
