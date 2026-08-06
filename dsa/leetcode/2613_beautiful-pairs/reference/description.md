## Description

Two 0-indexed integer arrays, `nums1` and `nums2`, have the same length. Treat every index $i$ as the point whose coordinates are `(nums1[i], nums2[i])`.

For a pair of indices $(i,j)$ with $i<j$, its Manhattan distance is

$$
\lvert \texttt{nums1}[i]-\texttt{nums1}[j] \rvert
+
\lvert \texttt{nums2}[i]-\texttt{nums2}[j] \rvert.
$$

A pair is beautiful when this value is the minimum among all possible index pairs. Return a beautiful pair. If several pairs attain the same minimum distance, choose the lexicographically smallest one: prefer the smaller first index, and when those are equal, prefer the smaller second index.
