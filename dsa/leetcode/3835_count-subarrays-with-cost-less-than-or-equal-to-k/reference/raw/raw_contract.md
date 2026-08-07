## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The inclusive upper bound allowed for a subarray's cost.

Let $N=\lvert\texttt{nums}\rvert$. For $0\le l\le r<N$, define

$$
\operatorname{cost}(l,r)
=
\left(
\max(\texttt{nums}[l..r])
-
\min(\texttt{nums}[l..r])
\right)(r-l+1).
$$

**Return value**

Return the number of index pairs $(l,r)$ for which $\operatorname{cost}(l,r)\le\texttt{k}$.

