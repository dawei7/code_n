## Description

An ordered triplet of distinct indices $(i,j,k)$ is a single divisor triplet when the sum

$$
\texttt{nums[i]}+\texttt{nums[j]}+\texttt{nums[k]}
$$

is divisible by exactly one of the three selected values. Divisibility is tested against each selected position, so equal values in two different positions still contribute two successful divisibility tests.

Given the positive-integer array `nums`, count all ordered triplets of distinct indices that satisfy this condition. Different orders of the same three indices are separate triplets.
