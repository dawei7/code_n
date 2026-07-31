## Function Contract

**Inputs**

- `nums`: The non-negative integer array from which a nonempty contiguous subarray is selected.
- `k`: The inclusive upper bound on the selected subarray's maximum-minus-minimum difference.

For boundaries $0\le l\le r<N$, where $N=\lvert\texttt{nums}\rvert$, the selected subarray is `nums[l:r + 1]`. It is valid when

$$
\max_{l\le i\le r}\texttt{nums}[i]
-
\min_{l\le i\le r}\texttt{nums}[i]
\le \texttt{k}.
$$

Its value is

$$
\texttt{nums}[l]\mathbin{\mathrm{XOR}}\texttt{nums}[l+1]
\mathbin{\mathrm{XOR}}\cdots\mathbin{\mathrm{XOR}}\texttt{nums}[r].
$$

Let $V=2^{15}$ denote the exclusive upper bound on every input value and on every prefix XOR.

**Return value**

Return the maximum XOR value over all valid pairs of boundaries $(l,r)$. A length-one subarray is always valid because its maximum and minimum are equal.
