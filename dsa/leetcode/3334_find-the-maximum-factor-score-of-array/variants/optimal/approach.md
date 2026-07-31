## General

Removing one position splits the remaining values into a prefix and a suffix. Both GCD and LCM are associative and commutative, so the aggregate of those two pieces can be combined without revisiting their elements.

Build four arrays with an extra identity slot. `prefix_gcd[i]` and `prefix_lcm[i]` aggregate `nums[0:i]`, while `suffix_gcd[i]` and `suffix_lcm[i]` aggregate `nums[i:n]`. Use $0$ as the identity for GCD because $\gcd(0,x)=x$, and use $1$ as the identity for LCM because $\operatorname{lcm}(1,x)=x$.

The full-array candidate is

$$
\texttt{prefix\_gcd[n]}\cdot\texttt{prefix\_lcm[n]}.
$$

If index `i` is removed, combine the aggregates on its two sides:

$$
g_i=\gcd(\texttt{prefix\_gcd[i]},\texttt{suffix\_gcd[i+1]}),
$$

$$
\ell_i=\operatorname{lcm}(\texttt{prefix\_lcm[i]},\texttt{suffix\_lcm[i+1]}).
$$

Then compare $g_i\ell_i$ with the best score seen so far. The prefix and suffix intervals partition every element except `nums[i]`, so associativity proves that $g_i$ and $\ell_i$ are exactly the GCD and LCM after that deletion. Considering the full array and every index covers all choices allowed by “at most one.”

For a one-element array, deleting its only element combines two empty sides. Their identities produce GCD $0$ and LCM $1$, hence score $0$, while the unchanged candidate correctly remains the element squared.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $M=\max(\texttt{nums})$. The two construction passes and the deletion pass perform $O(n)$ GCD/LCM combinations. A Euclidean GCD costs $O(\log M)$ for this bounded input domain, so the total time is $O(n\log M)$. The four aggregate arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Recompute after every deletion:** This straightforward method is correct but scans up to $n-1$ values for each of $n$ candidates, taking $O(n^2\log M)$ time.
- **Prime-exponent counts:** Because values are at most $30$, tracking the smallest and largest exponent of each prime can also support deletions, but it is more elaborate than prefix/suffix aggregation.
- **No deletion is best:** The original array's score must be evaluated separately; removing an element is optional.
- **One element:** Keeping `x` gives $x^2$, while deleting it gives the defined empty score $0$.
- **Two elements:** Removing either value leaves a singleton whose score is its square, which can exceed the pair's GCD-times-LCM score.
- **Repeated values:** Prefix and suffix identities still combine correctly even when deleting one copy changes neither aggregate.
