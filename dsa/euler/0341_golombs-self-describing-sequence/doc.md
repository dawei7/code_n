# Golomb's Self-describing Sequence

### Golomb's Self-describing Sequence

The Golomb's self-describing sequence $(G(n))$ is the only nondecreasing sequence of natural numbers such that $n$ appears exactly $G(n)$ times in the sequence. The values of $G(n)$ for the first few $n$ are






$$
\begin{matrix}
n &amp; 1 &amp; 2 &amp; 3 &amp; 4 &amp; 5 &amp; 6 &amp; 7 &amp; 8 &amp; 9 &amp; 10 &amp; 11 &amp; 12 &amp; 13 &amp; 14 &amp; 15 &amp; \ldots \\
G(n) &amp; 1 &amp; 2 &amp; 2 &amp; 3 &amp; 3 &amp; 4 &amp; 4 &amp; 4 &amp; 5 &amp; 5 &amp; 5 &amp; 6 &amp; 6 &amp; 6 &amp; 6 &amp; \ldots
\end{matrix}
$$


You are given that $G(10^3) = 86$, $G(10^6) = 6137$.

You are also given that $\sum G(n^3) = 153506976$ for $1 \le n \lt 10^3$.



Find $\sum G(n^3)$ for $1 \le n \lt 10^6$.
