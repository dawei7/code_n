## General

**A distribution is determined by its cut boundaries**

The contiguity rule means splitting `weights` into `k` non-empty bags requires choosing exactly `k-1` cuts between adjacent marbles.

A cut after index `i` separates:

- a left bag ending with `weights[i]`;
- a right bag beginning with `weights[i+1]`.

Its variable contribution to total score is:

$$
\texttt{weights}[i]+\texttt{weights}[i+1].
$$

The source constructs all `n-1` adjacent boundary contributions with `pairwise(weights)`.

**Separate the fixed endpoint contribution**

Regardless of cuts:

- the first marble is the first endpoint of the first bag;
- the last marble is the last endpoint of the final bag.

Their sum `weights[0]+weights[-1]` appears in every distribution score.

Every internal cut adds its two adjacent endpoint weights. Therefore:

$$
\text{score}
=
\texttt{weights}[0]+\texttt{weights}[n-1]
+
\sum_{\text{chosen cuts }i}
\bigl(\texttt{weights}[i]+\texttt{weights}[i+1]\bigr).
$$

When taking maximum score minus minimum score, the fixed outer-endpoint term cancels.

**Choose smallest cuts for the minimum**

Exactly `k-1` boundary values must be selected.

To minimize their sum, choose the `k-1` smallest contributions. If a chosen contribution were larger than an unchosen one, exchanging them would lower the score while preserving the number of cuts and validity.

After sorting `arr` ascending, these values are `arr[:k-1]`.

**Choose largest cuts for the maximum**

By the symmetric exchange argument, the maximum uses the `k-1` largest contributions.

`arr[len(arr)-k+1:]` is the suffix of exactly `k-1` values:

- `len(arr)=n-1`;
- start index is $(n-1)-k+1=n-k$;
- suffix length is $(n-1)-(n-k)=k-1$.

The method subtracts the small-prefix sum from the large-suffix sum.

**Trace the first sample**

For `weights=[1,3,5,1]`, adjacent contributions are:

$$
1+3=4,\quad3+5=8,\quad5+1=6.
$$

Sorted array is `[4,6,8]`. With `k=2`, choose one cut:

- minimum variable contribution is 4;
- maximum is 8.

Fixed endpoint contribution is $1+1=2$ in both scores, so their difference is $8-4=4$.

**Why each cut corresponds to a valid distribution**

Any set of `k-1` distinct gaps in increasing order partitions the array into exactly `k` contiguous, non-empty segments. Conversely, every valid distribution has those internal boundaries.

Thus optimizing over boundary subsets is exactly equivalent to optimizing over bag distributions.

**Derive the score decomposition from bag endpoints**

Suppose cuts occur after indices $c_1<c_2<\cdots<c_{k-1}$. Bag endpoints are:

$$
(0,c_1),\ (c_1+1,c_2),\ldots,(c_{k-1}+1,n-1).
$$

Adding every bag's first and last weight includes outer endpoints once. Around cut `c_t`, it additionally includes `weights[c_t]` as the left bag's last value and `weights[c_t+1]` as the right bag's first value.

There are no other terms, proving the fixed-plus-boundaries formula exactly rather than heuristically.

**Boundary contributions may share marbles**

Two adjacent cuts can both include the middle single-marble bag's weight. That is correct: a one-marble bag has the same marble as both its first and last endpoint, so its cost includes that weight twice.

The formula naturally reproduces this through the two neighboring cut contributions.

**The `k=1` case**

No cuts are chosen. Both slices are empty:

- `arr[len(arr):]`;
- `arr[:0]`.

Both sums are zero, so the returned difference is zero. There is only one possible bag and hence one possible score.

**The `k=n` case**

Every adjacent boundary must be selected. The smallest and largest sets are both the complete `arr`, so their sums match and the difference is zero.

Again, the distribution into single-marble bags is unique.


The score decomposition proves all distribution-dependent information lies in chosen adjacent boundary sums, with exactly `k-1` choices. Sorting and exchange arguments identify the minimum and maximum subsets. Their difference cancels the shared endpoint term and equals the requested score range.

Because cuts have no interaction beyond being distinct gaps, choosing one large boundary never invalidates another chosen boundary. This independence is what permits selecting the largest contributions individually.

## Complexity detail

Creating `n-1` adjacent sums costs $O(n)$. Sorting them costs $O(n\log n)$ and dominates. The two slice sums inspect $O(k)$ values.

Array `arr` uses $O(n)$ space. The slices in the exact Python expression can each allocate up to $O(n)$ additional space, so peak auxiliary storage remains $O(n)$.

The score difference may exceed 32-bit range; fixed-width languages should use 64-bit integers.

## Alternatives and edge cases

- **Heaps for partial selection:** Find `k-1` smallest and largest without a full sort when `k` is small.
- **`k=1`:** No boundaries, so difference zero.
- **`k=n`:** All boundaries are forced, also giving zero.
- **Single-marble bag:** Its weight appears as both endpoints, correctly through adjacent cuts.
- **Repeated weights:** Boundary values may tie; any tied choices give the same score.
- **Fixed first and last weights:** They cancel from maximum-minus-minimum.
- **Exactly `k-1` cuts:** This enforces `k` non-empty bags.
- **Contiguous bags:** Every gap subset automatically preserves contiguity.
- **Large sums:** Use wide arithmetic.
- **Pairwise iterator:** It generates every adjacent boundary exactly once.
