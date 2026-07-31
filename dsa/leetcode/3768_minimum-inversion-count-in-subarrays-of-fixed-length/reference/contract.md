## Function Contract

**Inputs**

- `nums`: The integer array in which fixed-length subarrays are examined.
- `k`: The exact length of every candidate subarray.

Let $N=\lvert\texttt{nums}\rvert$. A subarray is contiguous, and there are $N-K+1$ candidate windows, where $K=\texttt{k}$. Equal values do not form an inversion because the required comparison is strict.

**Return value**

Return the minimum number of pairs $(i,j)$ satisfying $i<j$ and `window[i] > window[j]` among all length-`k` windows. The result is an integer and may exceed the range of a signed 32-bit value.
