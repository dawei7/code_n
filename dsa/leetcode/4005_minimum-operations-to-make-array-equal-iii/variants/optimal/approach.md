## General

**First understand the cost of changing one value into a chosen target.**  Fix a target `t > 1` and an original value `x`.

- If `x == t`, the cost is `0`.
- If `x` divides `t`, multiply `x` by `t / x`. For unequal values this factor is at least two, so the cost is `1`.
- If `t` divides `x`, divide `x` by `x / t`. For unequal values, the factor is at least two; because `t > 1`, the factor is also strictly smaller than `x`. The cost is `1`.
- If neither value divides the other, the cost is `2`.

The last case is always achievable when both values exceed one. Multiply `x` by `t` to obtain `xt`, then divide by `x` to obtain `t`. The multiplication factor `t` is at least two, and the later division factor `x` is at least two and strictly smaller than `xt`.

Value `1` fits the one-step multiplication case because `1` divides every `t > 1`.

Target `1` is special. A value greater than one can never become one: a legal division factor must be strictly smaller than the current value, so the quotient remains greater than one, while multiplication only increases the value. Thus target one works only when every input is already one. The early “one distinct value” return handles that situation, and the later target loop correctly ignores `1`.

**Only existing targets can improve on a simple baseline.**  If a target `t` is not present in `nums`, no element has zero cost. Every element needs at least one operation, so the total cost is at least `n`.

A cost of `n` is always achievable for some common multiple: choose a multiple strictly larger than every input and multiply each value to it in one operation. Therefore, the best non-present target costs exactly `n` in the only sense relevant to minimization: no non-present target can beat `n`, and at least one reaches it.

This explains the source's initialization

`answer = n`.

It is not an arbitrary upper bound. It represents the best possible category of targets absent from the input. To find an answer below `n`, it is enough to evaluate targets that already appear and can give their own occurrences zero cost.

**Express the cost for an existing target through two occurrence counts.**  Start from a hypothetical cost of two operations for every element, totaling `2n`.

For a fixed existing `target > 1`:

- every occurrence whose value is a multiple of `target` needs at most one operation, saving one from the baseline;
- every occurrence whose value is a divisor of `target` also needs at most one operation, saving one;
- occurrences equal to `target` belong to both sets, so they save two and correctly have cost zero;
- values with neither divisibility relation remain at cost two.

Let:

- `multiples[target]` be the number of array occurrences whose values are multiples of `target`;
- `divisors_present[target]` be the number of array occurrences whose values divide `target`.

Then the exact cost is

`2 * n - multiples[target] - divisors_present[target]`.

The double counting at equality is intentional and is what changes cost two into cost zero.

**Compress duplicates before doing number theory.**  `frequency = Counter(nums)` stores each distinct value once with its occurrence count. Let `U` be the number of distinct values. Factorization and divisor generation then happen once per distinct value rather than once per array occurrence.

If `U == 1`, all elements are already equal and the source returns zero before any sieve work.

**Generate enough primes for every factorization.**  Let `V = max(nums)` and `limit = isqrt(V)`. Any composite remainder has a prime factor at most its square root, so primes through `sqrt(V)` are sufficient.

The byte array `is_prime` begins with every position marked and clears zero and one. The sieve clears multiples starting at `value * value`. The remaining marked positions form the `primes` list.

For one distinct `value > 1`, the source divides out each applicable prime and records `(prime, exponent)`. Once `prime * prime > remaining`, no further small factor is possible. If `remaining > 1` afterward, it is itself a final prime factor with exponent one.

**Generate every divisor from the prime factorization.**  Begin with `divisors = [1]`. For a factor `p^e`, copy the divisors formed from earlier primes, then extend the list with each old divisor multiplied by `p, p^2, ..., p^e`. This generates every divisor exactly once.

The source uses that list in two complementary ways.

First:

`divisors_present[value] = sum(frequency.get(divisor, 0) for divisor in divisors)`.

This counts all array occurrences whose values divide the current `value`. The count includes `1` when present and includes the current value itself.

Second, for every generated `divisor` that is itself present and greater than one:

`multiples[divisor] += count`.

Here `count` is the frequency of the current `value`. Since the current value is a multiple of each of its divisors, this adds all its occurrences to the correct multiple counters. Divisor one is skipped because target one is not legal for mixed input and is never evaluated.

After all distinct values have contributed, the source evaluates every present target greater than one with the cost formula and takes the minimum with the non-present-target baseline `n`.

**Walk through the first example.**  For `[6, 12, 8]` and target `6`:

- `multiples[6] = 2` because `6` and `12` are multiples of six;
- `divisors_present[6] = 1` because only the present value six divides six.

The formula gives

`2 * 3 - 2 - 1 = 3`.

This corresponds to zero operations for `6`, one division for `12`, and two operations for `8`.

For `[5, 15, 20]` and target `5`, all three values are multiples of five while only five is a present divisor of itself. The cost is `6 - 3 - 1 = 2`.

**Why the final minimum covers every possible target.**  Target one is either handled by the all-equal early return or impossible. Every target greater than one is either present or absent. Present targets are evaluated exactly by divisibility counts. Absent targets cannot cost below `n`, and `answer = n` covers their best attainable value. No other target category remains.

## Complexity detail

Let:

- `n` be the input length;
- `U` be the number of distinct values;
- `V = max(nums)`;
- `D` be the total number of divisors generated across distinct values;
- `P` denote the sieve work through `sqrt V`.

Building `Counter(nums)` and finding `max(nums)` take `O(n)` time. The sieve takes `O(P)` time. Trial factorization has the manifest's safe loose bound `O(U\sqrt V)`, and divisor generation plus the two divisor scans take `O(D)`.

- Total time complexity is `O(n + P + U\sqrt V + D)`.
- Auxiliary space complexity is `O(\sqrt V + U)`.

The manifest lists `O(P + U\sqrt V + D)` time, but the exact implementation must also read all `n` entries to build the frequency map and later calls `max(nums)`. When `n` is much larger than `U` because of duplicates, that `O(n)` term is real and should be stated explicitly.

The sieve byte array and prime list use `O(\sqrt V)` space. `frequency`, `multiples`, and `divisors_present` use `O(U)`. Only one distinct value's divisor list is held at a time; its size is covered by the stated bound for the supported range.

## Alternatives and edge cases

- **Try every integer target:** Targets are unbounded because multiplication can grow values arbitrarily. The absent-target baseline and exact evaluation of present targets reduce the search to `U` candidates.
- **Compute pairwise transformation costs:** Comparing every value with every target takes `O(U^2)` divisibility checks. Divisor enumeration aggregates both directions more efficiently.
- **Use a greatest common divisor only:** Sharing a common factor is not the same as one value dividing the other. Unrelated values still need two operations even when their gcd exceeds one.
- **Prime-factor distance:** One operation may multiply or divide by a composite integer, so counting individual prime additions/removals would overestimate the cost.
- **All values already equal:** The early return gives zero, including the all-ones case.
- **Mixed input containing one:** One can multiply one directly to any target greater than one in a single operation. It is counted as a present divisor of every target.
- **Trying to make mixed input equal to one:** This is impossible because legal division can never reduce a value greater than one to one.
- **Target absent from the input:** Every element costs at least one operation, so such a target cannot beat `n`. A sufficiently large common multiple attains the `n` baseline.
- **Target equal to an input value:** Its own occurrences must cost zero. Their presence in both the multiple and divisor counts supplies the required two-unit reduction.
- **One-way divisibility:** If `x` properly divides `target`, multiplication costs one. If `target` properly divides `x`, legal division costs one. The two aggregate maps count these directions separately.
- **No divisibility relation:** For `x, target > 1`, multiply to `x * target` and divide by `x`, proving the two-operation upper bound.
- **Duplicate values:** `Counter` prevents repeated factorization, while all formulas use frequencies so every array occurrence still contributes to the cost.
- **Prime input values:** Factorization leaves the prime as `remaining`, and divisor generation correctly produces `1` and the value itself.
- **Value one during factorization:** It is skipped because its only divisor is one and it cannot be a mixed-input target. Its frequency is still found through `frequency.get(1, 0)` when counting divisors of other targets.
- **Large maximum value:** Only primes through `sqrt V` are sieved. Any leftover factor after trial division is prime.
- **Input preservation:** The source builds derived counters and never mutates `nums`.
- **Manifest time bound:** The number-theory terms are correct for the distinct-value work, but a complete bound for the exact source also includes the initial `O(n)` scans.
