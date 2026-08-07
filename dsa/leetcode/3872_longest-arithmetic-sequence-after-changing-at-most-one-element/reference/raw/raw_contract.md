## Function Contract

**Inputs**

- `nums`: An array of integers from which a contiguous subarray will be selected.

At most one array position may receive any integer value. All other values and their order remain unchanged. A selected subarray with values $a_0,a_1,\ldots,a_{m-1}$ is arithmetic exactly when one integer difference $d$ satisfies $a_j-a_{j-1}=d$ for every $1\le j<m$.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the maximum attainable length of an arithmetic subarray. The result counts elements, not adjacent differences.
