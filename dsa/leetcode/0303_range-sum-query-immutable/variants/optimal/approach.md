## General

The array never changes after construction, but many range-sum queries may be asked. That makes preprocessing valuable: calculate cumulative information once, then reuse it for every query instead of adding the same elements repeatedly.

The source stores a prefix-sum array `self.s` with one extra leading zero. Its definition is

$$
\texttt{s}[k]=\sum_{i=0}^{k-1}\texttt{nums}[i].
$$

In words, `s[k]` is the sum of the first $k$ elements, which are the elements at indices 0 through $k-1$. It is also the sum of everything strictly before original index `k`.

This convention gives:

- `s[0] = 0`, because zero elements precede index 0;
- `s[1] = nums[0]`;
- `s[2] = nums[0] + nums[1]`;
- `s[n]` equals the sum of the complete array.

The constructor creates this structure with `accumulate(nums, initial=0)`. `accumulate` normally emits each running total after consuming an element. The `initial=0` argument first emits zero, so converting the result to a list produces exactly $n+1$ prefix boundaries.

**Why subtracting two prefixes isolates a range**

For an inclusive query `[left, right]`, `s[right + 1]` contains all values from index 0 through `right`:

$$
\texttt{s}[right+1]
=
\texttt{nums}[0]+\cdots+\texttt{nums}[left-1]
+
\texttt{nums}[left]+\cdots+\texttt{nums}[right].
$$

Meanwhile, `s[left]` contains exactly the portion before the requested range:

$$
\texttt{s}[left]
=
\texttt{nums}[0]+\cdots+\texttt{nums}[left-1].
$$

Subtracting cancels every element before `left`, leaving only the inclusive query range:

$$
\texttt{s}[right+1]-\texttt{s}[left]
=
\sum_{i=left}^{right}\texttt{nums}[i].
$$

This cancellation is the whole reason a query no longer needs a loop. Two already-computed cumulative totals encode the desired sum.

**Why `right + 1` is necessary**

Prefix index `k` is a boundary, not the index of the last included element. It represents the half-open original range `[0, k)`. To include original element `nums[right]`, the ending boundary must be one position after it, namely `right + 1`.

Using `s[right]` would sum only through original index `right - 1`, incorrectly excluding the query's last element. This is the most common off-by-one error in this pattern.

The left side does not need `left - 1`. Because `s[left]` already represents all elements strictly before `left`, it is exactly the amount that should be removed.

**Why the leading zero matters**

Suppose a query starts at index 0. There are no elements before the range, so the amount to subtract should be zero. With the leading prefix, `s[0]` supplies that zero naturally:

`s[right + 1] - s[0]`.

Without the leading zero, one common definition stores the sum through each index. Queries beginning at zero then require a separate conditional branch because there is no prefix at index `-1` that conceptually means zero. The extra element makes every valid query use the same formula.

It also makes a one-element query uniform. For `[i, i]`, the result is

$$
\texttt{s}[i+1]-\texttt{s}[i]=\texttt{nums}[i].
$$

Adjacent prefix boundaries differ by exactly the original element between them.

**Tracing the example**

For `nums = [-2, 0, 3, -5, 2, -1]`, the constructor builds:

| Prefix boundary `k` | Elements included | `s[k]` |
| --- | --- | --- |
| 0 | none | 0 |
| 1 | `[-2]` | -2 |
| 2 | `[-2, 0]` | -2 |
| 3 | `[-2, 0, 3]` | 1 |
| 4 | `[-2, 0, 3, -5]` | -4 |
| 5 | `[-2, 0, 3, -5, 2]` | -2 |
| 6 | all elements | -3 |

The query `[0, 2]` returns `s[3] - s[0] = 1 - 0 = 1`.

The query `[2, 5]` returns `s[6] - s[2] = -3 - (-2) = -1`.

The query `[0, 5]` returns `s[6] - s[0] = -3`, the sum of the full array.

Negative values do not disrupt the method. Prefix totals need not be increasing; they only need to preserve exact cumulative sums so subtraction can cancel the unwanted prefix.

**Why preprocessing remains valid**

The class is specifically for an immutable array. After `self.s` is built, no operation changes `nums`. Therefore, every stored prefix continues to describe the data used by all later queries.

The object does not need to retain the original list separately because every possible inclusive range sum can be derived from two entries in `self.s`. The prefix array is a complete sufficient summary for this query type.

For each query, the constraints guarantee `0 <= left <= right < len(nums)`. Therefore, both `self.s[left]` and `self.s[right + 1]` are valid indices in the $n+1$-element prefix list.

## Complexity detail

Let $n$ be the array length and $q$ the number of `sumRange` calls.

The constructor's `accumulate` operation visits each input element once, and converting its output to a list stores $n+1$ totals. Construction costs $O(n)$ time.

Each query performs two indexed reads and one subtraction. None of those operations depends on the range width, so one `sumRange` call costs $O(1)$ time. Across all queries, total query work is $O(q)$, and the complete constructor-plus-queries time is $O(n+q)$.

The prefix list contains $n+1$ integers, which is $O(n)$ space. Each query uses only constant temporary state. The returned integer is computed directly without allocating a slice of the original array.

Python integers expand as needed, so sums near the largest possible magnitude do not overflow a fixed-width integer. The asymptotic analysis treats arithmetic on the problem's bounded totals as constant time.

## Alternatives and edge cases

- **Sum every query directly:** Loop from `left` through `right`. It uses $O(1)$ extra space but costs $O(right-left+1)$ per query and can repeat the same additions up to $10^4$ times.
- **Precompute every possible range:** Store a sum for all pairs `(left, right)`. Queries become constant-time, but construction and storage both grow to $O(n^2)$, far more than the one-dimensional prefix array requires.
- **Fenwick tree:** It supports prefix sums and point updates in $O(\log n)$ time. Updates are absent here, so its logarithmic queries and more complex indexing are unnecessary compared with $O(1)$ prefix subtraction.
- **Segment tree:** It supports mutable range queries but needs more code and $O(\log n)$ query time. Immutability lets prefix sums do better.
- **Prefix sums without a leading zero:** This works with a special case for `left == 0`, but the exact source's leading zero gives one formula for every query.
- **Using `s[right] - s[left]`:** This excludes `nums[right]` because prefix indices represent half-open boundaries. The correct ending index is `right + 1`.
- **Using `s[right + 1] - s[left + 1]`:** This also removes `nums[left]`, turning an inclusive range into one that begins after `left`.
- **Single-element range:** `[i, i]` returns the difference of adjacent prefixes, exactly `nums[i]`.
- **Full-array range:** `[0, n - 1]` returns `s[n] - s[0]`, the complete sum.
- **One-element input:** The prefix list is `[0, nums[0]]`, and the only valid query returns their difference.
- **All zeros:** Every prefix is zero, and every range sum is zero.
- **Negative numbers:** Prefix values may fall as elements are added, but algebraic cancellation remains exact.
- **Mixed signs with a zero total:** Equal prefix totals at different boundaries correctly indicate that the intervening range sums to zero.
- **Repeated queries:** No cache lookup keyed by the query is needed; every query is already constant-time, whether repeated or new.
- **Mutation after construction:** If the original data could change, stored prefixes would become stale from the changed index onward. The immutable contract is what makes one-time preprocessing correct.
- **Bounds guarantee:** The method performs no explicit index validation because every query is guaranteed to satisfy `0 <= left <= right < n`.
