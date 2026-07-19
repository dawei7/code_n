## General
**Derive the maximum OR without searching**

Adding an element to a subset can only set additional bits; it never clears an
already set bit. Therefore the OR of all input elements is an upper bound on
every subset OR, and the full set attains it. Compute this target once.

**Explore each include-or-exclude choice**

Backtracking at index $i$ keeps the OR accumulated from earlier selected
indices. One branch excludes `nums[i]` and preserves that value; the other
includes it and updates the state with `current | nums[i]`. At the end, count
the branch exactly when its OR equals the target.

Each index subset corresponds to one unique sequence of include/exclude
decisions, so the recursion visits every subset once and cannot double-count.
The leaf comparison accepts exactly the subsets with maximum OR. Because all
values are positive, the empty subset's OR `0` cannot equal the positive
target.

**Count all remaining choices after reaching the target**

Once `current` already equals the target, OR-ing more values cannot change it.
Every combination of the remaining $N-i$ indices is valid, contributing
$2^{N-i}$ subsets immediately. Returning this count is an optional pruning
that preserves the worst-case bound while avoiding redundant recursion when
the target is reached early.

## Complexity detail
In the worst case, the target is reached only at leaves and the recursion visits
$O(2^N)$ states. Each state performs constant bitwise work. The recursion depth
is $N$, so auxiliary stack space is $O(N)$.

## Alternatives and edge cases
- **Iterative bitmask enumeration:** Compute the OR for every mask; updating
  incrementally can retain $O(2^N)$ time, while recomputing each mask from all
  indices takes $O(N2^N)$.
- **Count dynamic programming by OR value:** Maintain a frequency map of
  reachable OR values after each element. This can merge equal states but may
  store many distinct OR values.
- A single element creates exactly one nonempty subset.
- Equal values at different indices remain independently selectable and
  multiply the count.
- If every element already equals the target OR, every nonempty subset
  qualifies.
- Distinct single-bit powers may require selecting every element, leaving only
  one qualifying subset.
- The answer counts index subsets, not distinct value sequences or distinct OR
  values.
