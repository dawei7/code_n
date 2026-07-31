## Description

A staircase contains $n+1$ steps numbered from $0$ through $n$. The journey begins on step $0$ with a total cost of zero. The supplied array `costs` represents the remaining steps using one-based step numbering: `costs[i]` is the landing cost associated with step $i$.

From a current step $i$, a jump may advance by exactly one, two, or three positions. If that jump lands on step $j$, it contributes the destination cost plus the square of the jump length:

$$
\text{jump cost}(i,j)=\texttt{costs[j]}+(j-i)^2.
$$

Choose a valid sequence of jumps from step $0$ to step $n$ whose accumulated cost is as small as possible, and return that minimum total.
