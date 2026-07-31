## General

**Anchor the search at maximum profit**

Sort items by decreasing profit and initially select the first $k$. This maximizes total profit without considering category diversity. Track selected categories and place the profits of every duplicate-category selection into a min-heap; those duplicates can be removed without decreasing the category count.

**Exchange the cheapest duplicate for each new category**

Continue through the remaining items in decreasing profit order. When an item belongs to a new category and a duplicate slot remains, replace the smallest selected duplicate profit with this item. This is the least costly way to increase the distinct-category count by one. After each exchange, evaluate the new total profit plus the square of the category count.

For any fixed number of distinct categories, an optimal selection retains the greatest available profits compatible with that count. The initial prefix supplies maximum raw profit, the heap always discards the cheapest redundant choice, and the remaining scan encounters the most profitable representative of every new category first. Therefore the sequence of evaluated states contains an optimal selection for every reachable diversity count; taking their maximum yields the global optimum.

Once the heap is empty, every selected item already represents a distinct category, so no further exchange can increase diversity. Items from already selected categories cannot help because they arrive no earlier—and thus have no greater profit—than the selected alternatives.

## Complexity detail

Sorting $n$ items takes $O(n\log n)$ time. Each item is scanned once, and at most $k$ heap insertions and removals cost $O(\log k)$ each, so total time remains $O(n\log n)$. The category set, heap, and sorted item storage use $O(n)$ space.

## Alternatives and edge cases

- **Enumerate all size-k subsets:** This computes the definition directly but requires $\binom{n}{k}$ candidates.
- **Dynamic programming by category count:** Profit/category values make a dense state impractical, and the greedy exchange order already exposes every relevant diversity count.
- **Replace an arbitrary duplicate:** Removing anything other than the smallest duplicate can only reduce profit more for the same diversity gain.
- With `k = 1`, add a category bonus of one to the greatest selected profit.
- When all selected categories are distinct, the duplicate heap is empty and no exchange is possible or needed.
- Multiple items may share equal profit or category; set membership and the heap handle both ties.
- Use wide integer arithmetic because total profit can reach $10^{14}$ and the squared category count can reach $10^{10}$.
