## General

After $s$ right shifts, the value originally at index $i$ occupies index $(i+s)\bmod n$. It matches at its destination exactly when

$$
\texttt{nums1[i]}=\texttt{nums2[(i+s)\bmod n]}.
$$

Only the residue of $s$ modulo $n$ matters. Therefore there are exactly $n$ distinct circular alignments, represented by shifts $0,1,\ldots,n-1$; any larger number of shifts repeats one of them.

For each shift, scan every original index and count how many values satisfy the displayed equality. The modular destination lookup represents the shifted arrangement without copying or modifying either array. Retain the largest count across all shifts.

Every permitted final arrangement appears once in this enumeration, and the inner scan counts precisely the matching indices for that arrangement. Taking the maximum of these exact counts therefore returns the best result allowed by the contract.

## Complexity detail

Let $n$ be the common array length. There are $n$ offsets and each checks $n$ positions, so the algorithm takes $O(n^2)$ time. It stores only counters and indices, using $O(1)$ auxiliary space.

The benchmark defines `size` as $n$ and uses lengths 5, 10, and 20, spanning 4x. In every tier, `nums2` is `nums1` rotated left once, placing the full match at the last right-shift offset. The accepted method uses modular indexing for all $n^2$ comparisons. A correct slower baseline rebuilds each offset from the original via repeated explicit one-step shifts and fails only the scaling verdict.

## Alternatives and edge cases

- **Rotate once between comparisons:** Keep a copied array, compare it with `nums2`, then perform one right shift before the next comparison. This is also $O(n^2)$ time but needs $O(n)$ auxiliary space and repeated array writes.
- **Rebuild every shift independently:** Starting from `nums1` and applying $s$ one-step rotations for offset $s$ is correct but takes $O(n^3)$ total time.
- **Frequency-only comparison:** Equal multisets do not determine positional matches; the circular order and offset remain essential.
- **Stop after one full cycle:** Shifting $n$ times restores the original array, so further shifts cannot add a new alignment.
- **Zero shifts:** The unchanged input is a valid candidate and must be included.
- **Single element:** Its only alignment returns one if the two values are equal and zero otherwise.
- **No shared values:** Every offset has zero matches, so the initialized maximum of zero is the correct answer.
- **Duplicate values:** Multiple offsets may tie, but only the maximum count—not the chosen offset—is required.
