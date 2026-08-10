## General

The chosen original subarray must be contiguous, and after optionally deleting one element, at least one element must remain. Deleting an interior element can connect a profitable subarray on its left with a profitable subarray on its right. The exact solution prepares the best sum available on each side of every possible deletion.

**Best nonempty subarray ending at each index**

The array `left` is built from left to right. After processing index `i`, `left[i]` is the maximum sum of a nonempty contiguous subarray that ends exactly at `i`.

The running value is updated with

`s = max(s, 0) + x`.

Before adding current value `x`, the preceding best ending sum `s` has two possibilities. If it is positive, extending it with `x` is better than starting over. If it is zero or negative, including it cannot improve a subarray that must end at the current index, so the best choice starts fresh with `x`. This is Kadane’s recurrence in an ending-at-current-position form.

Starting `s` at zero does not incorrectly allow an empty answer. Every update adds `x` before storing the value, so `left[i]` always contains at least the current element.

**Best nonempty subarray starting at each index**

The reverse loop applies the same reasoning from right to left. After it processes `i`, `right[i]` is the maximum sum of a nonempty contiguous subarray that starts exactly at `i`. A positive best suffix from `i + 1` is worth extending; a nonpositive suffix is discarded, leaving `arr[i]` as the new start.

Together, the tables answer two precise questions in constant time: what is the best sum ending immediately before a deleted index, and what is the best sum starting immediately after it?

**Keep every element as one candidate**

The code initializes `ans = max(left)`. This is the best ordinary nonempty subarray sum with no deletion. The operation is optional, so every correct solution must consider this case.

This initialization also handles deletions at the edge of a chosen interval. If deleting the first element would leave a profitable contiguous block to its right, that remaining block can simply be chosen as the original subarray with no deletion. The same applies to deleting a final element. Therefore, only deletion indices with actual elements on both sides need an explicit join.

**Delete one interior element**

For each index `i` from one through `n - 2`, deleting `arr[i]` can connect a left piece ending at `i - 1` and a right piece starting at `i + 1`. Their best possible combined sum is

`left[i - 1] + right[i + 1]`.

Before deletion, the chosen original interval runs from the left piece’s start through the right piece’s end, so it is contiguous and contains `arr[i]`. After deleting that one element, the two retained pieces become adjacent in the resulting sequence. Both pieces are nonempty, so the post-deletion subarray is nonempty.

The loop takes the maximum of all such joined sums and the no-deletion answer. It does not add `arr[i]` because that is precisely the element being removed.

For `[1, -2, 0, 3]`, the best ending sum just before `-2` is one. The best starting sum immediately after it is three, obtained from `[0, 3]`. Deleting `-2` therefore gives `1 + 3 = 4`. The ordinary maximum without deletion is three, so the joined candidate wins.

**Why these candidates cover every legal optimum**

If an optimal choice performs no deletion, it is some nonempty ordinary subarray. `max(left)` includes its best possible ending-position value and is at least that sum.

If an optimal choice deletes an interior element, the retained elements before the deletion form a contiguous subarray ending immediately before it, and the retained elements after it form a contiguous subarray starting immediately after it. Replacing either side with the corresponding best `left` or `right` value cannot reduce the sum, so the loop’s candidate for that deletion is at least the optimum and is itself feasible.

If the deletion removes an endpoint, the remaining elements form an ordinary nonempty subarray and are already covered by `max(left)`. These cases exhaust every allowed solution, while every candidate constructed by the algorithm is valid. The maximum is therefore exact.

For an all-negative array, each ending-state recurrence starts over at the current value because extending a negative prefix is worse. `max(left)` becomes the largest individual element. The algorithm never returns zero by deleting the only chosen element, so it respects the nonempty requirement.

## Complexity detail

Let $n$ be the length of `arr`.

The forward pass, reverse pass, `max(left)` operation, and interior-deletion loop each scan at most $n$ entries. Every iteration performs constant work, so total time complexity is $O(n)$.

The exact implementation allocates two lists, `left` and `right`, each containing $n$ integers. Its auxiliary-space complexity is therefore $O(n)$. The remaining scalar variables use $O(1)$ space, and the output is one integer.

An alternative two-state dynamic program can obtain $O(1)$ auxiliary space, but that is not the storage behavior of this shipped solution. Complexity documentation should describe the arrays the code actually creates.

The largest absolute sum is bounded by roughly $10^9$ under the constraints. Python handles it safely; fixed-width implementations should choose an adequate integer type.

## Alternatives and edge cases

- **Two-state constant-space dynamic programming:** Maintain the best sum ending at the current position with no deletion and with one deletion already used. This preserves $O(n)$ time and reduces auxiliary space to $O(1)$.
- **Try every deletion and rerun Kadane’s algorithm:** This is straightforward but repeats a linear scan for every index, leading to $O(n^2)$ time.
- **No deletion is best:** `ans = max(left)` ensures the algorithm never forces an operation that lowers the result.
- **Single-element array:** There is no valid interior deletion. The join loop is empty, and the sole element is returned rather than an invalid empty sum.
- **All values negative:** The largest single value is returned. Deleting that only selected value to obtain zero is forbidden.
- **Deleting the first or last chosen element:** The remaining interval is already represented as a no-deletion subarray, so explicit endpoint joins are unnecessary.
- **Zero values:** A zero can be part of either best side and can also be deleted. The recurrence correctly treats a zero previous sum as no better than restarting.
- **Interior deletion connects two positive regions:** The left and right tables independently select the most profitable contiguous pieces adjacent to the deleted index.
- **At most one deletion:** Every joined candidate removes exactly one element, while `max(left)` removes none. No candidate uses two deletions.
- **Contiguity before deletion:** The joined pieces sit immediately on either side of `i`, so adding them corresponds to one original contiguous interval with only `arr[i]` removed.
