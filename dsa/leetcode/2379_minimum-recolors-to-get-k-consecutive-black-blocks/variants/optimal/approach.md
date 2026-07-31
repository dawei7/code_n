## General

If a particular contiguous length-`k` window is chosen as the final black run, every white block inside it must be recolored and every black block already satisfies the goal. The cost of that window is therefore exactly its number of `'W'` characters.

**Initialize the first candidate.** Count white blocks in `blocks[:k]`. This is both the current window cost and the best cost seen so far.

**Slide by one block.** When the right boundary advances, remove the contribution of the character leaving at index `right - k` and add the contribution of the new character at `right`. Record the smallest rolling white count across all windows.

Every possible location of `k` consecutive blocks appears once during the scan. The maintained count equals the recolors required for that location, so the minimum recorded count is exactly the fewest operations capable of producing at least one valid run.

## Complexity detail

Let $n = \lvert\texttt{blocks}\rvert$. Initializing the first window takes $O(k)$ time and all subsequent updates take $O(n-k)$ time, for $O(n)$ total. Only the current count and best count are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Rescan every window:** Counting white blocks from scratch for each starting position is correct but takes $O(nk)$ time, which becomes $O(n^2)$ when `k` grows with `n`.
- **Prefix sums:** A prefix count of white blocks answers every window in constant time after $O(n)$ preprocessing, but uses $O(n)$ space.
- **Existing run:** If some window contains no white blocks, the answer is zero.
- **All white:** Every candidate window costs exactly `k`.
- **Full-length window:** When `k = n`, count white blocks in the entire string once.
- **Single block:** For `k = 1`, the answer is zero if any black block exists and one otherwise.
