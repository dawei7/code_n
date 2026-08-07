## Function Contract

**Inputs**

- `nums1`: The first integer array.
- `nums2`: The second integer array.
- `k`: The exact number of ordered index pairs to select.

Let $N=\lvert\texttt{nums1}\rvert$, $M=\lvert\texttt{nums2}\rvert$, and $K=\texttt{k}$. A legal selection consists of index chains

$$
0\le i_1<i_2<\cdots<i_K<N
$$

and

$$
0\le j_1<j_2<\cdots<j_K<M.
$$

Its score is

$$
\sum_{t=1}^{K}\texttt{nums1}[i_t]\texttt{nums2}[j_t].
$$

**Return value**

Return the largest score among all legal selections of exactly $K$ pairs.

