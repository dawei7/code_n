## General

**Track only the remainder of each repunit**

The $L$-digit all-ones integer is

$$
R_L=11\ldots1.
$$

Constructing `R_L` directly creates integers with up to $K$ digits. Divisibility needs only its remainder modulo `k`.

Appending one decimal digit 1 satisfies

$$
R_{L+1}=10R_L+1.
$$

If `x=R_L\bmod k`, then

$$
R_{L+1}\bmod k=(10x+1)\bmod k.
$$

The source repeatedly applies `x = (x*10+1) % k`, so `x` always stays between zero and `k-1` regardless of how large the conceptual repunit becomes.

The update depends only on the current remainder. If two lengths ever produce the same remainder, every later extension from those states follows the same sequence. This deterministic finite-state behavior is what makes a bounded search possible.

**Reject even divisors immediately**

Every repunit ends in digit 1 and is therefore odd. It cannot be divisible by an even `k`, so the source returns `-1` when `k % 2 == 0`.

A divisor containing factor five is also impossible because a multiple of five ends in zero or five. The exact source does not reject that case immediately; odd multiples of five simply fail to reach remainder zero during the bounded loop and return `-1` at the end.

**Align the remainder and length counters**

The source initializes

`x = 1 % k` and `ans = 1`,

representing `R_1=1`.

Inside the loop, it first extends the repunit, then increments `ans`. After those two updates, `x` is the remainder of the `ans`-digit repunit. If `x==0`, that length is returned.

The code does not check the one-digit remainder before extension. This is safe because the constraints give `k>=2`, so one is never divisible by `k`.

For `k=3`:

- initialization represents length one with remainder one;
- first extension represents 11 with remainder two and length two;
- second extension represents 111 with remainder zero and length three.

The method returns three.

For `k=7`, the successive repunit remainders for lengths one through six are 1, 4, 6, 5, 2, and 0. The first zero appears at length six, so the source returns six without ever constructing 111111.

**Why a solution exists when `k` is coprime with ten**

Assume `k` has no factor two or five, so $\gcd(k,10)=1$. Consider remainders of `R_1,R_2,\ldots,R_k`.

If one is zero, a solution has been found within `k` digits.

Otherwise, if two remainders were equal, say $R_a\equiv R_b\pmod k$ with $a<b$, then

$$
R_b-R_a=10^aR_{b-a}
$$

would be divisible by `k`. Since $10^a$ is invertible modulo `k`, `R_{b-a}` would be divisible by `k`, contradicting the assumption that none of the first `k` repunits has remainder zero.

There are only `k-1` nonzero remainders, so `k` distinct nonzero remainders are impossible. A zero must occur.

This proves the bounded search is sufficient for every feasible divisor.

**Why the first zero gives the smallest integer**

The algorithm visits repunit lengths in increasing order. Each next repunit is numerically larger because it appends another one.

The first remainder zero therefore corresponds both to the shortest valid length and the smallest valid all-ones integer. Returning immediately is correct.

For impossible divisors, remainder states eventually repeat without hitting zero. The loop's fixed bound prevents an infinite search.

**Understand the exact loop bound**

The loop executes up to `k` extensions after representing length one, so it may form through `R_{k+1}`. Feasible `k>=2` values have a solution among `R_1..R_k`, so the extra possible extension is harmless. Impossible odd multiples of five still never produce zero.

A visited-remainder set could stop exactly at repetition, but the mathematical bound lets the source use constant space instead.

The returned value is the length counter, not the repunit or its remainder. Once zero appears, the potentially enormous numeric candidate is no longer needed because the problem asks only how many digits it has.

## Complexity detail

The loop performs at most `k` constant-size remainder updates under the usual machine-integer model, so time is $O(K)$.

Only `x`, `ans`, and the loop counter are stored. Auxiliary space is $O(1)$; the enormous conceptual repunit is never allocated.

## Alternatives and edge cases

- **Construct the actual integer:** Its digit count can be proportional to `k`, causing expensive big-integer operations and storage.
- **Store visited remainders:** This detects cycles explicitly in $O(K)$ space, but the fixed $K$-step bound makes it unnecessary.
- **Reject only even `k`:** That is exactly what the source does initially; odd multiples of five are rejected after the loop.
- **Early reject `k%5==0`:** This would be a valid constant-time optimization, but it is absent from the exact source.
- **Check remainder before extending:** It would be needed if `k=1` were legal; for `k>=2`, initialization cannot already be zero.
- **`k=2`:** Immediate even-divisor rejection returns `-1`.
- **`k=5`:** The loop never reaches zero because every repunit ends in one.
- **`k=3`:** Remainders lead to length three.
- **Repeated remainder:** It proves future evolution cycles because the update is deterministic.
- **First zero:** Increasing length order guarantees minimality.
- **No integer overflow:** Only remainders below `k` are retained.
- **Constant memory:** No candidate string or visited table is built.
