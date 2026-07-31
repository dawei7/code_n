## General

Start with the unchanged array because the operation is optional. Removing a positive value cannot improve the answer: any subarray in the shortened array that crosses removed positive elements corresponds to an original contiguous interval whose sum is larger after those positive elements are restored. Removing zero can only tie the unchanged result. It is therefore sufficient to test each distinct negative value.

Represent the current array with a segment tree. Every node stores four quantities for its interval:

- its total retained sum;
- the maximum sum of a non-empty retained prefix;
- the maximum sum of a non-empty retained suffix;
- the maximum sum of a non-empty retained subarray.

For adjacent nodes $L$ and $R$, the combined total is their sum. A best prefix is either a prefix of $L$ or all of $L$ followed by a prefix of $R$; the suffix is symmetric. A best subarray lies entirely in one child or crosses the boundary as the best suffix of $L$ plus the best prefix of $R$. These alternatives completely describe every non-empty contiguous choice after deletions.

A present array element $v$ is the leaf `(v, v, v, v)`. A removed position has total zero but negative infinity for its prefix, suffix, and best values. It therefore contributes no value when neighboring retained pieces join, while it can never become an empty maximum subarray. The same state safely pads the tree beyond the end of `nums`.

Group positions by their negative value. For one candidate $x$, update every position containing $x$ to the removed state, read the root's best subarray, and then restore those positions before testing another value. The initial root covers the no-operation choice. Each legal deletion is tested exactly once, and the root merge rules return precisely the maximum subarray of that resulting array, so the greatest recorded root value is the requested answer.

## Complexity detail

Building the segment tree takes $O(n)$ time. Each negative occurrence is removed once and restored once, and a point update touches $O(\log n)$ nodes. Across all distinct negative values there are at most $n$ such occurrences, so the total time is $O(n\log n)$. The tree, position groups, and stored indices use $O(n)$ space.

The benchmark defines `size` as $n$ and uses three arrays containing many distinct negative values. The accepted update sweep performs $O(n\log n)$ work. A correct baseline that filters the array and reruns Kadane's algorithm separately for every distinct negative value requires $O(n^2)$ time on these inputs and must fail only the scaling verdict.

## Alternatives and edge cases

- **Filter plus Kadane for every value:** This is straightforward and correct, but $O(n)$ work for each of up to $n$ distinct negative values yields $O(n^2)$ time.
- **Recompute the whole segment tree per value:** Rebuilding after every candidate also costs $O(n^2)$ instead of sharing point updates.
- **Positive or zero candidates:** Removing a positive value cannot help, and removing zero cannot beat the unchanged array, so neither needs a trial.
- **All-negative arrays:** The maximum subarray remains non-empty; the answer may be the largest single negative value.
- **One distinct value:** If removing it would empty the array, that operation is illegal, while the initial tree still supplies the unchanged answer.
- **Repeated chosen value:** Every occurrence must be disabled before the root is inspected and every one must be restored afterward.
- **Removed and padding leaves:** Negative-infinity prefix, suffix, and best values prevent empty leaves from being selected as a subarray.
