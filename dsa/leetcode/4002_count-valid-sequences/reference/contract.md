## Function Contract

**Inputs**

- `n`: The required sum of the sequence.
- `k`: The exact number of positive integers in the sequence.

A candidate sequence $(a_1,a_2,\ldots,a_k)$ is valid when every $a_i$ is positive,

$$
\sum_{i=1}^{k} a_i=n,
$$

and $\prod_{i=1}^{k}a_i$ is even.

**Return value**

Return the number of distinct valid ordered sequences, reduced modulo $10^9+7$.
