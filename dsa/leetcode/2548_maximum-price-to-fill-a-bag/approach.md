## General

**This is a fractional knapsack problem**

Every item may be divided in any ratio, and price scales linearly with weight. Therefore, a fraction of an item has the same price per unit weight as the whole item.

For item `[p,w]`, its value density is

$$
\frac pw.
$$

To maximize total price for an exact weight capacity, consume available weight from highest density to lowest density.

**Understand the stored sort key**

The source sorts by:

`x[1]/x[0]`,

which is `weight/price`, the reciprocal of price density. Ascending reciprocal order is equivalent to descending `price/weight` order because all prices and weights are positive.

Thus the first item processed provides the greatest price per unit of capacity.

The manifest describes density sorting directly; the exact key reaches the same order through reciprocals.

**Take as much as possible from each item**

For current item with weight `w` and remaining bag capacity, choose:

`v=min(w,capacity)`.

If the item fits entirely, `v=w`. Otherwise, take exactly the fraction needed to fill the remaining capacity.

The selected fraction is `v/w`, so its proportional price is:

`v/w*p`.

This is added to `ans`, and `v` is subtracted from remaining `capacity`.

**Why the greedy density order is optimal**

Suppose a proposed solution uses some positive weight of lower-density item `B` while unused weight remains in higher-density item `A`.

Exchange a small equal amount of weight $\delta$:

- remove $\delta$ weight from `B`;
- add $\delta$ weight from `A`.

Bag weight stays unchanged. Price changes by:

$$
\delta\left(\frac{p_A}{w_A}-\frac{p_B}{w_B}\right)\ge0.
$$

It strictly improves when `A` has strictly greater density.

Repeated exchanges transform an optimal solution into one that completely consumes higher-density items before lower-density ones, with at most one partially used item. This is exactly the source's greedy order.

**Why exact filling may be impossible**

Items can be divided, but total available weight cannot be increased. If the sum of all weights is below `capacity`, the bag cannot be filled exactly.

The loop consumes all items, and remaining `capacity` stays positive. The final expression returns `-1`.

If total weight is sufficient, some processed item fills the last capacity fraction and remaining capacity becomes zero. The result is `ans`.

**Continuing after capacity reaches zero is harmless**

The code does not break. For later items:

`v=min(w,0)=0`,

so they add zero price and leave capacity zero. The final answer remains unchanged.

An early break would be a small practical optimization but is not required for correctness.

**Trace the first sample**

Items are `[50,1]` and `[10,8]`:

- densities are 50 and 1.25;
- reciprocal sort puts the first item first.

Take all weight 1 for price 50, leaving capacity 4. Then take $4/8$ of the second item for price $(4/8)\cdot10=5$. Total is 55 and capacity reaches zero.

**Floating-point behavior**

The sort key and proportional price use floating-point division. The problem accepts answers within $10^{-5}$, so this representation is appropriate for the stated bounds.

For exact rational comparisons, one could compare cross-products `p1*w2` and `p2*w1` instead.

**Why taking a fraction does not change its density**

For fraction ratio $\alpha$ of an item, selected price is $\alpha p$ and weight is $\alpha w$. Their ratio is

$$
\frac{\alpha p}{\alpha w}=\frac pw
$$

for every positive $\alpha$. Dividing an item cannot create a richer or poorer sub-item, which is the property that makes the exchange proof and one sorted order valid.

Only the final used item may need a proper fraction. Earlier higher-density items are taken completely because leaving any of their weight unused while consuming a lower-density item would permit a profitable exchange.


The exchange argument proves every maximum-price exact fill can be arranged in nonincreasing density order. The loop takes the maximum available weight from each item in that order, so it constructs that canonical optimum whenever enough total weight exists. The remaining-capacity check distinguishes impossible fills.

## Complexity detail

Let $n$ be the number of items. Sorting costs $O(n\log n)$ time. The greedy scan is $O(n)$, so total time is $O(n\log n)$.

`sorted` creates a list of $n$ item references, and sorting may use linear temporary storage. Auxiliary space is $O(n)$.

The numeric answer is a floating-point value, while remaining capacity stays integral because selected weight `v` is integral under this implementation; the final fractional selection still uses an integer amount of capacity.

## Alternatives and edge cases

- **Cross-product comparator:** Avoid floating-point density keys by comparing `p1*w2` with `p2*w1`.
- **Indivisible knapsack DP:** It is unnecessary and incorrect for freely divisible items.
- **Insufficient total weight:** Return `-1`.
- **Capacity smaller than first item:** Take only the needed fraction of the best-density item.
- **Equal densities:** Their processing order does not affect total price.
- **Capacity exactly total weight:** Every item is consumed.
- **Capacity reaches zero early:** Later iterations contribute zero.
- **Positive prices and weights:** They make reciprocal sorting well-defined.
- **Exact fill:** Unused capacity is not allowed even if current price is maximal.
- **Input preservation:** `sorted` does not reorder the original outer list.
