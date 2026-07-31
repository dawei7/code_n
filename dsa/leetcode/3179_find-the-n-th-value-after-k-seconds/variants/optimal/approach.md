## General

**From prefix sums to Pascal's identity**

Let $A_t(i)$ be the value at index $i$ after $t$ seconds. The update rule says that $A_t(i)$ is the sum of $A_{t-1}(0)$ through $A_{t-1}(i)$. Consecutive prefix sums differ only in their last term, so

$$
A_t(i) = A_t(i-1) + A_{t-1}(i).
$$

The boundary values are $A_0(i)=1$ and $A_t(0)=1$. These are exactly the boundary and recurrence of Pascal's triangle. Applying Pascal's identity inductively gives

$$
A_t(i)=\binom{t+i}{i}.
$$

Therefore the requested last value is

$$
A_k(n-1)=\binom{n+k-1}{n-1}.
$$

This identity accounts for every simultaneous array update without constructing any intermediate array.

**Evaluating one coefficient modulo the prime**

Set $N=n+k-1$ and $r=\min(n-1,k)$. Symmetry of binomial coefficients allows the smaller side to be used:

$$
\binom{N}{r}
=
\frac{(N-r+1)(N-r+2)\cdots N}{1\cdot2\cdots r}.
$$

Accumulate the numerator and denominator separately modulo $M=10^9+7$. Because $r\le999<M$, the denominator is nonzero modulo the prime $M$ and has a modular inverse. Fermat's little theorem supplies that inverse as $	ext{denominator}^{M-2}\bmod M$. Multiplying the numerator by this inverse yields the same binomial coefficient modulo $M$, which the identity above proves is exactly the required array value.

## Complexity detail

Let $r=\min(n-1,k)$ and $M=10^9+7$. Building the two products takes $O(r)$ time, and binary exponentiation for the modular inverse takes $O(\log M)$ time. The total is $O(\min(n,k)+\log M)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Repeated in-place prefix sums:** Perform $k$ left-to-right prefix passes over an $n$-element array. This follows the statement directly and takes $O(nk)$ time and $O(n)$ space, but it does unnecessary work when only the last value is requested.
- **Factorials and inverse factorials:** Compute $N!/(r!(N-r)!)$ modulo $M$. This is useful when answering many coefficient queries, but tables require $O(n+k)$ space; for one query, the two short products are simpler.
- **Single-element array:** When $n=1$, $r=0$, both products remain $1$, and the method correctly returns the unchanged value $1$ for every legal $k$.
- **Simultaneous-update semantics:** A direct simulation must base every new entry on the previous second's array. A left-to-right in-place prefix pass is valid because the newly written left neighbor already represents exactly that old-row prefix sum.
- **Safe modular division:** Ordinary integer division after taking remainders is invalid. Division must use the modular inverse, which exists here because every denominator factor is smaller than the prime modulus.
