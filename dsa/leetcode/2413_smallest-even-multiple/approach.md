## General

**The requested number is a least common multiple**

A number that is a multiple of both `2` and `n` is a common multiple. The smallest positive one is:

$$
\operatorname{lcm}(2,n).
$$

Because one input is the fixed prime number two, the least common multiple depends only on whether `n` already contains a factor of two.

**Case one: `n` is even**

If `n % 2 == 0`, then `n` is divisible by two. It is obviously also divisible by itself. Therefore, `n` is a positive common multiple of two and `n`.

No smaller positive multiple of `n` exists. Positive multiples of `n` are:

$$
n,2n,3n,\ldots
$$

and the first is `n`. Hence, returning `n` is minimal.

For `n = 6`, six is divisible by both six and two, so there is no reason to double it.

**Case two: `n` is odd**

If `n` is odd, `n` itself is not divisible by two. The positive multiples of `n` are `n, 2n, 3n, ...`. A product of odd `n` and multiplier `m` is even exactly when `m` is even.

The smallest positive even multiplier is two. Therefore, `2n` is the first multiple of `n` that is also even, and it is the smallest common multiple.

For `n = 5`, five fails the even requirement, while ten is divisible by both two and five. No positive multiple of five lies strictly between five and ten.

**How the conditional expression implements the proof**

The exact source is:

```python
return n if n % 2 == 0 else n * 2
```

`n % 2` is the remainder after division by two. Remainder zero selects the already-even case. Remainder one for a positive odd integer selects doubling.

The code needs no loop, greatest-common-divisor helper, or list of multiples because the parity proof completely characterizes the answer.

**Connection to the standard LCM formula**

In general:

$$
\operatorname{lcm}(a,b)=\frac{ab}{\gcd(a,b)}.
$$

For even `n`, $\gcd(2,n)=2$, giving:

$$
\frac{2n}{2}=n.
$$

For odd `n`, $\gcd(2,n)=1$, giving:

$$
\frac{2n}{1}=2n.
$$

The conditional is therefore a specialized constant-time evaluation of the general formula.

**Why checking only parity is enough**

Other prime factors of `n` do not matter. Every candidate must already be a multiple of `n`, so all of those factors are automatically included. The only additional requirement imposed by “multiple of two” is one factor of two.

If `n` already has it, nothing must be added. If not, multiplying once by two supplies it. Higher powers of two are unnecessary because divisibility by two requires only one.

**Minimality in both branches**

The returned value is certainly a common multiple in each branch. To prove smallest:

- when `n` is even, every positive common multiple is a positive multiple of `n` and is therefore at least `n`;
- when `n` is odd, a common multiple must be `m*n` with even positive `m`, and the smallest such `m` is two.

This rules out every smaller positive candidate rather than merely showing the returned one works.

**Why positivity matters**

The problem asks for the smallest *positive* common multiple and guarantees positive `n`. There is no ambiguity involving zero, which is divisible by every nonzero integer but is not positive. Negative multiples are also outside the requested domain.

**Prime-factor interpretation**

Write the prime factorization of `n`. If it already contains at least one factor two, its factorization already satisfies every divisibility requirement contributed by the other input `2`. The least common multiple keeps the greatest exponent required for each prime, so nothing changes. If `n` contains no factor two, it is odd; the least common multiple adds exactly one factor two and leaves every other prime exponent unchanged, producing `2n`. Adding more than one factor two or changing another prime exponent would create a larger common multiple without satisfying any new requirement.

**A compact decision table**

```text
n parity   gcd(n, 2)   lcm(n, 2)
even       2           n
odd        1           2n
```

The source's conditional expression is this table translated directly into code. Since every positive integer is exactly even or odd, the cases are exhaustive and cannot overlap.

## Complexity detail

The function performs one modulo check and at most one multiplication. Time complexity is $O(1)$.

It stores no data structure or recursion state. Auxiliary space is $O(1)$.

With `n <= 150`, doubling cannot approach overflow in any ordinary integer type. The proof also applies to larger positive integers, subject only to numeric representation limits.

## Alternatives and edge cases

- **General `lcm` helper:** Compute `2*n // gcd(2,n)`. It is correct but more machinery than a parity branch.
- **Enumerate multiples:** Test `n, 2n, 3n, ...` until finding an even one. It stops within two trials but obscures the direct proof.
- **`n = 1`:** One is odd, so the answer is two.
- **`n = 2`:** It is already a multiple of both inputs, so the answer is two.
- **Any even `n`:** Return it unchanged, including powers of two and even composites.
- **Any odd `n`:** Exactly one factor of two is needed, so return `2n`.
- **Zero:** It is not an allowed input and not a positive answer.
- **No sorting or iteration:** The result depends only on parity.
