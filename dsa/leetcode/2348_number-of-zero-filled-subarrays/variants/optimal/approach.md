## General

**Count subarrays by where they end**

Every nonempty subarray has one unique ending index. Instead of generating all possible start-end pairs, the algorithm asks a smaller question at each position:

> How many zero-filled subarrays end at the current element?

If the current value is nonzero, the answer is zero. If it is zero and belongs to a consecutive run of `cnt` zeros ending here, then there are exactly `cnt` valid ending subarrays—one starting at each position in that run.

The solution maintains this run length and adds it to the total.

**Extend the current zero run**

`cnt` starts at zero. When current `x == 0`, the code increments `cnt`.

Suppose the previous position ended a run of `r` zeros. There were `r` zero-filled subarrays ending there. Appending the new zero extends each of those `r` subarrays and also creates the single-element subarray containing only the new zero. The new ending count is therefore `r + 1`, exactly the updated `cnt`.

The method immediately adds `cnt` to `ans`, recording every zero-filled subarray whose unique final index is the current position.

**Reset after a nonzero value**

When `x` is nonzero, no zero-filled subarray can end at it. A contiguous subarray cannot skip this value, so any earlier zero run is separated from future zeros.

The assignment `cnt = 0` clears the ending state. The code does not add anything to `ans` in this branch.

If the next element is zero, its run begins at length one rather than incorrectly continuing across the separator.

**A complete run contributes a triangular number**

Consider a consecutive run of `L` zeros. As the scan crosses it, the contributions are

`1 + 2 + 3 + ... + L = L(L+1)/2`.

This is exactly the number of nonempty subarrays contained in that run: there are `L` length-one choices, `L-1` length-two choices, and so on down to one length-`L` choice.

The streaming method computes this triangular total incrementally and automatically handles several runs without separately detecting their endpoints.

For `[0,0,0,2,0,0]`, the first run adds 1, 2, and 3 for a subtotal of 6. The value 2 resets `cnt`. The final run adds 1 and 2, producing total 9.

**Why no subarray is missed or counted twice**

Fix any zero-filled subarray ending at index `i`. Its start lies somewhere in the current consecutive zero run, so it is one of the `cnt` choices added while processing `i`.

Conversely, every one of those `cnt` start positions through `i` contains only zeros by the run invariant, so every counted object is valid.

Different iterations count subarrays with different ending indices, so they cannot duplicate the same subarray. Since every nonempty subarray has one end, the accumulated `ans` is exact.

**Loop invariant**

After processing each value:

- `cnt` equals the number of consecutive zeros ending at that position;
- `ans` equals the number of zero-filled subarrays wholly contained in the processed prefix.

The invariant holds initially with an empty prefix. A zero extends the run and contributes precisely the new ending subarrays. A nonzero resets the run and creates no new valid ending subarray. Induction proves the returned total.

**Why values other than zero need no distinction**

Positive and negative nonzero integers both break a zero-filled run in exactly the same way. Their magnitude and sign never enter the logic, so one equality check covers the full input range.

## Complexity detail

Let `n` be the array length. The loop visits every value exactly once and performs constant-time comparisons, increments, and assignments. Running time is `O(n)`.

Only `ans`, `cnt`, and the current value are stored, so auxiliary space is `O(1)`. The method does not build run lists, prefix arrays, or subarray objects.

The maximum result occurs for all zeros and equals `n(n+1)/2`. Python integers hold it safely. The input list is read without mutation.

## Alternatives and edge cases

- **Detect complete runs and use `L(L+1)/2`:** This is equally linear but requires finalizing a run at separators and after the loop. The ending-count method avoids a special final step.
- **Enumerate all subarrays:** There are `O(n^2)` candidates, and checking their contents can add another factor. The run invariant eliminates this work.
- **Prefix sums:** A zero-sum subarray is not necessarily zero-filled when negative values exist, so numeric prefix sums solve a different condition.
- **One zero:** It contributes exactly one subarray.
- **One nonzero:** The answer remains zero.
- **All zeros:** Contributions are 1 through `n`, giving the triangular maximum.
- **No zeros:** `cnt` is repeatedly reset and `ans` stays zero.
- **Separated single zeros:** Each run contributes one; no subarray crosses a nonzero separator.
- **Several long runs:** Their triangular contributions add independently.
- **Negative nonzero values:** They reset the run just like positive values.
- **Zero after a separator:** It begins a new run with `cnt = 1`.
- **Subarray identity:** Equal value sequences at different positions are distinct subarrays and are counted at their distinct endpoints.
- **No empty subarray:** Contributions start at one only when an actual zero is processed.
- **Input preservation:** The scan does not alter `nums`.
