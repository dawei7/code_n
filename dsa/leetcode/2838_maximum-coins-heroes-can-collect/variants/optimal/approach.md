## General

**Every hero wants the sum of a power prefix.** A hero with power `h` can defeat every monster whose power is at most `h`. Coins are all positive, the hero loses no health, and defeating one monster does not prevent another hero from defeating it. Therefore, each hero should defeat every eligible monster.

The question for each hero is simply: after ordering monsters by power, how many monsters lie at or below `h`, and what is the sum of their corresponding coin rewards?

**Sort indices to preserve the monster-coin pairing.** The source builds

`idx = sorted(range(m), key=lambda i: monsters[i])`.

This is a list of original monster indices ordered by `monsters[i]`. Sorting indices rather than `monsters` itself keeps each monster connected to `coins[i]` and leaves both input arrays unchanged.

If two monsters have equal power, their relative index order does not matter. Both fall on the same side of every hero threshold, and addition of their coins is commutative.

**Build prefix sums in sorted-monster order.** The generator `coins[i] for i in idx` yields rewards according to ascending monster power. `accumulate(..., initial=0)` creates `s` of length $m+1$.

`s[q]` is the sum of coins for the first `q` monsters in sorted order. The initial zero makes the no-defeatable-monster answer available at index zero and avoids a special branch.

**Find the eligible prefix length with upper bound.** For each hero power `h`, the code calls

`bisect_right(idx, h, key=lambda i: monsters[i])`.

Python's keyed binary search applies the key function to list elements, so comparisons use `monsters[idx[mid]]`. The search value `h` is already in the same power domain and is not transformed.

`bisect_right` returns the insertion position after every element whose key is at most `h`. Thus result `i` is exactly the count of monsters the hero can defeat. Using right rather than left bound is essential because equality is allowed.

The answer for that hero is `s[i]`.

**Preserve hero order.** Heroes are processed in their original array order, and one result is appended per hero. No hero sorting or index restoration is necessary. This differs from the manifest's two-sorted-list sweep but directly meets the required output alignment.
Sorting makes monster powers nondecreasing while retaining the matching coin for each index. Binary upper bound divides this order into exactly the eligible prefix and ineligible suffix for a hero. Since all eligible coins should be collected once, the prefix sum at that boundary is the maximum obtainable reward. Repeating independently for every hero returns all correct answers in their original order.

**Independence between heroes.** The note says multiple heroes may defeat the same monster. Therefore, answering one hero does not remove coins or modify state for another. Reusing the same prefix-sum table is valid.

**Why positive coins matter.** If negative coin rewards existed and defeating monsters were optional, a hero might skip an eligible monster. Here every reward is positive, so adding every eligible reward is always optimal. The task wording also frames coins earned after defeating; nothing forces an unhelpful fight, but positivity removes the ambiguity.

**The exact source differs from the manifest sweep.** The manifest describes sorting heroes and monsters and sweeping both lists, which costs $O(n\log n+m\log m)$ and answers all heroes after one monotone pass.

The source sorts only monsters and performs a binary search for every hero. Its time is $O(m\log m+n\log m)$. It avoids sorting heroes and naturally preserves their order.

## Complexity detail

Let $m$ be the number of monsters and $n$ the number of heroes. Sorting the $m$ indices costs $O(m\log m)$. Building prefix sums costs $O(m)$.

Each of $n$ heroes performs a keyed binary search over $m$ indices, taking $O(\log m)$ comparisons. Total time is

$$
O(m\log m+n\log m).
$$

This is slightly different from the manifest's $O(m\log m+n\log n)$ sorting-sweep expression, though both are efficient.

`idx` and `s` use $O(m)$ auxiliary space. The returned `ans` uses $O(n)$ required output space. Excluding output, auxiliary space is $O(m)$; including it is $O(m+n)$.

Prefix sums can reach $10^{14}$, but Python integers avoid overflow.

## Alternatives and edge cases

- **Sort heroes with original indices and sweep:** As hero power rises, add newly defeatable monster coins once and write the running total to the hero's original position. This matches the manifest and replaces $n$ binary searches with one linear merge after sorting.
- **Sort monster-coin tuples:** This is more explicit than sorting indices and has the same asymptotic cost, at the price of allocating tuple pairs.
- **Brute force per hero:** Testing all monsters takes $O(nm)$ time and is too slow at $10^5$ by $10^5$.
- **No defeatable monster:** Upper bound returns zero, and prefix sum `s[0]` is zero.
- **Hero matches a monster exactly:** `bisect_right` includes all monsters with that power.
- **Hero defeats every monster:** The boundary is $m$, and `s[m]` is the total coin sum.
- **Duplicate monster powers:** All equal-power monsters are included together when the threshold reaches that power.
- **Duplicate hero powers:** They independently receive the same prefix total without interfering.
- **Large coin sum:** Python's arbitrary-precision integers preserve the full result.
- **Input preservation:** Sorting the index list leaves `heroes`, `monsters`, and `coins` unchanged.
- **Keyed bisect availability:** The exact code relies on a Python version whose `bisect_right` supports `key`.
