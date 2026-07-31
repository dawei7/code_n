## Function Contract

**Inputs**

- `series1`: A nonempty array of `[timestamp, value]` pairs in strictly increasing timestamp order.
- `series2`: A second nonempty array with the same pair format and ordering guarantee.

Let $n=\lvert\texttt{series1}\rvert$ and $m=\lvert\texttt{series2}\rvert$. For a timestamp `t`, a series contributes the value belonging to its first entry whose timestamp is at least `t`, or zero if it has no such entry.

**Return value**

Return one `[timestamp, summedValue]` pair for every distinct timestamp present in either series, sorted in strictly increasing timestamp order.
