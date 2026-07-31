## General

Sort the point indices by `(nums1[i], i)` and process them from left to right. For a current index $i$, every previously inserted index $j$ satisfies $\texttt{nums1}[j] \leq \texttt{nums1}[i]$, so the first absolute-value term is already resolved.

Split prior points according to their second coordinate.

For $\texttt{nums2}[j] \leq \texttt{nums2}[i]$, the distance is

$$
(\texttt{nums1}[i]+\texttt{nums2}[i])
+
(-\texttt{nums1}[j]-\texttt{nums2}[j]).
$$

The current part is fixed, so only the prior index minimizing $-\texttt{nums1}[j]-\texttt{nums2}[j]$ can be best in this range. For $\texttt{nums2}[j] \geq \texttt{nums2}[i]$, the same expansion becomes

$$
(\texttt{nums1}[i]-\texttt{nums2}[i])
+
(-\texttt{nums1}[j]+\texttt{nums2}[j]),
$$

and the required prior index minimizes the second expression.

Maintain one segment tree over second-coordinate positions for each expression. A prefix query supplies the best candidate from coordinates at most the current value; a suffix query supplies the best candidate from coordinates at least it. Tree nodes compare both the minimized expression and the original index, so equal values retain the smaller index. Evaluate the two returned pairs using their actual Manhattan distance and compare `(distance, (smaller_index, larger_index))` tuples globally.

Every pair appears when its later point in sorted order is processed. Within each of the two second-coordinate ranges, the algebra shows that the tree's minimum is the best possible partner for the current point. The final tuple comparison therefore considers a minimum-distance representative from every relevant range and applies the required lexicographic tie-break.

## Complexity detail

Let $n$ be the common array length. Sorting costs $O(n\log n)$. Each point performs two segment-tree queries and two updates, each in $O(\log n)$ time because coordinates lie in $[0,n]$. The total time is $O(n\log n)$. The sorted indices and two segment trees use $O(n)$ space.

## Alternatives and edge cases

- **Divide and conquer:** A closest-pair recursion can also achieve $O(n\log n)$, but Manhattan-distance pruning and lexicographic ties make its implementation more delicate.
- **Check every pair:** Directly evaluating all $\binom{n}{2}$ pairs is simple and handles ties naturally, but requires $O(n^2)$ time.
- **Duplicate points:** Their distance is zero; the global tuple comparison still selects the smallest index pair.
- **Equal first coordinates:** Sorting by original index gives a deterministic processing order, and pairs with equal first coordinates are still considered exactly once.
- **Equal second coordinates:** The coordinate belongs to both query ranges; seeing the same candidate twice is harmless.
- **Lexicographic ties:** Segment-tree comparisons retain the smaller prior index, while the global comparison orders normalized pairs after distance.
- **Coordinate boundary:** Values may equal $n$, so the range structure must include every coordinate from $0$ through the largest value present.
