## Description

You are given an integer array `nums` of length $N$. From it, construct a second array named `prefixGcd`. For every index $i$, first determine the maximum value among `nums[0]` through `nums[i]`; call that prefix maximum $M_i$. The derived value at the same index is

$$
\texttt{prefixGcd[i]} = \gcd(\texttt{nums[i]}, M_i).
$$

After every derived value has been produced, sort `prefixGcd` in non-decreasing order. Repeatedly take the smallest element that has not yet been used together with the largest unused element. Each such pair contributes the greatest common divisor of its two members to the result. Continue until another pair cannot be formed. When $N$ is odd, the one middle element left in the sorted array is unpaired and contributes nothing.

Return the sum of the GCD values contributed by all formed pairs. Here, $\gcd(a,b)$ is the greatest common divisor of integers $a$ and $b$.
