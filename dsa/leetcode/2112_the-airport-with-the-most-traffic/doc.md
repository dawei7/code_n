# The Airport With the Most Traffic

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2112 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [the-airport-with-the-most-traffic](https://leetcode.com/problems/the-airport-with-the-most-traffic/) |

## Problem Description

### Goal

The `Flights` table summarizes directed airport routes. Each row identifies one departure airport, one arrival airport, and the number of flights recorded for that ordered pair. The two airport columns together form the table's primary key.

An airport's traffic is the total `flights_count` over every route departing from it plus every route arriving at it. Report the `airport_id` of each airport whose traffic equals the largest total among all airports. All ties must be retained, and the result rows may appear in any order.

### Function Contract

**Inputs**

- `Flights(departure_airport, arrival_airport, flights_count)`: a relation of $N$ unique directed airport pairs and their positive aggregated flight counts.

**Return value**

- Return one `airport_id` column containing every airport tied for the maximum combined departure-and-arrival traffic. Output order is unrestricted.

### Examples

**Example 1**

- Input: `Flights = [[1,2,4],[2,1,5],[2,4,5]]`
- Output: `[[2]]`
- Explanation: Airports $1$, $2$, and $4$ have traffic $9$, $14$, and $5$, respectively.

**Example 2**

- Input: `Flights = [[1,2,4],[2,1,5],[3,4,5],[4,3,4],[5,6,7]]`
- Output: `[[1],[2],[3],[4]]`
- Explanation: Airports $1$ through $4$ each have traffic $9$, while airports $5$ and $6$ each have traffic $7$.

**Example 3**

- Input: `Flights = [[10,20,3]]`
- Output: `[[10],[20]]`
- Explanation: Both endpoints participate in the same three flights and therefore tie.
