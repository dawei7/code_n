## General

**Aggregate at the comparison granularity.** First group `Orders` by `customer_id` and calendar year, summing all prices. Each resulting row is one yearly total; individual order ordering inside the year no longer matters.

**Compare adjacent observed years.** Apply `LAG(total_purchase)` within each customer partition ordered by year. The first observed year has no predecessor and therefore creates no condition. Every later observed total must be strictly greater than the previous observed total.

**Reject missing calendar years without generating them.** Order prices are positive. If any year between a customer's first and last order is missing, the sequence contains a transition from a positive total to zero, which cannot be strictly increasing. The observed years are contiguous exactly when their count equals `MAX(order_year) - MIN(order_year) + 1`. Combining that span check with the absence of non-increasing adjacent totals is therefore equivalent to checking the complete sequence that explicitly inserts zeros.

The final grouping returns one row per customer. A customer with orders in only one year passes both tests: its observed count equals its one-year span, and it has no adjacent comparison that fails.

## Complexity detail

Let $r$ be the number of rows in `Orders`. Grouping and the window ordering require at most $O(r\log r)$ time in the general comparison model, followed by linear scans of the grouped rows. The grouped relation and window state use $O(r)$ auxiliary space. Database indexes and execution plans may reduce the physical sorting work.

## Alternatives and edge cases

- **Recursive year calendar:** Generating every customer-year row and filling missing totals with zero follows the statement literally, but expands the intermediate relation and is unnecessary once contiguity is checked.
- **Correlated pair comparison:** Searching all later-year pairs can verify the order but may perform quadratic work per customer; `LAG` expresses the adjacent condition directly.
- **Single observed year:** It qualifies because strict increase is a relation between successive years and there is no such pair.
- **Multiple orders in one year:** Sum them before comparing years; comparing individual rows produces the wrong sequence.
- **Missing interior year:** It is a zero-total year and disqualifies the customer even if the next observed total is larger than the previous observed total.
- **Equal totals:** Equality fails because the requirement is strictly increasing, not non-decreasing.
