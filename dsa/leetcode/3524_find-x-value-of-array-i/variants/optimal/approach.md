## General

Removing a prefix and suffix leaves exactly one non-empty contiguous subarray, so the task is to classify every subarray by its product modulo `k`. Multiplication modulo `k` depends only on the operands' remainders, which leaves just $k$ possible states regardless of the products' actual sizes.

Before processing an index, let `ending[r]` count the subarrays ending at the preceding index whose product has remainder $r$. The current value creates one new length-one subarray. Every older ending subarray can also be extended by the current value; a previous remainder $r$ becomes $(r \cdot (\texttt{value} \bmod k)) \bmod k$. These are all and only the subarrays ending at the current index, because each either starts there or uniquely extends a subarray ending one position earlier.

Add the new ending counts into the global result after every index. Each non-empty subarray has one unique right endpoint, so it is accumulated exactly once in the component matching its product remainder.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each of the $n$ positions processes $k$ remainder states and accumulates $k$ counts, for $O(nk)$ time. The current and next state arrays plus the result each have length $k$, so the auxiliary space is $O(k)$.

## Alternatives and edge cases

- **Enumerate every subarray:** Extending a product from every left endpoint is straightforward, but it requires $O(n^2)$ time.
- **Store a table for every endpoint:** A full $n \times k$ dynamic-programming table preserves unnecessary history; rolling arrays reduce the auxiliary space to $O(k)$.
- **Remainder zero:** Once a subarray product reaches remainder `0`, extending it keeps the remainder at `0`.
- **Modulus one:** Every non-empty subarray belongs to remainder `0`, so the single result entry is $n(n+1)/2$.
- **Large products and counts:** Reducing after every multiplication avoids unbounded products, while the counts may still exceed 32-bit integer range.
