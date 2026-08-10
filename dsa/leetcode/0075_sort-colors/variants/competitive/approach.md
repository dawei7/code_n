## General

**Partition around the middle color**

`triPartition(nums, 1)` treats color code one as a target and divides values into three groups: values less than one, values equal to one, and values greater than one. Because the input domain is exactly `{0, 1, 2}`, these groups are precisely red zeroes, white ones, and blue twos. A general three-way partition therefore directly produces the required order.

The helper maintains four contiguous regions:

- `nums[0:left]` contains values less than `target`, hence zeroes.
- `nums[left:i]` contains values equal to `target`, hence ones.
- `nums[i:right + 1]` is unclassified.
- `nums[right + 1:]` contains values greater than `target`, hence twos.

Initially `i = 0`, `left = 0`, and `right = len(nums) - 1`. All classified regions are empty and every element is unknown. The inclusive unknown interval explains the condition `i <= right`.

**Move a value greater than the target to the right**

If `nums[i] > target`, the current value is a two. It is swapped with `nums[right]`, and `right` decreases. The two is now in the confirmed greater-than suffix.

The scan index `i` does not move because the value arriving from the old `right` position was unclassified. It may be zero, one, or two, so the next iteration must examine it. This is the same essential safety rule as in the Dutch National Flag algorithm: a swap with an unknown boundary does not automatically classify the incoming value.

When `i == right`, the swap is with itself. Decrementing `right` still removes that confirmed two from the unknown interval, and the loop can terminate.

**Move a value less than the target to the left**

For a value not greater than the target, the code next checks whether it is smaller. A zero belongs at `left`, the first position after the confirmed zero prefix. The source swaps `nums[left]` and `nums[i]` and increments `left`.

If `left < i`, the value at `left` before the swap is a confirmed one because `[left, i)` is the equality region. The swap places zero in the less-than region and moves that one to `i`. The following `i += 1` absorbs that moved one into the equality region. If `left == i`, the operation is a self-swap followed by advancing both boundaries. Either way, both positions have known roles.

**Leave an equal value in the middle**

If the current value is neither greater nor less than one, it equals one. No data movement is needed because `i` is already immediately after the existing equality region. Incrementing `i` extends that region by one.

The source places `i += 1` outside the inner less-than check but inside the not-greater branch. This is exact: both a zero swap and a directly observed one leave a classified value at the old `i`, whereas a two swap may bring an unknown value and therefore does not advance.

**Trace a boundary exchange**

With `[2, 0, 2, 1, 1, 0]`, the first value is greater than one. It swaps with the last zero, `right` decreases, and `i` remains zero. The arriving zero is then less than one, so it swaps into `left`—in this case with itself—and both `left` and `i` advance. The algorithm has correctly classified both ends without skipping the value brought from the right.

Later, a zero encountered after some ones swaps with the first one at `left`. The zero expands the prefix, and the displaced one lands at the current position before `i` advances. This explains why the method can gather zeroes through a region of already classified ones without losing the equality invariant.

**Why termination gives sorted colors**

The region invariant is true before scanning. A greater value extends the two suffix and leaves the incoming value unknown. A smaller value extends the zero prefix and preserves or extends the one middle. An equal value extends the one middle directly. Thus every branch preserves all four region meanings.

Every iteration either increments `i` or decrements `right`, so the inclusive unknown interval shrinks. When `i > right`, it is empty. The remaining regions appear in order `< 1`, `== 1`, and `> 1`; under the input domain, that is all zeroes, then all ones, then all twos. The helper mutates `nums`, and the outer method implicitly returns `None`.

**Why naming it `triPartition` is meaningful**

The helper is written relative to a target rather than hard-coding the three colors. Its control logic resembles the three-way partition used in quicksort when duplicate pivot values are common. For this problem, selecting the middle code as the pivot means that numerical comparison and desired color grouping coincide exactly.

## Complexity detail

Let $n$ be `len(nums)`. Index `i` moves right at most $n$ times and `right` moves left at most $n$ times. Neither reverses direction, so total iterations and swaps are $O(n)$. This is a one-pass partition in the standard sense and matches the manifest.

The helper stores three indices and one scalar target. Tuple swaps need only constant temporary references, and recursion or auxiliary arrays are absent. Auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Direct color-specific boundaries:** Track the last zero, current unknown, and first two explicitly. It is equivalent but names categories rather than comparing with a target.
- **Frequency counting:** Count each code and overwrite the array. It is simple and constant-space but requires a counting pass followed by a writing pass.
- **General sorting:** It is prohibited and does more comparison work than a three-value partition needs.
- **Stable three-way partition:** Stability is not required because all members of a color are represented by identical integers.
- **All values below target:** `left` and `i` advance together through self-swaps, leaving all zeroes.
- **All values equal target:** Only `i` advances, with no swaps.
- **All values above target:** Only `right` retreats while `i` stays at zero until no unknown value remains.
- **Value from the right boundary:** It is always reexamined because the greater-than branch does not increment `i`.
- **Value from the equality region:** A less-than swap moves a known one to `i`, so advancing afterward is safe.
- **One-element list:** The sole value is placed in its appropriate region in one iteration.
- **Already sorted list:** Comparisons confirm the regions; self-swaps of early zeroes do not alter the result.
- **Domain guarantee:** If values outside `0`, `1`, and `2` were allowed, the method would still partition relative to one but would no longer mean color sorting.
- **No explicit return:** Correct usage observes the mutated `nums` list.
