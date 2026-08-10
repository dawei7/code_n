## General

**Maintain sums strictly outside the current index**

For index `i`, the required left sum contains positions before `i`, while the right sum contains positions after `i`. The current value belongs to neither side.

The source maintains exactly these two quantities:

- `l` is the sum strictly left of the current index;
- after one subtraction, `r` is the sum strictly right of the current index.

It initializes `l = 0` because nothing lies before index zero. It initializes `r = sum(nums)`, which initially includes every value.

**Remove the current value before comparing**

At each loop iteration, `r -= x` removes `nums[i]` from the remaining total. Before this line, `r` contains the current value and everything to its right. After it, `r` contains only elements after `i`.

`l` has not yet been updated for the current iteration, so it still contains only positions before `i`. The test `if l == r` therefore checks the middle-index definition exactly.

Only after a failed comparison does `l += x` move the current value into the left sum for the next index.

Changing this order is a common bug. Adding to `l` before comparing or subtracting from `r` after comparing would include the candidate value on one side and test the wrong equation.

**Trace the first example**

For `[2, 3, -1, 8, 4]`, the total is 16.

At index zero, remove two from `r`, leaving 14; `l` is zero, so the index fails. Then add two left.

At index one, remove three, leaving 11; left is two, so it fails. Add three to make left five.

At index two, removing -1 increases `r` from 11 to 12; left is five, so it fails. Adding -1 changes left to four.

At index three, remove eight, leaving right sum four. Left is also four, so index three is returned.

This trace also shows why negative values cause no problem. Subtracting a negative correctly increases the remaining right sum.

**Why the first returned index is leftmost**

The loop uses `enumerate(nums)`, which visits indices in increasing order starting from zero. It returns immediately on equality. Therefore no later valid middle index can be returned ahead of an earlier one.

If no index passes, the loop completes and returns -1.

**Boundary indices need no special cases**

At index zero, `l` is zero by initialization. That matches the defined empty left side.

At the last index, subtracting the current value makes `r` zero because no later elements remain. That matches the defined empty right side.

The same invariant handles both boundaries naturally.

**Derive the equivalent total-sum equation**

Let total sum be $T$ and left sum before index $i$ be $L$. The right sum is

$$
T-L-\texttt{nums}[i].
$$

The condition is $L=T-L-\texttt{nums}[i]$. The source realizes this equation incrementally by shrinking `r` and growing `l`, avoiding repeated range summation.

**Why the algorithm is correct**

Initially, the invariant holds before index zero: left sum is zero, and `r` includes the unprocessed suffix.

At an iteration, removing `x` makes `r` the exact sum after the current index while `l` remains the exact sum before it. Equality is therefore necessary and sufficient for a middle index. If it fails, adding `x` prepares the exact left sum for the next iteration.

By induction, every index is tested with correct side sums. The first successful one is returned, and -1 is returned only when none succeeds.

**Why one initial full sum is worthwhile**

Computing left and right slices at every index would repeat work and allocate temporary lists in Python. One total-sum pass followed by one incremental pass keeps the overall work linear and storage constant.

The exact source performs two passes over the values: one inside `sum(nums)` and one in the loop. A constant number of linear passes is still $O(N)$.

## Complexity detail

Let $N$ be the array length. `sum(nums)` takes $O(N)$ time, and the loop takes another $O(N)$ time. Total time is $O(N)$.

Only `l`, `r`, `i`, and `x` are stored beyond the input, so auxiliary space is $O(1)$. No prefix array or slices are created.

## Alternatives and edge cases

- **Prefix-sum array:** Allows direct left/right queries but uses $O(N)$ extra space that the rolling sums avoid.
- **Recompute both sides for every index:** Straightforward but takes $O(N^2)$ time and Python slicing may allocate extra memory.
- **Equation with total and left only:** Check `2 * left + nums[i] == total`; it is equivalent and also uses constant space.
- **Valid index zero:** Detected when the remaining total after removing the first value is zero.
- **Valid last index:** Detected when the accumulated left sum is zero after the last value is removed from the right.
- **Single-element array:** Both sides are empty, so index zero is returned.
- **Negative values:** Fully supported; sums need not change monotonically.
- **Several valid indices:** Increasing traversal and immediate return select the leftmost.
- **No valid index:** The final result is -1.
- **Total sum zero:** It does not automatically make every index valid; the current value and left sum still matter.
- **Update order:** Subtract current from right, compare, then add current to left.
- **Input preservation:** The method reads values without changing `nums`.
