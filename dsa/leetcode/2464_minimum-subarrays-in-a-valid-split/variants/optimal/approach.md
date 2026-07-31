## General

Let $n=\lvert\texttt{nums}\rvert$ and $M=\max(\texttt{nums})$. Define `splits[i]` as the minimum number of valid parts covering the prefix before index $i$. If the last part begins at $j$ and ends at $i$, its endpoints are valid exactly when `nums[j]` and `nums[i]` share at least one prime factor.

The direct transition would inspect every $j\le i$. Instead, maintain `best_start[p]`, the minimum `splits[j]` among all potential start indices $j$ whose value is divisible by prime $p$. Before treating index $i$ as an ending position, factor `nums[i]` and insert `splits[i]` into every corresponding prime entry. This includes the valid singleton choice $j=i$ whenever the value exceeds `1`.

For the same set of distinct prime factors, the best last part uses the smallest stored prefix cost. Therefore

$$
\texttt{splits[i+1]}=1+\min_{p\mid\texttt{nums[i]}}\texttt{best\_start[p]}.
$$

Every stored candidate shares $p$ with the ending value, so the constructed part has endpoint GCD greater than $1$. Conversely, any valid last part has some shared prime and its starting prefix was inserted into that prime's entry, so the transition cannot miss an optimal split.

Build a smallest-prime-factor sieve through $M$ and use it to extract each value's distinct prime factors. The value `1` has no prime factors, cannot begin or end a valid part, and leaves its prefix state unreachable. A final cost greater than $n$ is therefore converted to `-1`.

## Complexity detail

The smallest-prime-factor sieve takes $O(M\log\log M)$ time. Each value has at most $O(\log M)$ prime factors counted through repeated division, so all dynamic-programming updates take $O(n\log M)$ time. Total time is $O(M\log\log M+n\log M)$.

The sieve uses $O(M)$ entries, the prefix DP uses $O(n)$ entries, and the prime-best map has at most $O(M)$ keys. Total auxiliary space is $O(M+n)$.

## Alternatives and edge cases

- **Quadratic prefix DP:** Testing every possible start with a GCD computes the same recurrence in $O(n^2\log M)$ time and $O(n)$ space.
- **Trial-division factorization:** Avoiding the sieve reduces preprocessing memory, but factoring every value independently can take $O(n\sqrt M)$ time.
- **Only adjacent GCDs:** Requiring neighboring values to share a divisor is incorrect because only each chosen subarray's first and last elements matter.
- **Singletons:** A one-element part is valid exactly when its value is greater than `1`, since $\gcd(x,x)=x$.
- **Value one:** No valid part can start or end at `1`; a leading or trailing `1` makes the entire split impossible.
- **Interior ones:** A `1` may appear inside a longer valid part because interior values do not affect the endpoint GCD.
- **Repeated prime powers:** Each distinct prime is processed once per value; repeated powers do not create different transitions.
- **Unreachable sentinel:** Arithmetic can raise an unreachable cost above its initial sentinel, so impossibility is detected with `splits[n] > n`, not sentinel equality.
