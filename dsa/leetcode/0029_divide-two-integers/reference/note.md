## Note

Assume the environment stores only signed 32-bit integers in $[-2^{31},2^{31}-1]$. Clamp a quotient above $2^{31}-1$ to $2^{31}-1$, and clamp a quotient below $-2^{31}$ to $-2^{31}$.
