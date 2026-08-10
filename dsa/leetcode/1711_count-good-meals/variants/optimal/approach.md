## General

**Count partners that appeared earlier**

A good meal consists of two different indices whose values sum to a power of two. The source scans `deliciousness` from left to right and maintains `cnt`, a `Counter` of values at earlier indices.

When the current value is `d` and the target power is `s`, the needed earlier value is uniquely

`s - d`.

`cnt[s - d]` tells how many earlier items have that value. Each one forms a different index pair with the current item, so the count is added to `ans`.

Only after checking all target powers does the source execute `cnt[d] += 1`. This order prevents the current item from pairing with itself while still allowing equal-valued items at different indices to pair.

**Why each unordered pair is counted once**

Take any two indices `i < j`. The item at `i` enters `cnt` after its iteration. When `j` becomes current, the algorithm considers every relevant power of two and counts `i` if their sum matches one.

The pair was not counted at `i` because `j` had not been inserted yet, and it will never be counted again because later iterations use a different current index. Thus chronological processing gives every unordered index pair exactly one opportunity.

If several earlier indices share the complement value, `Counter` stores their multiplicity. Adding that multiplicity counts each distinct choice of earlier food, as the contract requires.

**Enumerate every possible power-of-two sum**

The target `s` starts at one, which is $2^0$. Each `s <<= 1` doubles it, producing one, two, four, eight, and so on with no gaps or non-powers.

All deliciousness values are nonnegative. Let `M = max(deliciousness)`. Any two values sum to at most $2M$, so no achievable target power can exceed that bound. The source computes `mx = M << 1`, exactly $2M$, and continues while `s <= mx`.

Therefore the loop includes every power of two that any pair could reach and excludes larger targets that no pair could reach.

When `s - d` is negative, no nonnegative earlier value can match it. Python's `Counter` returns zero for the absent negative key, so no separate lower-bound test is needed.

**The all-zero case**

If every value is zero, `M=0` and `mx=0`. The inner loop starts at `s=1` and does not run. The method returns zero, correctly recognizing that zero plus zero is zero, not a power of two.

This also explains why the upper bound being below the first power causes no special failure.

**Trace repeated values**

For `[1,1,1,3,3,3,7]`:

- The first one has no earlier complement.
- Each later one can pair with earlier ones to make two. Their contributions are one and two, totaling three `(1,1)` pairs.
- When each three is processed, target four needs complement one. All three ones are already counted, so the three occurrences of value three contribute three each, totaling nine.
- Value seven considers target eight and finds three earlier ones, adding three.

The total is fifteen. Items with equal values are not deduplicated because `cnt` stores occurrence counts.

**Why the power loop does not double-count a pair**

A fixed pair has one fixed sum. A positive integer cannot equal two different powers of two, so at most one iteration of `s` counts that pair. Iterating several target powers is therefore exhaustive without overlap.

**Maintain the answer modulo the required constant**

The number of index pairs can be large. After each contribution, the source computes

`ans = (ans + cnt[s - d]) % mod`

with `mod = 10**9 + 7`. Modular addition is compatible with the final required remainder: reducing after each step produces the same final value as summing all pairs first and reducing once.

Python itself does not overflow, but regular reduction keeps `ans` bounded and directly implements the contract.

**Why the algorithm is correct**

Before processing current index `j`, `cnt[v]` equals the number of indices `i < j` with value `v`. For every attainable power `s`, exactly those earlier indices with value `s - d` form a good pair ending at `j`, and the algorithm adds their number.

Every good pair has one later endpoint and a power-of-two sum within the enumerated range, so it is included. No invalid pair is included because the complement equation guarantees the sum, and no pair repeats because only the later endpoint counts it. Updating `cnt` preserves the invariant for the next index.

## Complexity detail

Let $n$ be the number of items and $B$ be the number of powers of two no greater than twice the maximum value. The outer loop runs $n$ times and the inner loop runs $B$ times, giving $O(nB)$ expected time with constant-time `Counter` access.

Under the constraint `deliciousness[i] <= 2^{20}`, at most the powers from $2^0$ through $2^{21}$ are examined, so $B\le22$. It is a small fixed bound, making runtime effectively linear in $n$, while the manifest keeps the bit-range factor explicit.

`cnt` stores at most one entry per distinct value seen, no more than $n$, so auxiliary space is $O(n)$. The remaining variables are scalar.

## Alternatives and edge cases

- **Check every pair:** Test all $n(n-1)/2$ index pairs directly. It is simple but costs $O(n^2)$ time.
- **Sort and use two pointers per power:** It can count pairs but requires careful duplicate multiplicities and repeats a scan for each target power.
- **Precompute power list:** Store all relevant powers once instead of shifting `s` inside each outer iteration. It uses constant bounded extra space and similar complexity.
- **Two equal values:** They can form a meal when twice the value is a power of two; insertion after counting ensures distinct indices.
- **Current item pairing with itself:** Impossible because `cnt[d]` is incremented only after searches.
- **Duplicate items:** Counter multiplicity counts every distinct index combination.
- **Zero deliciousness:** It can pair with a positive power-of-two value; two zeros do not form a good meal.
- **Target one:** Starting `s` at one includes meals whose sum is $2^0$.
- **Maximum possible sum:** `s <= mx` includes a power equal to twice the maximum.
- **Negative complement:** Counter lookup returns zero because input values are nonnegative.
- **Single item:** No earlier partner exists, so the answer remains zero.
- **Modulo arithmetic:** Reducing after every addition preserves the required final remainder.
- **Power uniqueness:** A pair's sum can match at most one power, preventing duplication across inner-loop iterations.
