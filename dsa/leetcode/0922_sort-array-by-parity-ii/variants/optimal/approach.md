## General

Even indices must contain even values, and odd indices must contain odd values. Because the input contains equal numbers of even and odd values, every misplaced odd value at an even index can be paired with a misplaced even value at an odd index.

The solution scans only even indices:

```text
for i in range(0, n, 2)
```

Pointer `j` scans odd indices and begins at 1.

**When an even-index position is correct.** If `nums[i]` is even, it already satisfies the requirement and no action is needed.

**When an even-index position is wrong.** If `nums[i]` is odd, the solution advances `j` by two while `nums[j]` is also odd. Those odd-index positions are already correct and should not be disturbed.

The first odd index where `nums[j]` is even is a complementary mismatch. Swapping `nums[i]` and `nums[j]` places the even value at the even index and the odd value at the odd index, fixing both positions at once.

**Why `j` never needs to move backward or restart.** Every odd index below `j` has either been observed to contain a correct odd value or was repaired by an earlier swap. It will never become wrong again because later swaps use only the current even index and an odd index at or beyond `j`. Continuing forward avoids repeated scanning.

After a swap, `j` itself now contains an odd value and is correct. The code does not immediately increment it, but on the next needed search the while-loop sees that odd value and advances. This preserves correctness while keeping the code compact.

**Why a matching even value must exist.** Suppose an even position contains an odd value. Then among all even positions, at least one even slot is missing its required even value. Since the array contains exactly as many even values as even indices, some even value must occupy an odd index. Correct odd-index values are skipped, so the search eventually finds that misplaced even value before leaving the array.
Before each even index `i` is processed:

- all earlier even indices contain even values;
- all odd indices below `j` contain odd values;
- the remaining unprocessed positions contain equal numbers of each type needed to fill their parity slots.

If `nums[i]` is even, accepting it preserves the invariant. If it is odd, the search finds a complementary even at an odd position; swapping fixes both and preserves the remaining balance. When all even indices have been processed, every one contains an even value. Because half the positions and half the values are even, all remaining odd indices must contain odd values.

For `[4,2,5,7]`, even index 0 is correct. Even index 2 contains odd value 5. Pointer `j=1` finds even value 2 at an odd index, and swapping produces `[4,5,2,7]`. Both parity rules now hold.

For a longer array, `j` may skip several already-correct odd positions before finding a mismatch. Those skipped positions never need inspection again. If no even-position mismatch occurs for a while, `j` simply retains its location; the next swap search resumes from the same earliest unchecked odd slot. This monotone reuse is what makes the nested-looking while-loop linear overall rather than quadratic.

The equal-count guarantee can also be expressed as a conservation law. Every odd value misplaced in an even slot creates one deficit of even values among even slots, and that missing even value must appear in an odd slot. A swap resolves one deficit of each kind simultaneously, so repair never creates a new mismatch outside the two positions being fixed.

The method mutates and returns the input list. It does not promise stability or a unique ordering, which is acceptable because any valid array is allowed.

## Complexity detail

Let $n$ be the array length. The even-index loop processes $n/2$ positions. Pointer `j` moves only forward through odd indices, at most $n/2$ steps total.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(1)$ auxiliary space.

Every swap uses constant temporary storage. No output copy is allocated.

## Alternatives and edge cases

- **Two output arrays or one new result:** Place evens at even result indices and odds at odd indices. This is linear but uses $O(n)$ space.
- **Two mismatch pointers:** Advance one pointer over even indices looking for odd values and one over odd indices looking for even values, then swap. This is an equivalent in-place method.
- **Sort numerically:** Numerical order does not directly enforce index parity and costs extra time.
- **Scan every odd index from the beginning:** Correct but can repeat work and become quadratic.
- **Already valid array:** No swaps occur.
- **Minimum length two:** Either it is already valid or one swap fixes both positions.
- **Zero:** Zero is even and belongs at an even index.
- **Duplicate values:** Only parity matters, so duplicates require no special handling.
- **Equal parity counts:** This contract guarantee is what prevents `j` from running out during a needed search.
- **Odd value at even index:** It always pairs with some even value at an odd index.
- **Any answer order:** Values within parity classes may be rearranged freely.
- **Input mutation:** Pass a copy if original order must be preserved.
- **Follow-up:** The exact solution meets the in-place requirement with constant auxiliary storage.
