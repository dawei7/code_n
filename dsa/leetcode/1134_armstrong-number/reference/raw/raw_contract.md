## Function Contract

**Inputs**

- `n`: a positive integer. Let $k$ be the number of digits in its ordinary decimal representation, and let those digits be $d_1, d_2, \ldots, d_k$.

The Armstrong sum is

$$
\sum_{i=1}^{k} d_i^k.
$$

**Return value**

- `true` exactly when the Armstrong sum equals `n`; otherwise, `false`.

Repeated digits contribute separately, and a zero digit contributes $0^k = 0$.
