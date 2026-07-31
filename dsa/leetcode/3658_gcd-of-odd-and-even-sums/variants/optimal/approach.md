## General

The first $n$ positive odd integers sum to a square:

$$
1+3+\cdots+(2n-1)=n^2.
$$

The first $n$ positive even integers are twice the first $n$ positive integers, so their sum is

$$
2+4+\cdots+2n=2\frac{n(n+1)}{2}=n(n+1).
$$

Substitute these closed forms into the requested greatest common divisor and factor out the shared positive factor $n$:

$$
\gcd\bigl(n^2,n(n+1)\bigr)
=n\gcd(n,n+1).
$$

Consecutive integers are coprime: any common divisor of $n$ and $n+1$ must also divide their difference, which is $1$. Therefore $\gcd(n,n+1)=1$, and the expression reduces exactly to $n$. Returning the input directly is consequently correct for every legal positive value.

## Complexity detail

The method returns `n` without constructing either sequence, performing a summation, or invoking a GCD routine. Under the repository's integer-operation model, it takes $O(1)$ time and $O(1)$ auxiliary space.

The legal domain ends at $n=1000$. Across that bounded range, execution overhead prevents reliable runtime scaling from distinguishing the direct return from explicit linear summation. The package therefore uses a bounded-domain certificate: the algebra above proves the returned identity, and inspection of the accepted source proves that it performs no loop, sequence construction, or iterative GCD computation.

## Alternatives and edge cases

- **Explicitly summing both sequences:** This follows the definition directly but performs $O(n)$ additions and is unnecessary.
- **Closed forms followed by a GCD call:** Computing $n^2$, $n(n+1)$, and then Euclid's algorithm is correct, but it misses the final simplification and adds avoidable arithmetic.
- **Minimum input:** For $n=1$, the two sums are $1$ and $2$, so returning $1$ remains valid.
- **Even and odd values of n:** The derivation depends only on consecutive integers being coprime, not on the parity of $n$.
- **Maximum input:** The same identity applies at $n=1000$ without constructing 1000 odd and 1000 even terms.
