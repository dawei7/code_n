## General
**Build one sorted sequence per numerator**

Fix numerator index `i`. Starting with denominator `arr[n - 1]` gives the smallest fraction in that sequence. Decreasing the denominator index makes the fraction larger, so `arr[i]/arr[n-1], arr[i]/arr[n-2], ..., arr[i]/arr[i+1]` is already sorted.

**Merge the sequences with a heap**

Place the first fraction from every numerator sequence in a min-heap. Removing the smallest heap entry yields the next fraction globally; replace it with the next denominator from the same numerator sequence when one exists. After `k` removals, the last removed numerator and denominator form the answer.

**Compare fractions exactly**

Heap entries compare $a/b$ and $c/d$ by the integer products $ad$ and $cb$. This avoids rounding decisions. At every step the heap contains the smallest not-yet-removed fraction from each sequence. The ordinary k-way merge argument then proves that its minimum is the smallest remaining fraction overall, so the $k$-th removal has exactly rank $k$.

## Complexity detail
Creating and heapifying at most $n - 1$ entries takes $O(n)$ time. Each of the `k` removals and possible replacements costs $O(\log n)$, for $O(n + k \log n)$ total time. The heap stores $O(n)$ entries.

## Alternatives and edge cases
- **Denominator-based heap rows:** Start with numerator `1` for every denominator and advance numerator indices after pops; this is another $O(n + k \log n)$ merge.
- **Binary search by fraction value:** Count fractions below a midpoint with two pointers and track the largest one; this uses $O(n)$ work per precision step but requires careful termination.
- **Generate and sort every fraction:** Exact cross products can sort all $O(n^2)$ pairs, but total work becomes $O(n^2 \log n)$ and space $O(n^2)$.
- **Two array elements:** The sole fraction is always the answer.
- **First rank:** The minimum is `1 / arr[ - 1]`.
- **Last rank:** The answer is the numerically largest eligible pair, not necessarily the pair with adjacent largest values when prime gaps vary.
- **No floating-point keys:** Cross multiplication preserves exact ordering for close fractions.
