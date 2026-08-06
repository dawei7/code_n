## Description

An unknown integer $n$ lies in the inclusive interval $[0, 2^{30}-1]$. The task is to recover and return the **initial** value of this 30-bit number through a predefined interactive API, even though every query changes the hidden state.

Calling `commonBits(num)` first counts the bit positions at which the current $n$ and the query value `num` contain the same binary digit. Only the first 30 positions participate in this comparison. The API then performs `n = n XOR num` before returning the count, so later calls observe the mutated value of $n$.

Every query must also satisfy $0 \le \texttt{num} \le 2^{30}-1$; a result obtained with an out-of-range query is not guaranteed to be reliable. Use legal queries and account for every mutation to determine the original hidden number.
