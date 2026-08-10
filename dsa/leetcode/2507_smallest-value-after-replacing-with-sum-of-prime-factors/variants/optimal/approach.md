## General

**Simulate the required transformation until it stops changing**

For the current value, factor it into primes with multiplicity and add those primes. That sum becomes the next value. The method repeats until the factor sum equals the value it started that iteration with.

At the top of each outer iteration:

- `t` stores the current value before factorization;
- `n` is used as a shrinking residual during factorization;
- `s` accumulates the prime-factor sum;
- `i` is the trial divisor, beginning at two.

Saving `t` is essential because `n` is divided down and no longer represents the iteration's original value.

**Extract every copy of a factor**

For a candidate divisor `i`, the inner `while n%i==0` repeatedly:

1. divides one copy of `i` out of `n`;
2. adds `i` to `s`.

Repeated division handles multiplicity exactly. For 8:

$$
8=2\cdot2\cdot2,
$$

so the loop adds $2+2+2=6$, not merely one copy of 2.

Once `i` no longer divides the residual, the candidate increments by one.

**Why testing only through the square root is enough**

The condition `i <= n//i` is an overflow-safe form of $i^2\le n$ for positive integers.

If a composite residual had no factor at most its square root, both factors in any decomposition would be greater than the square root, making their product greater than the residual. That is impossible. Therefore, after trial division ends, any residual `n>1` must be prime.

The code adds that final residual once with `s += n`.

Notice that `n` shrinks as factors are removed. The square-root boundary shrinks with it, which safely avoids testing divisors that can no longer be needed.

**Trace the transformation from 15**

For `t=15`:

- 2 does not divide it;
- 3 divides once, leaving residual 5 and adding 3;
- the trial condition then ends, and residual prime 5 is added.

The factor sum is 8.

The next outer iterations compute:

$$
8\to2+2+2=6,
$$

$$
6\to2+3=5,
$$

and

$$
5\to5.
$$

When 5 maps to itself, the method returns 5.

**Why the sequence cannot skip below its final fixed point**

For factors $p_1,\ldots,p_k$, all at least two, their sum is no greater than their product except in equality cases such as a prime by itself or $2+2=2\cdot2$. Thus replacing a composite number by its prime-factor sum never increases it.

Whenever the sum differs from the current number, it is smaller. The sequence is therefore a nonincreasing sequence of positive integers and must eventually stabilize.

Because values never increase, the stabilized value is the smallest value reached anywhere in the process. Returning at the first fixed point answers the requested minimum.

**Prime and fixed composite behavior**

If `t` is prime, the trial loop extracts nothing, residual `n` remains `t`, and `s` becomes `t`. The equality check returns the prime immediately.

Value 4 is composite but also fixed:

$$
4=2\cdot2,\qquad2+2=4.
$$

The stopping rule correctly depends on `s==t` rather than on whether `t` is prime.

**Why assigning `n=s` is safe**

At the end of a non-fixed iteration, residual `n` may be one or a final prime factor; it is no longer the original number. The complete factor sum is held in `s`. Setting `n=s` establishes the next state exactly as the problem directs.

All variables are integers, and no factor list needs to be stored.


Repeated division plus the residual-prime rule makes `s` exactly the sum of the current number's prime factors with multiplicity. The outer loop consequently generates exactly the problem's replacement sequence.

That sequence never increases and terminates only when another replacement would reproduce the same value. Hence the returned fixed value is exactly the minimum value the required process attains.

## Complexity detail

For one current value $x$, trial division performs at most $O(\sqrt{x})$ candidate checks in the worst case, with additional successful divisions bounded by $O(\log x)$.

Every non-fixed replacement decreases a composite number substantially, and there are at most $O(\log n)$ outer iterations under the conservative manifest analysis. Bounding each by the original square root gives $O(\sqrt n\log n)$ time. In practice, later values are much smaller and the work is lower.

Only a fixed number of integer variables is stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Precomputed smallest prime factors:** A sieve supports fast repeated factorizations but uses $O(n)$ preprocessing and memory.
- **Store a factor list:** It is unnecessary because only the sum is needed.
- **Prime input:** Its only prime factor is itself, so it is returned immediately.
- **Repeated prime factor:** Add it once per division, preserving multiplicity.
- **Value 4:** It is a composite fixed point and must return 4.
- **Final residual:** If greater than one, it is prime and must be added.
- **Shrinking residual:** The square-root condition must use the current residual, as the exact code does.
- **Overflow-safe test:** `i<=n//i` avoids computing `i*i` in fixed-width languages.
- **No increase:** The prime-factor sum cannot exceed the original composite value.
- **Termination:** A decreasing positive-integer sequence must eventually reach a fixed point.
