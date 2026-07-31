## General

**The removed span can be treated as one interval.** Suppose an operation removes several characters whose first and last removed indices are `left` and `right`. Removing every remaining character between those endpoints does not change the score, because the span is still `[left, right]`, and deleting more characters cannot destroy the subsequence property of what remains. It is therefore sufficient to delete one contiguous interval from `t`, retaining a prefix `t[:i]` and a suffix `t[k:]`. The score is $k-i$.

**Prepare the suffix placements.** Scan `s` and `t` from right to left. For every suffix `t[k:]` that can be embedded in `s`, store the position in `s` used by its first character when the suffix is matched as far right as possible. Define the empty suffix `t[m:]` to begin at position $n$. Entries for suffixes that cannot be matched remain $-1$.

**Grow the retained prefix while moving one suffix boundary.** Greedily match `t` from left to right in `s`. Before consuming the next prefix character, `prefix_end` is the position of the last character used by the retained prefix `t[:i]`, with $-1$ for the empty prefix. Advance `k` until $k \ge i$ and the prepared start of `t[k:]` is strictly greater than `prefix_end`. Then the two retained pieces use disjoint, correctly ordered positions in `s`, so deleting `t[i:k]` is feasible and has score $k-i$.

Both greedy placements are extremal: the prefix ends as early as possible, and each suffix starts as late as possible. Thus, if those placements overlap, no other embedding of the same two pieces can separate them; if they do not overlap, their concatenation is a valid subsequence. As `i` increases, `prefix_end` and the smallest feasible `k` never move backward, so one forward suffix pointer examines every boundary at most once. Taking the minimum $k-i$ over all matchable prefixes includes deletion of a prefix, a middle interval, a suffix, all of `t`, and the empty interval.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$ and $m = \lvert\texttt{t}\rvert$. The right-to-left suffix scan, left-to-right prefix scan, and monotone suffix-boundary scan each move through their inputs at most once, for $O(n + m)$ time. The suffix-position array uses $O(m)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate deletion intervals:** Trying interval lengths and checking whether each remaining prefix-plus-suffix is a subsequence is direct, but can take cubic time when every candidate requires a full scan.
- **Binary search the score:** Feasibility is monotone in the allowed interval length, and prefix/suffix placement arrays can support a check, but the direct monotone merge already obtains the answer in linear time.
- **Already a subsequence:** The empty deletion interval is considered, so the result is $0$ when all of `t` can be matched.
- **Remove everything:** The empty retained string is always a subsequence, making $m$ a valid upper bound even when `s` and `t` share no characters.
- **Deletion at an end:** The empty prefix and empty suffix sentinels allow the optimal interval to be a prefix or suffix of `t`.
- **Noncontiguous original removals:** Filling the gaps between the first and last removed indices preserves the score and can only make matching easier, which justifies considering contiguous intervals only.
- **Repeated characters:** Greedy earliest-prefix and latest-suffix placements remain valid even when many equal characters offer multiple embeddings.
