## General
**Reduce equal partitioning to one target sum**

If the total is odd, two integer subset sums cannot be equal. Otherwise let `T = total / 2`. Choosing any subset with sum `T` automatically leaves all remaining elements with the same sum.

**Encode reachable sums as bits**

Use an integer whose bit `s` is one exactly when sum `s` is reachable. Initially only sum zero is reachable, so the bitset is `1`. For value `x`, shifting left by `x` maps every old reachable sum `s` to $s + x$; OR it with the old bitset to represent excluding or including the value.

**Why each value is used at most once**

Compute the shift from the pre-update bitset and combine it in one assignment. New sums created by the current value cannot feed another shift during that same iteration, matching the zero-or-one choice for each array element.

**Read the target decision**

After all values, bit `T` is set exactly when some subset choices total `T`. This follows inductively because each update enumerates both possibilities for the newest value over every subset of the processed prefix.

## Complexity detail
The language-neutral Boolean dynamic program has `n` updates across sums through `T`, taking $O(nT)$ time and $O(T)$ space. Python's packed integer performs each row as word-level shift and OR operations while preserving the same state semantics.

## Alternatives and edge cases
- **Descending Boolean array:** updates sums from `T` down to each value and has the stated $O(nT)$ time and $O(T)$ space.
- **Memoized include-or-exclude search:** visits at most $O(nT)$ index-and-sum states but adds recursion and hash overhead.
- **Uncached subset enumeration:** can explore $O(2^n)$ choices.
- An odd total is immediately impossible.
- One element alone cannot form two equal positive-sum subsets.
- Duplicate values are separate selectable elements.
- A value greater than `T` cannot belong to the target subset, though the bitset update remains safe.
