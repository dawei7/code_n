## General

**Classify every usable card by the position of `x`**

Only cards containing `x` can participate. Because every card has length two, a usable card belongs to one of three categories:

- `x?`: first character is `x` and the second is different.
- `?x`: second character is `x` and the first is different.
- `xx`: both characters are `x`.

Cards containing no `x` are ignored.

The source counts `x?` cards by their second character in `first`, counts `?x` cards by their first character in `second`, and stores the number of `xx` cards in `centers`.

**Understand which categories can pair**

Two `x?` cards already agree at position zero. They are compatible exactly when their other characters differ. For example, `"ab"` and `"ac"` differ only at position one, while two copies of `"ab"` differ nowhere and cannot pair.

The same rule applies within `?x`: their first characters must differ.

An `x?` card and a `?x` card differ in both positions because their non-`x` characters occupy opposite sides. They cannot pair directly.

An `xx` card is compatible with either side category. It differs from `x?` only at position one and from `?x` only at position zero. Two `xx` cards are identical and cannot pair with each other.

Thus the game consists of two independent “pair different labels” problems, except that center cards must be divided between them.

**Reduce one side to pairing different labels**

For the `x?` side, treat the second character as a label. Center cards allocated to this side behave as another label, namely `x`. A valid pair must use two different labels.

Suppose one side has `total` cards and its largest label frequency is `largest`.

There are two upper bounds on the number of pairs:

- Each pair consumes two cards, so there can be at most `floor(total / 2)` pairs.
- Every pair can contain at most one card from the largest label. Pairing a largest-label card requires a card outside that label, and there are `total - largest` such cards. Therefore there can be at most `total - largest` pairs.

The maximum is exactly

`min(total // 2, total - largest)`.

If no label dominates, cards can be alternated until at most one remains, reaching `floor(total / 2)`. If one label dominates, pair every non-dominant card with one dominant card, reaching `total - largest`. These constructions attain the smaller upper bound.

**Apply the side formula in `side_score`**

`side_score(counts, allocated)` receives the non-center label counts and the number of `xx` cards assigned to that side.

It computes:

- `side_total`: number of ordinary side cards.
- `total = side_total + allocated`.
- `largest`: maximum of the allocated center-label count and every ordinary label count.

It then returns the exact different-label pairing maximum.

Including `allocated` in the maximum is essential. Many center cards all share the same `xx` label and cannot pair with one another.

**Try every division of center cards**

If `allocated` centers go to the first-position-`x` side, then `centers - allocated` go to the second-position-`x` side.

For each allocation from zero through `centers`, the two side scores are independent and can be added. The source returns the maximum sum over all allocations.

This exhaustive allocation is affordable because the alphabet is fixed to ten letters `'a'` through `'j'`. Computing a side’s sum and maximum scans only a constant-sized set of possible label counts. There are at most `n + 1` allocations, so total work remains linear.

An allocation does not force every center to be used in a pair. `side_score` computes the maximum and naturally leaves unmatched cards when one label dominates or the total is odd.

**Trace the first example**

With `x = 'a'` and cards `["aa", "ab", "ba", "ac"]`:

- `centers = 1` from `"aa"`.
- The first-side labels are `b` and `c` from `"ab"` and `"ac"`.
- The second-side label is `b` from `"ba"`.

Allocate zero centers to the first side. Its two different labels pair for one point. Allocate the center to the second side, where labels `b` and center-label `a` pair for another point. Total score is two.

**Trace the incompatible cross-side example**

With `x = 'b'`, `"ab"` belongs to the `?x` side and `"ba"` belongs to the `x?` side. Each side has one card, there is no `"bb"` center, and cross-side pairing would differ in both positions. Both side scores are zero.

**Why play order no longer matters**

Within a side, only label multiplicities matter. Pairing two different labels reduces both counts by one. The closed-form maximum proves how many such removals can be scheduled, regardless of the exact order.

The only global decision is center allocation, and the source enumerates every possibility. Therefore the returned maximum covers every legal strategy.

## Complexity detail

Let `n` be the number of cards and let `A` be the alphabet size, fixed at ten by the constraints.

Classifying cards takes `O(n)` expected time. There are `centers + 1 <= n + 1` allocations. Each calls `side_score` twice, scanning at most `A` stored label counts, for `O(nA) = O(n)` time because `A` is constant.

The two counters hold at most `A - 1` keys each, so auxiliary space is `O(A) = O(1)` under the fixed alphabet.

If the alphabet were unbounded, the exact repeated `sum` and `max` operations would make the allocation phase `O(centers * d)` for `d` distinct side labels. The manifest’s linear and constant-space bounds rely on the stated ten-letter domain.

## Alternatives and edge cases

- **Maximum matching on individual cards:** Building compatibility edges can be quadratic. Category counts collapse the graph to constant many labels.
- **Greedily pair any compatible cards:** A poor use of `xx` centers can starve the other side. Enumerating their allocation avoids that choice error.
- **Pair `x?` with `?x`:** When neither card is `xx`, they differ at both positions and are incompatible.
- **Pair identical cards:** They differ in zero positions, but compatibility requires exactly one.
- **Pair two `xx` cards:** They are identical and cannot score.
- **No center cards:** The two sides are fully independent; the only allocation is zero.
- **All cards are centers:** No compatible pair exists, and the formula returns zero because one label contains every card.
- **One dominant label:** The number of pairs is limited by cards outside that label, captured by `total - largest`.
- **Odd side total:** At most `floor(total / 2)` pairs can be formed, leaving at least one card.
- **Cards without `x`:** They can never enter a legal pair and are correctly ignored.
- **Duplicate compatible labels:** Copies remain separate cards, but copies of the same label must pair with other labels.
- **Every center need not score:** The allocation loop assigns all conceptually, but the side formula may leave excess centers unused.
- **Input preservation:** The method counts cards without removing or reordering the input deck.
