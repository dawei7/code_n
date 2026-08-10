## General

**Use sorted order to remove absolute-value branches**

For current value `x = nums[i]`, every element to the left is at most `x` and every element to the right is at least `x`. Therefore:

- a left contribution is `x - nums[j]`;
- a right contribution is `nums[j] - x`.

The sorted guarantee is what lets the algorithm replace every absolute value with one known subtraction direction.

**Sum all left-side differences at once**

There are `i` elements before index `i`. If all of them were raised to `x`, their combined value would be `x * i`. Their actual combined value is the running prefix sum `t`.

Thus the total difference from the left side is

$$
x\cdot i-t.
$$

At the start of each iteration, `t` contains only indices strictly before `i` because the source adds `x` after computing the answer.

**Sum all right-side differences at once**

`s = sum(nums)` is the total of the entire array. The actual sum strictly to the right is

$$
s-t-x.
$$

There are `n-i-1` right-side elements. If each were reduced to `x`, their combined value would be

$$
x(n-i-1).
$$

So the right contribution is

$$
(s-t-x)-x(n-i-1).
$$

The exact source writes the complete expression as

`x * i - t + s - t - x * (len(nums) - i)`.

To see the equivalence, expand its right portion:

$$
s-t-x(n-i)
=s-t-x-x(n-i-1).
$$

That is exactly right sum minus the target total for the right-side count.

**Build each answer in constant time**

For each `i`, `v` adds the left and right contributions. The element at index `i` itself contributes zero, so it does not need an explicit term.

After appending `v`, `t += x` moves the current value into the prefix for the next iteration.

For `nums = [2, 3, 5]`, total `s` is ten.

- At `i = 0`, `t = 0`. The formula gives zero from the left and `(3-2)+(5-2)=4` from the right.
- At `i = 1`, `t = 2`. Left contribution is `3*1-2=1`; right contribution is `5-3=2`; total is three.
- At `i = 2`, `t = 5`. Left contribution is `5*2-5=5` and the right side is empty.

The result is `[4, 3, 5]`.

**Why duplicates are handled correctly**

Sorted order is non-decreasing, not necessarily strict. If a left or right value equals `x`, its difference is zero. The aggregate formulas automatically include that zero: adding another `x` increases both the count-times-`x` target and the actual side sum by the same amount.

No distinctness or strict-order assumption is used.

**Why the output is correct**

For each index, every other position lies uniquely on its left or right. Sorted order makes the corresponding absolute difference equal to the derived signed difference. The two aggregate formulas sum all positions on their respective sides exactly once.

Their sum is therefore $\sum_j |\texttt{nums[i]}-\texttt{nums[j]}|$, with the self-term implicitly zero. The loop evaluates every index and appends values in matching order, so the returned array satisfies the contract.

**The prefix invariant**

Before iteration `i`, `t` equals the sum of exactly `nums[0:i]`. This is true initially because the slice is empty and `t = 0`. The formula reads that value before changing it, and `t += x` then makes it the sum through index `i`, which is precisely the needed prefix for the next iteration. This invariant is what lets one scalar replace an entire prefix-sum array.

## Complexity detail

Let `n` be the length of `nums`. Computing `s` scans the array once, and the main loop scans it once more. Every iteration performs constant-time arithmetic, so total time is $O(n)$.

The required output list stores `n` integers. Excluding output, the algorithm keeps only `s`, `t`, `i`, `x`, and `v`, so auxiliary working space is $O(1)$. Including the returned list, total additional storage is $O(n)$.

The source repeatedly calls `len(nums)`, which is $O(1)$ for Python lists.

## Alternatives and edge cases

- **Full prefix-sum array:** It provides left and right sums by indexing and is easy to derive, but uses $O(n)$ auxiliary space beyond the output.
- **Brute force per index:** Summing all absolute differences independently takes $O(n^2)$ time and ignores sorted structure.
- **Unsorted input:** The signed-side formulas become invalid. Sorting first would cost $O(n\log n)$ and would also lose original output positions unless indices are tracked.
- **All values equal:** Both side formulas cancel to zero at every index, returning an all-zero result.
- **Duplicate runs:** Equal neighbors contribute zero and require no special branch.
- **First index:** The left count and prefix sum are zero, so only right contributions remain.
- **Last index:** The algebraic right contribution becomes zero, so only left contributions remain.
- **Two elements:** Each result is the same absolute difference between the pair.
- **Update prefix after calculation:** Moving `t += x` before the formula would include the current value in the left prefix and break the count relationship.
- **Large total sums:** Python integers avoid overflow. Fixed-width languages should use a sufficiently wide integer type because up to $10^5$ values contribute.
- **Output-space convention:** The manifest’s $O(1)$ space excludes the required result array; the implementation necessarily returns $O(n)$ values.
