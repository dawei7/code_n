## General

**A product is even exactly when it contains an even factor**

An integer product is odd only if every factor is odd. As soon as at least one factor is even, the whole product is divisible by two and therefore even.

So there is no need to calculate any products. Products could grow enormous, and their magnitudes do not matter. The task is simply to count subarrays containing at least one even number.

**Count valid starts for each right endpoint**

Fix a right endpoint `i`. Every subarray ending there is determined by a start index `l` between zero and `i`.

Let `last` be the index of the most recent even number at or before `i`. If no even number has appeared, `last=-1`.

When `last>=0`, a subarray `nums[l..i]` contains that most recent even value exactly when `l<=last`. The valid starts are therefore

$$
0,1,\ldots,\texttt{last},
$$

which is `last+1` choices.

Any start after `last` produces a suffix consisting entirely of odd values, because `last` was the most recent even index. Its product is odd and it must not be counted.

Thus `last+1` is not merely a convenient count; it partitions all possible starts into exactly the valid and invalid sets.

**Maintain the most recent even position**

The loop processes `nums` from left to right with index `i` and value `v`. If `v%2==0`, the current position becomes the most recent even index, so `last=i`. If `v` is odd, `last` remains unchanged.

After that possible update, the method adds `last+1` to `ans`. Updating first is important: when the current value is even, the one-element subarray `[v]` and all other subarrays ending at `i` must be counted immediately.

If no even value has appeared, `last=-1` makes the addition zero. This sentinel eliminates a special branch for an all-odd prefix.

**Why summing by endpoints counts every subarray once**

Every non-empty subarray has exactly one right endpoint. During the iteration for that endpoint, it is counted if and only if its start is at or before the most recent even index, which is equivalent to containing an even factor.

Subarrays ending at different indices are distinct and are handled in different iterations. Subarrays sharing a right endpoint have different start indices and correspond to different choices among the `last+1` valid starts.

Therefore, the accumulated answer contains every even-product subarray exactly once and no odd-product subarray.

**Trace the first sample**

For `nums=[9,6,7,13]`:

- At index 0, value 9 is odd. `last=-1` and zero subarrays ending here qualify.
- At index 1, value 6 is even. `last=1`, so starts 0 and 1 give two qualifying subarrays.
- At index 2, value 7 is odd. `last` stays 1, again giving starts 0 and 1, for two more.
- At index 3, value 13 is odd. The same two starts qualify.

The total is $0+2+2+2=6$.

Notice that the subarray starting at index 2 is excluded at the last two endpoints because it lies entirely after the latest even value.

**Another way to see the formula**

There are `i+1` total subarrays ending at `i`. If the most recent even is `last`, then the all-odd suffix after it has length `i-last`. Those are precisely the invalid starts `last+1` through `i`. Subtracting gives

$$
(i+1)-(i-\texttt{last})=\texttt{last}+1.
$$

This complementary derivation reaches the same update and confirms that no possible start is overlooked.

**Parity is enough**

Input values are positive, but the reasoning would also work for zero and negative integers: zero is even, and sign does not affect parity. Under the actual constraints, modulo two is straightforward and there are no empty subarrays to consider.

The method never mutates `nums` and stores no prefix array.

## Complexity detail

Let $n$ be the array length. The loop visits every element exactly once and performs constant-time parity, assignment, and addition operations. Total time is $O(n)$.

Only `ans`, `last`, and loop variables are stored, so auxiliary space is $O(1)$.

The answer can be as large as the total number of subarrays, $n(n+1)/2$. For $n=10^5$, that exceeds a 32-bit signed integer, so fixed-width implementations need a 64-bit result type. Python integers grow automatically.

No product is ever formed, avoiding both overflow and unnecessary multiplication.

## Alternatives and edge cases

- **Count all subarrays minus all-odd subarrays:** Sum triangular counts of maximal odd runs and subtract from $n(n+1)/2$. It is also linear but requires finalizing runs.
- **Dynamic count ending here:** Track how many even-product subarrays end at the previous position and update based on parity. This is equivalent to remembering the last even index.
- **Prefix parity products:** Multiplying prefix values is unsafe and far more information than needed.
- **All odd values:** `last` remains `-1` and the answer is zero.
- **All even values:** At index `i`, all `i+1` starts qualify, yielding every subarray.
- **First even late:** Earlier all-odd prefixes contribute zero; afterward, starts through that even remain valid.
- **Consecutive evens:** Updating `last` to the newer index increases the number of qualifying starts.
- **Single element:** It contributes one exactly when that element is even.
- **Large count:** Use 64-bit arithmetic outside Python.
- **No product calculation:** Parity alone completely determines whether a product is even.
