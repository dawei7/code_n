## Function Contract

**Inputs**

- `nums`: The integer array whose delayed equal-value occurrences must be counted.
- `k`: The number of positions immediately after each index that remain too close to count.

Let $N=\lvert\texttt{nums}\rvert$. For every index $i$, the returned value is

$$
\texttt{ans}[i]
=
\left\lvert
\left\{
j \mid i+\texttt{k}<j\le N-1
\text{ and }
\texttt{nums}[j]=\texttt{nums}[i]
\right\}
\right\rvert.
$$

The strict inequality excludes the position `i + k` as well as the `k` positions directly after `i`; the first eligible position is `i + k + 1`.

**Return value**

Return the length-$N$ array containing the delayed count for every original index.
