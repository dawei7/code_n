## General

Define an edge indicator for every index $i>0$: it is one when `s[i - 1] == s[i]` and zero otherwise. For any current substring `s[l..r]`, its minimum deletion count equals the sum of the indicators at indices $l+1$ through $r$.

To see why, divide the substring into maximal runs of equal characters. Consecutive runs necessarily alternate between `'A'` and `'B'`. Keeping one character from every run therefore produces an alternating subsequence, deleting exactly the run length minus one from each run. Those deletions total the number of equal adjacent pairs. No alternating subsequence can retain two characters from one run without selecting an intervening opposite character that does not exist inside that run, so no smaller deletion count is possible.

Store the edge indicators in a Fenwick tree. A type-2 query becomes the difference of two prefix sums. Flipping `s[j]` can change only the edges joining `j` to `j - 1` and `j + 1`; subtract each affected edge's old indicator, flip the character, and add each edge's new indicator.

Because a range query never changes the character array and a flip repairs precisely the two potentially stale edges, the structure always represents the current string. Each returned sum is consequently the proven minimum for the requested current substring.

## Complexity detail

Let $N=\lvert s\rvert$ and $Q=\lvert\texttt{queries}\rvert$. Building and processing with a Fenwick tree takes $O((N+Q)\log N)$ time; a linear segment-tree build gives the same overall bound. The character buffer and range-sum structure use $O(N)$ space, excluding the returned answers.

## Alternatives and edge cases

- **Segment tree:** It offers the same $O(\log N)$ point updates and range sums, but uses a larger array and more update bookkeeping than the Fenwick tree used here.
- **Direct substring scan:** Counting equal adjacent pairs separately for every type-2 query is simple and correct but may require $O(NQ)$ time.
- **Length-one range:** It contains no internal edge, so its answer is always `0`.
- **Endpoint flip:** Flipping index `0` or `N - 1` changes only one edge rather than two.
- **Repeated flip:** Flipping the same position twice restores both its character and its incident edge indicators.
- **Query state:** Type-1 operations mutate the string for later queries, while type-2 operations never alter it.
- **Answer order:** Only type-2 queries append results; update queries do not create placeholders.
