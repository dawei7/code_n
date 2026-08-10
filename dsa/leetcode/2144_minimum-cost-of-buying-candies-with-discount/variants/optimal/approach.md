## General

Every use of the promotion handles three candies: two are paid for and a third may be free, provided the free candy costs no more than either paid candy. The objective is equivalent to maximizing the total price of candies obtained for free, because the sum of all candy prices is fixed.

**Take the maximum possible number of free candies**

Each free candy requires two paid candies to support it. Therefore no plan can make more than $\lfloor n/3\rfloor$ candies free.

An optimal plan reaches this maximum count. If fewer than $\lfloor n/3\rfloor$ free candies were used, at least three candies would remain outside complete promotional triples. Among any three such candies, pay for the two more expensive ones and take the cheapest for free. This lowers the cost, contradicting optimality.

So the remaining question is not how many freebies to take, but which $\lfloor n/3\rfloor$ candies can be made free while satisfying the price restriction.

**Sort from most expensive to least expensive**

The exact source calls `cost.sort(reverse=True)`. After sorting, `cost[0] >= cost[1] >= ... >= cost[n - 1]`.

Consider the first three prices. The candy at index two is no more expensive than those at indexes zero and one, so the first two may be bought and the third taken free. The same is true for indexes three, four, and five, then six, seven, and eight, and so on.

Thus every index congruent to two modulo three—`2, 5, 8, ...`—is a legal free candy. The two immediately preceding prices pay for it.

**Why these are the most valuable possible freebies**

The most expensive free candy in any valid plan cannot be more expensive than the third-most-expensive candy overall, `cost[2]`. A free candy needs two candies at least as expensive to support it, and only the first two positions can be strictly ahead of index two.

After accounting for one free candy and its two supporting paid candies, the second-most-expensive free candy cannot exceed `cost[5]`. More generally, the $(q+1)$-st most expensive free candy cannot exceed `cost[3q+2]`: obtaining $q+1$ free candies requires at least $2(q+1)$ paid candies that can support them, so at least $3(q+1)$ candies participate.

The descending triples achieve each upper bound exactly by making `cost[3q+2]` free. Therefore they maximize the total saved price among all plans with the maximum number of free candies. Maximizing savings minimizes money paid.

For `[6,5,7,9,2,2]`, sorting gives `[9,7,6,5,2,2]`. The freebies are prices six and two, while `9,7,5,2` are paid. Total cost is 23.

**Compute paid cost by subtracting savings**

The expression `sum(cost)` is the price of paying for everything. The slice `cost[2::3]` contains indexes two, five, eight, and so on—the candies assigned for free. Subtracting their sum gives `sum(cost) - sum(cost[2::3])`.

This form avoids a conditional accumulation loop while implementing the exact same grouping. A final incomplete group contains one or two candies, neither of which appears at an index congruent to two modulo three, so both are paid as required.

**Why grouping expensive candies first matters**

If cheap candies are used as the two purchases, they can support only an equally cheap or cheaper free candy. Paying for the expensive candies first makes the highest legally possible third candy free in every group. Sorting provides the global ordering needed for that exchange argument.

## Complexity detail

Let $n$ be the number of candies. Sorting costs $O(n\log n)$ time. Both calls to `sum` process at most $n$ elements in total up to a constant factor, so they add $O(n)$ time. Sorting dominates, giving $O(n\log n)$ total time.

Python’s in-place TimSort may use $O(n)$ auxiliary memory in the worst case. In addition, `cost[2::3]` creates a new list containing about $n/3$ references, which is also $O(n)$ space. Thus the exact implementation’s auxiliary space is $O(n)$, matching the manifest.

The call to `sort` mutates the input list by rearranging its prices. The slice and sums do not change values.

## Alternatives and edge cases

- **Loop over sorted indexes:** Add `cost[i]` only when `i % 3 != 2`. This avoids the free-candy slice allocation but keeps the same sorting time and greedy proof.
- **Counting sort:** Prices are between one and 100, so a frequency array can compute the answer in $O(n+100)$ time and $O(100)$ space. It is asymptotically linear under the fixed price range but is not the exact source.
- **Sort ascending:** One can process from the end in groups of three, but the index pattern is less direct. Taking every third element from the front of ascending order would be wrong.
- **Choose cheapest candy free globally:** Taking the globally cheapest freebies satisfies legality but may waste the opportunity to save more expensive eligible candies.
- **Fewer than three candies:** The free slice is empty, so every candy is paid for.
- **Exactly three candies:** The two largest are paid and the smallest is free.
- **Length not divisible by three:** One or two cheapest candies remain after full triples and must be paid because no complete supporting pair remains.
- **Equal prices:** The free candy may cost exactly the minimum of the paid pair, so triples of equal prices are legal.
- **One candy:** Both sums behave correctly: total price minus zero savings.
- **Already descending input:** Sorting leaves the order effectively unchanged; the same index rule applies.
- **Duplicate prices:** Candy identity does not affect cost minimization, and stable ordering among equal values is irrelevant.
- **Input mutation:** Callers that need the original order must copy `cost` before invoking this exact implementation.
- **Savings viewpoint:** Subtraction is safe because every sliced price corresponds to one valid free candy and no price is subtracted twice.
