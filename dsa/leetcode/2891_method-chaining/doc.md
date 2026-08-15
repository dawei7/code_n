# Method Chaining

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2891 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/method-chaining/) |

## Problem Description

### Goal

An `animals` DataFrame records each animal's `name`, `species`, integer `age`, and integer `weight` in kilograms.

Select only animals whose weight is strictly greater than $100$ kilograms. Order those qualifying animals by weight in descending order, then return a DataFrame containing only their names in that order. Express the filtering, ordering, and projection as a pandas method chain rather than storing intermediate DataFrames.

### Function Contract

**Inputs**

- `animals`: A pandas DataFrame with object columns `name` and `species`, plus integer columns `age` and `weight`.

Let $n$ be the number of animals and $h$ the number whose weight is strictly greater than $100$.

**Return value**

Return a one-column DataFrame named `name` containing the $h$ qualifying animals, ordered from greatest to least weight.

### Examples

#### Example 1

- **Input:** `animals = [{"name": "Tatiana", "species": "Snake", "age": 98, "weight": 464}, {"name": "Khaled", "species": "Giraffe", "age": 50, "weight": 41}, {"name": "Alex", "species": "Leopard", "age": 6, "weight": 328}, {"name": "Jonathan", "species": "Monkey", "age": 45, "weight": 463}, {"name": "Stefan", "species": "Bear", "age": 100, "weight": 50}, {"name": "Tommy", "species": "Panda", "age": 26, "weight": 349}]`
- **Output:** `[{"name": "Tatiana"}, {"name": "Jonathan"}, {"name": "Tommy"}, {"name": "Alex"}]`

#### Example 2

- **Input:** `animals = [{"name": "Moose", "species": "Mammal", "age": 8, "weight": 101}, {"name": "Wolf", "species": "Mammal", "age": 5, "weight": 100}, {"name": "Fox", "species": "Mammal", "age": 3, "weight": 99}, {"name": "Bison", "species": "Mammal", "age": 12, "weight": 430}]`
- **Output:** `[{"name": "Bison"}, {"name": "Moose"}]`

#### Example 3

- **Input:** `animals = [{"name": "Rabbit", "species": "Mammal", "age": 2, "weight": 4}, {"name": "Eagle", "species": "Bird", "age": 7, "weight": 7}]`
- **Output:** `[]`
