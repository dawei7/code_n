## General

**Replace universal comparisons with extrema**

Beauty two requires every value left of index `i` to be smaller than `nums[i]` and every value right of it to be larger.

The left condition is equivalent to

$$
\max(\text{left values})<\texttt{nums}[i],
$$

and the right condition is equivalent to

$$
\texttt{nums}[i]<\min(\text{right values}).
$$

Knowing one prefix maximum and one suffix minimum is therefore enough to replace two potentially linear scans at each index.

**Precompute suffix minima**

`right[i]` stores the minimum of `nums[i:]`. The array begins filled with the final value. Scanning from `n-2` down to zero applies

`right[i] = min(right[i + 1], nums[i])`.

By induction, `right[i+1]` is exactly the minimum strictly right of index `i`.

During the later scan, the source sets `r = right[i + 1]` so the current value is excluded from the right side.

There is no need to store a matching prefix-maximum array. The forward loop encounters left values in exactly the order needed, so one scalar can summarize them. The right side cannot be summarized the same way during a forward scan because its values have not yet been visited; that asymmetry explains why the implementation precomputes only suffix minima and rolls only the prefix maximum.

**Maintain the left maximum incrementally**

Variable `l` starts as `nums[0]`. Before testing index one, this is the maximum of all values strictly left of it.

After testing index `i`, the update `l = max(l, nums[i])` prepares the prefix maximum for index `i+1`. Updating after the test is essential; otherwise the current value would be included in its own left side.

**Apply beauty rules in priority order**

The first `if` checks `l < nums[i] < r`. Both inequalities are strict, so equality with any side value prevents beauty two.

Only if that global condition fails does the `elif` check immediate neighbors:

`nums[i - 1] < nums[i] < nums[i + 1]`.

This ordering implements "beauty one only when the previous condition is not satisfied." A globally beautiful index also has locally increasing neighbors, but it must contribute two, not one.

If neither branch succeeds, the index contributes zero.

**Trace an example**

For `[2,4,6,4]`, suffix minima let index one see right minimum four. Its left maximum is two. Global condition `2 < 4 < 4` fails due to strict equality on the right, but local condition `2 < 4 < 6` succeeds, so it contributes one.

At index two, left maximum is four and right minimum is four. Neither the global nor local strict condition succeeds, so it contributes zero.

**Why endpoints are excluded**

Only indices one through $N-2$ have both a left and right neighbor. The loop `range(1, n - 1)` visits exactly those indices.

The constraints guarantee $N\ge3$, so the range and suffix accesses are valid.

**Why the algorithm is correct**

Before each iteration, `l` is the maximum strictly left and `right[i+1]` is the minimum strictly right. The first test is therefore equivalent to the problem's two universal quantifiers.

When that test fails, the second test exactly matches the local fallback definition. Mutually exclusive branching assigns the specified beauty once. Summing contributions across every eligible index gives the answer.

**Why strictness matters**

Replacing either less-than sign with less-than-or-equal would incorrectly accept duplicates. For beauty two, every left value must be strictly smaller and every right value strictly larger. For beauty one, both immediate comparisons are likewise strict.

For example, in `[1,2,2,3]` neither middle two has global beauty: one has an equal value on its right and the other has an equal value on its left. The local checks also reject equality, so the total remains zero rather than awarding beauty for a merely nondecreasing pattern.

## Complexity detail

Let $N$ be array length. Building suffix minima takes $O(N)$ time, and the forward beauty scan takes $O(N)$ time. Total time is $O(N)$.

The `right` array uses $O(N)$ space. The rolling left maximum, answer, and scalar values use $O(1)$ additional space. The input is not modified.

## Alternatives and edge cases

- **Prefix-max and suffix-min arrays:** Store both sides explicitly; still $O(N)$ time but uses another $O(N)$ array instead of rolling `l`.
- **Scan all left and right values per index:** Direct but takes $O(N^2)$ time.
- **Monotonic structures:** Unnecessary because static prefix and suffix extrema are simpler.
- **Strictly increasing array:** Every eligible index has beauty two, so total is $2(N-2)$.
- **Strictly decreasing array:** Every eligible index has beauty zero.
- **Duplicate boundary value:** Prevents beauty two because inequalities are strict.
- **Global condition succeeds:** Do not also add local beauty one.
- **Global fails but local succeeds:** Add exactly one.
- **Length three:** There is exactly one eligible middle index.
- **Large values:** Only comparisons and small beauty sums are used.
- **Update order:** Test with current excluded from `l`, then incorporate it.
- **Right index:** Use `right[i+1]`, not `right[i]`.
- **Input preservation:** The method creates a separate suffix array.
