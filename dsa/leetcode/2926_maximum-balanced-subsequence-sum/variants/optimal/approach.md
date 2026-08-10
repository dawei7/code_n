## General

For consecutive selected indices $p<i$, the balanced condition is

$$
\texttt{nums}[i]-\texttt{nums}[p]\ge i-p.
$$

Move the index terms to the same sides:

$$
\texttt{nums}[p]-p\le \texttt{nums}[i]-i.
$$

Define transformed key `key[i] = nums[i] - i`. A subsequence is balanced exactly when its transformed keys are non-decreasing in selected-index order. The original values, not the keys, are still what we add to the score.

This converts the problem into a maximum-sum subsequence with a key-order restriction. When processing index $i$, we need the greatest subsequence sum among earlier endpoints whose key is at most `key[i]`.

**Dynamic-programming recurrence**

Let `best[i]` be the maximum sum of a balanced subsequence ending at $i$. Any such subsequence either starts at $i$ or extends an earlier balanced subsequence ending at $p<i$ with `key[p] <= key[i]`:

$$
\texttt{best}[i]
=
\texttt{nums}[i]
+
\max\left(
0,
\max_{\substack{p<i\\\texttt{key}[p]\le\texttt{key}[i]}}
\texttt{best}[p]
\right).
$$

The zero means “start a new length-one subsequence.” This is necessary when every compatible earlier sum is negative: including one would reduce the score, while a single element is always balanced.

A direct implementation would scan all earlier $p$ for every $i$, taking $O(n^2)$. The source uses a Fenwick tree of prefix maxima to answer the inner maximum.

**Compress transformed keys**

Keys can be negative and as large in magnitude as the input values. Fenwick coordinates must be positive, dense indices. The source builds `arr = [x - i ...]`, removes duplicates, and sorts them into `s`.

For current key `x - i`, `bisect_left(s, x - i) + 1` gives its one-based compressed coordinate `j`. Sorted order is preserved:

$$
\texttt{key}[p]\le\texttt{key}[i]
\quad\Longleftrightarrow\quad
\texttt{coord}[p]\le\texttt{coord}[i].
$$

Equal keys share a coordinate and are compatible because the inequality is non-strict.

**Fenwick tree stores maximum sums**

`tree.query(j)` returns the largest DP value previously inserted at any compressed coordinate from $1$ through $j$. Those are precisely earlier endpoints with compatible keys.

The current value is

`v = max(tree.query(j), 0) + x`.

The method then calls `tree.update(j, v)`. The query occurs before the update, so the current element cannot extend itself. At each Fenwick ancestor, update keeps a maximum rather than adding values.

If multiple earlier indices have the same key, only their greatest ending sum matters to future elements. Discarding smaller sums at the same coordinate is safe because every future compatibility test treats those endpoints identically.

**Why querying the entire tree gives the answer**

Every nonempty balanced subsequence has some final selected index. When that index was processed, its optimal ending sum was inserted. `tree.query(len(s))` takes the maximum over every key coordinate and therefore over every possible endpoint.

This also handles arrays containing only negative values. Each `v` can start from zero and equal the current negative number. Although the tree begins with negative infinity, at least one value is inserted, and the final query returns the least negative single-element choice rather than an invalid empty sum of zero.


By induction, assume every earlier inserted value is the best balanced sum for its endpoint. The prefix query considers exactly all endpoints that may legally precede $i$. Extending the greatest positive one is optimal; if none is beneficial, starting at $i$ is optimal. Thus `v` equals `best[i]`.

Every constructed extension preserves increasing indices because processing is left to right, and it preserves the balanced inequality because the queried key is no larger. Conversely, every valid predecessor is inside the queried prefix, so no better legal extension is missed. The maximum over all inserted endpoints is consequently the global optimum.

## Complexity detail

Creating transformed keys takes $O(n)$ time. Deduplicating and sorting them takes $O(n\log n)$. Each of $n$ elements performs one binary search, one Fenwick query, and one Fenwick update, each $O(\log n)$. Total time is $O(n\log n)$.

The transformed list, sorted unique keys, and Fenwick array each contain $O(n)$ values, so auxiliary space is $O(n)$. The source does not store a separate `best` array because the tree retains all information future states require.

## Alternatives and edge cases

- **Quadratic DP:** Test every earlier endpoint and apply the transformed-key inequality directly. It is simple but costs $O(n^2)$.
- **Segment tree:** It can provide the same prefix maximum with $O(n\log n)$ time, but a Fenwick maximum tree is smaller for prefix-only queries.
- **All values negative:** Starting from zero before adding the current value ensures the answer is the greatest single value, not the empty subsequence.
- **Equal transformed keys:** They are compatible and share one compressed coordinate; update retains their best sum.
- **Negative compatible prefix:** Extending it would hurt, so `max(query, 0)` correctly starts anew.
- **Length-one subsequence:** It is always balanced and is represented by the zero-extension case.
- **Do not sort the input:** Elements must remain in original index order. Only distinct key values are sorted for coordinate mapping.
- **Non-strict key condition:** Using a query below coordinate `j` would wrongly exclude equality. The exact source queries through `j`.
- **Fenwick initialization:** Negative infinity represents no prior subsequence. Initializing nodes to zero would still help starts but would blur reachability and make the all-negative reasoning less explicit.
