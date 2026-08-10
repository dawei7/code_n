## General

**The chain performs three operations in contract order.** The requested table must first exclude light animals, then order qualifying animals from heaviest to lightest, then show only names. The source writes those operations as one returned expression:

`animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]`.

Method chaining shortens the syntax, but the intermediate tables still exist conceptually. Reading left to right reveals the complete algorithm.

**Step one: build a strict threshold mask.** `animals['weight']` selects the weight Series. Comparing it with `100` produces one Boolean per row. Exactly weights greater than 100 yield true. A weight equal to 100 yields false because the condition is strict, not `>=`.

Using that Boolean Series inside `animals[...]` filters whole rows. Each surviving record still contains `name`, `species`, `age`, and `weight`, because the weight column is needed for the next step.

**Step two: sort by weight descending.** `sort_values('weight', ascending=False)` orders filtered rows using their `weight` values. `ascending=False` puts larger numbers first. Tatiana at 464 therefore appears before Jonathan at 463, then Tommy at 349, then Alex at 328.

Sorting must occur before discarding `weight`. If the code projected the name column first, the numeric key would be unavailable. Sorting the full original DataFrame first would be correct but could spend time ordering rows that are immediately filtered out; the exact source sorts only the $h$ heavy rows.

**Step three: project a one-column DataFrame.** `[['name']]` uses a list containing one label. The double bracket form matters because it returns a DataFrame with one column. A single bracket `['name']` would return a Series and would not match the requested tabular result.

The final output excludes species, age, and weight. Weight influenced ordering but is not displayed.
For any input row, the first predicate includes it if and only if its weight is strictly above 100, so membership is exact. `sort_values` orders every included pair so a row with greater weight appears no later than a row with lower weight. The final projection preserves that row order while retaining exactly the name field. Therefore the result contains all and only qualifying animal names in descending-weight order.

**What method chaining does and does not mean.** The one-line requirement is about expression style. pandas still creates a Boolean mask, a filtered DataFrame, a sorted arrangement, and a projected result as needed. Chaining avoids naming `filtered_animals` and `sorted_animals` in Python; it does not magically make filtering or sorting constant-time.

**Input mutation.** None of the calls requests in-place behavior. Boolean indexing returns filtered data, `sort_values` returns sorted data by default, and projection returns a one-column result. The original `animals` table remains in its original order with all rows and columns.

**Tied weights.** The contract only requires descending order by weight. Two equal-weight animals are tied under that key, so either relative order satisfies the stated comparison unless a secondary order is specified. The source provides no secondary key and does not request a stable sort kind. Code should not promise alphabetical or input-order tie handling beyond pandas' behavior.

**Index labels.** Filtering and sorting carry original row labels with their rows. Projection does not reset them. The rendered result typically focuses on the `name` column, and the task does not ask for a fresh index.

**Filter-first also improves the expensive step.** Boolean comparison is linear regardless of how many animals qualify, but sorting depends on the number of retained rows. Applying the threshold before sorting reduces the sort from $n$ records to $h$ records while producing the same requested order among heavy animals.

## Complexity detail

Let $n$ be the total row count and $h$ the number of animals heavier than 100. Building and applying the mask takes $O(n)$. Sorting the qualifying rows takes $O(h\log h)$, and projecting names takes $O(h)$. Total time is $O(n+h\log h)$, matching the manifest.

The filtered and sorted intermediates and output require $O(h)$ data storage, but the Boolean mask itself has length $n$. Therefore the exact peak auxiliary-space bound is $O(n+h)=O(n)$, not strictly $O(h)$ when $h$ can be much smaller than $n$. The manifest's `O(h)` space omits this full-length mask.

## Alternatives and edge cases

- **Named intermediate variables:** They perform the same operations and can be easier to debug, but do not meet the optional one-line chaining challenge.
- **Sort before filtering:** Correct membership and order are possible, but sorting all $n$ rows costs $O(n\log n)$ instead of sorting only $h$ matches.
- **`query` method:** `animals.query('weight > 100')` can replace Boolean indexing but adds expression parsing.
- **Weight exactly 100:** It is excluded because the predicate is strictly greater.
- **No heavy animals:** The result is an empty DataFrame with one `name` column.
- **All animals heavy:** Sorting dominates at $O(n\log n)$.
- **Equal weights:** Their relative order is not explicitly defined by this source; only descending weight is guaranteed.
- **Space accounting:** Include the $n$-element Boolean mask when describing the exact implementation.
