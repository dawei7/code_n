## General

The contract defines two independent Boolean properties. A box is bulky if the maximum of its three dimensions is at least $10^4$ or if the product of the dimensions is at least $10^9$. Checking the maximum captures the rule that any one dimension is sufficient, while the logical `or` preserves the separate volume route. A box is heavy exactly when `mass >= 100`.

Once those two flags are known, their four possible combinations correspond one-to-one with the four required strings. Check the `bulky and heavy` combination first, then either individual flag, and use `"Neither"` when both are false. Because the threshold comparisons are inclusive, values exactly equal to a threshold satisfy that property.

## Complexity detail

The input always consists of four scalar values. The method performs a fixed number of arithmetic operations, comparisons, and branches, so it takes $O(1)$ time and uses $O(1)$ additional space. An asymptotic-optimality certificate records why runtime scaling is inapplicable to this fixed-arity contract.

## Alternatives and edge cases

- **Decision table:** Indexing a four-entry table by the two Boolean flags is equivalent, but explicit conditions make the required category names easier to audit.
- **Nested conditionals:** Testing bulky first and heavy inside each branch is correct, though it duplicates the heavy check or category structure.
- **Inclusive thresholds:** Dimensions of exactly $10^4$, volume exactly $10^9$, and mass exactly $100$ satisfy their respective predicates.
- **Independent bulky routes:** A box may be bulky because of one large dimension even with small volume, or because of volume even when every dimension is below $10^4$.
- **Both criteria:** `"Both"` must take precedence over either single-property label.
