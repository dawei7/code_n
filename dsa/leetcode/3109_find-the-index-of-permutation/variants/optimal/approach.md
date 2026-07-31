## General

**Lexicographic order forms factorial-sized blocks.** At position $i$, suppose $c_i$ unused values are smaller than `perm[i]`. Choosing any one of those smaller values at position $i$, while keeping the already fixed prefix unchanged, places the resulting permutation before `perm`. Each such choice allows the remaining $n-1-i$ values to appear in every possible order, so it contributes a block of $(n-1-i)!$ permutations. Therefore the zero-based rank is the Lehmer-code value

$$
\sum_{i=0}^{n-1} c_i (n-1-i)!.
$$

**Scan from right to left.** When position $i$ is processed from the end toward the beginning, the data structure contains exactly the values in the suffix `perm[i + 1:]`. Because `perm` is a permutation, these are precisely the values still available after fixing the prefix through position $i$. A prefix-count query for `perm[i] - 1` therefore returns $c_i$, the number of available values smaller than `perm[i]`.

Maintain the factorial weight alongside this reverse scan. It begins at $0!=1$ for the last position. After processing index $i$, multiply it by $n-i$, giving the correct factorial for the next position to the left. Add each weighted digit to the answer modulo $10^9+7$.

**Use a Fenwick tree for order statistics.** Values range from $1$ through $n$, so they can be used directly as one-based Fenwick indices. A point update inserts the current value, and a prefix sum counts inserted values no greater than a requested index. Both operations take logarithmic time. The block-count argument accounts for every preceding permutation exactly once, so the accumulated sum is the required index.

## Complexity detail

Let $n$ be the length of `perm` defined in the function contract. The algorithm performs one Fenwick prefix query and one point update per value, taking $O(n \log n)$ time. The Fenwick array uses $O(n)$ auxiliary space; all other state is constant-sized.

## Alternatives and edge cases

- **Sorted list of unused values:** Binary search can find each digit, but deleting from the middle of an array shifts elements and makes the total time $O(n^2)$.
- **Segment tree:** Store counts over the value range and perform the same prefix queries and removals in $O(n \log n)$ time, with a larger constant and more storage than a Fenwick tree.
- **Balanced order-statistics tree:** An augmented tree also supports rank queries and deletion in $O(\log n)$ time, but Python has no built-in version and the bounded value range makes a Fenwick tree simpler.
- **Enumerate permutations:** Generating permutations until reaching `perm` takes factorial time and is infeasible even far below the maximum $n$.
- **Singleton or ascending input:** Every Lehmer digit is zero, so the rank is zero.
- **Descending input:** Every digit is maximal, producing $n!-1$ before reduction modulo $10^9+7$.
- **Modulo placement:** Reduce weighted contributions and the rolling factorial during the scan; the Fenwick counts themselves remain ordinary integers.
