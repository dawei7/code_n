## Description

Given an integer array `nums`, choose three indices $(i, j, k)$ whose positions and values are both strictly increasing:

$$
i < j < k
\quad\text{and}\quad
\texttt{nums[i]} < \texttt{nums[j]} < \texttt{nums[k]}.
$$

The value of such a triplet is calculated by `nums[i] - nums[j] + nums[k]`. Return the maximum value over every triplet satisfying both strict inequalities.

The input is guaranteed to contain at least one valid increasing triplet.
