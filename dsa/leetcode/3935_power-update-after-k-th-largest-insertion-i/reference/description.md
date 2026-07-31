## Description

An integer array `nums` and an integer state `p` are updated by a sequence of queries. Query `i` is `[val_i, k_i]`, and consecutive requested ranks differ by fewer than ten whenever `i > 0`.

Process the queries in order. First insert `val_i` into `nums`; all earlier insertions remain present. Let `x` be the `k_i`th largest element of the resulting multiset, counting equal values according to their multiplicity. Then replace the current state with

$$
p\gets p^x\bmod(10^9+7).
$$

Record the new value of `p` after every query. Because each update uses the state produced by the preceding query, the modular-power calculations are sequential rather than independent.

Return the recorded values in query order.
