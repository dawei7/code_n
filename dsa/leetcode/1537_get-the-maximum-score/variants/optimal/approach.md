## General

**Common values are the only switching points**

Both arrays are strictly increasing, and traversal within the chosen array always moves left to right. A path may switch arrays only at a value appearing in both.

Between two common values, there is no legal place to switch. A path must take the entire intervening segment from one array or the entire segment from the other. At the next common value, it can choose whichever accumulated route has the larger score and then continue on either side.

This structure lets the solution avoid constructing paths. It maintains only the best score associated with each current array.

**Merge the sorted arrays with two pointers**

Pointers `i` and `j` indicate the next unprocessed values in `nums1` and `nums2`. Accumulator `f` represents the running best score for a path currently following the first array, while `g` represents the corresponding score for the second array.

If `nums1[i] < nums2[j]`, the first value occurs before the second array's next possible matching value. Because the arrays are sorted, it cannot match anything at or after `nums2[j]`. The code adds it to `f` and advances only `i`.

The symmetric case adds a smaller `nums2[j]` to `g` and advances only `j`.

This is the same ordering logic used by merging sorted lists. Every value is processed once, and equal values are detected exactly when both pointers reach them.

**Synchronize scores at an intersection**

When `nums1[i] == nums2[j]`, both pointers identify the same switching value. A best path arriving there may have followed either array up to that point.

The source computes:

`f = g = max(f, g) + nums1[i]`

Choosing `max(f, g)` keeps the better route into the intersection. Adding the common value once respects the rule that path score sums unique visited values; the same numeric intersection must not be counted twice.

Assigning the new total to both accumulators means that after visiting the intersection, the optimal path can legally continue in either array. Both pointers advance, so the common value is consumed once from each input representation.

**Handle an exhausted array**

The loop continues while either array still has values. If `i == m`, only `nums2` has unprocessed values. No future common value can exist because the first array is exhausted, so those remaining values can only extend the second-array route. The solution adds them to `g` one by one.

The case `j == n` is symmetric and extends `f`.

At the end, the path may finish in either array, so `max(f, g)` is the best complete score.

**Tracing the first example by segments**

Before common value four, the first route has collected two and the second has collected nothing. At four, the scores synchronize to six.

Between four and common value eight, the first side adds five while the second adds six. Their totals become eleven and twelve. At eight, the algorithm keeps twelve, adds eight, and sets both scores to twenty.

After eight, the first array contributes ten while the second contributes nine. The final alternatives are thirty and twenty-nine, so the returned score is thirty. This corresponds to path `[2,4,6,8,10]`.

**Why local synchronization gives the global optimum**

Consider the common values in increasing order. Before the first intersection, a path has only two choices: take the first array's prefix or the second array's prefix. The accumulators store exactly those scores.

At any intersection, every valid path reaching it must arrive through one of the two arrays. Taking the larger accumulator therefore preserves the best possible prefix. Once both accumulators receive that same best score plus the intersection value, all earlier decisions are summarized completely; future choices depend only on the current totals.

Inductively, after every common value, `f` and `g` represent optimal paths ending on their respective arrays. Exclusive values extend only their own route, and exhaustion handles the final suffix. The maximum at the end is consequently the maximum among all valid paths.

**Delay the modulo operation**

The source applies modulo $10^9+7$ only to the final maximum. This is essential for the comparisons at intersections: reducing partial sums modulo the constant can reverse their numeric ordering and cause `max(f, g)` to choose the truly smaller score.

Python integers grow as needed, so retaining exact totals does not overflow. Languages with fixed-width integers should use a sufficiently wide type for the unreduced sums.

## Complexity detail

Let $M$ and $N$ be the two array lengths. Every loop iteration advances `i`, `j`, or both. Neither pointer moves backward, so at most $M+N$ values are processed.

All work per value is constant, giving $O(M+N)$ time. The two arrays are already sorted, so no preprocessing sort is needed.

The algorithm stores two pointers, two lengths, two score accumulators, and the modulus. It creates no size-dependent data structure, so auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Dynamic programming table:** It could model positions explicitly but wastes $O(MN)$ work or storage when only intersections matter.
- **Hash common values:** A map can locate intersections but uses extra space and ignores the advantage of sorted arrays.
- **Segment-sum formulation:** Sum values between intersections separately, add the larger segment at each common value, and add the intersection once. It is equivalent to the two accumulators.
- **No common values:** The accumulators become the two complete array sums, and the larger is returned.
- **Common first value:** Both initial scores synchronize immediately at that value.
- **Common last value:** The better complete prefix is selected at the final intersection.
- **One array exhausted early:** Its score stops changing while the other route consumes its remaining suffix.
- **Strictly increasing arrays:** There are no duplicates within one array, so a common value is encountered only once per side.
- **Common-value counting:** The intersection value is added once, never once per array.
- **Switching repeatedly:** Synchronizing both accumulators at every intersection permits any legal sequence of switches.
- **Large totals:** Exact Python integers avoid overflow; modulo is applied only after optimization is complete.
- **Modulo during traversal:** It is unsafe because modular residues do not preserve which true sum is larger.
- **Positive values:** Every remaining suffix value helps its route; there is no decision to skip values within a traversal.
