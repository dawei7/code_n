## General
**Index the catalog once.** Build a hash map from every product ID to its unit price during construction. This makes each later price lookup constant expected time instead of searching the parallel catalog arrays.

**Track customer position.** Increment an order counter exactly once at the beginning of each `getBill` call. Compute the subtotal by summing `price_by_product[item] * quantity` for corresponding entries in the two order arrays.

If the updated counter is divisible by $n$, multiply the subtotal by `(100 - discount) / 100`; otherwise return the full subtotal. Divisibility selects exactly customers $n,2n,3n,\ldots$, and the line-item sum contains each requested quantity at its catalog price, so every returned bill follows the store rules.

## Complexity detail
Constructing the price map takes $O(P)$ time and space. Processing all $L$ line items across the order sequence takes $O(L)$ expected time, while discount scheduling adds constant work per bill. Total time is $O(P+L)$ and auxiliary space is $O(P)$.

## Alternatives and edge cases
- **Linear catalog lookup:** Searching `products` for every bill item is correct but can cost $O(PL)$ across a full-catalog order.
- **Precompute discounted prices:** This can reduce one multiplication per discounted line but duplicates catalog storage and is unnecessary because the discount applies to the subtotal.
- **Every customer discounted:** When $n=1$, each order receives the discount.
- **Full discount:** A $100\%$ discount makes each scheduled bill zero.
- **Multiple discount cycles:** The counter must use divisibility rather than reset incorrectly after only the first discounted order.
- **Several quantities:** Each unit price is multiplied by its parallel amount before the discount is applied.
