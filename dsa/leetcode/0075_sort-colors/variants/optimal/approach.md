## General

**Maintain four consecutive regions**

The array contains only `0`, `1`, and `2`, and their required sorted order is exactly their numeric order. The implementation uses three indices to maintain these regions:

- Positions `0` through `i` contain confirmed zeroes.
- Positions `i + 1` through `k - 1` contain confirmed ones.
- Positions `k` through `j - 1` have not yet been classified.
- Positions `j` through the end contain confirmed twos.

Here `i` is the last index of the zero region, `j` is the first index of the two region, and `k` is the first unclassified index. The initialization `i = -1`, `j = len(nums)`, and `k = 0` makes all three classified regions empty and makes the entire array the unknown region. Using `-1` and `len(nums)` as outside sentinels avoids special cases for the first zero and first two.

The loop continues while `k < j`. This condition says that at least one unclassified position remains. Each branch classifies at least one position, so the unknown interval steadily disappears.

**Place a zero at the next left position**

When `nums[k] == 0`, the zero belongs immediately after the existing zero region. The source first increments `i`, making it the destination for the next zero, and swaps `nums[i]` with `nums[k]`.

If `i == k`, the swap is with itself and simply confirms that position as zero. If `i < k`, the old value at the new `i` came from the confirmed-one region, because positions between the old zero boundary and `k` are all ones. The swap moves the zero left and moves that one to position `k`. Incrementing `k` then includes the moved one in the confirmed-one region. Both swapped values are therefore fully classified, which is why advancing `k` is safe in this branch.

**Place a two at the next right position**

When `nums[k] == 2`, the source decrements `j` and swaps the current two with `nums[j]`. The two is now at the first position of the confirmed-two suffix, so that suffix grows leftward by one.

Crucially, `k` does not advance. The value moved from `j` came from the unknown region unless `j` has just met `k`. It might be zero, one, or two and must be inspected. Advancing immediately would skip that value and could leave the array unsorted. Rechecking the same `k` is the defining asymmetry of the algorithm.

If decrementing `j` makes `j == k`, the swap is effectively at the boundary and the loop ends. No unknown position remains.

**Accept a one in the middle**

The only remaining value is one because the contract restricts every element to `0`, `1`, or `2`. A one already belongs between the zero prefix and two suffix, so no swap is needed. Incrementing `k` extends the confirmed-one region by one position.

An explicit `nums[k] == 1` test is unnecessary under the input guarantee. The `else` branch relies on that guarantee; with an unexpected value it would incorrectly treat the value as a one.

**Trace the reason for rechecking after a right swap**

Start with `[2, 0, 2, 1, 1, 0]`. The first value is two, so `j` moves from 6 to 5 and the two swaps with the zero at index 5. The array begins `[0, ...]`, but `k` remains zero. On the next iteration, that newly arrived zero is recognized and moved into the left region. If `k` had advanced after the first swap, the zero at index zero would never have been placed through the zero branch.

As processing continues, every zero joins the prefix, every two joins the suffix, and ones fill the space between. Values may be swapped more than once, but an index leaves the unknown interval after a boundary crosses it and never becomes unknown again.

**Prove the region invariant**

The four-region description is true initially. In the zero branch, the next zero position receives zero, the displaced one is absorbed by incrementing `k`, and the two suffix is untouched. In the two branch, the new `j` position receives two, `k` stays at the first unknown value, and the left classified regions are untouched. In the one branch, incrementing `k` classifies exactly that one.

Thus every branch preserves the invariant and strictly decreases the size `j - k` of the unknown region. At termination `k == j`, so the unknown region is empty. The entire array is then a zero prefix, followed by a one region, followed by a two suffix, which is exactly sorted color order.

The operations are swaps within the supplied list. The method has no explicit return statement and therefore returns `None`, as required for an in-place procedure.

## Complexity detail

Let $n$ be the array length. In every iteration either `k` increases or `j` decreases. Neither moves in the opposite direction, so there are at most about $2n$ pointer movements and $O(n)$ total time. This matches the manifest and fulfills the one-pass follow-up even though a value swapped from the right may be inspected on the next iteration.

Only three indices and the temporary references used by tuple assignment are required. No counting array or output list is allocated, so auxiliary space is $O(1)$, also matching the manifest.

## Alternatives and edge cases

- **Counting two passes:** Count how many zeroes, ones, and twos occur, then overwrite the array in blocks. It is $O(n)$ time and $O(1)$ space but does not satisfy the one-pass follow-up.
- **Library sort:** It would obscure the three-value structure, typically costs $O(n\log n)$, and is explicitly forbidden.
- **Stable partition:** Preserving relative identity within each color is unnecessary because equal integer color codes are indistinguishable; stable in-place partitioning would add complexity.
- **All zeroes:** Every iteration grows the zero prefix, often through self-swaps.
- **All ones:** `k` simply scans to `j` without any swaps.
- **All twos:** `j` repeatedly moves left while `k` stays until the unknown interval vanishes.
- **Single element:** One branch classifies it and the loop ends.
- **Zero swapped from the right:** The unchanged `k` after a two swap ensures it is processed next.
- **Two swapped from the right:** It is processed again and moved into the still-growing suffix.
- **Already sorted input:** The pointers scan once; zero self-swaps are harmless and the result remains sorted.
- **Reverse-grouped input:** Swaps progressively exchange left twos with right zeroes without extra storage.
- **Input-domain reliance:** The `else` branch means “one” only because no other integer is allowed.
- **Mutation contract:** Callers must inspect the changed list, not a return value.
