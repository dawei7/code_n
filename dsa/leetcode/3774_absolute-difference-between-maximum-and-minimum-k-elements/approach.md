## General

**Expose both extreme groups by sorting**

The exact source sorts `nums` in nondecreasing order. After sorting:

- `nums[:k]` contains the `k` smallest occurrences;
- `nums[-k:]` contains the `k` largest occurrences.

Occurrences matter. If a value appears several times near an extreme, each copy occupies a sorted position and may contribute separately.

The two groups are chosen independently. Their slices may overlap when `2*k > n`, which is allowed. Sorting still identifies each requested group correctly; overlap does not mean an occurrence must be removed from one group because it appears in the other.

**Subtract smallest sum from largest sum**

The source returns

`sum(nums[-k:]) - sum(nums[:k])`.

Although the statement asks for an absolute difference, this subtraction is already nonnegative. Pair the sorted smallest values `nums[0]` through `nums[k-1]` with the sorted largest values `nums[n-k]` through `nums[n-1]`. For every pair position $t$,

$$
\texttt{nums}[n-k+t]\ge\texttt{nums}[t],
$$

because the left index is no smaller than the right index when `k <= n`. Summing these inequalities proves that the largest-group sum is at least the smallest-group sum.

Therefore

$$
\left|\text{largest sum}-\text{smallest sum}\right|
=\text{largest sum}-\text{smallest sum},
$$

and no explicit `abs` call is needed.

**Trace duplicates and overlap correctly**

For `[5,2,2,4]` with `k=2`, sorting gives `[2,2,4,5]`. The first slice sums to four, the last slice sums to nine, and the returned difference is five.

For `[1,2,3]` with `k=2`, the smallest group is `[1,2]` and the largest is `[2,3]`. The middle occurrence belongs to both independently chosen groups. The two sums are three and five, so the result is two.

When `k=n`, both slices are the entire sorted list. Their sums are equal and the result is zero.

Slice boundaries remain correct at every legal `k`. Negative indexing makes `-k` equal to `n-k`, the first position of the largest group. Because `k>=1`, neither requested slice is accidentally empty. Because `k<=n`, both boundaries stay inside the list.

**Why the selected slices are optimal extremes**

Suppose a purported set of `k` smallest occurrences excludes a value `x` but includes a larger value `y`. Replacing `y` with `x` cannot increase the sum. Repeating this exchange leads exactly to the first `k` sorted positions, so that prefix has the minimum possible `k`-occurrence sum.

The symmetric exchange shows the last `k` positions have the maximum possible sum: if a chosen occurrence is smaller than an unchosen one, replacing it cannot decrease the sum.

The source subtracts these two exact extreme sums. Sorting also handles all ties without special logic because exchanging equal values changes neither sum.

Notice that the method optimizes the two sums separately, not the difference by choosing one joint partition. That matches the contract: “the `k` largest” and “the `k` smallest” are already uniquely defined as multisets up to ties.

**The manifest describes a different implementation**

The manifest says the bounded values are counted and then consumed from each end of the value domain, with $O(N+V)$ time and $O(V)$ space. The exact source does not build a frequency array. It calls `nums.sort()` and slices the sorted list.

Its actual general time is $O(N\log N)$, and Python's sort plus slices may use $O(N)$ auxiliary space. The small constraints make this entirely practical, but the documentation must describe the algorithm that executes.

## Complexity detail

Sorting $N$ occurrences takes $O(N\log N)$ worst-case time. Each length-`k` slice is created and summed in $O(K)$ time, so the total is $O(N\log N+K)=O(N\log N)$.

Python's Timsort may use $O(N)$ temporary memory. In addition, `nums[:k]` and `nums[-k:]` create temporary lists of $K$ references while their sums are evaluated. Peak auxiliary space remains $O(N)$.

The method mutates `nums` into sorted order. This side effect is part of the exact source even though the returned value is only an integer.

## Alternatives and edge cases

- **Frequency array over values 1 through 100:** It can achieve the manifest's $O(N+V)$ time and $O(V)$ space, but it is not the exact implementation.
- **Two heaps or selection algorithms:** They can avoid a full sort for small `k`, at the cost of more complicated logic.
- **Use `abs` explicitly:** It is harmless but unnecessary because the largest `k`-sum cannot be smaller than the smallest `k`-sum.
- **Choose distinct values only:** The problem selects elements, so duplicate occurrences count separately.
- **Forbid overlap:** The two groups are independent and may share occurrences when `2*k>n`.
- **`k=1`:** The result is maximum value minus minimum value.
- **`k=n`:** Both sums use the whole array and the answer is zero.
- **Single-element array:** It is the `k=n=1` case and returns zero.
- **All values equal:** Both sums are identical for every legal `k`.
- **Many boundary duplicates:** Any tied occurrences can fill the extreme positions without changing the sums.
- **Positive values:** Positivity is not needed for the sorted-order proof; the same subtraction remains nonnegative even for generalized signed values.
- **Input mutation:** Callers needing the original order would have to sort a copy.
- **Source/manifest mismatch:** Complexity for this source must include full sorting and slice allocation.
