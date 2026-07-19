# Big Countries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 595 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/big-countries/) |

## Problem Description
### Goal
Given a `World` table containing each country's name, continent, area, population, and GDP, classify a country as big when its area is at least `3,000,000` square kilometers or its population is at least `25,000,000`.

Return the `name`, `population`, and `area` of every big country in any order. The two thresholds are inclusive and joined by `or`, so meeting either condition is sufficient; a country does not need to satisfy both, and values exactly equal to a threshold qualify.

### Function Contract
**Inputs**

- `World(name, continent, area, population, gdp)`: country statistics

**Return value**

- Columns `name`, `population`, and `area` for every country satisfying either inclusive threshold

### Examples
**Example 1**

- Input: a country has area `3,000,000`
- Output: that country's name, population, and area

**Example 2**

- Input: a country has population `25,000,000` but smaller area
- Output: that country

**Example 3**

- Input: both measures are below their thresholds
- Output: no row for that country
