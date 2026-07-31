## Function Contract

**Inputs**

- `nums`: The nonempty initial multiset, represented as an integer array.
- `p`: The initial positive integer state.
- `queries`: An ordered array whose element `i` is `[val_i, k_i]`, giving the value to insert and the requested largest rank after that insertion.

Let $N$ be the initial length, $Q$ the query count, and $V$ the maximum inserted or initial array value. The insertion for query `i` happens before rank `k_i` is selected. Duplicate values occupy separate ranks. Every query's rank is valid for the current length, and adjacent ranks obey $\lvert k_i-k_{i-1}\rvert<10$ for $i>0$.

**Return value**

Return an array of length $Q$ whose element `i` is the updated `p` after query `i` has been processed.
