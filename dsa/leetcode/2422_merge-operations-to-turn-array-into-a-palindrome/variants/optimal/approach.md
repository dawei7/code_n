## General

**Think of merges as forming contiguous blocks**

Merging adjacent elements replaces them by their sum. After any sequence of operations, each remaining element is therefore the sum of one contiguous block of the original array, and the blocks form a partition in original order. Turning the array into a palindrome means choosing such blocks so that the sum of the first block equals the sum of the last, the second equals the second-last, and so on.

Because every input number is positive, extending a block strictly increases its sum. This monotonicity makes a greedy comparison from the two ends safe.

The solution uses pointers `i` and `j` at the current outermost unconsumed positions. The variables `a` and `b` are the sums of the left and right blocks currently being formed. Initially those blocks contain only `nums[0]` and `nums[n - 1]`. The answer `ans` counts every time one more adjacent original element is absorbed into an existing block; each such absorption corresponds to exactly one merge operation.

**When the left sum is smaller**

If `a < b`, the two current blocks cannot be matched as they are. The left block must become larger before this outer palindrome pair can be completed. Since all values are positive, extending the already larger right block would only increase `b` and could never repair `a < b`. Nor can the left block be paired with some later inner block while leaving the current rightmost block unmatched: palindrome construction must account for the outer blocks together.

The only useful move is therefore to absorb the next value from the left. The code increments `i`, adds `nums[i]` to `a`, and increments `ans`. This models merging that newly included element with the accumulated left block. The physical array need not be modified because only the resulting sum and boundary matter.

The case `b < a` is symmetric. The right pointer moves left, `nums[j]` is added to `b`, and one merge is counted.

**When the sums match**

If `a == b`, the current outer blocks can serve as a matching palindrome pair. There is no reason to merge either block further: doing so would spend an operation and consume values that can instead be handled in the interior. The algorithm fixes this pair and moves both pointers inward with `i, j = i + 1, j - 1`.

It then resets `a` and `b` to the new boundary values. When the pointers meet, both assignments read the same center element, which needs no matching partner. When the pointers cross after matching a two-sided pair, the assigned positions are still valid positions that were just passed; the loop condition immediately stops further processing. The array is non-empty, so the initial reads are safe.

**Tracing the greedy balance**

For `nums = [1, 2, 3, 4]`, the outer sums begin as 1 and 4. The left is smaller, so it absorbs 2, giving 3 and costing one merge. It is still smaller, so it absorbs 3, giving 6 and costing another. Now the right is smaller, so it absorbs that same interior boundary from its side as the pointers converge, giving 10 and costing the third merge. The process leaves one total block, which is always a palindrome, and returns 3.

For the longer example `[4, 3, 2, 1, 2, 3, 1]`, the left sum begins at 4 and the right at 1. The right absorbs 3 to reach 4, costing one operation, and that outer pair is fixed. The next outer values are 3 and 2. The right absorbs 1 to reach 3, costing one more operation. The remaining middle is symmetric, so the answer is 2.

**Why every greedy merge is forced in an optimum**

Suppose `a < b` at some stage. Any valid final partition extending the current boundaries must eventually produce equal outer block sums. The current left block alone is too small. Since positive values are the only additions possible, at least one boundary between it and the next original element must be removed, meaning at least one left-side merge is unavoidable. Performing that forced merge immediately cannot use more operations than an optimal solution. The same argument holds when `b < a`.

When `a == b`, fixing the pair spends no additional operation. Any solution that merges one of these already equal blocks farther would remove another boundary. Keeping the boundary preserves more blocks and cannot increase the merge count. The remaining task is independent inside those matched outer blocks.

Applying these arguments repeatedly shows that every counted operation is necessary at the moment it is chosen, while every equality safely removes a solved outer pair. When the pointers meet or cross, no unmatched pair remains. The constructed block sums form a palindrome, and no solution can use fewer forced merges, so `ans` is minimal.

## Complexity detail

Let $n$ be the length of `nums`. Each loop iteration either increments `i`, decrements `j`, or moves both pointers. Neither pointer ever reverses direction. Across the entire method, at most $n-1$ boundaries are crossed, so the running time is $O(n)$.

The algorithm stores two indices, two accumulated sums, and one counter. It does not allocate an array proportional to the input and does not modify `nums`, so auxiliary space is $O(1)$.

An accumulated sum can be as large as the sum of all input values, at most $10^5 \cdot 10^6 = 10^{11}$ under the constraints. Python integers handle this exactly. In a fixed-width language, a 64-bit integer is needed even though each individual input fits in 32 bits.

## Alternatives and edge cases

- **Actually mutate the array:** Replacing adjacent elements and shifting storage can simulate the statement literally, but repeated deletions may make the implementation $O(n^2)$. Accumulated boundary sums represent the same merges without movement.
- **Dynamic programming over intervals:** One could search for minimum operations for every subarray, but that introduces quadratic states and overlooks positivity's forced greedy choice.
- **Prefix-sum partition search:** Choosing matching block boundaries through prefix sums can describe the final partition, yet two pointers find those boundaries online with constant extra space.
- **Non-positive numbers:** The proof would fail if zeros or negatives were allowed because extending the larger side might leave it unchanged or reduce it. The strict positivity constraint is what makes extending only the smaller sum safe.
- **One element:** The loop never executes and zero operations are returned because a singleton is already a palindrome.
- **Already palindromic input:** Equal outer values are fixed successively, and no merge is counted.
- **All mass must combine:** If no outer block sums match before convergence, the algorithm performs $n-1$ merges and forms one element, which is always a palindrome.
- **Equal accumulated sums from unequal block lengths:** Blocks need equal sums, not equal numbers of original elements. The method correctly fixes them regardless of how many values each side absorbed.
- **Pointer meeting:** A central block needs no partner and requires no extra operation. The `i < j` condition stops at exactly that point.
- **Input preservation:** Only sums and pointers change; callers retain the original array unchanged.
