## Description

You are given an integer array `nums` of length `n`. Let `arr_k` be the array produced by rotating `nums` clockwise by `k` positions, and define

$$
F(k)=0\cdot\texttt{arr}_k[0]+1\cdot\texttt{arr}_k[1]+\cdots+(n-1)\cdot\texttt{arr}_k[n-1].
$$

Return the maximum among $F(0),F(1),\ldots,F(n-1)$. The test cases guarantee that the result fits in a 32-bit integer.
