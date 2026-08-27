## Description

Any positive real number $x$ can be decomposed into integer and fractional parts $\lfloor x \rfloor + \{x\}$, where $\lfloor x \rfloor$ (the floor function) is an integer, and $0\le \{x\} < 1$.

For positive integers $k$ and $n$, define the function

$$
\begin{aligned}
f_k(n) = \sum_{i=1}^{n}\left\{ \frac{i^k}{n} \right\}
\end{aligned}
$$

For example, $f_5(10)=4.5$ and $f_7(1234)=616.5$.

Let

$$
\begin{aligned}
S(N) = \sum_{\substack{k=1 \\ k\text{ odd}}}^{N} \sum_{n=1}^{N}  f_k(n)
\end{aligned}
$$

You are given that $S(10)=100.5$ and $S(10^3)=123687804$.

Find $\lfloor S(33557799775533) \rfloor$. Give your answer modulo 977676779.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

