## General

**Organize all fractions into sorted lists**

Every valid pair satisfies `i < j` and represents fraction `arr[i] / arr[j]`. Instead of generating all $\frac{n(n-1)}{2}$ fractions, group them by their denominator index `j`.

For a fixed `j`, valid numerator indices are:

`0, 1, 2, ..., j - 1`.

Because `arr` is strictly increasing and the denominator stays fixed, these fractions are already sorted:

$$
\frac{arr[0]}{arr[j]}
<
\frac{arr[1]}{arr[j]}
<
\cdots
<
\frac{arr[j-1]}{arr[j]}.
$$

There are `n - 1` such lists, one for every denominator index from one through `n - 1`. The problem is now to find the `k`th item in the sorted merge of these lists.

**Put the first item of every list in a min-heap**

The smallest fraction for denominator `j` uses numerator index zero. Since `arr[0] = 1`, the initial heap entry is:

`(1 / arr[j], 0, j)`.

The list comprehension builds one entry for each denominator. Its actual code uses `enumerate(arr[1:])`, so the enumeration position `j` is shifted back to the array index with `j + 1`.

The heap therefore exposes the smallest not-yet-consumed fraction across all denominator lists. Calling `heapify` constructs this min-heap in linear time.

**Advance only the list whose front was removed**

Suppose the heap removes entry `(value, i, j)`. This fraction is the globally smallest remaining front.

The next unseen item from that same denominator list uses numerator `i + 1`. It is valid only when `i + 1 < j`, preserving the required numerator-index-before-denominator-index rule.

If valid, the method pushes:

`(arr[i + 1] / arr[j], i + 1, j)`.

All other lists keep their current fronts in the heap. This is the standard multiway merge idea used to combine sorted sequences.

If `i + 1 == j`, that denominator list is exhausted. Pushing it would create the invalid fraction `arr[j] / arr[j] = 1`, so no replacement is added.

**Why the heap front is always globally next**

For every denominator list, all consumed fractions come before its current heap representative, and every unseen fraction comes at or after that representative.

Therefore any globally smallest unseen fraction must be one of the list fronts stored in the heap. The heap root is the smallest among those fronts, so it is the globally smallest unseen fraction.

After popping that root and advancing exactly its list, the same property remains true. This invariant avoids ever inserting later fractions before they can possibly be needed.

**Stop after `k - 1` removals**

Initially, no fraction has been consumed, so the heap root is the first smallest. Each pop consumes exactly the next fraction in global sorted order.

After `k - 1` pops, exactly the first `k - 1` fractions have been removed. The current heap root is therefore the `k`th smallest. The method returns the original array values at the root's stored numerator and denominator indices.

The constraint guarantees that `k` does not exceed the total number of valid fractions. Consequently, although individual lists may become exhausted, the heap cannot become empty before the required root is available.

**Trace `arr = [1,2,3,5]`**

The denominator lists are:

- denominator two: `1/2`;
- denominator three: `1/3, 2/3`;
- denominator five: `1/5, 2/5, 3/5`.

The heap begins with `1/2`, `1/3`, and `1/5`. Its first pop is `1/5`, which is replaced by `2/5`. Its second pop is `1/3`, which is replaced by `2/3`.

After two removals, the root is `2/5`. For `k = 3`, the algorithm returns `[2,5]`.

**Why every valid fraction appears exactly once**

Every pair `(i, j)` belongs to exactly one list identified by denominator `j`. That list begins with `i = 0` and advances numerator indices in order, never skipping a valid index and never moving past `j - 1`.

Thus each valid fraction is eventually pushed once and popped at most once. No pair belongs to two lists, so duplicates are not created by the enumeration.

**Tuple ordering and fraction values**

Python compares heap tuples from left to right. The first field is the numeric fraction value, so it provides the intended priority. The indices are deterministic tie-breakers if two stored floating values compare equal.

With the stated inputs—one and distinct primes—mathematically distinct valid index pairs produce reduced fractions that are distinct. The exact implementation nevertheless uses binary floating-point division for heap priorities. That is the behavior of the accepted local solution.

An implementation seeking comparison exactness could store indices in a custom heap item and compare `arr[i1] * arr[j2]` with `arr[i2] * arr[j1]`, avoiding rounding. The present constraints and source rely on floating ordering.

**Why this beats constructing all fractions**

There may be $O(n^2)$ valid pairs, but the heap stores only one frontier item per denominator. To obtain an early rank `k`, it advances only the lists responsible for the first `k` fractions.

The algorithm therefore pays for initializing $O(n)$ lists and for approximately `k` heap operations, rather than materializing and sorting every pair.

## Complexity detail

Let $n$ be the array length. Creating the `n - 1` initial entries and heapifying them costs $O(n)$ time.

The loop runs `k - 1` times. Each pop and possible push operates on a heap of at most $n - 1$ entries and costs $O(\log n)$. Total time is $O(n + k\log n)$.

The heap contains at most one entry per denominator, so it uses $O(n)$ auxiliary space. Other variables use $O(1)$ space.

## Alternatives and edge cases

- **Value binary search with two-pointer counting:** Count fractions below a candidate in $O(n)$ time and track the largest qualifying fraction. It can avoid dependence on `k` but needs careful termination and fraction recovery.

- **Generate and sort all pairs:** It is straightforward but costs $O(n^2)$ space and $O(n^2\log n)$ sorting time.

- **Exact cross-multiplication heap comparator:** It avoids floating-point priorities while retaining the same multiway-merge structure and asymptotic bounds.

- **Smallest rank:** For `k = 1`, the loop performs no pop and returns the initial heap minimum.

- **Largest valid rank:** Lists may exhaust one by one, but the valid-rank guarantee leaves the final required entry available.

- **Two-element array:** There is one denominator list with one fraction, which is returned directly.

- **List exhaustion:** Do not push when `i + 1 == j`, because equal numerator and denominator indices are forbidden.

- **Strictly increasing input:** It makes every fixed-denominator list strictly increasing.

- **Prime-and-one property:** It prevents mathematical equality between distinct reduced fraction pairs in this input family.
