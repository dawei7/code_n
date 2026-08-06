## Description

You are given a 0-indexed integer array `nums` and a positive integer `d`.
Choose three distinct indices in strictly increasing order, $i<j<k$.

Count the index triplets for which the sum of their three array values is
divisible by `d`:

$$
(\texttt{nums[i]}+\texttt{nums[j]}+\texttt{nums[k]})\bmod d=0.
$$

Triplets are distinguished by indices, so repeated values may participate in
several different choices.
