## Description

Begin with an integer array `nums` and an integer state `p`. A sequence of queries arrives in the form `[val_i, k_i]`, and the queries must be processed in their given order.

For query $i$, first insert `val_i` into the current array. Among all values now present, including duplicates, let $x$ be the `k_i`th largest element. Replace the current state by

$$
p\gets p^x\bmod(10^9+7).
$$

The updated state carries forward to the next query. Return an array whose $i$th entry is the value of `p` immediately after query $i$ has completed.
