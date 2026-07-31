## Function Contract

**Inputs**

- `nums`: A nonempty integer array whose indices are zero-based.

Let $N = \lvert\texttt{nums}\rvert$. For an index `i`, define its left sum as

$$
L_i = \sum_{j=0}^{i-1} \texttt{nums[j]},
$$

where $L_0 = 0$. Define its right product as

$$
R_i = \prod_{j=i+1}^{N-1} \texttt{nums[j]},
$$

where $R_{N-1} = 1$. Index `i` is balanced exactly when $L_i = R_i$.

**Return value**

Return the smallest balanced index. Return `-1` when no index satisfies the
equality.
