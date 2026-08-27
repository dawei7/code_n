## Description

The Fibonacci sequence $(f_i)$ is the unique sequence such that

$f_0=0$
$f_1=1$
$f_{i+1}=f_i+f_{i-1}$

Similarly, there is a unique function $A(m,n)$ such that

$A(0,0)=0$
$A(0,1)=1$
$A(m+1,n)=A(m,n+1)+A(m,n)$
$A(m+1,n+1)=2A(m+1,n)+A(m,n)$

Define $S(k)=\displaystyle\sum_{i=2}^k\sum_{j=2}^k A(f_i,f_j)$. For example

$$
\begin{aligned}
S(3)&=A(1,1)+A(1,2)+A(2,1)+A(2,2)\\
&=2+5+7+16\\
&=30
\end{aligned}
$$

You are also given $S(5)=10396$.

Find $S(50)$, giving your answer modulo $1123581313$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

