# Orders With Maximum Quantity Above Average

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/orders-with-maximum-quantity-above-average/) |
| Frontend ID | 1867 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `OrdersDetails` table stores the products included in customer orders. An order may contain several products, and each row gives one product's `quantity` within its `order_id`. The pair `(order_id, product_id)` uniquely identifies a row.

For every order, consider both its average product quantity and its largest product quantity. Return the identifiers of the orders whose largest quantity is strictly greater than the average quantity of every order in the table. Equivalently, an order qualifies only when its maximum exceeds the greatest of all per-order averages. The result may be returned in any order.

### Function Contract

**Inputs**

- `OrdersDetails(order_id, product_id, quantity)`: one row for each product appearing in an order. `(order_id, product_id)` is unique, and every `quantity` is positive.
- Let $R$ be the number of rows and $G$ the number of distinct orders.

**Return value**

- Return one column named `order_id`.
- Include an order exactly when its maximum `quantity` is strictly greater than every order's average `quantity`.
- Do not include equality, and do not return duplicate order identifiers.
- Result order is unrestricted.

### Examples

**Example 1**

- Input: order `1` has quantities `[12,10,15]`, order `2` has `[8,4,6,4]`, order `3` has `[5,18,20]`, order `4` has `[2,8]`, and order `5` has `[9,9]`
- Output: `[[1],[3]]`

The largest per-order average is order `3`'s $43/3$. The maxima of orders `1` and `3`, respectively $15$ and $20$, exceed that threshold.

**Example 2**

- Input: order `1` has quantities `[4,4]` and order `2` has `[1,7]`
- Output: `[[2]]`

Both averages are $4$, while only order `2` has a maximum above $4$.

**Example 3**

- Input: order `1` has `[9]` and order `2` has `[9,9]`
- Output: `[]`

The greatest average is $9$, and the comparison is strict, so a maximum of $9$ does not qualify.

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(G)$

<details>
<summary>Approach</summary>

#### General

**Reduce each order to the two statistics that matter**

Group `OrdersDetails` by `order_id`. For each group, compute `AVG(quantity)` and `MAX(quantity)`. This produces one compact row per order: its comparison threshold contribution and its candidate maximum. No product-level distinction is relevant after these aggregates have been calculated.

**Turn “every order” into one global threshold**

An order maximum must exceed every per-order average. A value exceeds every member of a finite set exactly when it exceeds that set's maximum, so compute `MAX(average_quantity)` over the grouped rows. This preserves the strict comparison: a maximum equal to the largest average must still be rejected.

**Filter the same grouped relation**

Select each grouped `order_id` whose `maximum_quantity` is greater than the global threshold. Every returned row therefore beats every order average. Conversely, any order satisfying the original condition beats their maximum and passes the filter. Since the grouped relation contains one row per order, the result cannot contain duplicates.

#### Complexity detail

A hash aggregation reads the $R$ detail rows once and maintains an average accumulator and maximum for each of the $G$ orders. Scanning the resulting $G$ rows to find the largest average and filter candidates adds $O(G)$ time. Because $G \le R$, total time is $O(R)$. The grouped state and result relation use $O(G)$ space. A physical database plan may instead sort by `order_id`, which can add sorting cost when no suitable access path exists; the required bound describes the direct hash-grouping strategy.

#### Alternatives and edge cases

- **Window functions over grouped rows:** `MAX(AVG(quantity)) OVER ()` can attach the global threshold to every order in one expression, but it requires a dialect with the needed window support.
- **Repeat the grouped subquery:** Computing order aggregates once for candidates and again for the threshold is logically correct, but it performs avoidable duplicate work.
- **Correlated rescans:** Recomputing an order's maximum for every detail row is correct after `DISTINCT`, yet it can degrade to $O(R^2)$ work without an index-aware optimizer.
- **Strict equality:** An order whose maximum equals the largest average is excluded because the predicate is `>`, not `>=`.
- **Single-product orders:** Their maximum equals their own average, so they cannot qualify when their average is the global maximum.
- **Fractional averages:** Compare numeric aggregate values directly; do not truncate or round them before filtering.
- **Several qualifying orders:** Return all of them, each exactly once.
- **Output order:** No `ORDER BY` is required.

</details>
