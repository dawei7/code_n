## General

**Separate the only possible compatibility families.** A usable non-`xx` card has one of two forms:

- `x?`, where its first position is `x`;
- `?x`, where its second position is `x`.

Two `x?` cards are compatible exactly when their second letters differ. Likewise, two `?x` cards are compatible exactly when their first letters differ. But a noncentral card from the first family and one from the second differ in both positions, so they cannot pair. Cards containing no `x` never participate.

A card `xx` is compatible with every noncentral card in either family, but two `xx` cards are identical and incompatible. The central cards form a shared resource: allocate some to the first family and all remaining ones to the second.

**Solve one family as complete multipartite matching.** Group a family by its non-`x` letter and treat allocated `xx` cards as one additional category. Cards from different categories are mutually compatible; cards within a category are not.

Suppose the category sizes total $T$ and the largest category has size $M$. No matching can exceed $\lfloor T/2\rfloor$ pairs because each pair consumes two cards. It also cannot exceed $T-M$, because every card paired from the largest category needs a partner outside it, and if the largest category is not used, only the $T-M$ outside cards remain.

Both bounds are achievable by repeatedly pairing cards from the two currently largest nonempty categories. This keeps the largest remaining category from becoming unnecessarily stranded. Therefore the exact side score is

$$
\min\left(\left\lfloor\frac{T}{2}\right\rfloor,\ T-M\right).
$$

**Enumerate the center split.** If there are $C$ copies of `xx`, try every allocation $t$ from $0$ through $C$. Add the first-family score with an extra category of size $t$ to the second-family score with an extra category of size $C-t$. Every legal global matching assigns each used center card to exactly one family, so it appears in one enumerated split. Conversely, combining the two independent family matchings for a split is valid. The maximum sum is therefore optimal.

## Complexity detail

Let $n$ be the number of cards and $C$ the number of `xx` cards. Counting categories takes $O(n)$ time. There are $C+1\le n+1$ allocations, and each score examines at most ten fixed alphabet categories, so enumeration takes $O(n)$ time. Total time is $O(n)$.

Only the at-most-ten letter counts for each family are stored, so auxiliary space is $O(1)$ under the fixed `'a'` through `'j'` alphabet.

The benchmark defines its size as $n$, uses half `xx` and half identical `x?` cards, and spans three legal tiers. The accepted implementation evaluates each split from fixed counts. A calibrated correct alternative rebuilds full category multisets and repeatedly scans them for every split, producing quadratic growth while preserving the same matching formula.

## Alternatives and edge cases

- **General graph maximum matching:** Modeling every physical card as a vertex is correct but creates up to quadratic edges and ignores the ten-letter structure.
- **Greedily consume xx cards first:** Assigning every center to one family can be suboptimal because centers may be needed to relieve dominant categories on both sides.
- **Only identical noncentral cards:** They cannot pair with one another; each needs a center card.
- **Balanced noncentral categories:** They can pair among themselves without using any center.
- **Only xx cards:** All cards are identical, so the score is zero.
- **Cards without x:** Ignore them completely.
- **Cross-family noncentral cards:** An `x?` card and a `?x` card differ in both positions and are incompatible.
- **Duplicate cards:** Each occurrence is a separate card, but equal strings belong to one incompatible category.
- **Unused cards:** An optimal matching may leave cards from a dominant category or excess centers unmatched.
