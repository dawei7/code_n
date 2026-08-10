## General

**Construct repunits through their remainders**

A positive integer containing only digit one is a repunit:

`R_1 = 1, R_2 = 11, R_3 = 111`, and so on.

The numbers grow too large to store for large lengths, but divisibility by `k` depends only on the remainder modulo `k`.

Appending one digit to decimal number `R` gives `10R + 1`. Therefore, if `r` is `R % k`, the next remainder is:

`(10r + 1) % k`.

This recurrence lets the algorithm test arbitrary repunit lengths while every stored value stays below `k`.

**Initialize the length-one remainder**

`n = 1 % k`

is the remainder of the one-digit repunit. The loop variable `i` runs from one through `k` and represents the length associated with the current remainder `n`.

At the start of each iteration, if `n == 0`, the length-`i` repunit is divisible by `k` and the method returns `i`.

Only after the check does it update `n` to the remainder for length `i + 1`.

For `k = 1`, initialization yields zero and the first iteration immediately returns one.

**Why the first zero remainder gives the smallest length**

Lengths are tested strictly in increasing order: one, two, three, and so on. The method returns at the first zero remainder.

No shorter repunit was divisible—otherwise an earlier iteration would already have returned. Thus the returned length is minimal, not merely some working length.

**Why checking at most `k` lengths is enough**

There are exactly `k` possible remainders modulo `k`: zero through `k - 1`.

If none of the first `k` repunits has remainder zero, all `k` observed remainders are nonzero but there are only `k - 1` nonzero values. By the pigeonhole principle, some remainder repeats.

The transition from one remainder to the next is deterministic. Once a remainder repeats, all future remainders repeat the same cycle. Since zero did not occur before the cycle repeated, it will never occur later.

Therefore, failure within the first `k` lengths proves no answer exists, and the method returns `-1`.

**Trace `k = 3`**

- Length one: remainder of one is one.
- Update to length two: `(1 * 10 + 1) % 3 = 2`.
- Length two is not divisible.
- Update to length three: `(2 * 10 + 1) % 3 = 0`.
- At iteration three, zero is detected and the method returns three.

The actual value 111 need never be stored.

**Why factors two and five make a solution impossible**

Every repunit ends in digit one. It is never even and never ends in zero or five. Therefore, no repunit is divisible by two or five.

The code does not special-case these factors. Their remainder sequences fail to reach zero within `k` steps, so the general pigeonhole loop returns `-1`.

Conversely, when `k` is coprime with ten, a repunit divisible by `k` exists; the bounded remainder process finds its smallest length.

**Modular replacement does not change future behavior**

Suppose the real repunit `R` and stored `r` satisfy `R \equiv r \pmod{k}`. Multiplying both by ten and adding one preserves congruence:

`10R + 1 \equiv 10r + 1 \pmod{k}`.

Taking the new remainder therefore produces exactly the same divisibility state as constructing the full next repunit. Induction proves every stored `n` is the correct remainder for its stated length.

**Understand the final update on iteration `k`**

If length `k` is not divisible, the body computes the remainder for length `k + 1`, but the loop then ends and returns `-1` without checking it.

This extra constant-time update is harmless. The pigeonhole argument already proves no later zero can appear once all first `k` lengths failed.

**Why a seen set is unnecessary**

One could store every visited remainder and return `-1` when one repeats. The bounded for-loop obtains the same guarantee from the pigeonhole principle and uses constant auxiliary space.

**The loop invariant**

At the start of iteration `i`, `n` equals `R_i % k`. The zero test therefore answers exactly whether the length-`i` repunit is divisible. If not, the recurrence computes `R_{i+1} % k`, preserving the invariant.

Together with increasing lengths and the bounded-cycle proof, this establishes both correctness and termination.

## Complexity detail

The loop executes at most `k` iterations, each using constant-time arithmetic on values below `k` under the usual integer model. Time complexity is `O(k)`.

Only the current remainder and loop index are stored, so auxiliary space is `O(1)`. The potentially enormous repunit itself is never constructed.

## Alternatives and edge cases

- **Explicit factor check:** Return `-1` immediately when `k` is divisible by two or five, then run the remainder loop. It saves work on impossible cases but is not required.
- **Seen-remainder set:** Detect a repeated remainder directly. It uses `O(k)` space instead of relying on a fixed `k`-iteration bound.
- **Construct the full integer:** Repeatedly compute `value = value * 10 + 1`. Arbitrary-precision values become enormous and make arithmetic unnecessarily expensive.
- **`k = 1`:** The initialized remainder is zero, so length one is returned.
- **`k = 2` or `k = 5`:** No repunit can be divisible because its final digit is one; return `-1` after the bounded loop.
- **First zero at length `k`:** The zero check occurs before the final update, so that valid boundary case is returned.
- **Repeated nonzero remainder:** It proves the deterministic sequence has entered a cycle that cannot later reach zero.
- **Large `k`:** Memory remains constant and the loop performs at most one hundred thousand iterations.
- **Smallest requirement:** Increasing iteration order guarantees the first returned length is minimal.
