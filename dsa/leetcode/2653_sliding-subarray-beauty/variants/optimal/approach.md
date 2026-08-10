## General

**Exploit the tiny value domain**

Values lie only between $-50$ and $50$. Instead of sorting every length-$k$ window, the solution stores a frequency for each possible value.

Array `cnt` has 101 entries. Value $v$ maps to index:

$$
v+50.
$$

Thus:

- $-50$ maps to zero;
- $-1$ maps to 49;
- zero maps to 50;
- 50 maps to 100.

Frequency updates are constant time when the window slides.

**Initialize the first window**

For each value in `nums[:k]`, the code increments `cnt[v + 50]`.

After this pass, `cnt[r]` equals the number of occurrences of value $r-50$ in the first window.

The first beauty is computed immediately and placed in `ans`. Since $1\le k\le n$, there is always at least one window.

**Find the x-th smallest negative value**

Helper `f(x)` scans indices zero through 49, corresponding in ascending order to negative values $-50$ through $-1$.

Variable `s` accumulates frequencies:

$$
s
=
\#\{\text{negative window values}\le i-50\}.
$$

The first index where `s >= x` represents the x-th element in the sorted multiset of negative values. The helper returns `i - 50`.

If the scan finishes with cumulative negative count below $x$, fewer than $x$ negative numbers exist and the required beauty is zero.

**Why nonnegative values are ignored during selection**

The beauty is the x-th smallest integer only if that integer is negative; otherwise the answer is zero.

If at least $x$ negatives exist, all of them precede zero and positives in sorted order, so the x-th smallest is found entirely among indices zero through 49.

If fewer than $x$ negatives exist, the x-th overall item is zero or positive—or may not be relevant under the definition—and beauty is explicitly zero. Scanning nonnegative buckets is unnecessary.

**Slide by one position**

For each new right endpoint `i` from $k$ through $n-1$:

1. add incoming value `nums[i]` to its frequency;
2. remove outgoing value `nums[i-k]` from its frequency;
3. compute the new beauty.

The resulting multiset is exactly the window:

$$
\texttt{nums[i-k+1..i]}.
$$

Adding before removing is safe even when the two values are equal: the net frequency remains unchanged.

**Trace the first example**

For first window `[1,-1,-3]` with $x=2$, negative frequencies represent $-3$ and $-1$.

Scanning upward:

- cumulative count reaches one at $-3$;
- it reaches two at $-1$.

The beauty is $-1$.

Slide to `[-1,-3,-2]` by adding $-2$ and removing one. Sorted negatives are $[-3,-2,-1]$, so the second is $-2$.

The next window `[-3,-2,3]` removes $-1$ and adds three. The second negative remains $-2$.

**Why multiplicity matters**

If a negative value occurs several times, each occurrence occupies its own position in sorted order.

Frequency accumulation handles this automatically. If `cnt[index] = 3`, crossing that bucket advances the cumulative rank by three.

No set should be used because a set would discard duplicates and produce incorrect order statistics.


Before each call to `f`, maintain:

> For every allowed value $v$, `cnt[v+50]` equals its number of occurrences in the current length-$k$ window.

Initialization establishes the invariant by counting the first $k$ elements. Each slide adds exactly the entering occurrence and removes exactly the leaving occurrence, preserving it.

Given the invariant, scanning negative buckets in increasing value order is equivalent to traversing the sorted negative multiset. The first cumulative count reaching $x$ is exactly the x-th negative; failure to reach $x$ means the contract requires zero.

Thus every appended beauty is correct and appears in window order.

**Why fixed scanning is effectively constant per window**

The helper checks exactly 50 negative-value buckets, independent of $k$ and $n$. Fifty is a constraint constant.

Therefore, although conceptually it performs an order-statistic scan for every window, total work remains linear in the number of windows.

**Output length**

There are:

$$
n-k+1
$$

contiguous windows of length $k$. The code produces one initial answer and one for every index from $k$ through $n-1$, totaling exactly that number.

## Complexity detail

Initializing the first window takes $O(k)$. There are $n-k$ slides, each with $O(1)$ updates and a scan of 50 buckets. Total time is:

$$
O(k+50(n-k+1))=O(n).
$$

The 101-entry frequency array is fixed-size $O(1)$ auxiliary storage. The returned answer has $n-k+1$ entries, so total space including output is $O(n)$, matching the manifest.

## Alternatives and edge cases

- **Sort every window:** Costs $O((n-k+1)k\log k)$ and repeats most work.
- **Balanced ordered multiset:** Supports general values in $O(\log k)$ updates but is unnecessary for the fixed 101-value domain.
- **Fenwick tree:** Can find ranks efficiently for a larger compressed domain, with more implementation overhead.
- **No negative values:** Negative scan never reaches $x$, so beauty is zero.
- **Fewer than `x` negatives:** Return zero even if nonnegative values fill the window.
- **Duplicate negatives:** Frequencies preserve their multiplicity in rank counting.
- **`x = 1`:** Return the smallest negative in each window, or zero.
- **`k = n`:** Only the initialized full-array window contributes an answer.
- **Incoming equals outgoing:** Frequency changes cancel and the multiset stays the same.
- **Value boundaries:** Offset mapping safely covers both $-50$ and 50.
