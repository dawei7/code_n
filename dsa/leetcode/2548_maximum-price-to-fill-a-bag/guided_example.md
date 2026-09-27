# Guided Example: Maximum Price to Fill a Bag

## 1. The instance, and the exchange rate hidden in it

Take the first official sample: `items = [[50,1],[10,8]]` with `capacity = 5`, whose required output is `55.00000`. Each entry is a pair (price, weight): the first item is worth $50$ and weighs $1$, the second is worth $10$ and weighs $8$.

The decisive property is that items are **divisible**. An item may be cut into two parts with proportions adding to $1$, and each part keeps the same proportion of both price and weight. So an item is not something you either take or leave; it is a commodity whose price and weight scale together. If a fraction $x$ of item $i$ is placed in the bag, it contributes weight $x \cdot \text{weight}_i$ and price $x \cdot \text{price}_i$, with $0 \le x \le 1$.

Because price and weight scale together, the only number that matters about an item is its **price density**

$$
d_i = \frac{\text{price}_i}{\text{weight}_i},
$$

the price bought by one unit of the bag's capacity. Table 1 lists the two sample items with their densities.

| Item | Price $\text{price}_i$ | Weight $\text{weight}_i$ | Density $d_i = \text{price}_i / \text{weight}_i$ | Price of one unit of capacity |
|---|---|---|---|---|
| A | 50 | 1 | $50 / 1 = 50$ | $50$ |
| B | 10 | 8 | $10 / 8 = 1.25$ | $1.25$ |

Item A returns $40$ times as much price per unit of capacity as item B. Any filling that puts weight into B while A is not completely used is therefore throwing money away, which is the intuition the next section turns into a proof.

## 2. What "fill the bag" means, and when it is impossible

The bag must be filled **exactly**: the returned price is the maximum over fillings whose total weight equals `capacity`. That is a genuine constraint, not a formality, because fractional items cannot manufacture weight out of nothing. If the items together weigh less than the capacity,

$$
W = \sum_{i} \text{weight}_i < \text{capacity},
$$

no filling can reach the required weight and the answer is `-1`. For the traced instance $W = 1 + 8 = 9 \ge 5$, so the bag can be filled; the second official sample, a single item `[100,30]` with `capacity = 50`, has $W = 30 < 50$ and returns `-1.00000`.

For the traced instance, the *average* density of a filling is fixed by the arithmetic: any exact filling of $5$ units of capacity contains exactly $5$ units of weight, so its price is $\sum_i d_i \cdot (\text{weight taken from } i)$. Maximizing the price means maximizing a density-weighted average, and the average can never exceed the largest density involved — here $50$. The best conceivable filling would put all $5$ units at density $50$, costing $5 \times 50 = 250$, but item A only offers $1$ unit of weight, so at most $1$ unit can be bought at that density. The remaining $4$ units must come from item B at density $1.25$. That accounting already forces the answer:

$$
1 \cdot 50 + 4 \cdot 1.25 = 50 + 5 = 55 .
$$

## 3. The exchange argument that forces the density order

The reasoning above is not specific to two items. Suppose a feasible exact filling, described by fractions $x_i \in [0,1]$, and suppose two items $i$ and $j$ satisfy $d_i > d_j$ while $x_j > 0$ and $x_i < 1$. Shift a small amount of weight $\delta > 0$ from item $j$ to item $i$, choosing $\delta$ small enough that both bounds survive: the new fractions are $x_i + \delta / \text{weight}_i$ and $x_j - \delta / \text{weight}_j$. The total weight is unchanged, so the filling is still exact and still feasible, but the price changes by

$$
\delta \cdot d_i - \delta \cdot d_j = \delta\,(d_i - d_j) > 0 .
$$

The original filling was therefore not optimal. Contrapositively, in every optimal filling there is a **density threshold**: no item with density strictly above the threshold is left partially used, and no item with density strictly below it carries any weight at all. Only items *at* the threshold may be split, and an exact fill needs just one of them to absorb the leftover capacity.

That single observation yields the whole algorithm and its correctness:

- **Sort by decreasing density.** Process items from the highest $d_i$ to the lowest.
- **Saturate greedily.** For each item in turn, put in as much of it as the remaining capacity allows: either the entire item, or the exact fraction that consumes the remaining capacity and finishes the bag.
- **Stop when the capacity is exhausted.** Later items have lower density and, by the exchange argument, cannot appear in any optimal filling that this prefix already fills exactly.

Soundness is immediate: the procedure places only feasible fractions and stops exactly at zero remaining capacity, so it constructs a genuine filling. Completeness is the exchange argument, which shows that any filling deviating from this order can be strictly improved. Nothing else is needed — no dynamic program, no search over subsets — because divisibility collapses the choice space to a single critical item.

## 4. Executing the greedy on `[[50,1],[10,8]]` with `capacity = 5`

The processing order is by increasing ratio $\text{weight}_i / \text{price}_i$, which is the same as decreasing density. Item A has ratio $1/50 = 0.02$ and item B has $8/10 = 0.8$, so A is processed first.

| Step | Item | Density $d_i$ | Capacity before | Weight taken $v$ | Fraction $v / \text{weight}_i$ | Price added $v \cdot d_i$ | Capacity after | Running price |
|---|---|---|---|---|---|---|---|---|
| 1 | A, `[50,1]` | 50 | 5 | $\min(1,5) = 1$ | $1/1 = 1$ | $1 \times 50 = 50$ | 4 | 50 |
| 2 | B, `[10,8]` | 1.25 | 4 | $\min(8,4) = 4$ | $4/8 = 0.5$ | $4 \times 1.25 = 5$ | 0 | 55 |

Item A is small enough to fit whole, so it is taken entirely. Item B cannot fit whole — its weight $8$ exceeds the remaining $4$ — so only the fraction $0.5$ enters, and the bag closes exactly. In the language of the statement, item B is divided with `part1 = 0.5` and `part2 = 0.5`, and the half of weight $4$ and price $5$ is the half used.

```text
bag weight : 0         1                            5
             |---------|----------------------------|
content    : |  item A |      half of item B         |
weight     : |  1 unit |         4 units              |
price      : |    50   |            5                 |
```

The final price is $50 + 5 = 55$, matching the required output `55.00000`. Notice that the answer is not a sum of whole prices ($50 + 10 = 60$ is unattainable, since item B does not fit) and not the price of the cheapest way to reach weight $5$; it is exactly the density accounting of Section 2.

## 5. Where the remaining-capacity rule comes from

The greedy's stopping condition is worth deriving rather than assuming. Write $v_i = \min(\text{weight}_i, \text{remaining})$ for the weight taken at step $i$. In sorted order, the total weight accepted is $\min(\text{capacity}, W)$, because the procedure keeps accepting until either the capacity is exhausted or the items run out. Hence the residual capacity at the end is

$$
\text{remaining}_{\text{final}} = \max(0,\ \text{capacity} - W),
$$

so the bag is filled exactly if and only if $W \ge \text{capacity}$. The impossibility test is therefore a total-weight comparison, not a property of some item, and it never depends on the order in which items are examined.

| Instance | $W = \sum \text{weight}_i$ | capacity | Residual | Outcome |
|---|---|---|---|---|
| `[[50,1],[10,8]]` | 9 | 5 | $\max(0, 5-9) = 0$ | fills; price `55` |
| `[100,30]` | 30 | 50 | $\max(0, 50-30) = 20$ | impossible, `-1` |
| `[[8,2],[12,3]]` | 5 | 5 | 0 | fills exactly; price `8 + 12 = 20` |
| `[[5,2],[9,3]]` | 5 | 6 | $\max(0, 6-5) = 1$ | one unit short, `-1` |

The third row is the boundary where the residual hits zero with no fraction taken at all: every item is consumed whole, and the price is the plain sum of all prices. The fourth row shows how unforgiving the exact-fill rule is — being short by a single unit of weight is the same failure as being short by twenty, because a fractional item can shrink but never grow.

## 6. Traps this instance exposes

| Situation | Naive expectation | Actual behaviour | Where it bites |
|---|---|---|---|
| Choosing what to take first | take the most expensive items | take the highest **price per unit weight** | `[[10,5],[9,3]]` with `capacity = 4` gives `11`, not the `8` from taking item `[10,5]` first |
| Sorting key | sort by price, or by weight | sort by $\text{weight}_i / \text{price}_i$ ascending, i.e. density descending | reversing the key silently returns a smaller price |
| Comparing densities | divide and compare decimals | compare $p_i \cdot w_j$ against $p_j \cdot w_i$ with integers | floating-point ties can reorder near-equal densities |
| Equal densities | the order matters | any order is optimal; the price is density $\times$ capacity | `[[6,3],[10,5]]` with `capacity = 4`: both densities $2$, price `8` either way |
| Filling the bag | fill it as full as possible | it must be filled **exactly** | `[[5,2],[9,3]]` with `capacity = 6` is `-1`, not `14` |
| Reusing an item | split an item and use it twice | `part1 + part2 = 1`; total taken of one item never exceeds $1$ | double-counting an item's price |
| The returned value | always a sum of whole prices | the last item can contribute a fractional price | `[[9,3],[8,8]]` with `capacity = 2` returns `6`, not `9` |
| Numeric range | small totals | $10^5$ items with prices up to $10^4$ | intermediate sums need wide accumulators, and the answer is compared with $10^{-5}$ tolerance |

The sharpest of these is the first. Price and density disagree precisely when a cheap item is light and an expensive item is heavy, and then the light cheap item wins: in `[[10,5],[9,3]]` with `capacity = 4`, the $10$-price item has density $2$ while the $9$-price item has density $3$, so the optimum takes the $9$-price item whole, spends the last unit of capacity inside the $10$-price item, and collects $9 + 2 = 11$.

## 7. Time and auxiliary space

Let $m = \text{items.length}$. Ordering the items by density is a comparison sort and costs $\Theta(m \log m)$ comparisons, each of which is exact when implemented as a cross-multiplication of integers. The subsequent sweep visits every item once, performs one comparison against the remaining capacity, and updates a running price, so it costs $\Theta(m)$. The total running time is therefore

$$
O(m \log m),
$$

dominated entirely by the sort, with the linear sweep as a lower-order term. Note what is *not* needed: the bag capacity can be as large as $10^9$, so a capacity-indexed dynamic program, which would cost $\Theta(m \cdot \text{capacity})$ states and is the standard tool for the indivisible version of this problem, is hopeless here. Divisibility is what makes the greedy exact and removes the capacity axis from the complexity.

Auxiliary space is $O(m)$ for the sorted sequence of items — $\Theta(m)$ if the sort is performed on a copy, or $O(1)$ beyond the input if a dense index array is sorted in place — plus $O(1)$ working state for the remaining capacity and the running price. No table of subproblem answers is stored, because the exchange argument proves there is only one candidate order and one critical item to split. The trimmed set of fractions used is never materialized either: only the amount taken from the current item is needed at each step, and it is immediately folded into the running total.
