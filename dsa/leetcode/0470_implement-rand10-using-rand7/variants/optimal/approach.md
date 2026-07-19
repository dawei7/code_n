## General
**Create 49 equally likely outcomes**

Call `rand7()` twice. Treat the first result minus one as a base-7 row and the second as a column, producing `cell = (first - 1) * 7 + second`. Independence and uniformity make every integer from 1 through 49 equally likely.

**Keep a multiple of ten outcomes**

Accept cells 1 through 40 and reject 41 through 49. Each residue class modulo 10 then has exactly four accepted cells, so `1 + (cell - 1) % 10` is uniform on 1 through 10. Mapping all 49 cells directly would bias nine outputs because 49 is not divisible by 10.

**Repeat only after rejection**

Rejected cells reveal no accepted output and are discarded before drawing a fresh independent pair. An attempt succeeds with probability $40/49$, so the expected attempts per result are $49/40$, a constant.

**Make randomized behavior testable in the app**

The app adapter reads authored `rand7_values` cyclically, which makes rejection paths and outputs deterministic. It runs the same cell construction and rejection logic as the native method; only the source of `rand7()` calls differs.

## Complexity detail
Each output needs a constant expected number of attempts, so generating `draws` results takes expected $O(draws)$ time. The returned trace occupies $O(draws)$ space; one native `rand10()` call uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Recycle rejected entropy:** cells 41 through 49 can be combined with another `rand7()` call to reduce expected API calls, but the bookkeeping is more involved.
- **Generate a larger base-7 range:** using more calls and rejecting down to a multiple of ten remains unbiased with different efficiency.
- **Modulo all 49 cells:** is invalid because output frequencies are unequal.
- **Boundary cell 40:** is accepted and maps to 10.
- **Cells 41 through 49:** must trigger a fresh attempt rather than an output.
- **Independent calls:** the uniformity proof assumes each provided `rand7()` call is independent and uniform.
- **Deterministic app stream:** cycling is a test harness device, not part of the native randomized API.
