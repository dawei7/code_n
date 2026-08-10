## General

**Create large distinct differences first, then repeat one**

The output must be a permutation of one through `n`, and adjacent absolute differences must contain exactly `k` distinct values.

Alternating between the smallest and largest unused numbers creates a predictable descending sequence of large differences. Once enough distinct differences have been created, consuming the remaining consecutive numbers from one side produces only difference one repeatedly.

The exact solution maintains the unused interval `[l, r]`, initially `[1, n]`.

**The alternating first phase**

For exactly `k` iterations:

- on even iteration `i`, append `l` and increment `l`;
- on odd iteration `i`, append `r` and decrement `r`.

The sequence begins:

`1, n, 2, n - 1, 3, n - 2, ...`.

Among these first `k` elements, adjacent differences are:

`n - 1, n - 2, n - 3, ..., n - k + 1`.

There are `k - 1` of these when `k > 1`, and they are all distinct.

Why does each decrease by one? The chosen low endpoint increases by one whenever it is used, and the chosen high endpoint decreases by one whenever it is used. The distance across the remaining interval therefore shrinks by exactly one on each alternating step.

**The monotonic second phase**

After `k` alternating choices, all unused values form one consecutive interval from `l` through `r`.

The direction used to consume that interval depends on the parity of `k`:

- if `k` is even, the last alternating value came from the high side, so append remaining values from `r` downward;
- if `k` is odd, the last alternating value came from the low side, so append remaining values from `l` upward.

The first tail value differs from the last alternating value by exactly one. Every later tail step also differs by one because it moves through consecutive integers.

Thus the entire second phase contributes only the distinct difference one.

**Why there are exactly `k` differences**

The alternating phase contributes the `k - 1` distinct values:

`n - 1` down through `n - k + 1`.

Because the constraint says `k < n`, the smallest of these is at least two. Therefore, none equals the tail's difference one.

Adding difference one gives exactly:

`(k - 1) + 1 = k`

distinct adjacent differences.

When `k = 1`, the alternating phase contains only the first value and contributes no adjacent difference. The tail is a simple increasing sequence with every difference equal to one, so the same conclusion holds.

**A walkthrough with even `k`**

For `n = 7` and `k = 4`, the alternating phase produces:

`1, 7, 2, 6`.

Its differences are six, five, and four. Four is even, so the remaining interval is consumed from the high side:

`5, 4, 3`.

The full answer is `[1, 7, 2, 6, 5, 4, 3]`. Its differences are:

`[6, 5, 4, 1, 1, 1]`,

whose distinct set has exactly four values.

**A walkthrough with odd `k`**

For `n = 7` and `k = 3`, the first phase gives `[1, 7, 2]` with differences six and five. Since `k` is odd, consume the remaining low side upward:

`[3, 4, 5, 6]`.

All added differences are one, so the distinct set is `{6, 5, 1}`, exactly three values.

**Why the output is a permutation**

Each first-phase operation removes one endpoint from the unused interval. Low-side and high-side selections cannot overlap while values remain because `k < n` ensures the construction has enough distinct numbers.

After the first phase, the second loop consumes every value in the remaining interval exactly once from one direction. No previously used endpoint lies inside that interval.

Therefore, the output has length `n`, contains only values one through `n`, and contains no duplicate. It is a valid permutation.

**Why the parity rule matters**

If the last first-phase value came from the low side but the tail began from the high side, the boundary could introduce another large difference not already controlled. Continuing from the same side as the most recent choice makes the next unused value adjacent numerically, guaranteeing difference one.

The parity of the number of first-phase choices identifies which side supplied the final value.

**Why construction beats search**

The problem accepts any valid answer. There is no need to enumerate permutations or test difference sets. The endpoint pattern proves the desired properties in advance and writes one answer directly.

## Complexity detail

The two loops append exactly `n` values in total. Each iteration performs constant-time arithmetic and one list append, so running time is `O(N)`.

The returned list contains `N` integers and therefore uses `O(N)` output space. Excluding required output, the algorithm stores only `l`, `r`, and loop indices, so auxiliary working space is `O(1)`.

The manifest lists `O(N)` space, which includes the returned permutation. Both descriptions are compatible once output-space convention is stated.

## Alternatives and edge cases

- **Increasing prefix plus alternating suffix:** Write `1` through `n - k - 1` in order, then alternate endpoints of the remaining `k + 1` values. This is the editorial construction and also gives `O(N)` time.

- **Backtracking over permutations:** It can test difference counts but has factorial search space and ignores the direct construction.

- **Random shuffling:** Finding a valid permutation by chance offers no guarantee and makes correctness difficult to prove.

- **`k = 1`:** The exact output becomes `[1, 2, ..., n]`, whose only distinct difference is one.

- **`k = n - 1`:** Alternation creates differences `n - 1` down to two, and the final remaining value adds one. Every possible positive difference appears exactly once as a distinct value.

- **Smallest valid `n = 2`:** Necessarily `k = 1`, and the construction returns `[1, 2]`.

- **Repeated difference one:** Repetition is allowed. The requirement counts distinct values, not how many times each difference occurs.

- **Permutation uniqueness:** The answer itself must use each number once, but adjacent differences are allowed to repeat.

- **Wrong tail direction:** It can introduce an unintended new difference. The parity-based direction ensures the boundary and tail all use one.

- **Run the first phase `k + 1` times:** That would create `k` large differences before the tail and then potentially add one more distinct value. The exact phase length of `k` is intentional.

- **Values outside one through `n`:** Endpoint pointers begin at those limits and move inward, so the construction cannot produce an out-of-range number.

- **Multiple valid answers:** The contract permits any one. This deterministic pattern is easy to verify and reproduce.

- **Absolute differences:** Direction changes do not make differences negative; the proof uses magnitudes of endpoint gaps.
