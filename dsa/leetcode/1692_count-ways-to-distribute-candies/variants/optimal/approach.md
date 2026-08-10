## General

**Recognize an unlabeled set-partition problem**

Candies are unique, but bags are not ordered. A distribution is therefore a partition of `n` labeled items into exactly `k` nonempty, unlabeled groups. The recurrence can build these partitions one candy at a time without assigning names to bags.

Define `f[i][j]` as the number of ways to partition the first `i` candies into exactly `j` nonempty bags.

**The empty base case**

`f[0][0] = 1` because there is one way to distribute no candies into no bags: choose the empty partition.

Every other table entry begins at zero. In particular, positive candies cannot occupy zero bags, and zero candies cannot fill a positive number of nonempty bags.

This seemingly abstract base case makes the recurrence create the first singleton bag correctly.

**Place candy `i` in an existing bag**

Start with a partition of the previous `i - 1` candies into `j` nonempty bags. The new candy may be inserted into any one of those `j` bags.

Each previous partition therefore creates `j` new distributions, contributing:

`f[i - 1][j] * j`.

Although bags are unlabeled, they are distinguishable by their current candy contents. Placing the new unique candy into one existing subset versus another produces a different partition.

**Place candy `i` in a new singleton bag**

Alternatively, start with `j - 1` bags holding the first `i - 1` candies and create a new bag containing only candy `i`. This contributes:

`f[i - 1][j - 1]`.

There is no multiplier for choosing a position or label for the new bag because bag order does not matter. The singleton subset `{i}` is simply added to the unordered collection of existing subsets.

**Combine the exhaustive cases**

Every final partition places candy `i` either with at least one earlier candy or alone. These cases are disjoint and exhaustive, giving:

`f[i][j] = f[i - 1][j] * j + f[i - 1][j - 1]`.

The source reduces the sum modulo $10^9+7$ at every state. Modular reduction is safe because later recurrence operations use only addition and multiplication, both compatible with congruence.

**Trace `n = 3, k = 2`**

For one candy, `f[1][1] = 1`.

For two candies:

- `f[2][1] = 1`, putting both together;
- `f[2][2] = 1`, putting each in its own bag.

For the third candy and two bags:

$$
f[3][2]
=2f[2][2]+f[2][1]
=2\cdot1+1
=3.
$$

The first term inserts candy three into either existing singleton bag; the second creates `{3}` beside the prior one-bag group `{1,2}`. These are exactly the three listed distributions.

**Why the DP neither misses nor double-counts**

Take any partition of candies one through `i` into `j` bags. Inspect the bag containing candy `i`. If it contains other candies, removing `i` leaves a unique partition counted by `f[i-1][j]` plus a unique choice of destination bag. If it is a singleton, removing that entire bag leaves a unique partition counted by `f[i-1][j-1]`.

This reverse operation maps every final partition to exactly one recurrence construction. Therefore the recurrence counts every valid distribution once.

The loops also evaluate entries with `j > i`, but their predecessor values remain zero because more nonempty bags than candies are impossible. No special branch is required.

## Complexity detail

The nested loops compute `n*k` states, each in constant time, so running time is $O(nk)$.

The exact source allocates `(n+1)(k+1)` integers in `f`, using $O(nk)$ space. This does not match the manifest’s $O(k)$ space. Since row `i` depends only on row `i-1`, rolling two rows or updating one row backward can achieve $O(k)$, but the documented implementation retains the complete table.

Modulo keeps stored numeric values bounded, although Python integers would not overflow without it.

## Alternatives and edge cases

- **One-dimensional rolling DP:** Update `j` from high to low so old-row values are not overwritten too early. This preserves $O(nk)$ time and reduces space to $O(k)$.
- **Closed-form inclusion-exclusion:** Stirling numbers of the second kind have formulas involving powers and binomial coefficients, but DP is simpler and numerically direct modulo the prime.
- **`k == 1`:** All candies must share one bag, so the recurrence returns one.
- **`k == n`:** Every candy must be alone, also giving one.
- **More bags than candies:** It would be impossible and yield zero, though the constraints enforce `k <= n`.
- **Unique candies:** Uniqueness is essential; inserting a new labeled candy into different existing groups creates distinct partitions.
- **Unlabeled bags:** No factorial multiplier is applied. Labeling bags would count permutations of the same groups separately.
- **Nonempty requirement:** The state uses exactly `j` nonempty groups; no empty bag is represented.
- **Modulo:** Reduction at each cell gives the same final remainder as reducing the enormous exact count only at the end.
- **Full-table storage:** Earlier rows are not read after the next row is complete, so they are conceptually unnecessary despite being allocated by the exact source.
