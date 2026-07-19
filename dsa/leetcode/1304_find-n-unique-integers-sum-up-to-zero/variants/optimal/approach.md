## General
**Build canceling pairs**

For every positive integer $v$ from 1 through $\lfloor n/2\rfloor$, append both $v$ and $-v$. The two values are distinct, and their contribution to the total is $v+(-v)=0$. Different magnitudes produce no duplicates across pairs.

When $n$ is even, these pairs already provide exactly $n$ values. When $n$ is odd, append 0 after the pairs. Zero is different from every nonzero paired value and does not change the sum.

Thus the construction always has the requested length, every value is unique, and the complete sum is zero. Because the contract accepts any valid construction, the semantic validator checks these properties rather than comparing the returned array to one fixed ordering.

## Complexity detail
Creating and returning $n$ integers takes $O(n)$ time. The result array occupies $O(n)$ space; aside from that required output, the construction uses only constant loop state.

## Alternatives and edge cases
- **Arithmetic sequence plus balancing value:** Returning `1, 2, ..., n - 1` and their negated sum is also valid, though its magnitudes grow quadratically with $n$.
- **Repeated membership checks:** Searching the partial list before adding each symmetric value preserves correctness but can take $O(n^2)$ time.
- **`n = 1`:** The only one-element zero-sum array is `[0]`.
- **Odd length:** Include zero exactly once after all nonzero pairs.
- **Even length:** Use only positive-negative pairs; zero is unnecessary.
- **Output order:** Reordering a valid set does not change uniqueness or its sum and must remain accepted.
