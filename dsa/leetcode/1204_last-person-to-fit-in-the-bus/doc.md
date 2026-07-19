# Last Person to Fit in the Bus

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1204 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/last-person-to-fit-in-the-bus/) |

## Problem Description

### Goal

The `Queue` table describes every person waiting to board a bus. Both `person_id` and `turn` contain each integer from 1 through the number of rows exactly once. A smaller `turn` means that the person boards earlier, and `weight` records that person's weight in kilograms. Only one person boards at each turn.

The bus has a weight limit of 1000 kilograms, so boarding stops before the first person whose addition would make the accumulated weight exceed that limit. Find the `person_name` of the last person who can board. The test data guarantees that the first person fits.

### Function Contract

**Input table**

- `Queue(person_id, person_name, weight, turn)`: `person_id` is unique; `person_id` and `turn` are both permutations of the integers from 1 through $n$.
- Let $n$ be the number of people in the queue.

**Return value**

- One row with the column `person_name`, identifying the last person whose cumulative weight in `turn` order is at most 1000 kilograms.

### Examples

**Example 1**

`Queue`

| person_id | person_name | weight | turn |
|---:|---|---:|---:|
| 5 | Alice | 250 | 1 |
| 4 | Bob | 175 | 5 |
| 3 | Alex | 350 | 2 |
| 6 | John Cena | 400 | 3 |
| 1 | Winston | 500 | 6 |
| 2 | Marie | 200 | 4 |

Output:

| person_name |
|---|
| John Cena |

In boarding order, the cumulative weights are 250, 600, and 1000 through John Cena. Adding Marie would raise the total to 1200, so John Cena is the last person who fits.

**Example 2**

If the first person's weight is exactly 1000, that person is returned and nobody later in the queue can board.

**Example 3**

The physical row order of `Queue` does not determine boarding order; only `turn` does.
