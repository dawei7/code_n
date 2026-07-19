## General
**Count orders by customer**

Group `Orders` rows by `customer_number`. Each row represents one order, so `COUNT(*)` within a group is exactly that customer's order total.

**Select the largest group**

Order the grouped totals descending and keep the first row. The contract guarantees a unique maximum, so no secondary tie rule is needed and exactly one customer identifier is returned.

**Why the selected identifier is correct**

Grouping assigns every order to exactly one customer group without duplication or loss. Sorting those exact group sizes in descending order places the uniquely largest count first. Therefore the retained group belongs to precisely the customer who placed the most orders.

## Complexity detail
For `n` orders and `c` distinct customers, aggregation processes all rows and stores $O(c)$ groups. Ordering the groups takes $O(c \log c)$, giving $O(n + c \log c)$, bounded by $O(n \log c)$, time and $O(c)$ working space.

## Alternatives and edge cases
- **Aggregate in a common table expression:** calculate customer totals first and order that named relation; it has the same asymptotic behavior.
- **Window rank over grouped totals:** works but is unnecessary when only one guaranteed winner is required.
- **Correlated count per distinct customer:** may rescan all orders for every customer and take $O(cn)$ time.
- **Count distinct order numbers:** is unnecessary because each input row already represents one unique order.
- **One customer:** that customer is the winner.
- **Unsorted order numbers:** do not affect grouping.
- **Nonconsecutive customer identifiers:** are ordinary grouping keys.
- **Unique winner guarantee:** means the query should not invent a tie-breaker.
