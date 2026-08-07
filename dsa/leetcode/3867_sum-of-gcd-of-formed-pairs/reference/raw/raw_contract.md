## Function Contract

**Inputs**

- `nums`: An array of positive integers.

Let $N=\lvert\texttt{nums}\rvert$ and $V=\max(\texttt{nums})$. For each index $i$, the inclusive prefix maximum and derived value are

$$
M_i = \max_{0 \le j \le i}\texttt{nums[j]},
\qquad
P_i = \gcd(\texttt{nums[i]}, M_i).
$$

The pairing rule applies to the non-decreasing ordering of all $P_i$ values, not to the original `nums` values. Pair the first with the last, the second with the second-to-last, and so on for exactly $\lfloor N/2 \rfloor$ pairs.

**Return value**

Return an integer equal to the sum of the GCD of every formed pair. A singleton input forms no pair and therefore returns `0`.
