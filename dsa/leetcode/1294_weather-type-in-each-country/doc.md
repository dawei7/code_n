# Weather Type in Each Country

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1294 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/weather-type-in-each-country/) |

## Problem Description
### Goal
The `Countries` table maps country identifiers to names, while `Weather` records a country's weather state on a particular day. For each country having weather records during November 2019, compute the average `weather_state` over that month only.

Classify an average at most 15 as `"Cold"`, an average at least 25 as `"Hot"`, and every average strictly between those boundaries as `"Warm"`. Return each qualifying `country_name` with its `weather_type`; countries without a November 2019 record are omitted.

### Function Contract
**Inputs**

- `Countries(country_id, country_name)`: one row per country.
- `Weather(country_id, weather_state, day)`: dated integer weather observations.
- Let $C$ be the number of country rows and $W$ the number of weather rows.

**Return value**

A relation with columns `country_name` and `weather_type`, containing one classified row for each country represented in the November 2019 observations.

### Examples
**Example 1**

- Input: USA has one November value of 15; Australia has values $-2$, $0$, and $3$.
- Output: `[["Australia","Cold"],["USA","Cold"]]`

**Example 2**

- Input: China has November values `[16,18,21]`.
- Output: `[["China","Warm"]]`

**Example 3**

- Input: Morocco has November values `[25,27,31]`.
- Output: `[["Morocco","Hot"]]`

### Required Complexity
- **Time:** $O(C+W)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

Join `Countries` with `Weather` by `country_id`, then filter observations to dates from `2019-11-01` through `2019-11-30`, inclusive. Group the retained rows by country so `AVG(weather_state)` describes exactly that country's target month.

A `CASE` expression maps the grouped average to the three required labels. Test the cold boundary first with `<= 15`, the hot boundary with `>= 25`, and use `ELSE` for the open interval between them. Because the join is inner and the date predicate is applied before grouping, a country without a qualifying observation cannot produce an output row. Ordering by country name is added only to make local results deterministic.

#### Complexity detail

Under the standard hash join and hash aggregation model, scanning $C$ country rows and $W$ weather rows takes $O(C+W)$ expected time. The country lookup and grouped accumulators use $O(C)$ working space in the worst case. Physical database plans may use indexes or sorting, but the query does not rescan the weather table per country.

#### Alternatives and edge cases

- **Correlated average per country:** A scalar subquery can express the classification but may rescan all $W$ observations for each of $C$ countries, taking $O(CW)$ time.
- **Filter after aggregation:** Averaging all dates and then filtering cannot recover the November-only average.
- **Boundary average 15:** It is classified as `"Cold"`, not `"Warm"`.
- **Boundary average 25:** It is classified as `"Hot"`, not `"Warm"`.
- **No November observations:** The country must be absent rather than assigned a label from a null average.

</details>
