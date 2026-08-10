## General

**What one operation really changes.** An operation removes two elements only when their values are different. The positions of those elements do not otherwise matter: after deletion, the remaining elements keep their order, but no future choice depends on adjacency. It is therefore useful to forget the individual indices and keep only the frequency of each distinct value. If the multiset has frequencies such as `4, 3, 1`, one operation chooses two different frequency buckets and subtracts one from each.

The protected solution implements exactly that multiset view. `Counter(nums)` creates the frequency table. It then negates every frequency and places the negated values in `pq`. Python's heap is a min-heap, so the most negative entry represents the largest remaining frequency. Negation is the standard way to use a min-heap as a max-heap.

**Why always take the two largest buckets.** The obstruction is concentration. A value cannot be paired with another copy of itself, so copies of the most frequent value need copies of all other values as partners. If one bucket is allowed to remain much larger than the rest, those surplus copies can eventually become impossible to remove. Taking one item from each of the two largest buckets reduces the greatest concentrations as evenly as possible.

There is also an exchange argument. Suppose a valid next operation uses a smaller nonempty bucket while leaving a larger bucket untouched. Replace that chosen smaller bucket by the untouched larger one. The operation is still legal because the two chosen buckets represent distinct values. Afterward, the new frequency vector is no more concentrated than before: the larger bucket has decreased, while the smaller one has not. That replacement cannot reduce the number of pairs that can ultimately be removed. Repeating the exchange shows that some maximum-length sequence of removals always begins with the two largest frequencies. Thus the heap's greedy choice is safe at every iteration.

**Following the implementation line by line.** `ans` begins as `len(nums)`, the number of elements still present before any operation. While at least two distinct values remain, the code pops the two largest frequencies into `x` and `y`. It subtracts one from both because one copy of each value has just been removed. A positive remainder is pushed back; a zero remainder disappears, accurately representing an exhausted value. Finally, `ans -= 2` records the two removed elements. When the heap contains zero or one frequency, no legal pair remains. Returning `ans` therefore returns the minimum reachable length.

For a small trace, consider frequencies `3, 2, 1`. The heap first chooses `3` and `2`, leaving `2, 1, 1`; it then chooses two of the largest buckets, leaving `1, 1`; and the final pair leaves nothing. For frequencies `4, 1, 1`, two operations can use the two minority copies as partners, but the remaining two copies of the majority value are equal and cannot be paired. The returned length is `2`.

**A closed-form way to understand the answer.** Let $n$ be the original length and let $m$ be the largest frequency. If $m \le n-m$, the most frequent value has enough differently valued partners. Pairing can continue until at most one item remains, so parity forces a remainder of $n \bmod 2$. If $m>n-m$, every one of the $n-m$ minority items can remove only one majority item, leaving

$$
m-(n-m)=2m-n
$$

copies. Hence the mathematical answer is $\max(n\bmod 2,\,2m-n)$. The heap simulation reaches that same bound, although it computes it operation by operation.

**An important implementation-versus-manifest distinction.** The manifest describes a linear scan over sorted runs with constant auxiliary space. That is not what the protected Python source does. The source builds a `Counter`, builds a heap, and performs heap operations for every removed pair. This document explains the executable source rather than silently attributing a different algorithm to it.

## Complexity detail

Let $n$ be the number of elements and $u$ the number of distinct values. Building the counter takes expected $O(n)$ time and stores $u$ entries. Creating and heapifying the frequency list takes $O(u)$ time. Every loop iteration removes one legal pair, so there are at most $\lfloor n/2\rfloor$ iterations. Each iteration performs two heap pops and up to two pushes, each costing $O(\log u)$ in the worst case. The exact implementation therefore takes $O(n\log u)$ worst-case time after counting, or $O(n+n\log u)=O(n\log u)$ overall.

The counter and heap each contain at most $u$ entries, so auxiliary space is $O(u)$. Because $u$ can equal $n$, worst-case auxiliary space is $O(n)$. These are the real bounds of the checked-in solution; the manifest's `O(n)` time and `O(1)` space describe the simpler sorted-run formula, not this heap implementation. The returned integer and scalar variables use constant additional space.

## Alternatives and edge cases

- **Sorted-run formula:** Because `nums` is already non-decreasing, scan once to find the maximum run length $m$, then return $\max(n\bmod 2,2m-n)$. This genuinely achieves $O(n)$ time and $O(1)$ auxiliary space and is the best match for the manifest.
- **Two-pointer pairing:** Pair elements from the first half with sufficiently larger elements from the second half. This also exploits sorted order, but the frequency formula is shorter and makes the unavoidable remainder more explicit.
- **Only one distinct value:** The heap starts with one entry, the loop never executes, and the answer remains $n$. No two equal values form a legal pair.
- **Perfectly balanceable even length:** When the largest frequency is at most $n/2$, every item can be removed and the result is `0`.
- **Perfectly balanceable odd length:** Pair removals always change the length by two, so an odd array cannot become empty. The best possible remainder is `1`.
- **Large majority:** If one value occurs more often than all other values combined, every minority copy is consumed as a partner and exactly $2m-n$ majority copies remain.
- **Input ordering:** The heap solution does not actually use the promised sorted order; it remains correct for an unsorted array. The constant-space formula alternative does rely on sorted runs.
