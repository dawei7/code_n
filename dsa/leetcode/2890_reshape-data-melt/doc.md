# Reshape Data: Melt

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2890 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/reshape-data-melt/) |

## Problem Description

### Goal

A sales report stores one product per row in a wide format. The `product` column identifies the item, while the integer columns `quarter_1`, `quarter_2`, `quarter_3`, and `quarter_4` hold its sales for the four quarters.

Reshape this report into a long DataFrame in which every row describes one product-quarter combination. The result must have the columns `product`, `quarter`, and `sales`: `quarter` contains the name of the original quarter column, and `sales` contains that column's integer value. Emit the four quarter groups in their original column order while preserving the input product order within each group.

### Function Contract

**Inputs**

- `report`: A pandas DataFrame with an object column `product` and integer columns `quarter_1`, `quarter_2`, `quarter_3`, and `quarter_4`.

Let $n$ be the number of products in `report`. The reshaped result contains exactly $4n$ rows.

**Return value**

Return a pandas DataFrame with columns `product`, `quarter`, and `sales`, containing one row for every product and quarter.

### Examples

#### Example 1

- **Input:** `report = [{"product": "Umbrella", "quarter_1": 417, "quarter_2": 224, "quarter_3": 379, "quarter_4": 611}, {"product": "SleepingBag", "quarter_1": 800, "quarter_2": 936, "quarter_3": 93, "quarter_4": 875}]`
- **Output:** `[{"product": "Umbrella", "quarter": "quarter_1", "sales": 417}, {"product": "SleepingBag", "quarter": "quarter_1", "sales": 800}, {"product": "Umbrella", "quarter": "quarter_2", "sales": 224}, {"product": "SleepingBag", "quarter": "quarter_2", "sales": 936}, {"product": "Umbrella", "quarter": "quarter_3", "sales": 379}, {"product": "SleepingBag", "quarter": "quarter_3", "sales": 93}, {"product": "Umbrella", "quarter": "quarter_4", "sales": 611}, {"product": "SleepingBag", "quarter": "quarter_4", "sales": 875}]`

#### Example 2

- **Input:** `report = [{"product": "Notebook", "quarter_1": 12, "quarter_2": 18, "quarter_3": 15, "quarter_4": 21}]`
- **Output:** `[{"product": "Notebook", "quarter": "quarter_1", "sales": 12}, {"product": "Notebook", "quarter": "quarter_2", "sales": 18}, {"product": "Notebook", "quarter": "quarter_3", "sales": 15}, {"product": "Notebook", "quarter": "quarter_4", "sales": 21}]`

#### Example 3

- **Input:** `report = [{"product": "Lamp", "quarter_1": 7, "quarter_2": 7, "quarter_3": 11, "quarter_4": 9}, {"product": "Desk", "quarter_1": 3, "quarter_2": 8, "quarter_3": 8, "quarter_4": 14}]`
- **Output:** `[{"product": "Lamp", "quarter": "quarter_1", "sales": 7}, {"product": "Desk", "quarter": "quarter_1", "sales": 3}, {"product": "Lamp", "quarter": "quarter_2", "sales": 7}, {"product": "Desk", "quarter": "quarter_2", "sales": 8}, {"product": "Lamp", "quarter": "quarter_3", "sales": 11}, {"product": "Desk", "quarter": "quarter_3", "sales": 8}, {"product": "Lamp", "quarter": "quarter_4", "sales": 9}, {"product": "Desk", "quarter": "quarter_4", "sales": 14}]`
