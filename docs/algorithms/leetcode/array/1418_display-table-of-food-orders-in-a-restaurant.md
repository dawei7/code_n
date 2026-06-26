# Display Table of Food Orders in a Restaurant

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1418 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting, Ordered Set |
| Official Link | [display-table-of-food-orders-in-a-restaurant](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/) |

## Problem Description & Examples
### Goal
Build a display table for restaurant orders. Rows are table numbers in numeric order, columns are food names in lexicographic order, and each cell contains how many times that food was ordered at that table.

### Function Contract
**Inputs**

- `orders`: a list of `[customerName, tableNumber, foodItem]` records.

**Return value**

A table represented as a list of rows. The first row is the header `Table` plus sorted food names; each following row starts with a table number string and then count strings.

### Examples
**Example 1**

- Input: `orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]`
- Output: `[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]`

**Example 2**

- Input: `orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]`
- Output: `[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]`

**Example 3**

- Input: `orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]`
- Output: `[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]`

---

## Underlying Base Algorithm(s)
Hash-map aggregation with sorted dimensions. Count `(table, food)` pairs, collect the set of food names, then emit rows in numeric table order and food-name order.

---

## Complexity Analysis
- **Time Complexity**: `O(o + f log f + t log t + tf)`, where `o` is the order count, `f` food count, and `t` table count.
- **Space Complexity**: `O(o + f + t)` for counts and dimension sets.
