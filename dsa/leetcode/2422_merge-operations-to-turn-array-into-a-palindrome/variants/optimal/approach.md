## General

**View merges as forming mirrored contiguous groups.** Any sequence of adjacent merges partitions the original positive array into contiguous groups whose sums are the elements of the final array. For that final array to be a palindrome, the leftmost group sum must equal the rightmost group sum, then the next two group sums must match, and so on.

Start with one element in the left group and one in the right group. When their sums are equal, those groups can be fixed as a mirrored pair, so move both pointers inward and begin two new groups. When the left sum is smaller, positivity makes it impossible to reduce either sum; the left group must absorb its next element. Symmetrically, a smaller right sum must absorb the next element from the right.

Each absorption corresponds to exactly one merge operation. Choosing the smaller side is forced: extending the larger side would only increase the imbalance and could not produce a matched outer pair with fewer merges. Repeating this rule until the pointers meet therefore constructs a palindromic grouping with the minimum possible number of absorbed boundaries.

## Complexity detail

Each pointer moves inward at most $n-1$ times, and every step does constant work. The running time is $O(n)$. The algorithm stores two indices, two accumulated sums, and the operation count, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Physically merge a mutable list:** Applying the same greedy rule with deletions is correct, but shifting list elements after each deletion can make the implementation $O(n^2)$.
- **Interval dynamic programming:** Considering all palindromic merge partitions is unnecessary and requires at least quadratic state.
- **Already palindromic:** Equal outer elements repeatedly close groups without any merge.
- **Single element:** It is already a palindrome, so the answer is 0.
- **One side absorbs repeatedly:** Several small values may need to combine before matching one large value on the opposite side.
- **Positive values:** The forced smaller-side argument relies on every absorbed element increasing its group's sum.
- **Crossing pointers:** Once the two groups meet or cross, the unmatched middle portion forms the palindrome's center and needs no additional merge.
