## General

**Focus on the selected `Solution` class**

The competitive file contains `Solution` followed by four numbered alternative
classes. The standard platform invokes `Solution.rotate`, whose algorithm is
the three-reversal method. `Solution2` through `Solution5` are inert unless a
caller names them explicitly. They illustrate other techniques but do not
participate in the selected method's execution.

**Normalize the distance**

The selected method first evaluates `k %= len(nums)`. An element returns to the
same index after a full cycle of `len(nums)` right shifts, so values of `k`
that differ by a multiple of the length describe identical rotations.

The local contract guarantees a nonempty list. Without that guarantee, taking
a remainder modulo zero would fail and an early return would be required.

**Use half-open interval reversal**

The helper `reverse(nums, start, end)` reverses the half-open interval
`[start, end)`. The last included index is `end - 1`. During each iteration it
swaps `nums[start]` with `nums[end - 1]`, increments `start`, and decrements
`end`.

This endpoint convention differs from helpers that accept an inclusive right
index. The calls are correct specifically because they pass `len(nums)`, `k`,
and `len(nums)` as exclusive endpoints. Mixing the two conventions would
either omit a boundary element or access the wrong location.

**Reverse the whole array, then repair two blocks**

Let `A` be the original first $n-k$ elements and `B` the original last $k$
elements. The target is `B A`.

The call `reverse(nums, 0, len(nums))` changes `A B` into
`reverse(B) reverse(A)`. Next, `reverse(nums, 0, k)` restores the first block
to `B`. Finally, `reverse(nums, k, len(nums))` restores the second block to
`A`. The array is therefore `B A` without any auxiliary array.

For `[1,2,3,4,5,6,7]` and three steps, the states are
`[7,6,5,4,3,2,1]`, then `[5,6,7,4,3,2,1]`, and finally
`[5,6,7,1,2,3,4]`.

**Why relative order is preserved**

The global reversal moves every suffix element before every prefix element but
reverses the order within both groups. Each group-specific reversal applies a
second reversal to that group. Since reversing the same finite sequence twice
restores it, the suffix and prefix both regain their original internal order
in their new positions.

The blocks are disjoint and cover all indices, so no element is omitted or
duplicated. This proves the exact right-rotation mapping.

**Handle zero and extreme normalized shifts**

When normalized `k` is zero, the prefix interval `[0, 0)` is empty. The final
interval `[0, n)` reverses the entire list a second time, cancelling the first
reversal. This safely leaves the input unchanged.

For a one-element list, `k` always normalizes to zero and both full reversals
perform no swaps. For `k = n - 1`, the first restored block has $n-1$ elements
and the second has one; the same reasoning applies.

**Mutate instead of replacing**

All helper operations assign into existing list positions. `rotate` returns
implicitly with `None`, as required. No slicing is used by the selected class,
so it meets the constant-extra-space follow-up in Python as well as in the
abstract algorithm.

**Understand the inactive alternatives and their defects**

`Solution2` attempts cycle decomposition using the greatest common divisor.
In modern Python, `fractions.gcd` has been removed in favor of `math.gcd`, and
`cycle_len = len(nums) / num_cycles` produces a float that cannot be used by
`range`. As written, it is not a valid modern Python 3 fallback.

`Solution3` performs cyclic replacement and counts moved elements. It does not
normalize `k`, though modulo arithmetic inside target computation still maps
large nonnegative `k` correctly. Its count prevents infinite repetition across
multiple cycles.

`Solution4` builds two slices and concatenates them. It mutates the caller's
list through `nums[:]`, but uses $O(n)$ extra space and does not normalize `k`;
for `k > n`, its slice boundaries do not express the proper remainder rotation.

`Solution5` repeatedly pops the last value and inserts it at the front. It is
easy to understand but front insertion shifts the list, producing $O(nk)$
time, and it also fails to reduce unnecessarily large `k`.

These observations do not weaken the selected `Solution`, which is the clean
and correct half-open three-reversal implementation.

## Complexity detail

The selected method reverses intervals of lengths $n$, $k$, and $n-k$, totaling
$2n$ visited positions up to constant factors. Its time complexity is $O(n)$.
Modulo normalization is $O(1)$.

Only `start`, `end`, `k`, and swap temporaries are stored. The nested helper's
memory does not scale with input, so auxiliary space is $O(1)$. In contrast,
inactive `Solution4` uses $O(n)$ space and `Solution5` can take $O(nk)$ time.

## Alternatives and edge cases

- **Inclusive reversal helper:** Equally valid, but calls must use endpoints `n - 1`, `k - 1`, and `n - 1` rather than this source's exclusive bounds.
- **Corrected cycle decomposition:** Use `math.gcd` and integer division to obtain $O(n)$ time and $O(1)$ space.
- **Counted cyclic replacement:** `Solution3` moves every element once with a temporary, though the proof across multiple cycles is less immediate.
- **Slice concatenation:** Concise but violates the constant-space follow-up and needs `k %= n` first.
- **Repeated shifts:** Simple but inefficient for large `k`.
- **Normalized zero:** Empty middle reversal is safe and two whole reversals cancel.
- **One element:** Always unchanged.
- **Duplicate values:** The algorithm moves positions and does not rely on values being distinct.
- **Empty input:** Outside the Reference; add an early return before modulo for a generalized function.
- **Half-open endpoints:** Treat `end` as excluded in every call to avoid off-by-one errors.
