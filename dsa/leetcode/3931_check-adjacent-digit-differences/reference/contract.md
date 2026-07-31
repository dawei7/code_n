## Function Contract

**Input**

- `s`: A string containing only the characters `0` through `9`.

Let $N=\lvert\texttt{s}\rvert$. Every index from $0$ through $N-2$ begins exactly one adjacent pair, namely `s[i]` and `s[i + 1]`. Leading zeroes are ordinary digits and remain part of the string.

**Return value**

Return a boolean that is `true` exactly when

$$
\left\lvert \operatorname{digit}(\texttt{s[i]})-
\operatorname{digit}(\texttt{s[i+1]})\right\rvert\le 2
$$

for every integer $i$ satisfying $0\le i<N-1$. Equality with $2$ is allowed.
