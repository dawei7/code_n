## General

**Check each starting position while updating three aggregates.** A subarray is product equivalent when

$$
\operatorname{prod}(\textit{arr})
=
\gcd(\textit{arr})\cdot\operatorname{lcm}(\textit{arr}).
$$

The protected source enumerates every possible left endpoint $i$. For that fixed start, it extends the right endpoint $j$ one position at a time and maintains:

- `p`, the product of `nums[i : j + 1]`;
- `g`, the greatest common divisor of that subarray;
- `l`, the least common multiple of that subarray.

The initial values are the identities for these updates: `p = 1`, `g = 0`, and `l = 1`. Python's `gcd(0, x)` is $x$, so the first element correctly initializes the GCD. Likewise, `lcm(1, x)` is $x$, and multiplying one by the first value initializes the product.

When a new rightmost value `nums[j]` is included, the source updates all three quantities:

`p *= nums[j]`,

`g = gcd(g, nums[j])`,

and

`l = lcm(l, nums[j])`.

It then tests `p == g * l`. If equality holds, the current subarray is product equivalent and its length `j - i + 1` can improve `ans`. Because each aggregate is carried forward, extending one starting position does not rescan the elements already inside the subarray.

For example, for `[3, 4, 5]`, the product is $60$, the GCD is $1$, and the LCM is $60$, so equality holds and length $3$ is recorded. For two positive integers $a$ and $b$, the identity

$$
\gcd(a,b)\operatorname{lcm}(a,b)=ab
$$

means every length-$2$ subarray is product equivalent. Since the input length is at least two, the answer is always at least two, even though the source safely initializes `ans` to zero and discovers that fact through enumeration.

**Understand the equality through prime exponents.** This is not required to execute the code, but it clarifies what the test means. For a fixed prime, suppose its exponents across the subarray are $e_1,e_2,\ldots,e_r$. The product uses exponent $\sum e_t$, the GCD uses $\min e_t$, and the LCM uses $\max e_t$. Equality requires

$$
\sum_t e_t=\min_t e_t+\max_t e_t
$$

for every prime. Ones contribute exponent zero for every prime, which is why a subarray can contain many ones without breaking equality. The direct aggregate check handles all primes at once and avoids explicit factorization.

**Use a global ceiling to stop hopeless extensions.** A straightforward double loop is already acceptable for $n\le100$, but the source adds a safe early break. Before enumeration it computes

`max_p = lcm(*nums) * max(nums)`.

Let $L_{\mathrm{all}}$ be the LCM of the complete input and $M$ its largest element. For any subarray:

- its LCM divides $L_{\mathrm{all}}$, so it is at most $L_{\mathrm{all}}$;
- its GCD is at most every element in it and therefore at most $M$.

Consequently,

$$
\gcd(\textit{subarray})\operatorname{lcm}(\textit{subarray})
\le M L_{\mathrm{all}}
=\texttt{max\_p}.
$$

If the running product `p` becomes greater than `max_p`, the current subarray cannot satisfy equality. All input values are positive, so extending farther can never decrease `p`. Meanwhile, the right-hand side of every longer subarray remains bounded by the same global ceiling. No longer extension from this $i$ can work, and `break` is correct.

The break occurs after checking the current subarray. That ordering is logically harmless because a product larger than the ceiling cannot pass the equality test anyway, and then every later extension is discarded.

**Why the result is exact.** Every pair $(i,j)$ reached by the loops identifies a genuine contiguous subarray, and `p`, `g`, and `l` are its exact aggregates by induction on $j$. The code records its length if and only if the defining equality holds, so it never accepts an invalid subarray.

Conversely, consider any product-equivalent subarray. Its left endpoint is visited by the outer loop. The inner loop cannot break before reaching its right endpoint: if it did, the running product would already exceed the universal bound and, because products do not decrease, the candidate's product would also exceed what its GCD times LCM can reach. That would contradict product equivalence. Thus every valid subarray is tested, and `ans` becomes the maximum valid length.

The manifest summary describes a linear sliding window in which prime factors occur in at most one element. The exact protected source does not factor values or maintain such a window. It uses quadratic endpoint enumeration with an early product ceiling. This explanation and its complexity deliberately follow the code that actually runs.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. In the worst case, the early break never triggers. An all-ones array is a simple example: the running product and global ceiling are both one for every endpoint. The loops then inspect

$$
\frac{n(n+1)}2=O(n^2)
$$

subarrays. Each extension performs multiplication, GCD, and LCM on values bounded by the problem's tiny domain and by the early-break ceiling. Under the standard word-operation model, this is $O(1)$ work per extension, so worst-case time is $O(n^2)$, not the manifest's $O(n)$.

The nested loops retain only scalar aggregates, indices, and the answer, giving $O(1)$ persistent auxiliary space. The call `lcm(*nums)` passes all values as arguments; a literal CPython accounting may include an $O(n)$ transient argument tuple, but no table proportional to the number of subarrays is stored. With values restricted to $1$ through $10$, $L_{\mathrm{all}}$ is itself small, so integer growth is tightly bounded once the break is applied.

## Alternatives and edge cases

- **Prime-factor sliding window:** A more specialized method can track prime-factor conflicts and may achieve linear time under the small value bound. That is closer to the manifest summary, but it is not implemented in this protected file.
- **Recompute aggregates for every subarray:** Taking a slice and separately calculating its product, GCD, and LCM would add another factor of $n$, reaching $O(n^3)$ time.
- **Prefix products alone:** Products support division here because values are positive, but GCD and LCM do not have equally simple inverse prefix operations. Incremental extension keeps all three exact.
- **All ones:** Every subarray has product, GCD, and LCM equal to one. The break never fires, and the full array is correctly returned.
- **Length one:** A singleton $[x]$ has product $x$ but GCD times LCM $x^2$, so it is equivalent only when $x=1$. The source tests this literally.
- **Length two:** Every positive pair satisfies the standard GCD-LCM identity, guaranteeing a valid length of at least two under the input constraints.
- **Repeated prime factors:** Sharing a prime does not automatically invalidate a subarray; the exact exponent relationship determines validity. The aggregate equality avoids unsafe informal shortcuts.
- **Safe early break:** The proof depends on positive elements. With zeros or negatives, the running product would not be monotone and this stopping rule would require reconsideration, but such values are excluded.
- **Global rather than local bound:** `max_p` may be loose for a particular start, yet looseness only delays a break. It never removes a candidate that could satisfy the equality.
- **Quadratic worst case:** The early break is an optimization, not a change to the asymptotic worst-case guarantee. Complexity should not be reported as linear merely because many typical products grow quickly.
