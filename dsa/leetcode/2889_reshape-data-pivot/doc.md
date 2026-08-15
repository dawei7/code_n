# Reshape Data: Pivot

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2889 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/reshape-data-pivot/) |

## Problem Description

### Goal

A weather DataFrame stores observations in long form. Each row contains a `city`, a `month`, and the integer `temperature` recorded for that city-month pair. The same month therefore appears in multiple rows, once for each represented city.

Pivot this data into a wide table in which each row represents one month and each distinct city becomes its own temperature column. Place the corresponding temperature at the intersection of its month and city, preserving the exact recorded values. The result exposes `month` first, followed by the city columns.

### Function Contract

**Inputs**

- `weather`: A pandas DataFrame with object columns `city` and `month`, plus an integer column `temperature`; each city-month pair identifies one temperature.

Let $r$ be the number of observations, $c$ the number of distinct cities, and $m$ the number of distinct months.

**Return value**

Return the pivoted DataFrame with one row per month, one column per city, and each temperature placed at its matching month-city intersection.

### Examples

#### Example 1

- **Input:** `weather = [{"city": "Jacksonville", "month": "January", "temperature": 13}, {"city": "Jacksonville", "month": "February", "temperature": 23}, {"city": "Jacksonville", "month": "March", "temperature": 38}, {"city": "Jacksonville", "month": "April", "temperature": 5}, {"city": "Jacksonville", "month": "May", "temperature": 34}, {"city": "ElPaso", "month": "January", "temperature": 20}, {"city": "ElPaso", "month": "February", "temperature": 6}, {"city": "ElPaso", "month": "March", "temperature": 26}, {"city": "ElPaso", "month": "April", "temperature": 2}, {"city": "ElPaso", "month": "May", "temperature": 43}]`
- **Output:** `[{"month": "April", "ElPaso": 2, "Jacksonville": 5}, {"month": "February", "ElPaso": 6, "Jacksonville": 23}, {"month": "January", "ElPaso": 20, "Jacksonville": 13}, {"month": "March", "ElPaso": 26, "Jacksonville": 38}, {"month": "May", "ElPaso": 43, "Jacksonville": 34}]`

#### Example 2

- **Input:** `weather = [{"city": "Oslo", "month": "June", "temperature": 17}, {"city": "Oslo", "month": "January", "temperature": -4}]`
- **Output:** `[{"month": "January", "Oslo": -4}, {"month": "June", "Oslo": 17}]`

#### Example 3

- **Input:** `weather = [{"city": "Rome", "month": "March", "temperature": 15}, {"city": "Bern", "month": "January", "temperature": -2}, {"city": "Rome", "month": "January", "temperature": 8}, {"city": "Bern", "month": "March", "temperature": 7}]`
- **Output:** `[{"month": "January", "Bern": -2, "Rome": 8}, {"month": "March", "Bern": 7, "Rome": 15}]`
