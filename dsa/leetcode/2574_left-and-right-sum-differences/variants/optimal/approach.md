## General

**Maintain both sides instead of building two arrays**

For each index $i$, the required values are the sum strictly before $i$ and the sum strictly after $i$. Recomputing both sums independently at every index would repeat work and cost $O(n^2)$ time.

The solution carries two running totals:

- `l` is the sum of elements already passed, so it represents the current left sum;
- `r` is the sum of elements not yet passed.

Initially no element lies to the left, so `l = 0`. The initial `r = sum(nums)` contains the entire array, including the first current element. The order of updates inside the loop removes that current element before using `r`.

**Why the update order matters**

For each current value `x`, the statements occur in this exact order:

1. `r -= x`;
2. append `abs(l - r)`;
3. `l += x`.

Before step one, `r` includes the current value and everything to its right. Subtracting `x` makes it equal to the sum strictly to the right, which is `rightSum[i]`.

At that same moment, `l` contains only earlier values because the current value has not yet been added. It is exactly `leftSum[i]`. The appended absolute difference is therefore correct for the current index.

Only after recording the answer does the code add `x` to `l`, preparing it to be part of the left side at the next index.

If the last two updates were reversed, the current element would incorrectly appear on the left. If the subtraction from `r` occurred after appending, it would incorrectly appear on the right. The compact algorithm depends on this sequencing.

**A loop invariant**

At the beginning of the iteration for index $i$:

$$
\texttt{l}=\sum_{k=0}^{i-1}\texttt{nums[k]}
$$

and

$$
\texttt{r}=\sum_{k=i}^{n-1}\texttt{nums[k]}.
$$

Subtracting `nums[i]` changes `r` into the suffix strictly after $i$. The algorithm appends the exact absolute difference, then adding `nums[i]` changes `l` into the prefix through $i$. Those are precisely the invariant values required at the beginning of iteration $i+1$.

The invariant is true initially because the empty prefix sums to zero and `r` is the total array sum. By induction, every appended result is correct.

**Trace the sample**

For `nums = [10,4,8,3]`, initial state is `l=0` and `r=25`.

- At $10$, subtracting it gives right sum $15$. The difference is $|0-15|=15$. Then `l` becomes $10$.
- At $4$, `r` falls from $15$ to $11$. The difference is $|10-11|=1$. Then `l` becomes $14$.
- At $8$, `r` falls to $3$. The difference is $|14-3|=11$. Then `l` becomes $22$.
- At $3$, `r` becomes $0$. The difference is $|22-0|=22$.

The output is `[15,1,11,22]`, matching explicit left and right sum arrays without ever storing those arrays.

**Why absolute value is applied last**

The problem asks for the magnitude of the difference. Either side may be larger. Taking `abs(l-r)` after both exact sums are known handles both cases. Taking absolute values of individual elements or intermediate running changes would lose sign information and would not compute the difference of sums.

Although all input values are positive here, the same invariant and formula would also work with negative values. Positivity merely makes left sums non-decreasing and right sums non-increasing; correctness does not depend on those monotonic properties.

**Input and output behavior**

The loop reads `nums` in its original order and never assigns into it, so the caller's input remains unchanged. `ans` grows by exactly one value per input element, guaranteeing the required output length $n$.

At the first index, `l` correctly remains zero because nothing is to the left. At the last index, subtracting the last current value makes `r` zero because nothing is to the right. No boundary branches are needed.

## Complexity detail

Computing `sum(nums)` takes $O(n)$ time. The loop visits each element once and does constant work, adding another $O(n)$. Total time is $O(n)$.

The returned `ans` list holds $n$ integers, so output-inclusive space is $O(n)$ as stated in the manifest. Excluding required output, `l`, `r`, and `x` use $O(1)$ auxiliary space. The input list is not copied.

## Alternatives and edge cases

- **Explicit left and right arrays:** Two prefix/suffix passes are correct but allocate two additional $O(n)$ arrays when two running totals suffice.
- **Recompute sums for each index:** Slicing and summing both sides at every position costs $O(n^2)$ time.
- **One prefix array plus total sum:** This also answers each position in $O(1)$ after preprocessing, but still stores $O(n)$ auxiliary prefix values.
- **Single element:** Subtracting it makes `r=0` while `l=0`, so the sole answer is zero.
- **First position:** The initialized left sum is the required empty-side zero.
- **Last position:** Removing the current value from `r` leaves the required empty-side zero.
- **Equal side sums:** Absolute difference is zero, which the code appends normally.
- **Large total:** The maximum sum can exceed a 32-bit integer under broader constraints; Python integers expand automatically.
- **Update order:** Remove the current value from the right before measuring, and add it to the left only afterward.
- **Input preservation:** All updates affect scalar totals and the new answer list, never `nums`.
