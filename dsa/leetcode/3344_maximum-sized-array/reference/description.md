## Description

For a chosen positive integer $n$, define a three-dimensional $n \times n \times n$ array $A$. Its indices satisfy $0 \le i,j,k<n$, and each entry is

$$
A[i][j][k]=i\,(j\mathbin{\mathrm{OR}}k),
$$

where $\mathrm{OR}$ is bitwise OR on the non-negative indices.

You are given a non-negative budget `s`. Find the largest positive dimension $n$ for which the sum of every entry in $A$ is at most `s`. The array is conceptual; its elements do not need to be constructed or stored.
