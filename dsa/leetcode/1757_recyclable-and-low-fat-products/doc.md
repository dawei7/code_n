# Recyclable and Low Fat Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1757 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/recyclable-and-low-fat-products/) |

## Problem Description

### Goal

The `Products` table records each product's identifier and two independent yes-or-no properties. The `low_fats` column indicates whether the product is low fat, while `recyclable` indicates whether it can be recycled.

Find the products for which both properties are marked `"Y"`. Return only their `product_id` values. Products satisfying just one of the two conditions must not appear, and the result rows may be returned in any order.

### Function Contract

**Inputs**

- `Products(product_id, low_fats, recyclable)`: one row per product, with `product_id` as the primary key and each property containing either `"Y"` or `"N"`.

Let $R$ be the number of product rows and $K$ the number of rows satisfying both predicates.

**Return value**

- Return a one-column table named `product_id`.
- Include exactly those identifiers whose rows have both `low_fats = "Y"` and `recyclable = "Y"`.

### Examples

**Example 1**

- Input: products `1` and `3` have both flags set to `"Y"`, while the other rows fail at least one flag.
- Output: product identifiers `1` and `3`.
- Explanation: Both required predicates hold for exactly those two rows.

**Example 2**

- Input: one product has `low_fats = "Y"` and `recyclable = "N"`.
- Output: an empty result.
- Explanation: Being low fat alone does not satisfy the conjunction.

**Example 3**

- Input: every product has both flags set to `"Y"`.
- Output: every product identifier.
- Explanation: No qualifying row is excluded by the projection.

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(K)$

<details>
<summary>Approach</summary>

#### General

**Test the low-fat flag**

Keep only rows whose `low_fats` value is exactly `"Y"`. Comparing the stored categorical value directly avoids treating `"N"` as truthy text.

**Require recyclability at the same time**

Combine `recyclable = "Y"` with the first predicate using `AND`. This conjunction expresses the requirement that one product row must satisfy both properties; using `OR` would incorrectly admit products possessing only one.

**Project only the requested identifier**

Select `product_id` and no property columns. Because it is the table's primary key, every returned identifier is already unique. Ordering by `product_id` is optional under the contract but makes local fixture output deterministic.

Scanning the table considers every possible qualifying row, the conjunction accepts exactly the rows with both flags, and the projection emits exactly their identifiers. The query therefore produces neither false positives nor omissions.

#### Complexity detail

A table or primary-key-index scan examines each of the $R$ rows once and evaluates two constant-time predicates, giving $O(R)$ time. The returned table contains $K$ identifiers and therefore occupies $O(K)$ output space; the filter itself needs only constant auxiliary state. A suitable composite index may reduce rows examined for particular data distributions without changing the worst-case bound.

#### Alternatives and edge cases

- **Use `OR` between predicates:** This returns products that are low fat or recyclable, including rows that fail one required condition.
- **Filter in a nested subquery:** Applying one predicate inside and the other outside is equivalent but adds unnecessary structure to this direct selection.
- **Conditional aggregation:** Grouping is unnecessary because each primary-key product already occupies one row.
- **No qualifying products:** Return the correct column with zero result rows.
- **Every product qualifies:** Return every identifier exactly once.
- **Only one flag is `"Y"`:** Exclude the row regardless of which property is the positive one.
- **Primary-key uniqueness:** No `DISTINCT` operation is needed because `product_id` cannot repeat.
- **Result order:** The problem permits any order; an explicit ascending order is only for deterministic presentation.

</details>
