## General

Every value that ever appears in the array was present initially: an operation copies an existing value and creates nothing new. If an original value $x$ changes through a chain $x \to d_1 \to d_2 \to \cdots \to d_k$, then each new value divides the preceding one. Divisibility is transitive, so the final value $d_k$ is an initially present divisor of $x$. This gives a lower bound for each position: it cannot finish below the smallest value from the original array that divides its original value.

That bound is attainable. Let $d$ be the smallest initially present divisor of $x$. If some smaller present value divided $d$, it would also divide $x$, contradicting the choice of $d$. Thus an occurrence of $d$ never needs to be reduced to attain its own minimum and can remain available as a donor. Copying it directly into every original multiple assigned to $d$ realizes all per-position minima simultaneously.

Record the distinct values in a set, sort them, and process those present divisors from smallest to largest. For each divisor, visit its multiples through $V$ and update only multiples that belong to the set. The first improvement assigns the smallest possible present divisor. Finally, replace each array value conceptually with its stored divisor and sum those minima. No simulation or operation ordering is required.

## Complexity detail

Let $n$ be the array length, $V$ its maximum value, and $N=\max(n,V)$. Building the presence table and summing the answer take $O(n)$ time. The sieve visits at most

$$
V\left(1 + \frac12 + \frac13 + \cdots + \frac1V\right)=O(V\log V)
$$

divisor-multiple pairs. Sorting the distinct values costs $O(n\log n)$. The total $O(n\log n + V\log V)$ time is $O(N\log N)$ under the single combined bound used by the app. The set and minimum-divisor map use $O(n)$ space, hence $O(N)$ space.

## Alternatives and edge cases

- **Compare every pair of distinct values:** Testing every present candidate divisor for every value is correct but takes $O(k^2)$ time for $k$ distinct values.
- **Enumerate divisors of every element:** Factoring each value independently and checking a hash set of present values can take $O(n\sqrt V)$ time and repeats work for duplicates.
- **Use the greatest common divisor:** A gcd that is absent from the initial array can never be created, so values such as `[6,10]` cannot be reduced to `2`.
- **Replacement chains:** They cannot reveal a better answer than the smallest original divisor because every link preserves the relation “final value divides the original value.”
- **Value `1`:** If `1` occurs, it divides every element and the minimum sum is exactly $n$.
- **Duplicates:** Equal values share the same minimum divisor, and every occurrence contributes separately to the sum.
- **No divisible pair:** Each value is its own smallest present divisor, so the answer equals the original sum.
- **Large totals:** Up to $10^5$ elements of value $10^5$ can produce a sum of $10^{10}$ when no smaller divisor is present.
