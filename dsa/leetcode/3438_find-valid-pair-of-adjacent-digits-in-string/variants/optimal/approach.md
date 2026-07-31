## General

Whether a pair is valid depends on frequencies across the entire string, not merely on the two adjacent positions. Count all digit occurrences in one pass. Then examine adjacent characters from left to right, checking that they differ and that each stored frequency equals the digit's numeric value.

Return immediately when both frequency checks succeed. Because pairs are visited in increasing starting-index order, this is necessarily the first valid pair. If the scan ends, every adjacent pair has failed at least one required condition, so the empty string is correct.

## Complexity detail

Let $n$ be the length of `s`. Counting and scanning each take $O(n)$ time. The frequency table has at most nine entries because the alphabet is fixed to digits `1` through `9`, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recount each candidate digit:** Calling a full-string count for every adjacent pair is correct but can require $O(n^2)$ time.
- **Check only local occurrences:** A digit's required frequency concerns the entire string, so inspecting only the current pair is insufficient.
- **Equal adjacent digits:** They never form a valid pair, even when their global frequency matches their value.
- **Several valid pairs:** Return the leftmost one rather than collecting or sorting all matches.
- **No valid pair:** Return `""`, including when every adjacent pair contains equal digits.
