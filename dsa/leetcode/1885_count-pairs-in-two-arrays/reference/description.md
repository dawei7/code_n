## Description

Two integer arrays, `nums1` and `nums2`, have the same length $N$. Choose two distinct positions in increasing index order, $(i,j)$ with $i<j$, and compare the sum of the two values selected from `nums1` with the sum at those same positions in `nums2`.

Count how many index pairs satisfy the strict inequality

$$
\texttt{nums1[i]}+\texttt{nums1[j]} >
\texttt{nums2[i]}+\texttt{nums2[j]}.
$$

Pairs whose two sums are equal do not count. Return the total over all possible index pairs.
