## General

**The key effect of deleting one position**

Deleting index `i` does not merely remove `nums[i]`. Every element to the right shifts one position left, so its parity changes: original even indices become odd indices, and original odd indices become even indices. Elements to the left keep their indices and therefore keep their parity.

Rebuilding the array and resumming it for every possible deletion would make this parity shift easy to model but would cost quadratic time. The source instead separates each candidate array into a left part that keeps parity and a right part that swaps parity.

`s1 = sum(nums[::2])` is the total of all original even-indexed values. `s2 = sum(nums[1::2])` is the total of all original odd-indexed values. During the scan:

- `t1` is the sum of original even-indexed values strictly before `i`;
- `t2` is the sum of original odd-indexed values strictly before `i`.

Both prefix variables start at zero. Crucially, the fairness test occurs before the current value is added, so they always describe only indices to the left of the candidate deletion.

**Deleting an even index**

Suppose `i` is even and `v = nums[i]`. On the left, the new even-index sum receives `t1` and the new odd-index sum receives `t2`.

On the right, parities swap. The original odd-indexed suffix becomes even-indexed after deletion. Its sum is `s2 - t2` because the current even value is not part of `s2`. Therefore

$$
\text{newEven} = t1 + s2 - t2.
$$

The original even-indexed suffix becomes odd-indexed. From the original even total `s1`, subtract the earlier even prefix `t1` and also subtract the deleted current value `v`. Therefore

$$
\text{newOdd} = t2 + s1 - t1 - v.
$$

The first Boolean expression in the source compares exactly these two quantities:

`t2 + s1 - t1 - v == t1 + s2 - t2`.

It is guarded by `i % 2 == 0`, so it contributes only for an even deletion.

**Deleting an odd index**

If `i` is odd, the left contributions are still `t1` to new even and `t2` to new odd. The right suffix again swaps parity.

The original odd suffix, excluding current `v`, moves to even positions. Its sum is `s2 - t2 - v`. The original even suffix moves to odd positions and has sum `s1 - t1`. Hence

$$
\text{newEven} = t1 + s2 - t2 - v
$$

and

$$
\text{newOdd} = t2 + s1 - t1.
$$

The second source expression checks their equality and is guarded by `i % 2 == 1`.

**Counting with Boolean arithmetic**

In Python, `True` behaves as integer one and `False` as integer zero in addition. Each line of the form `ans += condition` therefore increments `ans` exactly when that candidate deletion produces a fair array. Because an index cannot be both even and odd, at most one of the two guarded conditions contributes during an iteration.

After testing index `i`, the method updates the matching prefix total. If `i` is even, `v` is added to `t1`; if odd, it is added to `t2`. This establishes the prefix invariant for the next index.

For `nums = [2, 1, 6, 4]`, the original even total is `8` and odd total is `5`. At `i = 1`, `t1 = 2` and `t2 = 0`. Deleting odd value `1` gives new even `2 + 5 - 0 - 1 = 6` and new odd `0 + 8 - 2 = 6`, so that index is counted.

**Why every counted index and only every valid index is counted**

For a fixed deletion, every remaining element lies either before or after `i`. The formulas include every left value in its original parity total and every right value in the opposite parity total. They exclude `v` exactly once. Thus the two calculated sums are precisely the even- and odd-indexed sums of the post-deletion array.

Equality is the definition of fairness, so a true test means the deletion is valid. If the test is false, the actual post-deletion sums differ, so that index is invalid. The loop considers every index once and accumulates exactly the true cases, making the returned `ans` correct.

## Complexity detail

Let `n` be the length of `nums`. The two total-sum computations together inspect all elements once, and the main loop inspects all elements once more. Every loop iteration performs constant-time arithmetic, so total running time is $O(n)$.

The scalar algorithmic state—`s1`, `s2`, `t1`, `t2`, `ans`, `i`, and `v`—is $O(1)$. However, the exact Python expressions `nums[::2]` and `nums[1::2]` create sliced lists before summing them. Their combined sizes are linear, and peak temporary auxiliary memory is $O(n)$. The manifest’s $O(1)$ space bound would match totals computed by a loop or generator without materializing slices, but not these exact slice operations.

No post-deletion arrays are created inside the main loop, which is what preserves linear rather than quadratic time.

## Alternatives and edge cases

- **Four running sums without slices:** First accumulate even and odd totals in one loop, then use the same prefix formulas. This preserves $O(n)$ time and achieves true $O(1)$ auxiliary space.
- **Prefix arrays:** Store even and odd prefix sums for every boundary and evaluate each deletion from those arrays. The formulas can be intuitive, but storage is $O(n)$ and more than the exact rolling state needs.
- **Delete and rescan for every index:** This directly follows the definition but takes $O(n^2)$ time and repeatedly shifts or reconstructs data.
- **Single-element array:** Removing its only element leaves an empty array; both parity sums are zero, so the sole index is correctly counted.
- **Deletion at index zero:** Both prefix sums are zero, and every surviving original index shifts parity. The formulas reduce to the swapped suffix totals.
- **Deletion at the last index:** There is no right suffix to swap. The total-minus-prefix expressions correctly reduce to zero after excluding the current value.
- **Odd array length:** Nothing requires equal counts of even and odd positions; only their value sums after deletion must match.
- **All equal values:** Some or all removals may work depending on length. The parity formulas handle the shifted counts rather than assuming equality automatically.
- **Positive-value constraint:** The derivation uses only addition and subtraction, so it would remain correct for zero or negative values as well.
- **Update ordering:** Adding `v` to `t1` or `t2` before testing would incorrectly treat the deleted value as part of the preserved left prefix.
- **Slice-memory subtlety:** Slicing is not a view in Python lists. A constant-space rewrite must avoid `nums[::2]` and `nums[1::2]` rather than merely discarding them after `sum`.
