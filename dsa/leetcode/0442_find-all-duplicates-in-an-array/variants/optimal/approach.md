## General

**Use each value's natural destination index**

The length is $n$, and every value lies in `[1,n]`. Therefore value `v` has a valid canonical array position `v - 1`. If every distinct value is moved to its canonical position, a second occurrence cannot occupy that same position. It must remain somewhere whose index does not match its value, revealing the duplicate.

The solution performs an in-place cycle-placement process. For each index `i`, it repeatedly examines the current value `nums[i]` and its canonical destination `nums[i] - 1`.

**When to swap**

The condition is

`nums[i] != nums[nums[i] - 1]`.

If the destination contains a different value, the current value is not yet represented there. The simultaneous assignment

`nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]`

moves the current value into its canonical slot and brings the displaced value back to index `i` for examination.

Python evaluates all right-hand expressions before performing left-hand assignments. In particular, both destination calculations use the pre-swap `nums[i]`, so the exchange is well-defined even though the array changes.

After a swap, the `while` loop repeats because `nums[i]` is now a different displaced value that may also belong elsewhere.

**Why the destination test stops safely**

If `nums[i] == nums[nums[i] - 1]`, the canonical slot for this value already contains an equal copy.

There are two possibilities. If `i == nums[i]-1`, the current occurrence itself is correctly placed. Otherwise, the canonical position contains the first occurrence and `nums[i]` is the second copy. Swapping equal values would make no progress and loop forever, so equality is exactly the correct stopping condition.

The “at most twice” guarantee means there is only one extra copy to account for per duplicate value.

**Why every swap makes permanent progress**

Let the current value be `v` and its destination be `v-1`. A swap occurs only if the destination does not already contain `v`. After the swap, `nums[v-1] == v`, so one canonical position becomes correct.

Moreover, the destination could not have held its own correct value before the swap unless that value was `v`; index `v-1`'s correct value is exactly `v`, which the inequality says was absent. Thus the swap does not destroy a correct canonical placement at the destination.

At most $n$ canonical positions can become newly correct, so the total number of swaps across all `while` loops is $O(n)$, even though a single index may perform several swaps.

**What the array looks like afterward**

For every distinct value `v` appearing in the input, one copy ends at index `v-1`. If `v` appears twice, its second copy cannot share that cell and occupies an index associated with a missing value.

Therefore:

- `nums[i] == i + 1` indicates a canonical first occurrence; and
- `nums[i] != i + 1` indicates an extra duplicate occurrence.

The final comprehension returns every `v` at a mismatched position.

For `[4,3,2,7,8,2,3,1]`, placement eventually puts one copy of each present distinct value at its natural index. Because values 2 and 3 each have an extra copy, and some values are missing, those extra copies remain in mismatched cells. The comprehension returns `[2,3]` in whatever order those cells appear.

**Why no nonduplicate is returned**

A value appearing once is placed at its canonical index by the swap process. It has no second occurrence that could remain elsewhere. A value appearing twice has exactly one canonical copy and one mismatched copy, so it is returned exactly once. This establishes both soundness and completeness under the occurrence constraint.

**Input mutation is intentional**

The algorithm rearranges `nums`. The contract requires constant auxiliary space and does not require preserving input order, so this mutation is the storage mechanism that replaces a separate seen set. Callers needing the original order would have to copy the array, which would use $O(n)$ extra space.

## Complexity detail

The outer loop visits $n$ indices. Across all indices, at most $O(n)$ swaps occur because each swap establishes a previously absent canonical placement. The final comprehension performs one more linear scan. Total time is $O(n)$.

Only loop variables and swap temporaries are used beyond the returned list, so auxiliary space is $O(1)$. The output can contain up to $O(n)$ values and is excluded by the problem's stated space rule.

## Alternatives and edge cases

- **Sign marking:** For value `v`, use the sign of `nums[v-1]` as a seen bit; an already negative location reveals a duplicate. It also achieves $O(n)$ time and $O(1)$ auxiliary space but changes signs rather than positions.
- **Hash set:** Track seen values and append repeats. It is linear average time but uses $O(n)$ extra memory.
- **Sort then compare adjacent values:** This costs $O(n\log n)$ time with comparison sorting and also mutates order.
- **Brute-force later occurrences:** It needs $O(n^2)$ time.
- **Single element:** It moves nowhere and produces an empty output.
- **No duplicates:** Every present value reaches its canonical index, leaving no mismatches.
- **One duplicate:** Exactly one extra occurrence remains at the index of a missing value.
- **Already canonical values:** The equality condition stops without a useless self-swap.
- **Duplicate at a noncanonical index:** Equality with the canonical copy stops the loop and preserves it for final reporting.
- **Values outside `[1,n]`:** Destination indexing would be invalid, which is why the range guarantee is essential.
- **More than two occurrences:** The comprehension could return the same value multiple times; the contract excludes this case.
