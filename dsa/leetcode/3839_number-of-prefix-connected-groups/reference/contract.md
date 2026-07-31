## Function Contract

**Inputs**

- `words`: The array whose words may form prefix-connected groups.
- `k`: The exact prefix length used for every connectivity comparison.

Let $N=\lvert\texttt{words}\rvert$ and $K=\texttt{k}$. Only a word of length at least $K$ has a valid length-$K$ prefix. For every such prefix $p$, define

$$
C(p)=\left\lvert\left\{i\mid \lvert\texttt{words}[i]\rvert\ge K
\text{ and }\texttt{words}[i][0..K-1]=p\right\}\right\rvert.
$$

All indices with the same prefix form one maximal connected group. The requested groups are exactly the prefixes $p$ for which $C(p)\ge 2$.

**Return value**

Return the number of distinct valid length-$K$ prefixes that occur at two or more indices.
