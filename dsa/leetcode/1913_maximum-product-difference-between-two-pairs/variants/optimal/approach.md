## General

**Separate the expression into a maximum product and minimum product.** The objective is `a * b - c * d` using four distinct indices. Because every input value is positive, increasing either factor of the first product cannot reduce it, and increasing either factor of the subtracted product cannot improve the difference. The best choice is therefore the two largest occurrences for the positive product and the two smallest occurrences for the negative product.

**Sort to expose all four extremes.** `nums.sort()` arranges occurrences in nondecreasing order. `nums[-1]` and `nums[-2]` are the largest and second-largest occurrences; `nums[0]` and `nums[1]` are the smallest and second-smallest. The returned expression multiplies the upper pair and subtracts the lower pair.

Occurrences matter rather than distinct values. If the largest value appears twice, the two final sorted positions correspond to two distinct indices and may both be selected. If it appears once, the second-last position supplies the next available occurrence. Sorting preserves multiplicity automatically.

**Why the chosen indices are distinct.** The array contains at least four elements. Sorted positions zero, one, `n - 2`, and `n - 1` are four different positions when `n >= 4`. Even if some or all values are equal, the positions still represent distinct original occurrences. Thus maximizing and minimizing the two products independently does not accidentally reuse an index.

**Prove the maximum product choice.** For any two selected positive values `u <= v`, neither can exceed the two largest sorted occurrences in a way that creates a larger pair product. Replacing a chosen factor with an unused larger occurrence weakly increases the product. Repeating yields the final two positions, so their product is maximal among pairs.

The same exchange argument in the opposite direction shows replacing either factor of a candidate minimum product with an unused smaller occurrence weakly decreases it. The first two positions therefore minimize the subtracted product.

Because the four extreme positions are disjoint, both improvements can be realized simultaneously. Subtracting the smallest possible second product from the largest possible first product gives the global maximum difference.

Another way to see the disjointness is to remove the two largest occurrences first. At least two occurrences remain because `n >= 4`, and the global two smallest positions are among those remaining unless all four positions exhaust the array, in which case they are exactly the other two. Thus optimizing the positive pair never steals an index required by the chosen minimum pair.

**Trace `[5,6,2,7,4]`.** Sorting produces `[2,4,5,6,7]`. The largest product is `7 * 6 = 42`, and the smallest product is `2 * 4 = 8`. Their difference is 34. The middle value five is unused because replacing an extreme with it would either lower the first product or raise the second.

**Why positivity matters.** With negative values, two very negative numbers might form the largest positive product, and a negative product could minimize the subtracted term. The simple “two largest minus two smallest” rule would need reanalysis. The contract's lower bound of one makes monotonic factor reasoning valid.

**The method mutates input.** `list.sort` rearranges `nums` in place. The challenge asks only for a number, so preserving order is unnecessary. External callers needing original order must pass a copy or use `sorted(nums)`.

## Complexity detail

Let $n$ be the array length. Python sorting takes $O(n\log n)$ time; the final indexing and arithmetic are constant. The exact source therefore does not match the manifest's $O(n)$ time label. A one-pass four-extrema tracker can achieve linear time, but it is not executed here.

Python's Timsort may allocate $O(n)$ temporary memory in the worst case. Thus exact auxiliary sort space is $O(n)$, not the manifest's $O(1)$ label, despite sorting the list in place. The input array storage itself is reused and reordered.

Each value is at most $10^4$, so products are at most $10^8$ and their difference fits a signed 32-bit integer. Python arithmetic is safe regardless.

## Alternatives and edge cases

- **Track two minima and two maxima:** Update four scalar extrema in one pass, obtaining the manifest's $O(n)$ time and $O(1)$ space without mutation.
- **Heap selection:** Keeping two-element min/max heaps also works in $O(n)$ time but adds unnecessary data-structure overhead for fixed-size extrema.
- **Enumerate four indices:** Brute force is $O(n^4)$ and repeats information that extremes settle directly.
- **Exactly four elements:** All occurrences are used; sorting determines which pair is added and which is subtracted.
- **Duplicate extremes:** Equal values at different sorted positions are valid distinct-index choices.
- **All values equal:** Both products are equal and the maximum difference is zero.
- **Positive-value guarantee:** It is essential to the monotonic product proof. General signed arrays need consideration of negative extremes.
- **Input mutation:** The exact solution leaves `nums` sorted. Use a copy if callers require the original order.
- **Manifest mismatch:** Linear constant-space tracking is available, but complexity documentation must reflect this source's sorting behavior.
- **Four distinct indices versus values:** The values themselves need not differ. What matters is that the four selected sorted positions represent four occurrences from distinct original indices.
