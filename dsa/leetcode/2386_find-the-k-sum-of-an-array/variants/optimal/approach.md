## General

The greatest subsequence sum includes every positive value and excludes every negative value. Call it `maximum_sum`. Any other subsequence differs by omitting some positive values or including some nonpositive values. Either decision reduces the total by that element's absolute value, so every subsequence sum equals `maximum_sum - loss` for a subset of the absolute values.

The requested $k$-th largest sum therefore corresponds to the $k$-th smallest subset loss, including the empty loss zero. Sort the absolute values as `losses`.

**Enumerate losses in increasing order.** A heap state `(loss, i)` represents a nonempty chosen index set whose greatest index is `i`. Start with the singleton loss `losses[0]`. After removing `(loss, i)`, two children introduce index `i + 1`: extend the current set, producing `loss + losses[i + 1]`, or replace index `i` by `i + 1`, producing `loss - losses[i] + losses[i + 1]`.

These transitions partition the nonempty subsets by their greatest chosen index and generate every index subset once. Equal values may create equal numeric losses, but their separate heap states remain present, preserving the required multiplicity.

The empty loss is rank one. Pop the heap `k - 1` times to reach the $k$-th smallest loss, then subtract it from `maximum_sum`. If `k = 1`, return `maximum_sum` immediately.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Sorting absolute values costs $O(n\log n)$. At most two heap entries are added per one of $k-1$ removals, so heap work costs $O(k\log k)$. The sorted values and heap use $O(n+k)$ space.

## Alternatives and edge cases

- **Enumerate every subsequence:** Generating and sorting all $2^n$ sums is correct but exponential and infeasible for the legal $n$.
- **Binary search a sum threshold:** Counting subsequences above a threshold is difficult with mixed signs and multiplicities; the bounded $k \le 2000$ favors best-first enumeration.
- **Duplicate sums:** Do not deduplicate heap values because different subsequences occupy separate ranks.
- **Empty subsequence:** Its zero loss makes `maximum_sum` the first-ranked answer.
- **All negative values:** `maximum_sum` is zero, corresponding to choosing no elements.
- **Zero values:** Distinct choices involving zero create duplicate losses that must remain in the ranking.
- **Large totals:** Fixed-width implementations need 64-bit arithmetic for sums and losses.
