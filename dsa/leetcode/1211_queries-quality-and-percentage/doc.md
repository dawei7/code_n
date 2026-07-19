# Queries Quality and Percentage

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1211 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/queries-quality-and-percentage/) |

## Problem Description

### Goal

The `Queries` table contains collected database-query results and may include duplicate rows. Each row has a `query_name`, a result value, its `position` from 1 through 500, and its `rating` from 1 through 5. A row is a poor query result when its rating is less than 3.

For each distinct `query_name`, compute its quality as the average of $\texttt{rating}/\texttt{position}$ across all rows with that name. Also compute its poor query percentage as 100 times the fraction of those rows whose rating is less than 3. Round both metrics to two decimal places and return the groups in any order.

### Function Contract

**Input table**

- `Queries(query_name, result, position, rating)`: Duplicate rows are allowed; $1\le\texttt{position}\le500$ and $1\le\texttt{rating}\le5$.
- Let $n$ be the row count and $g$ the number of distinct query names.

**Return value**

- One row per query name with columns `query_name`, `quality`, and `poor_query_percentage`, with both numeric metrics rounded to two decimal places.

### Examples

**Example 1**

`Queries`

| query_name | result | position | rating |
|---|---|---:|---:|
| Dog | Golden Retriever | 1 | 5 |
| Dog | German Shepherd | 2 | 5 |
| Dog | Mule | 200 | 1 |
| Cat | Shirazi | 5 | 2 |
| Cat | Siamese | 3 | 3 |
| Cat | Sphynx | 7 | 4 |

Output:

| query_name | quality | poor_query_percentage |
|---|---:|---:|
| Cat | 0.66 | 33.33 |
| Dog | 2.50 | 33.33 |

**Example 2**

A group in which no rating is below 3 has a poor query percentage of `0.00`.

**Example 3**

Duplicate table rows each contribute separately to both averages.
