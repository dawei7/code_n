## General

**Separate filler values from median candidates.** Let $k=n/3$, the required number of groups. Every group needs one value no larger than its median and one value no smaller than its median. To maximize the medians, spend the globally smallest $k$ values as the low fillers; assigning any larger value to that role can only remove a value that might improve a median.

**Pair the remaining values from the top.** Sort `nums` in non-decreasing order. After the first $k$ fillers, exactly $2k$ values remain. Pair these values adjacently in sorted order. In each pair, the smaller value becomes a median and the larger value supplies the required upper companion. Therefore the answer is the sum at sorted indices $k,k+2,k+4,\ldots,n-2$.

This construction is feasible by combining each chosen median-companion pair with one reserved filler. It is optimal because every median needs a distinct companion at least as large; among the upper $2k$ values, taking the smaller member of each adjacent pair leaves no larger possible sequence of $k$ medians.

## Complexity detail

Let $n$ be the array length. Sorting takes $O(n\log n)$ time, and summing the $n/3$ selected positions takes $O(n)$ time. Python's in-place sort uses $O(n)$ auxiliary space in the worst case, so the package bound is $O(n)$ space.

The benchmark uses $S=n$. The accepted method is $O(S\log S)$, while a correct simulation that repeatedly searches for and removes the smallest value and two largest values is $O(S^2)$.

## Alternatives and edge cases

- **Repeated minimum/maximum removal:** It mirrors the greedy choice directly and is correct, but list searches and removals make it quadratic.
- **Heap-based selection:** Two heaps can reproduce the ordering, but sorting is simpler and has the same $O(n\log n)$ time bound.
- **One group:** With exactly three values, the answer is their ordinary median.
- **Duplicate values:** Equal fillers, medians, or companions do not affect the positional argument.
- **Already sorted input:** The same index rule applies; no special handling is required.
- **Large answer:** The sum can exceed 32-bit range because both $n$ and the values are large.

