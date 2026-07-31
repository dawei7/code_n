## General

A customer's consecutive dates form a classic gaps-and-islands structure. Sort that customer's rows by `transaction_date` and assign row numbers $1,2,\ldots$. Advancing to the next calendar day increases both the numeric date and the row number by one, so their difference stays constant throughout one consecutive streak. A missing day changes that difference and starts another island.

The first common table expression computes this island key independently for every customer. Grouping by `customer_id` and the key then produces one row per maximal streak, with `COUNT(*)` as its length.

Rank those streak rows by length in descending order with `DENSE_RANK`. Every row having rank 1 reaches the global maximum. Selecting their customer identifiers and sorting them ascending gives the required relation. No `DISTINCT` belongs in the final projection: two different winning islands owned by the same customer are two judge-visible result rows.

The island key is constant for every pair of adjacent dates inside a streak, so each group cannot cross a date gap. Conversely, all dates in one maximal consecutive run receive the same key and are grouped together. Ranking the resulting counts therefore selects exactly every globally longest streak.

## Complexity detail

Let $n$ be the number of transaction rows. Partition ordering for `ROW_NUMBER` and ordering or ranking the grouped streaks requires $O(n \log n)$ time in the general case. Window and grouping state can occupy $O(n)$ auxiliary space. Database indexes and optimizer choices may reduce physical sorting work but do not change the required bound.

## Alternatives and edge cases

- **Lag plus cumulative markers:** Compare each date with `LAG`, mark every break, and cumulatively sum the markers. This is equally sound but needs an additional window stage.
- **Recursive date expansion:** Starting a recursive search from each transaction is substantially more expensive and obscures the simple island invariant.
- **Final distinct projection:** `SELECT DISTINCT customer_id` is incorrect for this judge because it collapses separate winning streak rows owned by one customer.
- A one-row customer has a streak of length one and can win when no longer streak exists.
- Transaction amounts are irrelevant, including decreases or repeated values.
- The uniqueness of `(customer_id, transaction_date)` prevents duplicate dates from distorting row numbers.

