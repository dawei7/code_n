# Find Cities in Each State

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3198 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-cities-in-each-state/) |

## Problem Description

### Goal

The `cities` table records a city together with the state that contains it. Combine all cities belonging to the same state into one comma-and-space-separated string.

Within each combined string, list city names in ascending order. Return one row per represented state, and order those rows by state name in ascending order.

Each `(state, city)` pair is unique, so every stored city contributes once to its state's list. Preserve each name exactly as stored while applying the two required ascending orders.

### Function Contract

**Input table**

- `cities(state, city)`: `state` and `city` are strings, and `(state, city)` is the composite primary key. Thus, the same city-state pair cannot occur twice.

**Return value**

- A table with columns `state` and `cities`. Each `cities` value contains that state's city names in ascending order, joined with `, `, and result rows are ordered by `state` ascending.

Let $r$ be the number of rows in `cities`.

### Examples

**Example 1**

Input:

| state | city |
|---|---|
| California | Los Angeles |
| California | San Francisco |
| California | San Diego |
| Texas | Houston |
| Texas | Austin |
| Texas | Dallas |
| New York | New York City |
| New York | Buffalo |
| New York | Rochester |

Output:

| state | cities |
|---|---|
| California | Los Angeles, San Diego, San Francisco |
| New York | Buffalo, New York City, Rochester |
| Texas | Austin, Dallas, Houston |

The state rows and the city names within each aggregate are both in ascending order.
