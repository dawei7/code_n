## General

One call to `rand7()` has only seven outcomes, so it cannot directly supply ten equally likely results. Two independent calls have $7\cdot7=49$ equally likely ordered pairs. The exact solution maps those pairs to uniform integers from 1 through 49, keeps the largest prefix whose size is divisible by 10, and retries whenever the pair falls outside that prefix.

This technique is rejection sampling: discard outcomes that would make equal grouping impossible, then map accepted outcomes evenly to the desired range.

**Create 49 equiprobable cells**

The first call is converted from `1..7` to `0..6`:

`i = rand7() - 1`.

The second call remains `j` in `1..7`. The expression

$$
x=7i+j
$$

maps each ordered pair uniquely to an integer in `1..49`.

For `i = 0`, results are `1..7`; for `i = 1`, they are `8..14`; and so on through `43..49` for `i = 6`. Because the two `rand7()` calls are independent and uniform, every pair has probability $1/49$, and therefore every `x` is equally likely.

**Why only 1 through 40 are accepted**

Ten output values need equal-sized groups. Forty is the largest multiple of 10 not exceeding 49. Accepting `x <= 40` gives exactly 40 equiprobable cells, which can be divided into ten groups of four.

Values `41..49` cannot be distributed equally among ten outputs. Returning something for them would make some outputs more likely than others, so the loop rejects those nine cells and draws a fresh independent pair.

Conditioning on acceptance preserves equality: each accepted cell originally had the same probability, so after ignoring rejected trials each still has probability $1/40$ within the accepted trial.

**Map accepted cells to 1 through 10**

The code returns

`x % 10 + 1`.

Across `x = 1..40`, each remainder from zero through nine occurs exactly four times. Remainder zero comes from `10,20,30,40` and maps to output one. Remainder one comes from `1,11,21,31` and maps to output two. Continuing this pattern, every output from 1 through 10 receives four cells and therefore probability $4/40=1/10$.

The mapping is rotated compared with the common formula `(x - 1) % 10 + 1`, but rotation does not affect uniformity.

**Why retries do not bias later output**

Every loop iteration uses a new independent pair. Rejection reveals only that the previous pair was among `41..49`; it gives no information about the next pair. On whichever iteration first succeeds, its accepted `x` is uniform over `1..40`, so the returned value is uniform over `1..10`.

The probability of rejecting forever is zero under the random API because each attempt succeeds with probability $40/49>0$. There is no finite worst-case number of calls, but termination occurs almost surely.

**Expected number of calls**

An attempt uses exactly two `rand7()` calls and succeeds with probability $40/49$. The expected number of attempts for a geometric distribution is

$$
\frac{1}{40/49}=\frac{49}{40}.
$$

Therefore the expected number of `rand7()` calls per `rand10()` result is

$$
2\cdot\frac{49}{40}=\frac{49}{20}=2.45.
$$

This is slightly above the unavoidable minimum of two calls because some pairs must be discarded.

**Native and deterministic app behavior**

The native method takes no arguments and calls the platform-provided random API. The app adapter supplies a deterministic cyclic stream only to reproduce the same control flow during tests. Its contract requires that the stream eventually produce an accepted pair for every requested output; otherwise this same rejection loop would continue forever.

## Complexity detail

For one native `rand10()` call, expected time is $O(1)$ because the expected attempt count is $49/40$. The worst-case running time is unbounded: random draws may reject any finite number of times, although the probability of infinite rejection is zero. Auxiliary space is $O(1)$.

For an app trace requesting $D$ outputs, expected generation time is $O(D)$, and the returned output list uses $O(D)$ space. Those are the `draws`-based manifest bounds; the random-generation state itself remains constant space.

The analysis assumes independent uniform `rand7()` calls, exactly as the native API promises.

## Alternatives and edge cases

- **Modulo a single `rand7` result:** Seven source outcomes cannot produce ten values at all.
- **Use two draws and take modulo 10 without rejection:** Forty-nine is not divisible by ten, so nine outputs would create uneven remainder frequencies and bias the result.
- **Reuse rejected entropy:** Values `41..49` form nine uniform states that can be combined with another `rand7()` call, then further leftovers can be reused. This lowers the expected call count to about 2.193, but the exact source uses simpler two-draw rejection.
- **Built-in random API:** Forbidden by the contract; all entropy must come from `rand7()`.
- **Long rejection streak:** Valid and possible, so worst-case time is not finite even though expected time is constant.
- **Deterministic adapter stream:** It must eventually enter `1..40` pairs, as the local contract states.
- **Endpoint `x = 40`:** Accepted because it completes the fourth cell for one output class.
- **Endpoint `x = 41`:** Rejected because accepting any of `41..49` would make equal ten-way grouping impossible.
- **Independence assumption:** Correlated `rand7()` results would invalidate the 49-cell uniformity proof; the provided API guarantees independent uniform draws.
