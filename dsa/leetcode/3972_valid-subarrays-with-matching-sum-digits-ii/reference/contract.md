## Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers.
- `x`: A digit from `1` through `9` that must match both boundary digits of a qualifying subarray sum.

Let $n = \lvert\texttt{nums}\rvert$ and

$$
S = \sum_{v \in \texttt{nums}} v.
$$

For $0 \le l \le r < n$, `nums[l..r]` is the contiguous nonempty interval from index `l` through index `r`. Positivity guarantees that every such sum has a well-defined leading digit and that prefix sums are strictly increasing.

**Return value**

Return the number of pairs $(l,r)$ for which the decimal representation of $\sum_{i=l}^{r}\texttt{nums[i]}$ starts with `x` and ends with `x`.
