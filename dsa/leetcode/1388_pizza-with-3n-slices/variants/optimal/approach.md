## General
**Break the circular conflict.** The first and last slices are adjacent, so they cannot both be chosen. Every valid selection therefore belongs to at least one of two linear cases: exclude the last slice, or exclude the first slice. Solve both and keep the larger sum.

**Track an exact selection count.** For one linear array, let the dynamic-programming state after a prefix record the best sum for each count from `0` through `C`. When processing a slice, either skip it and retain the previous-prefix value, or take it and add its size to the state from two prefixes earlier with one fewer selected slice.

Initialize count zero to sum zero and all impossible positive counts to negative infinity. This prevents a state from claiming more selections than its prefix can supply. Rolling the arrays for the previous one and two prefixes preserves every recurrence dependency.

The recurrence considers both possibilities for the final slice of every prefix, so it covers all nonadjacent exact-count selections. The two outer cases cover the circular boundary, establishing the global optimum.

## Complexity detail
Each linear case processes $O(L)$ slices and updates $C$ counts, giving $O(LC)$ time. Three rolling count arrays use $O(C)$ space.

## Alternatives and edge cases
- **Full table dynamic programming:** Store every prefix-and-count state. It has the same $O(LC)$ time but uses $O(LC)$ space.
- **Rescan prior endpoints:** For every chosen count and ending position, search all compatible previous endpoints. It is correct but takes $O(L^2C)$ time.
- **Greedy largest slice:** Taking the current largest value can block two moderately large neighbors whose combined contribution is better.
- **First and last conflict:** Solve two linear exclusions; never allow both circular endpoints.
- **Exactly `C` selections:** Do not maximize over smaller counts, even though all sizes are positive.
- **Three slices:** Alice chooses the single largest slice.
- **Equal sizes:** Any valid $C$ nonadjacent positions give the same total.
