## General
**Expose the ordering already present in each tree**

An in-order traversal visits a binary search tree's values in ascending order. Traverse each tree iteratively with a stack, producing two sorted arrays `first` and `second`. The iterative form also handles a valid tree that degenerates into a chain without depending on the language's recursion limit.

**Merge instead of sorting again**

Maintain one index into each sorted array. At every step, append the smaller current value; when the values are equal, either side may be chosen because the other equal value remains available for a later step. Once one array is exhausted, append the unused suffix of the other.

Every node enters exactly one traversal array. During the merge, the smallest value not yet returned must be at the front of one of the two remaining suffixes, so choosing the smaller front preserves ascending order. Advancing exactly one index per append also preserves duplicates and places all $N$ node values in the answer.

## Complexity detail
The two traversals visit $n+m=N$ nodes, and the merge processes $N$ values, for $O(N)$ time. The traversal arrays, result, and explicit stacks use $O(N)$ space in the worst case. If only auxiliary space beyond the returned array is counted, the two stored traversal arrays still require $O(N)$.

## Alternatives and edge cases
- **Collect then sort:** Traversing both trees into one unsorted array and applying a comparison sort is simpler, but it takes $O(N\log N)$ time instead of using the BST ordering.
- **Two lazy in-order iterators:** Keeping one stack per tree and merging their next values avoids the two complete traversal arrays; auxiliary space becomes $O(h_1+h_2)$ beyond the output, where $h_1$ and $h_2$ are tree heights.
- **Repeated sorted insertion:** Inserting each visited value into its position in a growing array is correct but can take $O(N^2)$ time because later insertions may scan and shift many entries.
- **Empty input trees:** If one root is null, return the other tree's in-order sequence; if both are null, return an empty array.
- **Repeated values:** Equal values from different nodes must appear separately in the result.
- **Skewed trees:** An explicit traversal stack avoids recursion-depth failures on long chains.
