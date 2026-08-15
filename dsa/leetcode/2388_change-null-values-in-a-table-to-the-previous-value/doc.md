# Change Null Values in a Table to the Previous Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2388 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value/) |

## Problem Description

### Goal

The `CoffeeShop` table records drink orders with a unique integer `id` and a nullable text column `drink`. Its rows have a presented input order that is independent of the numeric identifier. The first row is guaranteed to name a drink, but later rows may contain `NULL`.

Return every input row in exactly that same order. Keep each non-null drink unchanged, and replace each null drink with the closest non-null drink appearing earlier in the presented sequence. A run of several null rows therefore carries forward the same most recent drink until another named drink appears.

### Function Contract

**Input table**

- `CoffeeShop(id, drink)`: `id` is unique; `drink` is a nullable string.

The first presented row has a non-null `drink`.

**Return value**

- Return columns `id` and `drink` for every input row in the original presented order.
- Each null `drink` is replaced by the nearest preceding non-null value.

**Ordering semantics**

- “Previous” refers to input row sequence, not ascending or descending `id`.
- Filling a null does not alter its row's identifier or position.

### Examples

#### Example 1

- Input rows: `[(9,"Rum and Coke"), (6,NULL), (7,NULL), (3,"St Germain Spritz"), (1,"Orange Margarita"), (2,NULL)]`
- Output rows: `[(9,"Rum and Coke"), (6,"Rum and Coke"), (7,"Rum and Coke"), (3,"St Germain Spritz"), (1,"Orange Margarita"), (2,"Orange Margarita")]`
