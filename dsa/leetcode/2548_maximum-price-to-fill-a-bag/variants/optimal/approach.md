## General

An item with price `price` and weight `weight` contributes `price / weight` for every unit of it placed in the bag. Because arbitrary fractions are allowed, the selection can be viewed as choosing units of available weight rather than indivisible objects. Sort the items by this density from greatest to least, then consume as much as possible from each item until the capacity reaches zero.

**Why richest weight must come first**

Suppose a feasible selection uses some positive weight from a lower-density item while leaving the same amount available in a higher-density item. Exchanging those equal weights preserves the total bag weight and strictly increases, or at least preserves, the price. Repeating the exchange removes every such inversion, producing exactly the density-sorted greedy selection. Therefore no other exact-capacity selection has a greater price.

Before sorting, compare total available weight with `capacity`. Fractions allow any remaining amount of a positive-weight item to be taken, so total weight is the only feasibility condition. If enough weight exists, all but possibly the final selected item are taken whole, and that last item supplies the exact residual capacity.

## Complexity detail

Let $n$ be the number of items. Summing weights and scanning the sorted items take $O(n)$ time, while sorting by price density takes $O(n \log n)$ time overall. Python's in-place sort may use $O(n)$ auxiliary storage, and the remaining variables use constant space.

## Alternatives and edge cases

- **Repeatedly search for the best remaining density:** This makes the same greedy choices but can take $O(n^2)$ time.
- **0/1 knapsack dynamic programming:** Treating items as indivisible solves a different problem and wastes the fractional structure; the capacity can also be as large as $10^9$.
- **Sort by total price:** A costly heavy item may provide less price per unit than a cheaper light item, so total price alone is not the correct priority.
- **Insufficient total weight:** Return `-1` before attempting the greedy fill.
- **Capacity equals total weight:** Every item is consumed completely, regardless of density order.
- **Fractional final item:** Multiply its total price by `taken / weight`; do not round the fraction prematurely.
- **Equal densities:** Either order gives the same price per unit and therefore the same optimum.
- **Input mutation:** Sorting may reorder the outer `items` list, which does not change the required returned value.
