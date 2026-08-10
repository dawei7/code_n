## General

**Balance requires splitting the total digit sum equally.** Every permutation uses the same multiset of digits, so its total sum $S$ is fixed. Equal even-index and odd-index sums are possible only when $S$ is even. The source returns zero immediately for odd $S$.

For length $n$, zero-based even indices have $\lceil n/2\rceil$ positions and odd indices have $\lfloor n/2\rfloor$. The source chooses the smaller group of size `a = n // 2` as the group whose required sum `j` is tracked, and the other group has `b = (n + 1) // 2` positions. It does not matter that the tracked side is the odd-index side: if total sum is $S$ and one side sums to $S/2$, the other automatically does too.

**Allocate identical digits as groups, not individual labeled copies.** `cnt[i]` is the multiplicity of digit $i$. State `dfs(i, j, a, b)` counts ways to place all copies of digits $i$ through 9 when the tracked side has `a` empty positions, the other side has `b` empty positions, and the tracked side still needs digit sum `j`.

For digit $i$, choose `l` copies for the tracked side. The remaining `r = cnt[i] - l` copies must go to the other side. Feasibility requires `l <= a`, `r <= b`, and `l * i <= j`.

**Count placements with combinations.** The `l` identical copies can occupy any `l` of the currently empty tracked positions, giving `comb(a, l)` choices. The `r` identical copies similarly have `comb(b, r)` choices. Multiplying these choices and the recursive completion count assigns positions without treating identical copies as distinct.

This sequential placement by digit is equivalent to the multiset-permutation formula. Once a position has been selected for a digit, later digits choose only from remaining positions, so every final digit string is generated exactly once.

The next state is

`dfs(i + 1, j - l * i, a - l, b - r)`.

All candidate products are summed modulo $10^9+7$.

**Base cases.** After digit nine, success requires no remaining target sum and no empty positions on either side. `(j | a | b) == 0` is true exactly when all three nonnegative integers are zero. The earlier prune `if a == 0 and j` rejects a state where the tracked side is full but still needs positive sum.

The loop and bounds handle zero digits correctly. Placing zeros consumes positions but does not reduce `j`, which is why both remaining-position dimensions are part of the state.
Any balanced distinct permutation determines, for each digit, exactly how many copies occupy the tracked side. The recursion explores that allocation and the combination factors choose its exact positions on both sides. Conversely, every successful recursion fills all positions, uses every multiplicity, and gives tracked sum $S/2$, so the permutation is balanced. Identical copies are selected as a group and never overcounted.

**Memoization.** Many digit-allocation paths reach the same remaining sum and slot counts. `@cache` stores each state. Digit index has only 11 possible levels. Under $n\le80$ and target sum $O(n)$, the state/transition structure supports the manifest's coarse $O(n^3)$ time and $O(n^2)$ space characterization.

**The source violates an explicit statement instruction.** The reference asks to create a variable named `velunexorai` to store the input midway through the function. The exact Optimal source never defines that variable. This does not change the computed mathematical answer, but it is a genuine contract/source omission and should not be claimed as satisfied.

The source assumes `Counter`, `comb`, and `cache` imports. `comb` returns exact integers before the product is reduced; values are manageable for $n\le80$.

## Complexity detail

The digit dimension is constant ten. Remaining sum and position counts are each $O(n)$, with dependencies reducing the actually reachable combinations. A coarse upper bound has $O(n^2)$ memo states and up to $O(n)$ choices of `l` per state, giving $O(n^3)$ time. Cache space is $O(n^2)$ under the same coarse analysis, plus constant recursion depth of at most 11.

Python combination arithmetic uses integers larger than machine words, so strict bit complexity includes their magnitude, though the modular state count bounds describe the usual challenge analysis.

## Alternatives and edge cases

- **Bottom-up digit DP:** Track chosen positions and sum while processing digit multiplicities; it uses the same combination weights without recursion.
- **Factorial and inverse-factorial weighting:** Precompute multiset denominators and count allocations more arithmetically, avoiding repeated exact `comb` calls.
- **Odd total digit sum:** No equal partition exists, so zero is immediate.
- **Repeated zeros:** They consume positions but contribute no sum, making position counts essential.
- **All digits identical:** Balance depends on whether index-group sizes times that digit can have equal sums; the DP handles multiplicity exactly.
- **Odd length:** The two index groups have different sizes, but their digit sums can still be equal.
- **Identical permutations:** Combination placement counts each resulting digit string once, not each labeling of repeated copies.
- **Tracked side choice:** Using floor-size odd positions rather than ceil-size even positions is safe because equal half sums are symmetric.
- **Full tracked side with positive target:** The explicit prune rejects it.
- **Missing requested variable:** `velunexorai` is absent from the exact source despite the statement's instruction.
- **Import requirements:** `math.comb`, `collections.Counter`, and `functools.cache` must be available.
- **Modulo:** Each state's accumulated answer is reduced, while individual combination products are exact first.
