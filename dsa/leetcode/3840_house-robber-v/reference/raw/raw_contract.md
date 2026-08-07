## Function Contract

**Inputs**

- `nums`: The money stored in the houses, in street order.
- `colors`: The corresponding security color code for every house.

Let $N=\lvert\texttt{nums}\rvert=\lvert\texttt{colors}\rvert$. A chosen index set $S\subseteq\{0,\ldots,N-1\}$ is valid exactly when

$$
i\in S \text{ and } i+1\in S
\quad\Longrightarrow\quad
\texttt{colors}[i]\ne\texttt{colors}[i+1].
$$

Thus, equality of color codes matters only for two consecutive selected indices that are also adjacent houses; the same color may occur at any distance elsewhere.

**Return value**

Return the maximum possible value of $\sum_{i\in S}\texttt{nums}[i]$ over all valid choices $S$.
