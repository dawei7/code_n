## General

The required output has one partition boundary: every even value must appear before every odd value. Relative order inside the even group and inside the odd group is irrelevant because any satisfying array is accepted.

The exact solution partitions in place with two pointers:

- `i` searches from the left for a misplaced odd value.
- `j` searches from the right for a misplaced even value.

While `i < j`, one of three actions applies.

**Left value is already even.** If `nums[i] % 2 == 0`, it belongs in the left partition. Advancing `i` permanently accepts that position.

**Right value is already odd.** If the left value is not even and `nums[j] % 2 == 1`, the right value belongs in the right partition. Decrementing `j` permanently accepts that position.

**Both endpoints are misplaced.** Reaching the final branch means `nums[i]` is odd and `nums[j]` is even. Swapping them fixes both positions simultaneously. Both pointers then move inward.

Because values are nonnegative under the contract, remainders are zero for even and one for odd. In Python the parity tests also behave correctly for negative integers, though valid inputs do not require that extension.

**Partition invariant.** At the beginning of each loop:

- every index smaller than `i` contains an even value;
- every index larger than `j` contains an odd value;
- only the interval `i..j` remains unresolved.

Advancing `i` happens only after confirming an even value, so the left property expands. Decreasing `j` happens only after confirming an odd value, so the right property expands. A swap places an even at `i` and an odd at `j` before both regions expand. Thus every branch preserves the invariant.

When `i >= j`, at most one unresolved position remains between the verified regions. One value cannot form an odd-before-even inversion with itself. Consequently all evens lie before all odds.

To see the final boundary more explicitly, let the loop finish at index `p`. All indices below `p` have been certified even except possibly `p` itself, and all indices above `p` have been certified odd except possibly `p` itself. If `nums[p]` is even, it belongs with the verified left side and the odd suffix still follows it. If it is odd, it belongs with the verified right side and every certified even still precedes it. Either parity of the meeting element therefore produces a valid partition.

Termination follows from the same pointer movement. The even-left branch increases `i`, the odd-right branch decreases `j`, and the swap branch does both. Hence `j - i` decreases by at least one every iteration and can never decrease forever. No accepted position is revisited, which is why total work remains linear.

**Why no sorting within groups is needed.** The task does not request numerical ascending order. It asks only for parity grouping. A linear partition avoids spending $O(n\log n)$ time solving a stronger problem than required.

For `[3,1,2,4]`, pointers start at 3 and 4. They are a misplaced odd/even pair, so swapping produces `[4,1,2,3]`. Next, the left pointer stops at 1 and the right pointer moves past already-correct 3. Values 1 and 2 swap, yielding `[4,2,1,3]`. The pointers meet, and the array satisfies the condition.

**Why every original element is retained.** The algorithm only swaps existing positions. It never creates, removes, or duplicates values, so the returned array is a permutation of the input.

The method mutates `nums` and returns the same list object. That is consistent with the in-place space bound but is observable to callers.

## Complexity detail

Let $n$ be the array length. In every loop iteration, `i` increases, `j` decreases, or both. The unresolved interval strictly shrinks, so total iterations are $O(n)$.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(1)$ auxiliary space.

Swapping uses only temporary references. The returned array is the modified input rather than a separately allocated result.

## Alternatives and edge cases

- **Two output lists:** Collect evens and odds separately, then concatenate. This is easy but uses $O(n)$ extra space.
- **Stable in-place partition:** Preserving relative order generally requires shifting elements and can cost $O(n^2)$ without extra storage. Stability is not required.
- **Sort by parity key:** It works but usually costs $O(n\log n)$ and may use sorting workspace.
- **Single write pointer:** Scan for evens and swap each into the next left slot. This is another $O(n)$, $O(1)$ partition.
- **All even:** The left pointer advances across the array, and the order remains unchanged.
- **All odd:** The right pointer retreats across the array, and the order remains unchanged.
- **One value:** The loop never runs; either parity already satisfies the condition.
- **Zero:** Zero is even because `0 % 2 == 0` and belongs in the front group.
- **Alternating parity:** Several swaps may occur, but each fixes boundary positions permanently.
- **Duplicate values:** Parity, not uniqueness, determines placement.
- **Any accepted order:** The algorithm is free to reverse or rearrange members within a parity group.
- **Input mutation:** Callers needing the original order should pass a copy.
- **Pointer meeting:** The single middle value needs no classification action because verified groups on either side cannot be inverted through one cell.
