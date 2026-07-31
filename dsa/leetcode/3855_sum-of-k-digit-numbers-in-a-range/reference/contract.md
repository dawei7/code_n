## Function Contract

**Inputs**

- `l`: The smallest digit that may be chosen.
- `r`: The largest digit that may be chosen; the interval includes both endpoints.
- `k`: The exact number of independently chosen digit positions in every sequence.

For digits $d_{k-1},d_{k-2},\ldots,d_0$, the represented integer is

$$
\sum_{p=0}^{k-1} d_p10^p.
$$

Every one of the $(r-l+1)^k$ digit sequences contributes once, including sequences whose first digit is zero.

**Return value**

Return the sum of all represented integers reduced modulo $1{,}000{,}000{,}007$.
