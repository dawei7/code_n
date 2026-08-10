## General

The score at index $i$ needs the largest value on its left-inclusive side and the smallest value on its right-inclusive side:

$$
S_i
=
\max_{0\le j\le i}\texttt{nums}[j]
-
\min_{i\le j<n}\texttt{nums}[j].
$$

Version II permits up to $10^5$ elements, so rebuilding those two aggregates for each candidate would be too expensive. The exact source reduces the work to two linear passes:

1. a right-to-left pass stores every suffix minimum; and
2. a left-to-right pass maintains one prefix maximum and returns at the first stable index.

**The repeated-work problem**

At consecutive indices, the ranges overlap almost completely. Prefix $0..i+1$ differs from prefix $0..i$ by only one element. Suffix $i..n-1$ differs from suffix $i+1..n-1$ by only one element.

Recomputing `max(nums[:i + 1])` and `min(nums[i:])` independently would ignore that overlap. Across all indices, the total number of examined entries would grow quadratically.

The source summarizes each changing range with the recurrence that adds its one new endpoint.

**Backward construction of every suffix minimum**

Define

$$
R_i=\min_{i\le j<n}\texttt{nums}[j].
$$

The base case is $R_{n-1}=\texttt{nums}[n-1]$. For $i<n-1$,

$$
R_i
=
\min(\texttt{nums}[i],R_{i+1}).
$$

The list `right` stores these $R_i$ values. It is initially filled with the last array value, which establishes the correct final entry. The loop then moves backward, so `right[i + 1]` is already correct when `right[i]` is assigned.

After this pass, looking up the smallest value from any index through the end costs $O(1)$.

**Forward maintenance of the prefix maximum**

Define

$$
L_i=\max_{0\le j\le i}\texttt{nums}[j].
$$

The forward recurrence is

$$
L_i=\max(L_{i-1},\texttt{nums}[i]).
$$

The scalar `left` holds this value. At the start of each loop iteration, it summarizes the previous prefix; after `left = max(left, x)`, it summarizes the current inclusive prefix.

The source begins with zero. That works because the contract guarantees nonnegative input values, so zero cannot incorrectly exceed a real prefix maximum. More generally, one could initialize from `nums[0]`.

**An invariant at the moment of testing**

Immediately before evaluating the condition at index $i$:

$$
\texttt{left}=L_i
\quad\text{and}\quad
\texttt{right}[i]=R_i.
$$

For $i=0$, the update incorporates the first element, and the precomputed array already contains $R_0$. If the invariant holds after index $i-1$, taking the maximum with `nums[i]` produces $L_i$, while `right[i]` was independently established by the backward recurrence. Thus it holds for every scanned index.

The expression

```text
left - right[i]
```

is therefore exactly $S_i$, not a bound or estimate.

**Why inclusive endpoints matter**

The current value `nums[i]` belongs to both the prefix and suffix. The suffix recurrence includes it through `min(nums[i], right[i + 1])`. The prefix loop updates `left` with `x` before checking the score.

Changing either order would implement a different formula. In particular, checking before updating `left` would omit `nums[i]` from the prefix maximum.

**Selecting the smallest stable index**

The condition is $S_i\le k$. The source scans $i=0,1,\ldots,n-1$ and returns as soon as this inclusive inequality holds.

At that moment, all smaller indices are known to be unstable because their exact scores were tested earlier. The immediate return is therefore both valid and sufficient to establish minimality.

If no iteration returns, every possible index violates the limit and `-1` is required.

**Example**

For `nums = [3, 2, 1]`:

$$
\texttt{right}=[1,1,1].
$$

The forward prefix maxima are 3, 3, and 3. Every score is $3-1=2$. With $k=1$, no index qualifies, so the method returns `-1`.

For `nums = [0]`, `right[0]=0` and the first prefix maximum is 0. The score is zero, so index 0 is returned when $k=0$.

## Complexity detail

Let $N$ be the array length. Filling `right`, computing its suffix recurrence, and scanning candidates each take linear time. The total is

$$
O(N).
$$

This bound is important for the $N\le10^5$ Version II constraint. A quadratic implementation could perform roughly $10^{10}$ element inspections and is not viable.

The suffix-minimum list contains $N$ integers, so auxiliary space is

$$
O(N).
$$

The prefix side uses only one scalar rather than another $N$-element array. The source leaves `nums` unchanged.

It is possible to solve this static problem with $O(1)$ extra space only if one can avoid retaining future suffix information, but a simple left-to-right scan cannot reconstruct arbitrary suffix minima after passing their values. The stored suffix array is the direct linear-time tradeoff used here.

## Alternatives and edge cases

- **Quadratic direct evaluation:** Compute a fresh prefix maximum and suffix minimum for each $i$. It matches the definition but cannot scale to $10^5$ elements.
- **Two full aggregate arrays:** Prefix maxima plus suffix minima make every score a constant-time lookup, but the source saves one array by maintaining the prefix online.
- **Segment tree:** Range maximum and minimum queries would cost $O(\log N)$ per index after preprocessing, making the solution slower and more complex than static linear passes.
- **Sparse table:** Constant-time range queries after $O(N\log N)$ preprocessing are unnecessary because only one fixed prefix and suffix per index are queried.
- **Single-element array:** Its score is always zero, making index 0 the answer for any nonnegative $k$.
- **Threshold equality:** A score exactly equal to $k$ qualifies.
- **Current element belongs to both ranges:** The update order and suffix recurrence both preserve the inclusive definition.
- **Score is not guaranteed monotone:** Prefix maxima never decrease and suffix minima never decrease as $i$ moves right, but their difference can move in either direction; binary search is unsafe.
- **Large values:** Values and $k$ up to $10^9$ fit comfortably in Python integers, and subtraction is exact.
- **Nonnegative initialization:** `left = 0` is valid only because the documented domain excludes negative values.
- **No qualifying index:** The source returns `-1` only after testing every exact score in ascending index order.
- **No input mutation:** The algorithm allocates its own suffix list and does not reorder or overwrite `nums`.
