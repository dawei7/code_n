## General

There are exactly $n-1$ adjacent pairs: the pair beginning at index $0$, then the pair beginning at index $1$, and so on through the pair beginning at index $n-2$. Traverse those pairs in that order and compute the bitwise OR of the pair's two values.

Pairing `nums` with the shifted view `nums[1:]` expresses this traversal directly. The first pair is `(nums[0], nums[1])`, the next is `(nums[1], nums[2])`, and the final pair is `(nums[n - 2], nums[n - 1])`. Taking `left | right` for every pair therefore produces exactly the required value at every output index, in the required order. No pair is skipped or repeated.

## Complexity detail

The algorithm evaluates one constant-time OR operation for each of the $n-1$ output positions, so its time complexity is $O(n)$. The returned list contains $n-1$ integers and therefore uses $O(n)$ space. Apart from that output, the traversal needs only $O(1)$ additional state; in Python, `nums[1:]` also materializes an $O(n)$ slice, which does not change the stated bound.

## Alternatives and edge cases

- **Index-based loop:** Iterate `i` from `0` through `n - 2` and append `nums[i] | nums[i + 1]`. It has the same asymptotic bounds and avoids the Python slice.
- **Rebuild every prefix:** Recomputing all adjacent OR values from the start for each new endpoint is correct but takes $O(n^2)$ time and discards repeated work.
- **Minimum length:** When $n=2$, there is exactly one adjacent pair and the result has one element.
- **Zeros:** Since `0 | x = x`, a zero simply copies the neighboring value's set bits into that pair's result.
- **Shared bits and repeated values:** Bitwise OR is applied independently to each pair; overlap between neighboring pairs does not merge or remove output positions.
- **Input preservation:** The result is a new array, and `nums` does not need to be modified.
