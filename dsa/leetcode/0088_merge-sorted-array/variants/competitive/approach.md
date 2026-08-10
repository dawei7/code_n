## General

**Track the three ends explicitly**

`i = m - 1` points to the final meaningful value in `A`, `j = n - 1` points to the final value in `B`, and `last = m + n - 1` points to the final available result slot in `A`.

Both meaningful input portions are non-decreasing, so their largest unread values are at `A[i]` and `B[j]`. The largest of those two must occupy `A[last]`. Filling this destination from right to left uses the placeholder capacity before touching positions that may still contain unread first-array values.

**Merge while both arrays have unread values**

The first loop requires `i >= 0 and j >= 0`, so both comparisons are safe. If `A[i] > B[j]`, the first-array value is copied to `A[last]`, then both `last` and `i` decrease. Otherwise, the second-array value is copied and `last` plus `j` decrease.

Selecting from `B` on equality is harmless because equal integer values are indistinguishable for the requested sorted output. A stable cross-array identity order is not part of the contract.

Every iteration finalizes one position and consumes exactly one unread value.

**Why backward writes do not erase unread first-array data**

The write index begins `n` positions after `i`, precisely because `A` has `n` capacity slots. It moves left once per consumed value. The unread first-array pointer moves left whenever its value is selected; when a second-array value is selected, one of the finite `n` extra values consumes one unit of the original gap.

Therefore `last` cannot pass an unread `i`. By the time the gap closes, all second-array values responsible for closing it have been placed. This is the core safety guarantee that a forward in-place merge lacks.

**Only the second array needs a cleanup loop**

The first loop stops when either input prefix is exhausted.

If `j < 0`, every `B` value is already placed. Any unread `A[0:i + 1]` values are sitting in the exact leading positions they should occupy, so the function can finish without copying them.

If `i < 0` while `j >= 0`, there are second-array values still missing from the output. The second loop copies them backward one by one into `A[last]`. Their own order remains correct because it consumes and writes from largest to smallest.

This asymmetry explains why there is a cleanup loop for `B` but none for `A`.

**Trace first-array exhaustion**

For `A = [4,5,6,0,0,0]` and `B = [1,2,3]`, the first loop repeatedly chooses 6, 5, and 4, moving them into the final three positions. Then `i` becomes negative while all of `B` remains.

The cleanup loop copies 3, then 2, then 1 into positions two, one, and zero. The result is `[1,2,3,4,5,6]`. No copy of the original first prefix was lost because each was moved before its old position could be overwritten.

**Trace second-array exhaustion**

For `A = [1,2,3,0,0,0]` and `B = [4,5,6]`, all `B` values are larger and fill the final capacity slots. `j` becomes negative, the cleanup loop is skipped, and `[1,2,3]` remains untouched at the front.

**A loop invariant**

Before each comparison, `A[last + 1:]` is the sorted suffix containing the largest values already consumed from the two inputs. The unread values are exactly `A[:i + 1]` and `B[:j + 1]`.

The maximum unread value is at `A[i]` or `B[j]`; placing the larger one at `last` preserves the suffix invariant. When the comparison loop ends, either remaining `A` values are already positioned or remaining `B` values are copied into the only unfilled prefix. The final `A` is therefore the complete non-decreasing merge.

**Exact contract behavior**

The method changes `A` in place and falls off the end without a return expression, producing `None`. Its comments call the time bound `O(n)`, using one generic size symbol, while the manifest's `O(m+n)` states the two-input bound more precisely.

## Complexity detail

Across both loops, `i` decreases at most `m` times and `j` decreases at most `n` times. Each movement performs constant work, so total time is $O(m+n)$, matching the manifest.

The implementation stores three integer indices and no size-dependent collection. It reuses `A`'s promised capacity, giving $O(1)$ auxiliary space, also matching the manifest.

## Alternatives and edge cases

- **Single loop while `j >= 0`:** Fold first-array exhaustion into the comparison condition and omit a separate `B` cleanup loop, as the optimal source does.
- **Forward merge after copying `A[:m]`:** It is linear but uses extra storage proportional to `m`.
- **Concatenate and sort:** Simpler but slower than the required exploitation of sorted input.
- **Empty `B`:** Both loops skip and `A` remains unchanged.
- **Empty meaningful `A`:** The comparison loop skips and the cleanup copies all of `B`.
- **First array exhausts first:** The second loop fills every remaining leading slot from `B`.
- **Second array exhausts first:** Remaining `A` values need no movement.
- **Equal endpoints:** The `else` branch takes `B` and still preserves non-decreasing order.
- **Physical versus meaningful length:** Only `A[:m]` is input data; `A[m:]` is capacity even if placeholder zero is a valid numeric value elsewhere.
- **Maximum and minimum allowed integers:** Direct comparison is safe and independent of magnitude.
- **No output allocation:** The caller reads the modified `A` rather than a returned list.
- **`B` preservation:** The second input is never modified.
- **Indentation of cleanup body:** The extra visual indentation in the file is still syntactically within the `while` suite and does not change logic.
