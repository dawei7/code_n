## General

**Reduce the median to one-indexed `k`-th values**

Let the combined number of elements be

$$
T = \lvert\texttt{nums1}\rvert + \lvert\texttt{nums2}\rvert.
$$

If $T$ is odd, the median is the $(\lfloor T/2 \rfloor+1)$-th smallest value. If $T$ is even, it is the average of the $(T/2)$-th and $(T/2+1)$-th smallest values. The primary `Solution` class therefore delegates to `getKth(A, B, k)` once or twice.

`k` is one-indexed. That convention is visible in expressions such as `k - 1 - i`: when a group contains `k - i` selected elements, its last selected zero-based index is `k - i - 1`.

The file also contains `Solution_Generic`, which performs a different search over the numerical value range. LeetCode uses the class named `Solution`, so the smaller-array partition algorithm in that class is the selected competitive method.

**Always search the smaller array**

Inside `getKth`, the arrays are locally swapped when necessary:

```python
if m > n:
    m, n = n, m
    A, B = B, A
```

After this step, $m \le n$. The algorithm will binary-search only a cut position in `A`, so choosing the shorter array limits the search to $O(\log(\min(m,n)))$ iterations. The swap changes only local names and lengths; it does not reorder or mutate either input.

**Describe a candidate partition by how many values come from `A`**

Suppose the left partition must contain exactly `k` values—the first `k` values of the conceptual merged order. Let `i` be the number taken from the beginning of `A`. Then the number taken from `B` is forced to be `k - i`.

The four boundaries are:

- `A[i - 1]`: last value selected from `A`, when `i > 0`;
- `A[i]`: first value not selected from `A`, when `i < m`;
- `B[k - i - 1]`: last value selected from `B`, when `k - i > 0`;
- `B[k - i]`: first value not selected from `B`, when `k - i < n`.

If every selected-left value is no greater than every unselected-right value, the `k` selected values really are the `k` smallest. Since each individual array is already sorted, only the two **cross-array** inequalities need attention:

$$
A[i-1] \le B[k-i]
$$

and

$$
B[k-i-1] \le A[i].
$$

Once both hold, the $k$-th smallest value is the largest value on the selected left side:

$$
\max(A[i-1], B[k-i-1]).
$$

**Restrict `i` to feasible counts**

The cut cannot select a negative number of elements or more elements than an array owns.

Because `k - i <= n`, `i` must be at least `k - n`. It also cannot be below zero, giving

```python
max(k - n, 0)
```

as the lower feasible cut.

Because `i <= m` and `i <= k`, the largest feasible cut is `min(m, k)`. The code's predicate needs to read `A[i]`, so the explicit binary-search calls stop one position earlier:

```python
min(m, k) - 1
```

If every tested cut fails the predicate, `binary_search` returns one past that right endpoint, which is exactly the feasible boundary `min(m, k)`. This is how a cut that selects all of `A`, or all `k` values from `A`, is represented without ever evaluating the out-of-bounds `A[i]` inside the predicate.

**Search for the first cut satisfying the right cross-boundary inequality**

The nested `binary_search` finds the smallest index for which `check(mid)` is true. It uses the standard lower-bound pattern:

```python
if check(mid):
    right = mid - 1
else:
    left = mid + 1
```

The check passed by `getKth` is

```python
lambda i: A[i] >= B[k - 1 - i]
```

The right-hand value is `B[k - i - 1]`, the last value selected from `B`. Thus the predicate asks whether

$$
B[k-i-1] \le A[i],
$$

which is the second cross-boundary inequality.

This predicate is monotone. As `i` increases, `A[i]` stays the same or increases because `A` is sorted. At the same time, `k - 1 - i` decreases, so the inspected value in `B` stays the same or decreases. Once the inequality becomes true, it remains true for every larger feasible tested cut. Binary search is therefore valid.

**Why the first true cut also satisfies the other inequality**

Finding just any true cut would not be enough; the selected tail of `A` could still exceed the first unselected value of `B`. Choosing the **first** true cut supplies the missing fact.

If `i` is not the lower boundary, then the preceding cut `i - 1` was false:

$$
A[i-1] < B[k-i].
$$

That is exactly the other required cross inequality, even slightly stronger than `<=`. At a boundary where one side is empty, the inequality holds automatically and is represented later by negative infinity.

The returned `i` therefore divides the arrays so that:

- the left side contains exactly `i + (k-i) = k` elements;
- neither selected tail exceeds the opposite unselected head.

All selected values precede all unselected values in the conceptual merge. The `k`-th value is the maximum selected tail.

**Read the maximum left boundary safely**

The return statement is

```python
return max(
    A[i - 1] if i - 1 >= 0 else float("-inf"),
    B[k - 1 - i] if k - 1 - i >= 0 else float("-inf"),
)
```

If the cut selects no elements from one array, that array has no left-tail value. Negative infinity acts as a sentinel smaller than every legal input, so it cannot win the maximum. The other array supplies the $k$-th value. This also handles an entirely empty `A` after the local size swap.

**Trace both ranks for `[1, 2]` and `[3, 4]`**

For `k = 2`, feasible tested `i` values are `0` and `1`.

- At `i = 0`, test `A[0] >= B[1]`, or `1 >= 4`, which is false.
- At `i = 1`, test `A[1] >= B[0]`, or `2 >= 3`, which is false.
- No tested cut is true, so the lower-bound search returns `i = 2`, selecting both values from `A` and none from `B`. The maximum left boundary is `2`.

For `k = 3`, feasibility requires at least one value from `A`, and the only tested cut is `i = 1`.

- Test `A[1] >= B[1]`, or `2 >= 4`, which is false.
- The returned boundary is `i = 2`. The selected side contains `A[:2] = [1, 2]` and `B[:1] = [3]`. Its maximum is `3`.

The even-length result is `(2 + 3) * 0.5 = 2.5`. Multiplication by `0.5` ensures floating-point division.

**Why every `getKth` result has the requested rank**

The chosen cut selects exactly `k` elements. Sorted order handles comparisons within each array, the true predicate handles the selected `B` tail against unselected `A`, and first-true minimality handles the selected `A` tail against unselected `B`. Therefore every selected value is no greater than every unselected value. The largest selected value has exactly the required $k$-th position, counting duplicates by occurrence.

The outer method asks for precisely the central rank or ranks, so its returned value is the combined median without merging the arrays.

## Complexity detail

Let $m$ and $n$ be the original array lengths, and assume the local swap makes $m \le n$ inside `getKth`.

- **Time complexity: $O(\log(\min(m,n)))$.** The feasible `i` interval contains at most the number of positions in the smaller array, and `binary_search` halves that interval per iteration. An odd total calls `getKth` once; an even total calls it twice. Two logarithmic searches differ only by a constant factor.
- **Space complexity: $O(1)$.** The algorithm stores lengths, cut bounds, indices, sentinels, and a few local function frames of fixed depth. Its binary search is iterative, and it never builds a merged array, suffix copy, or recursion chain. Swapping `A` and `B` swaps references only.

Dictionary-style hashing is not involved; all operations are array indexing, comparisons, and integer arithmetic. The `Solution_Generic` class has different complexity and is not used by the selected `Solution` entry point.

## Alternatives and edge cases

- **Standard two-cut partition search:** Search a cut `i` in the smaller array and derive `j = (T+1)//2 - i`, then compare four boundary values. This is the more common presentation of the same $O(\log(\min(m,n)))$ idea. The competitive code generalizes the partition to an arbitrary one-indexed rank `k`.
- **Recursive `k`-th prefix elimination:** Compare halfway candidates and discard a prefix from one active suffix. It is logarithmic in the combined rank, but a direct recursive Python version uses logarithmic stack space and may not achieve the stronger `log(min(m,n))` bound for highly unequal lengths.
- **Two-pointer merge to the middle:** This is simpler but takes $O(m+n)$ time in the worst case, even if it stops after the central ranks.
- **`Solution_Generic` value-domain search:** The additional class binary-searches candidate values and counts how many array elements are at most each candidate. Its cost depends on both array-search logarithms and the numerical range, so it is not the selected optimal method for two arrays.
- **First array longer than the second:** `getKth` swaps local references so the binary search always uses the shorter array. The caller's arrays are untouched.
- **One array empty:** The feasible search interval is empty, so `binary_search` returns `i = 0`; the negative-infinity sentinel removes the absent `A` tail from consideration, and `B[k-1]` is returned.
- **Cut selects zero from an array:** The missing left boundary is represented by negative infinity. No invalid negative Python index is evaluated because the condition is checked before indexing.
- **Cut selects all of the smaller array:** The lower-bound helper can return one past its tested right endpoint. The final expression reads `A[i-1]`, which remains valid, and never reads `A[i]` there.
- **Odd total length:** One `getKth` call returns the sole middle occurrence.
- **Even total length:** Two adjacent ranks are found independently and averaged. Duplicate middle values naturally produce that same value.
- **Duplicate values across arrays:** The predicate uses `>=`, and the partition reasoning is non-strict. Equal occurrences can lie on either side without changing the $k$-th value.
- **Negative values:** Negative infinity remains below every legal value, and all partition comparisons work without sign-specific logic.
- **At least one value overall:** The constraint $m+n \ge 1$ ensures that every requested median rank exists.
- **No input mutation:** The method changes only local references and indices; it never merges, sorts, or writes either input.
