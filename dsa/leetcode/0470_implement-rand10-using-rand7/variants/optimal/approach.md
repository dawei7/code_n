## General

**Create 49 equally likely cells**

Call `rand7()` twice. Treat the first result minus one as a zero-based row and the second result as a one-based column, so `cell = (first - 1) * 7 + second` ranges from `1` through `49`. Independence and uniformity of the two API calls make all 49 cells equally likely.

**Retain a multiple of ten outcomes**

Accept cells `1` through `40` and reject `41` through `49`. Among the accepted cells, every residue modulo 10 occurs exactly four times. The expression `1 + (cell - 1) % 10` therefore maps the accepted sample uniformly to `1` through `10`. Mapping all 49 cells directly would bias nine outputs because 49 is not divisible by 10.

After rejection, draw a fresh independent pair and repeat. An attempt succeeds with probability $40/49$, so the expected attempt count is $49/40$. Every attempt makes two `rand7()` calls, giving an expected $49/20 = 2.45$ calls for each native `rand10()` result.

**Use the same control flow in the deterministic adapter**

The app-local `rand7()` reads `rand7_values` cyclically through `stream_index`; this makes accepted cells, rejections, and outputs reproducible. Its nested `rand10()` performs exactly the native cell construction and rejection rule. The outer list comprehension invokes it `draws` times and retains the resulting trace.

## Complexity detail

Each native output requires a constant expected number of attempts, so generating `draws` results takes expected $O(\texttt{draws})$ time. Rejection sampling has no finite worst-case call bound under genuine randomness. The returned app trace occupies $O(\texttt{draws})$ space, while one native `rand10()` call uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recycle rejected entropy:** cells `41` through `49` can be combined with another `rand7()` call, retaining 60 of 63 outcomes and then 20 of a possible 21, which lowers the expected API-call count at the cost of more bookkeeping.
- **Generate a larger base-7 range:** using more calls and rejecting down to a multiple of ten remains unbiased but changes the expected call count.
- **Take every cell modulo 10:** is invalid because 49 equiprobable cells cannot be divided equally among ten outputs.
- **Boundary cell `40`:** is accepted and maps to `10`.
- **Cells `41` through `49`:** trigger a fresh attempt rather than an output.
- **Empty deterministic stream:** violates the app contract because cyclic access requires at least one value.
- **Perpetually rejected deterministic cycle:** violates the app contract and would never finish the requested trace.
- **Independent native calls:** are required by the uniformity proof; cycling is solely an app test-harness device.
