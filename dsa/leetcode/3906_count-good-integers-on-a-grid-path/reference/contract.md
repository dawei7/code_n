## Function Contract

**Inputs**

- `l`: The inclusive lower endpoint of the positive integer range.
- `r`: The inclusive upper endpoint of the range.
- `directions`: Six moves containing exactly three `D` characters and three `R` characters.

For each candidate integer, use its 16-character zero-padded decimal form. Character position $4a+b$ is placed at grid cell $(a,b)$. The path always starts at `(0, 0)`, uses every move in `directions`, and includes both endpoints.

**Return value**

Return the number of integers $x$ satisfying $l\le x\le r$ for which the seven path digits obey

$$
d_0\le d_1\le\cdots\le d_6.
$$

Leading zeros are actual grid digits and participate in this comparison.
