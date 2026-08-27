## Description

The function $\operatorname{\mathbf{lcm}}(a,b)$ denotes the least common multiple of $a$ and $b$.

Let $A(n)$ be the average of the values of $\operatorname{lcm}(n,i)$ for $1 \le i \le n$.

E.g: $A(2)=(2+2)/2=2$ and $A(10)=(10+10+30+20+10+30+70+40+90+10)/10=32$. 

Let $S(n)=\sum A(k)$ for $1 \le k \le n$.

$S(100)=122726$.

Find $S(99999999019) \bmod 999999017$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

