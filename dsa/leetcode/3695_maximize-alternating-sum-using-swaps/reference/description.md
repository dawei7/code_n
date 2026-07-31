## Description

For an integer array `nums`, its alternating sum adds values at even indices and subtracts values at odd indices:

$$
\texttt{nums[0]}-\texttt{nums[1]}+\texttt{nums[2]}-\texttt{nums[3]}+\cdots.
$$

The array `swaps` lists allowed index pairs. For every pair `[p_i, q_i]`, the values currently stored at indices `p_i` and `q_i` may be exchanged. Any allowed exchange can be used repeatedly, and the exchanges may be performed in any order.

Rearrange the values through zero or more allowed swaps so that the resulting alternating sum is as large as possible. Return that maximum value.
