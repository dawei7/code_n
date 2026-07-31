## Description

You are given an integer array `capacity`.

A subarray `capacity[l..r]` is **stable** when both of these conditions hold:

- Its length is at least 3.
- Its first element and its last element are each equal to the sum of every element strictly between them. In other words,

  $$
  \texttt{capacity}[l]
  = \texttt{capacity}[r]
  = \sum_{i=l+1}^{r-1} \texttt{capacity}[i].
  $$

Return the number of stable subarrays in `capacity`.
