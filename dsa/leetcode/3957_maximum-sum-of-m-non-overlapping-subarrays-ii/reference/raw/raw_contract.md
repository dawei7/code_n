## Function Contract

**Inputs**

- `nums`: The integer array from which subarrays are selected.
- `m`: The maximum number of selected subarrays; at least one must be chosen.
- `l`: The inclusive minimum length of each selected subarray.
- `r`: The inclusive maximum length of each selected subarray.

**Return value**

Return the largest possible total sum of between one and `m` pairwise non-overlapping subarrays, with every selected length between `l` and `r` inclusive.

Let $n = \lvert\texttt{nums}\rvert$ and define

$$
S = 1 + \sum_{v \in \texttt{nums}} \max(v, 0).
$$
