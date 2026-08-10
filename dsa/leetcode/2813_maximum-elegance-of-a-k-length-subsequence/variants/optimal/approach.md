## General

**Balance two competing rewards.** Selecting exactly `k` items earns their total profit plus the square of the number of distinct selected categories. High-profit duplicate-category items help only the profit term. Replacing one of them with an item from a new category may reduce profit but increases the category-square bonus. The algorithm evaluates precisely these useful exchanges.

Although the statement says subsequence, only the chosen indices matter to the score; their output order is never requested. Any subset of `k` positions forms a subsequence when listed in original index order. Therefore, the source may sort items by profit to reason about selection without losing a constraint.

**Start with the maximum possible raw profit.** `items.sort(key=lambda x: -x[0])` sorts the input list in descending profit order. The first `k` items have the largest total profit among all size-$k$ selections, so they provide the best starting point before rewarding extra categories.

The loop over `items[:k]` adds each profit to `tot` and records categories in `vis`. When a category appears for the first time, it increases the distinct count. If it has already appeared, the selected item is redundant with respect to category diversity, and its profit is appended to `dup`.

Because selected items are encountered in descending profit order, `dup` is also in nonincreasing profit order. Its last element is therefore the cheapest currently selected redundant item.

**Record the starting score.** With no exchanges, elegance is `tot + len(vis) ** 2`. The variable `ans` stores this score before considering whether accepting lower profit can buy a larger category bonus. This matters when no exchange improves the result.

**Scan excluded items from highest profit to lowest.** The remaining slice `items[k:]` is still in descending profit order. An excluded item whose category is already in `vis` cannot increase the number of distinct categories, so exchanging it for a selected item would only fail to improve raw profit: the initial top-$k$ choice already favored higher profits. The code skips it.

An excluded item from a new category can increase the distinct count by one, but selection size must remain exactly `k`. Therefore, some selected item must be removed. Removing the only representative of an existing category would lose one category while gaining one, producing no diversity increase. The useful removable items are precisely those stored in `dup`, because another selected item still represents their category.

**Remove the cheapest duplicate.** If `dup` is nonempty, `dup.pop()` removes its last and smallest profit. The new item is the best remaining candidate for its category because excluded items are scanned in descending profit order, and the removed duplicate is the least costly way to free a slot without decreasing the current distinct-category count.

The update `tot += p - dup.pop()` adjusts raw profit, and adding `c` to `vis` raises the distinct count by one. The method then compares the new elegance with `ans`.

For example, suppose the first `k` items include profits ten and eight from the same category, plus profit seven from another category. The eight is redundant. If the next useful excluded item has profit six in a new category, replacing eight lowers profit by two but changes the category bonus from $2^2$ to $3^2$, a gain of five, so elegance improves by three.

**Why exchanges only need this form.** Any size-$k$ selection with more categories than the initial top-$k$ set can be reached by repeatedly adding a previously absent category and removing a duplicate-category item. At each step, removing the cheapest available duplicate maximizes profit for the new category count. Likewise, scanning excluded items by descending profit chooses the most profitable available representative whenever a new category is introduced.

The algorithm evaluates the best achievable profit after each possible increase in distinct-category count along this greedy exchange path. The objective for that count is then determined by adding its square. Taking the maximum over the starting state and every exchange covers the optimal tradeoff.

**Why it stops exchanging when `dup` is empty.** With no redundant selected category, every selected item is the sole representative of its category. Replacing one with a new category would keep the distinct count unchanged. Since remaining candidates have no greater profit than the items considered for the top-$k$ start and exchanges, such a replacement cannot create a better state through diversity. The source skips all further exchanges.

**Input mutation is observable.** `items.sort` changes the caller-provided outer list order in place. The nested two-element item lists are not modified. Mutation does not affect the computed answer, but callers retaining the input see profit-sorted order afterward.

## Complexity detail

Sorting $n$ items costs $O(n \log n)$ time. The initial selection loop processes $k$ items, and the exchange loop processes the remaining $n-k$ items once. Set membership and insertion are expected $O(1)$, and each duplicate is pushed and popped at most once. Work after sorting is expected $O(n)$, so total time is $O(n \log n)$.

The set `vis` can contain up to $n$ categories. The `dup` list can contain up to $k-1$ profits. Python sorting the list also uses implementation-dependent temporary memory, bounded by $O(n)$. Total auxiliary space is $O(n)$.

The slices `items[:k]` and `items[k:]` each allocate lists of references. They are used in separate loops, and their total sizes are $O(n)$, consistent with the space bound. Iterating by indices could avoid those explicit slices but would not change the asymptotic result.

Profit sums and squared category counts can exceed 32-bit integers, but Python integers grow automatically. With up to $10^5$ items and profit up to $10^9$, this safety is relevant.

## Alternatives and edge cases

- **Heap of duplicate profits:** A min-heap can retrieve the cheapest duplicate even if processing order does not guarantee stack ordering. Here descending profit order makes `dup.pop()` sufficient and slightly simpler.
- **Enumerate all subsets:** This examines exponentially many size-$k$ choices and is impossible at $n=10^5$.
- **Greedy only by profit:** Taking the first $k$ and stopping can miss a large increase in the squared category bonus.
- **Greedy only by category count:** Maximizing distinct categories can sacrifice too much profit. Recording the score after every exchange balances both terms.
- **All selected categories distinct initially:** `dup` is empty, no diversity-increasing exchange is possible, and the top-$k$ profit selection is optimal.
- **All items share one category:** Every excluded item also belongs to `vis`, so no exchange occurs; the answer is the sum of the top $k$ profits plus one.
- **Repeated excluded category:** After the first selected representative adds it to `vis`, later items of that category are skipped because they cannot add another distinct category.
- **Equal profits:** Their sort order does not matter to total profit. Any resulting duplicate stack still permits an equally cheap valid removal.
- **Exactly `k = 1`:** The first item has maximum profit, its category count is one, and there can be no duplicate to replace. It is optimal.
- **Selection size remains fixed:** Every accepted new item is paired with exactly one `dup.pop()`, so the number of selected items never changes.
- **Cheapest removable item:** Only redundant representatives may be removed without losing a category. Removing a sole representative would defeat the intended category-count increase.
- **In-place sorting:** Copy `items` first if caller-visible order must be preserved; the exact method does not.
