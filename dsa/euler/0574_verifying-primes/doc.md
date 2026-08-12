# Verifying Primes

### Verifying Primes

Let $q$ be a prime and $A \ge B &gt;0$ be two integers with the following properties:


 $A$ and $B$ have no prime factor in common, that is $\gcd(A,B)=1$.
 The product $AB$ is divisible by every prime less than q.

It can be shown that, given these conditions, any sum $A+B&lt;q^2$ and any difference $1&lt;A-B&lt;q^2$ has to be a prime number. Thus you can verify that a number $p$ is prime by showing that either $p=A+B&lt;q^2$ or $p=A-B&lt;q^2$ for some $A,B,q$ fulfilling the conditions listed above.



Let $V(p)$ be the smallest possible value of $A$ in any sum $p=A+B$ and any difference $p=A-B$, that verifies $p$ being prime. Examples:

$V(2)=1$, since $2=1+1&lt; 2^2$. 

$V(37)=22$, since $37=22+15=2 \cdot 11+3 \cdot 5&lt; 7^2$ is the associated sum with the smallest possible $A$.

$V(151)=165$ since $151=165-14=3 \cdot 5 \cdot 11 - 2 \cdot 7&lt;13^2$ is the associated difference with the smallest possible $A$. 



Let $S(n)$ be the sum of $V(p)$ for all primes $p&lt;n$. For example, $S(10)=10$ and $S(200)=7177$.



Find $S(3800)$.
