# Pizza Toppings Cost Analysis

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3050 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/pizza-toppings-cost-analysis/) |

## Problem Description

### Goal

A pizza shop stores each available topping and its price in `Toppings`. Build
every possible pizza that uses exactly three different toppings. A topping
cannot be selected more than once within one pizza, and pizzas that differ
only in the order of the same three toppings represent the same combination.

For each combination, list its three topping names in alphabetical order,
joined with commas as `pizza`, and report their summed price as `total_cost`
rounded to two decimal places. Return all combinations with the most expensive
total first. When totals tie, order the `pizza` strings alphabetically.

### Function Contract

**Inputs**

- `Toppings(topping_name, cost)`: One row per available topping;
  `topping_name` is the primary key and `cost` is its decimal price.

Let $n$ be the number of rows in `Toppings`, and let
$K = \binom{n}{3}$ be the number of returned combinations when $n \ge 3$.

**Return value**

- An ordered table with columns `pizza` and `total_cost`. Each row represents
  one distinct three-topping combination, with names alphabetized and joined
  by commas and the summed cost rounded to two decimal places. Rows are sorted
  by `total_cost` descending and then `pizza` ascending.

### Examples

**Example 1**

For `Chicken` at `0.55`, `Extra Cheese` at `0.40`, `Pepperoni` at `0.50`,
and `Sausage` at `0.70`, the most expensive combination is:

| pizza | total_cost |
|---|---:|
| Chicken,Pepperoni,Sausage | 1.75 |

The other three combinations follow in descending total-cost order.

**Example 2**

With exactly three toppings named `Basil`, `Olive`, and `Tomato`, exactly one
row is returned. Its `pizza` value is `Basil,Olive,Tomato`, regardless of the
input row order.

**Example 3**

If four toppings all cost `1.00`, every combination costs `3.00`; the four
rows are therefore ordered alphabetically by their `pizza` strings.
