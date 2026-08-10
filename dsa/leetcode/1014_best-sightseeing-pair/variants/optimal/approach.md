## General

**Separate the pair formula into a left and right contribution**

For `i < j`, the score is:

`values[i] + values[j] + i - j`.

Regroup it as:

`(values[i] + i) + (values[j] - j)`.

Once the right endpoint `j` is fixed, its contribution `values[j] - j` is fixed. The best partner is whichever earlier index maximizes `values[i] + i`.

This removes the need to compare `j` with every earlier position individually.

**Maintain the best left contribution seen so far**

Variable `mx` stores the maximum value of `values[i] + i` among positions available as left endpoints for a later spot.

At current `j` with value `x`:

`mx + x - j`

is the best score of any pair ending at `j`. The method uses this to update `ans`.

After evaluating `j` as a right endpoint, it updates:

`mx = max(mx, x + j)`.

Only then does current `j` become eligible as a left endpoint for future indices.

The order of these two statements is what enforces `i < j`. Updating `mx` first could allow index `j` to pair with itself.

**Why one maximum summarizes all earlier spots**

Future scores involving earlier index `i` use that index only through `values[i] + i`. Once another earlier index has a contribution at least as large, the smaller one can never be better for any future `j` because both would receive the same right contribution.

Discarding all but the maximum therefore loses no possible optimum.

**Understand the compact initialization**

The exact code starts `ans = mx = 0` and loops from index zero.

At `j = 0`, there is no legal earlier partner. The temporary candidate `0 + values[0]` may update `ans` even though it is not a real pair. The subsequent update sets `mx = values[0]`, which is the correct left contribution for index zero.

At `j = 1`, the valid pair `(0, 1)` has score

`values[0] + values[1] - 1`.

Because all values are at least one, this score is at least `values[0]`, which is at least the temporary index-zero value retained in `ans`. Thus by the first legal pair, the initialization artifact is overwritten or tied, and it cannot affect the final result.

A more conventional presentation initializes `mx = values[0]` and begins the loop at one. The protected implementation folds that setup into the general loop using the positive-value constraint.

**Trace `[8, 1, 5, 2, 6]`**

After index zero, `mx = 8`.

- At `j = 1`, the best ending score is `8 + 1 - 1 = 8`. The new left contribution `1 + 1 = 2` does not replace eight.
- At `j = 2`, the best ending score is `8 + 5 - 2 = 11`. This corresponds to pair `(0, 2)`. The new left contribution is seven, still below eight.
- At `j = 3`, the candidate is `8 + 2 - 3 = 7`.
- At `j = 4`, the candidate is `8 + 6 - 4 = 10`.

The maximum remains eleven.

**How distance is incorporated**

The term `+i` rewards a later left index, while `-j` penalizes a later right index. Together they equal `-(j - i)`, exactly the distance penalty.

No separate distance calculation is needed once the score is decomposed.

**The loop invariant after legal pairs begin**

After processing index `j`:

- `mx` is the maximum `values[i] + i` over every index from zero through `j`;
- `ans` is the maximum score among every legal pair whose right endpoint is at most `j`.

At the next index, combining its right contribution with the stored `mx` checks the best pair ending there. Taking the maximum with `ans` preserves all earlier pair results. Updating `mx` then extends the left-candidate invariant.

The base legal pair at `j = 1` establishes the answer invariant despite the compact index-zero initialization.

**Why the final answer is globally optimal**

Every legal pair has one right endpoint `j`. When the scan reaches that endpoint, `mx` is at least the left contribution of its `i`, so the computed candidate is at least that pair's score. It is also achievable by some earlier index attaining `mx`.

Therefore, the best candidate considered over all `j` equals the maximum score over all legal pairs.

## Complexity detail

Let `N` be the number of sightseeing spots.

The method performs one pass with constant arithmetic and comparisons per spot, so time complexity is `O(N)`.

Only `ans`, `mx`, the current index, and value are stored. Auxiliary space is `O(1)`.

The linear scan is asymptotically optimal because all values may influence the answer.

## Alternatives and edge cases

- **Check every pair:** Two loops directly evaluate the formula in `O(N^2)` time.
- **DP array of prefix maxima:** Store the best `values[i] + i` through each position. It is linear but uses `O(N)` space when only the latest maximum is needed.
- **Conventional loop from index one:** Initialize `mx = values[0]` and `ans` to a safe low value, then process legal right endpoints only. It avoids the initialization artifact and uses the same recurrence.
- **Exactly two spots:** The sole legal pair is evaluated at index one and returned.
- **All equal values:** The smallest distance gives the best score, which the running maximum captures.
- **Large later value:** Its right contribution may overcome the distance penalty, and after evaluation it may also become the best future left contribution.
- **Order of updates:** Candidate evaluation must precede inserting current `j` into `mx` to avoid self-pairing.
- **Positive-value constraint:** It makes the compact zero initialization harmless by ensuring the first legal pair dominates the temporary index-zero candidate.
- **Input preservation:** The values list is scanned but never changed.
