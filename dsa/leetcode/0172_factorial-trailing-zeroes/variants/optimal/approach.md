## General

**Count factors that create tens**

A decimal trailing zero is produced by a factor of ten, and:

$$
10=2\cdot5.
$$

Therefore the number of trailing zeros in $n!$ is the number of pairs of prime
factors two and five in its complete factorization.

There are always more factors of two than factors of five in a factorial:
every second number contributes a two, while only every fifth number
contributes a five; higher powers of two are also more frequent than
corresponding powers of five. The scarce factor is five, so counting all
factors of five gives the answer.

The method never calculates the enormous factorial itself.

**Count first factors of five**

Every multiple of five contributes at least one factor five. The number of
multiples of five from one through `n` is:

$$
\left\lfloor\frac{n}{5}\right\rfloor.
$$

This count includes 5, 10, 15, 20, 25, and so on. However, it counts 25 only
once even though $25=5^2$ contributes two factors. Additional terms are needed
for these repeated factors.

**Count extra factors from higher powers**

Every multiple of 25 contributes a second factor five, so add
$\lfloor n/25\rfloor$. Every multiple of 125 contributes a third factor, so
add $\lfloor n/125\rfloor$. Continue for every power of five:

$$
\left\lfloor\frac{n}{5}\right\rfloor+
\left\lfloor\frac{n}{25}\right\rfloor+
\left\lfloor\frac{n}{125}\right\rfloor+\cdots.
$$

Once a power exceeds `n`, its quotient and every later quotient are zero.

The selected source generates the same series by repeatedly replacing `n`
with `n // 5` and adding that quotient to `ans`. After one division the value
is $\lfloor n/5\rfloor$; after two it is $\lfloor n/25\rfloor$, and so on.

**Trace a small factorial**

For `n = 5`, the first division changes five to one and adds one. The next
division changes one to zero and adds zero. The answer is one, matching
$5!=120$.

For `n = 3`, the first division immediately produces zero, so the answer
remains zero.

For `n = 25`, the successive quotients are five, one, and zero. Their sum is
six. Multiples 5, 10, 15, 20, and 25 contribute five first factors, while 25
contributes one additional factor.

For `n = 100`, the nonzero terms are 20 and 4, yielding 24 trailing zeros.
There is no contribution from 125 because it exceeds the input.

**Why repeated division preserves floors**

For nonnegative integers:

$$
\left\lfloor
\frac{\left\lfloor n/5\right\rfloor}{5}
\right\rfloor
=
\left\lfloor\frac{n}{25}\right\rfloor.
$$

The same identity extends to later divisions. Integer division at each step
therefore produces exactly the desired count for the next power, not an
approximation.

The source mutates only its local parameter variable `n`; integers are
immutable, so the caller's original value is unaffected.

**Why counting five factors is sufficient**

Among numbers one through `n`, every multiple of ten itself contributes both a
two and a five. Additional even numbers, powers of two, and even multiples of
five provide still more twos. Formally, for every positive power, there are at
least as many multiples of $2^k$ as of $5^k$.

Thus every counted factor five can pair with a distinct factor two. No five is
left unmatched because of too few twos, and the number of pairs equals the
sum.

**Handle zero factorial**

The mathematical value $0!$ is one, whose decimal representation has no
trailing zero. With input zero, the loop condition `while n` is false
immediately and returns zero.

Notice that the returned count concerns digits at the end only. Zero digits
inside the decimal expansion of the factorial do not correspond to additional
complete factors of ten at its lowest decimal positions and must not be
counted.

## Complexity detail

Each iteration divides `n` by five. The number of positive quotients is
$\lfloor\log_5 n\rfloor+1$ for positive `n`, so time is $O(\log n)$.

The method stores only `ans` and the shrinking integer. Auxiliary space is
$O(1)$. These bounds match the manifest and the logarithmic follow-up.

## Alternatives and edge cases

- **Explicit powers of five:** Maintain `power = 5`, add `n // power`, and multiply the power by five. It computes the same series without changing local `n`.
- **Compute the factorial:** Produces enormous integers and does far more work than necessary.
- **Inspect every multiple of five:** Count repeated factors in each multiple; correct but takes $O(n)$ total time.
- **Count both twos and fives:** Correct but redundant because twos are never the limiting factor.
- **`n = 0`:** Returns zero because $0!=1$.
- **`n < 5`:** No factor five appears, so the answer is zero.
- **Power of five:** Inputs such as 25 contribute an extra count at each applicable power.
- **Nonnegative guarantee:** `while n` and floor division rely on the specified domain.
- **Integer division:** `//` is essential; fractional division does not count multiples.
- **No factorial storage:** The algorithm's memory stays constant even when `n!` has many digits.
