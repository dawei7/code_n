## Function Contract

**Inputs**

- `sweetness`: The sweetness values of the chocolate chunks in their fixed order.
- `k`: The number of friends and the exact number of cuts to make.

Let $n = \lvert\texttt{sweetness}\rvert$. Exactly `k` cuts divide the bar into `k + 1` nonempty contiguous pieces. Define the total sweetness as

$$
S = \sum_{i=0}^{n-1} \texttt{sweetness[i]}.
$$

After the division, your piece is the one with minimum total sweetness among all pieces.

**Return value**

Return the greatest minimum piece sweetness achievable over every valid placement of the `k` cuts.
