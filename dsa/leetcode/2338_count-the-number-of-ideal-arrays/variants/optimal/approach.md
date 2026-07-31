## General

Fix the final value $x$ of an ideal array and write its prime factorization as

$$
x=\prod_p p^{e_p}.
$$

Divisibility means that, for every prime $p$, its exponent can only stay equal
or increase from one position to the next. Equivalently, distribute the final
exponent $e_p$ as $n$ nonnegative increments: the first increment supplies the
exponent in `arr[0]`, and every later increment supplies the new factors
introduced at that position.

**Count exponent distributions**

Stars and bars gives

$$
\binom{n+e_p-1}{e_p}
$$

ways to distribute exponent $e_p$. Choices for different primes are
independent, so the number of ideal arrays ending at $x$ is the product of
those binomial coefficients. Summing that product for every
$1 \le x \le \texttt{maxValue}$ counts every ideal array exactly once by its
last value.

Precompute the few needed coefficients modulo $10^9+7$. No exponent can exceed
$\lfloor\log_2 \texttt{maxValue}\rfloor$. A smallest-prime-factor sieve then
lets each final value be factored by repeatedly removing its current smallest
prime. Whenever a run of one prime ends, multiply the contribution for that
run's exponent into the value's count.

The correspondence is reversible: every exponent distribution constructs one
divisibility chain, and subtracting consecutive exponent vectors from any
ideal array recovers exactly one distribution. The product and final-value sum
therefore neither omit nor duplicate an array.

## Complexity detail

Let $M=\texttt{maxValue}$. Building the smallest-prime-factor table costs
$O(M\log\log M)$ time. Factoring all values takes $O(M\log M)$ time as a safe
upper bound, so the complete method is $O(M\log M)$ time. The sieve uses
$O(M)$ space; the coefficient table has only $O(\log M)$ entries.

## Alternatives and edge cases

- **Dynamic programming over multiples:** Extending divisor chains by visiting
  multiples can count chains by their number of distinct values and then place
  repeats combinatorially, but it needs a larger two-dimensional state.
- **Trial division for every final value:** The same formula remains correct,
  but independently searching divisors up to each square root costs
  $O(M\sqrt M)$ time in the worst case.
- **Final value one:** Its factorization is empty, whose product is 1; this
  represents the all-ones array.
- **Equal neighbors:** Zero exponent increments are allowed, so repeated values
  are included automatically.
- **Modular arithmetic:** Reduce every product and the final sum modulo
  $10^9+7$; the small modular inverses used in the coefficient recurrence
  exist because their denominators are below the prime modulus.
