## General

Each index produces its own decreasing arithmetic progression of possible gains. For index `i`, the sequence is

$$
\texttt{value}[i],\
\texttt{value}[i]-\texttt{decay}[i],\
\texttt{value}[i]-2\texttt{decay}[i],\ldots
$$

Selecting the index repeatedly consumes this sequence from left to right. Selections at different indices do not interact, so the optimization is equivalent to choosing the largest useful gains across all these progressions.

There is one prefix restriction: the third gain of an index cannot be taken without taking its first two gains. Because every progression is decreasing, this restriction is automatically respected by choosing globally largest gains. If a later term is worth choosing, every earlier term from the same index is at least as large and belongs before it in an optimal selection.

The challenge is that `m` can be as large as `10^9`. A heap that extracts one gain per selection can take `O(m\log n)` time. The source instead finds a gain threshold and sums many terms at once.

**Why nonpositive gains should never be selected**

The contract allows at most `m` selections, not exactly `m`. Selecting a zero does not increase the total, and selecting a negative gain makes it worse. Therefore an optimal plan uses:

$$
q
=
\min\left(
m,\
\text{number of strictly positive terms in all progressions}
\right)
$$

selections.

For progression with initial value `a` and step `d>0`, its `t`-th gain is positive when

$$
a-d(t-1)\ge1.
$$

The number of positive terms is

$$
\left\lfloor\frac{a-1}{d}\right\rfloor+1.
$$

This is exactly the first loop's expression:

```python
(initial - 1) // step + 1
```

The source accumulates these counts into `selections` but caps it at `m` and stops early once `m` is reached. If enough positive gains exist, only the fact that `q=m` matters; counting the rest would be wasted work.

Since every initial value is positive and `m\ge1`, `selections` is always at least one.

**Counting gains at or above a threshold**

For an integer threshold `T\ge1`, define `C(T)` as the number of progression terms whose gain is at least `T`.

For one progression, if `a<T` it contributes zero. Otherwise,

$$
a-d(t-1)\ge T
$$

holds for

$$
\left\lfloor\frac{a-T}{d}\right\rfloor+1
$$

terms.

Adding this quantity across indices computes `C(T)` in `O(n)` time.

As `T` increases, `C(T)` never increases. A higher required gain can only remove eligible terms. This monotonicity permits binary search.

**The cutoff chosen by binary search**

The search interval is from one through

$$
A=\max(\texttt{value}),
$$

because every useful gain is a positive integer and no progression begins above `A`.

The source finds the greatest threshold `T` satisfying

$$
C(T)\ge q.
$$

Threshold one is always feasible by the definition of `q`. For each upper midpoint, if at least `q` terms meet the threshold, the cutoff can be raised; otherwise it must be lowered.

At the end:

- at least `q` gains are at least `T`;
- fewer than `q` gains are strictly greater than `T`, because integer gains greater than `T` are exactly those at least `T+1`.

The second fact also holds when `T=A`: no gain is strictly greater than the maximum initial value.

Thus every gain greater than `T` must be selected, and enough gains equal to `T` are selected to reach exactly `q`. Any remaining terms equal to `T` are interchangeable.

**Why a threshold describes an optimal selection**

Suppose a chosen gain were smaller than an unchosen available gain. Exchanging them would increase the total and would not violate per-index order: all earlier terms before the larger gain are even larger and therefore also belong above the cutoff.

Repeating this exchange shows that some optimal plan consists of the `q` largest positive terms in the union of all progressions. The threshold `T` separates exactly those terms:

- all values above `T` are among the top `q`;
- some or all values equal to `T` fill the remaining slots;
- no value below `T` is needed.

This establishes both value optimality and feasibility.

**Summing one progression without enumerating it**

After the threshold is known, the source revisits each progression. If `initial < threshold`, it contributes no selected candidate.

Otherwise, it computes the number of terms at least `T`:

```python
terms = (initial - threshold) // step + 1
```

and the final included term:

```python
last = initial - (terms - 1) * step
```

These `terms` values form an arithmetic progression from `initial` to `last`. Their sum is

$$
\frac{\texttt{terms}\,(\texttt{initial}+\texttt{last})}{2}.
$$

The product is always even because it is twice the sum of an integer arithmetic progression, so `// 2` is exact.

The loop adds every term at least `T` and records their total count `C(T)`. This count may exceed `q` because several progressions can contain a gain exactly equal to the cutoff.

**Removing only the excess cutoff values**

There are

$$
C(T)-q
$$

too many collected terms. Because fewer than `q` terms are strictly greater than `T`, all removable excess terms have value exactly `T`. The source therefore performs:

```python
total -= (count - selections) * threshold
```

This leaves the sum of exactly the `q` greatest positive gains.

For example, suppose the collected values at cutoff four are `7,6,5,4,4,4` but only four selections are needed. There are two excess values, both equal to four. Subtracting `2\cdot4` leaves `7+6+5+4`.

**Applying the modulus at the correct time**

The source performs all comparisons, threshold counting, and summation on actual integer gains. It applies `% MODULO` only to the final maximum.

Maximizing residues instead would be incorrect because modular order does not preserve ordinary numerical order. Python's arbitrary-precision integers allow the exact total to be accumulated safely before reduction.

## Complexity detail

Let `n` be the number of indices and

$$
A=\max(\texttt{value}).
$$

Counting positive terms takes `O(n)` time. Binary search uses `O(\log A)` threshold iterations, and each iteration scans up to `n` progressions, for `O(n\log A)` time. The final arithmetic-progression summation takes another `O(n)`. Total time is

$$
O(n\log A).
$$

The early break inside a threshold count can reduce actual work after `q` terms are known to exist, but the worst-case bound remains unchanged.

The algorithm stores scalar counters, bounds, and arithmetic intermediates. `zip(value, decay)` produces an iterator rather than a copied pair list. Auxiliary space is `O(1)`, excluding the input arrays.

No loop depends directly on `m`. This is essential because `m` may be `10^9`.

In a bit-complexity model, operations on the potentially large exact total depend on its bit length. The stated bound follows the conventional unit-cost model for integer arithmetic under the problem constraints.

Neither input list is modified.

## Alternatives and edge cases

- **Max-heap simulation:** Repeatedly take the current largest gain and push that index's next gain. This is correct but costs `O(m\log n)` when enough positive terms exist, which is impractical for `m=10^9`.

- **Materialize every positive gain:** A single index can have up to roughly `10^9` positive terms, so building and sorting the complete multiset is not feasible.

- **Take exactly `m` selections:** This can force zero or negative gains after all positive gains are exhausted. Because selections are optional, the source correctly caps the count at the number of positive terms.

- **Binary-search the total directly:** The total is not a simple monotone predicate. The count of gains above a threshold is monotone and leads to the desired order statistic.

- **Select all terms at the cutoff:** Ties can make `C(T)>q`. The final subtraction is necessary to remove the extra cutoff-valued terms.

- **Subtract arbitrary collected terms:** Only cutoff-valued terms may be removed safely. Removing a larger term would no longer leave the top `q` values.

- **A progression that skips the threshold:** Its last collected value may be greater than `T`. That causes no problem; excess terms globally are still equal to `T` because `C(T+1)<q`.

- **More selection capacity than positive gains:** Then `q` equals the total positive count, the cutoff becomes one or the smallest present positive level, and every positive term is retained. Nonpositive continuation terms are ignored.

- **Decay larger than initial value:** The progression has exactly one positive term, its initial value. The count formula returns one.

- **Equal gains from different indices:** They are interchangeable. The threshold method needs only their multiplicity, not which index supplies the final tied selections.

- **Large `m`:** Counts are computed algebraically and capped, so runtime does not grow with `m`.

- **Modulo reduction:** It occurs after the real maximum is established. Applying it to individual gains is algebraically safe for summation but must never be used to decide which gains are largest.

- **Integer division:** Both count formulas use floor division to count complete progression steps. The arithmetic-series division by two is exact.

- **Input order:** Reordering indices changes neither the union of gain progressions nor the result. Early breaks may happen at different times but do not change the threshold predicate.
