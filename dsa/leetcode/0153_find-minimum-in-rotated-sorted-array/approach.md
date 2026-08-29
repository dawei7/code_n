## General

**Use the last value to distinguish the two sorted pieces**

Rotating a strictly ascending array produces at most two ascending segments:

- a high-valued prefix that came from the end of the original array;
- a low-valued suffix that begins with the original minimum.

When the array is genuinely rotated, every value in the high prefix is greater than `nums[-1]`, while every value in the low suffix is less than or equal to `nums[-1]`.

If the rotation is effectively a full length and the array remains sorted, every element is at most the last value and the minimum is already at index zero. The same comparison rule still works.

The algorithm binary-searches for the first index belonging to the low suffix.

**Maintain an interval that must contain the minimum**

`l` and `r` are inclusive indices. Initially they cover the complete array.

The loop continues while more than one candidate index remains. `mid = (l + r) >> 1` computes the floor midpoint; right shift by one is integer division by two for this nonnegative sum.

There are two cases.

If `nums[mid] > nums[-1]`, `mid` lies in the high prefix. The minimum cannot be at `mid` or anywhere earlier within the current high-side reasoning, so the source sets `l = mid + 1`.

If `nums[mid] <= nums[-1]`, `mid` lies in the low suffix. It might itself be the minimum, or the minimum might be earlier in the search interval. The source keeps `mid` with `r = mid`.

Keeping `mid` in the second case is essential. Setting `r = mid - 1` could discard the minimum when `mid` is exactly the rotation point.

**Why uniqueness makes the boundary clear**

All values are distinct. The only array entry equal to `nums[-1]` is the final entry itself.

There is no ambiguous block of duplicates straddling the high/low boundary. Every midpoint can be assigned decisively to the high prefix or low suffix, so each step removes about half the candidate indices.

With duplicates, a comparison equal to the last value could fail to reveal which side contains the minimum, and the worst case might require shrinking one position at a time. That is a different problem.

**Trace a rotated example**

For `[4,5,6,7,0,1,2]`, the target comparison value is two.

- The first midpoint holds seven, which is greater than two, so the minimum must be to its right.
- The narrowed midpoint holds one, which is at most two, so the minimum is at that index or to its left.
- Further narrowing isolates index four, whose value is zero.

For `[11,13,15,17]`, every inspected midpoint is at most the final value. `r` repeatedly moves left until index zero remains, returning eleven.

For one element, `l == r` initially, the loop skips, and that element is returned.

**Why termination returns the minimum**

The update rules preserve the claim that the minimum index lies in `[l, r]`. Each iteration strictly shrinks the interval:

- the high-side case moves `l` beyond `mid`;
- the low-side case moves `r` to `mid`, which is less than the old `r` while `l < r`.

Eventually `l == r`. Since the interval still contains the minimum and now has one index, that index must be the minimum.

The input is never modified.

Another useful way to state the invariant is that every index before `l` has
already been proved to belong to the high segment, while no index after `r`
can be the first member of the low segment. The answer is not guessed from the
smallest value seen so far; it remains physically inside the shrinking
interval. This distinction explains why the procedure is a true binary search
and why it does not need an accumulator for the current minimum.

The final array value is a classification threshold, not the value being
searched for as an ordinary equality target. The search asks where the
predicate `nums[i] <= nums[-1]` first becomes true. Thinking in terms of that
monotone predicate makes both update rules easier to derive and avoids trying
to reason about all rotations separately.

## Complexity detail

Let $n$ be the array length.

Each iteration reduces the candidate interval by roughly half. There are $O(\log n)$ iterations, each with constant-time arithmetic and comparisons. Time is $O(\log n)$.

The method stores only `l`, `r`, and `mid`, so auxiliary space is $O(1)$. These bounds match the manifest.

Index arithmetic is safe in Python. In fixed-width languages, `l + (r - l) // 2` is often used to avoid theoretical overflow from `l + r`.

## Alternatives and edge cases

- **Compare with current right endpoint:** Use `nums[mid] > nums[r]` instead of the fixed final value. With distinct values, it gives the same binary-search direction.
- **Detect the inflection directly:** Check neighboring values around `mid` for the descent. It works but requires careful boundary guards.
- **Linear scan:** `min(nums)` is simple but violates the required $O(\log n)$ time.
- **One element:** The initial interval is already the answer.
- **No visible rotation:** Repeated low-side decisions lead to index zero.
- **Minimum at final index:** High-side decisions move `l` all the way to `r = n - 1`.
- **Negative values:** Only relative ordering matters; signs do not change the logic.
- **Unique-elements guarantee:** It is what allows decisive comparison without a duplicate-shrinking case.
- **Nonempty input:** The source reads `nums[-1]` and relies on at least one element.
- **Runtime dependency:** The source uses `List` without importing it. Standalone Python needs `from typing import List`.
