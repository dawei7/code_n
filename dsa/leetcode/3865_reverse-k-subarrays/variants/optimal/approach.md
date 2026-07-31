## General

**Derive the fixed block boundaries**

Let $N$ be the array length. Because the contract guarantees that $N$ is divisible by `k`, every block has the integer length $B=N/k$. Block $b$ begins at $bB$ and ends at $(b+1)B-1$. These intervals are disjoint, cover every array position exactly once, and already appear in the required final block order.

**Reverse one block with converging pointers**

For each block, place one pointer at its first position and another at its last position. Swap those elements, advance the left pointer, and retreat the right pointer. Continue until the pointers meet or cross. The swap at offset $d$ places the original element at $bB+d$ into position $bB+B-1-d$, which is exactly its position in that block's reversal.

No swap crosses a block boundary. Consequently, after a block's pointer loop ends, that interval contains precisely the reverse of its original sequence and all other blocks are unchanged. Applying the same argument to every block proves that the returned array is the concatenation of all `k` independently reversed subarrays.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and $B=N/k$. Reversing one block performs $\lfloor B/2\rfloor$ swaps. Across all `k` blocks, the total work is $k\lfloor B/2\rfloor=O(N)$. The algorithm modifies `nums` in place and stores only indices and the block size, so it uses $O(1)$ auxiliary space.

The benchmark defines size as $N$ and fixes `k = 4`. Each tier therefore performs four complete legal block reversals. The accepted two-pointer implementation and an independent slice-based construction should retain linear growth, while a correct implementation that rescans the input for every mapped output position performs $O(N^2)$ work and should fail only the scaling verdict.

## Alternatives and edge cases

- **Slice reversal per block:** Replacing each slice with its reverse is concise and still $O(N)$ time, but it materializes up to $O(B)$ temporary elements for a block.
- **Mapped output construction:** Compute each output position's mirrored source index and append that value to a new array. This is $O(N)$ time with direct indexing but requires $O(N)$ additional output storage beyond the input.
- **Reverse the complete array:** This is correct only when `k = 1`; for multiple blocks it also reverses the order of the blocks and violates their fixed boundaries.
- **One block:** When `k = 1`, $B=N$ and the operation is an ordinary full-array reversal.
- **Unit blocks:** When `k = N`, $B=1$ and every block is already equal to its reverse, so the array remains unchanged.
- **Odd block length:** The two pointers meet at the middle element, which stays in its original position inside that block.
- **Repeated values:** Equal elements do not change the positional rule; every position is mirrored within its own block regardless of value.
