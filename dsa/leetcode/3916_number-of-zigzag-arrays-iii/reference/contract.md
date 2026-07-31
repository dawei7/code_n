## Function Contract

**Inputs**

- `n`: The required length of every counted array.
- `l`: The smallest value permitted in an array.
- `r`: The largest value permitted in an array.

Let $m=	exttt{r}-	exttt{l}+1$ be the number of available values.

**Return value**

Return, modulo $10^9+7$, the number of length-`n` arrays over `[l, r]` in which adjacent entries differ and every pair of consecutive comparison directions is opposite.
