## General
**Reverse the direction of the question**

At index `i`, the desired count concerns only the suffix after `i`. Scanning from right to left turns that suffix into the set of values already processed. The remaining operation is dynamic: count processed values smaller than `nums[i]`, then insert `nums[i]` for the next iteration.

A plain set cannot answer how many stored values lie below a threshold, and a sorted list makes insertion linear. A Fenwick tree supports both prefix-frequency queries and single-rank updates in logarithmic time.

**Compress values without changing comparisons**

Array values may be negative, large, or widely spaced, whereas a Fenwick tree uses dense positive indices. Sort the distinct values and assign ranks starting at one. Rank order exactly preserves numeric order: $a < b$ if and only if $\operatorname{rank}(a) < \operatorname{rank}(b)$.

The tree stores frequencies rather than mere presence, so duplicates remain separate processed elements. For a value at rank `r`, querying the prefix through $r - 1$ counts only strictly smaller values. Equal values at rank `r` are deliberately excluded.

**Query before inserting the current value**

Process `[5, 2, 6, 1]` from the end. After inserting `1`, the query for `6` returns one. After inserting `6`, the query for `2` also returns one. When `5` is reached, the stored suffix is `{2, 6, 1}` and the prefix below rank `5` contains two elements.

Before each query, the Fenwick frequencies represent exactly the elements at indices greater than the current index. The prefix below the current rank therefore equals the required count. Inserting the current value restores the same statement for the next index to the left, so every result position is correct.

## Complexity detail
Sorting at most `n` distinct values costs $O(n \log n)$. Each of the `n` elements performs one Fenwick prefix query and one update, each in $O(\log n)$ time, so total time is $O(n \log n)$. The ranks, frequency tree, and result use $O(n)$ space.

## Alternatives and edge cases
- **Compare every pair:** is direct and correct but takes $O(n^2)$ time, especially on descending input.
- **Modified merge sort:** can count right-half elements moved before each left-half element in $O(n \log n)$ time and is an equally strong solution.
- **Insert into a sorted array:** permits logarithmic search but still requires linear shifting per insertion.
- Equal values do not count one another. Negative numbers need no special handling after coordinate compression, and a one-element array returns `[0]`.
