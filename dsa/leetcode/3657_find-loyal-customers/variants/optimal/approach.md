## General

**Reduce each customer's entire history to the three required measurements.** Group all rows by `customer_id`. A conditional sum counts only `purchase` rows, while another conditional sum counts `refund` rows. The difference between the maximum and minimum transaction dates measures the customer's full activity span; both purchases and refunds participate because the contract refers to the customer's transaction activity.

Apply every loyalty rule in `HAVING`, after aggregation. The purchase sum must be at least three, and the date difference must be at least 30 days. For the rate condition, a refund count $R$ among $T$ total transactions must satisfy

$$
\frac{R}{T}<\frac{1}{5}.
$$

Since every customer group is nonempty, multiplying by the positive value $5T$ gives the exactly equivalent integer comparison $5R<T$. This avoids floating-point division, percentage rounding, and accidental inclusion of the 20% boundary.

Each customer produces one aggregate group, so a group surviving all three predicates represents exactly one loyal customer. Conversely, any loyal customer has measurements satisfying every predicate and therefore survives. Sorting those identifiers ascending produces the required result.

## Complexity detail

Let $N$ be the number of transaction rows and $C$ the number of distinct customers. Without assuming a hash aggregate or supporting index, grouping can require $O(N\log N)$ comparison work, and ordering the surviving customer groups costs $O(C\log C)$. The working space is $O(N+C)$ in a general sort-based execution plan. Database indexes or hash aggregation can improve practical execution.

The benchmark defines its size $S=C$ and supplies six transactions per customer, so $N=6S$. The accepted strategy aggregates the transaction table once. A calibrated correct alternative performs multiple correlated scans for each outer transaction row, preserving the same output while exhibiting quadratic growth.

## Alternatives and edge cases

- **Floating-point refund division:** It can express the percentage directly, but an integer cross-product is exact and makes the strict 20% boundary explicit.
- **Correlated subqueries per customer row:** They can compute the same counts and date span, but repeated full-table scans may grow quadratically.
- **Exactly three purchases:** The purchase threshold is inclusive, so three purchases are sufficient when the other criteria hold.
- **Exactly 30 active days:** The activity threshold is inclusive; a first-to-last difference of 30 days qualifies.
- **Exactly 20% refunds:** The refund threshold is strict, so one refund among five total transactions is excluded.
- **Refunds at a date extreme:** Refund rows count toward the earliest and latest transaction dates because activity covers the complete transaction history.
- **Transaction amounts:** Positive or differing amounts do not change the count-based criteria.
- **Ordering:** Qualifying identifiers must appear in ascending numeric order.
