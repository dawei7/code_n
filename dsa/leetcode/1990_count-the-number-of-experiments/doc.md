# Count the Number of Experiments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1990 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-experiments/) |

## Problem Description
### Goal
The `Experiments` table records individual experiments by unique identifier.
Every row uses one of three platforms—`Android`, `IOS`, or `Web`—and one of
three experiment names—`Reading`, `Sports`, or `Programming`.

Report the number of recorded experiments for every one of the nine possible
platform-and-name combinations. A combination must still appear with count `0`
when no input row uses it. Return the result rows in any order.

### Function Contract
**Inputs**

- `Experiments(experiment_id, platform, experiment_name)`: `experiment_id` is
  unique; `platform` belongs to `{Android, IOS, Web}` and `experiment_name`
  belongs to `{Reading, Sports, Programming}`.
- Let $N$ be the number of rows in `Experiments`.

**Return value**

- A nine-row table with columns `platform`, `experiment_name`, and
  `num_experiments`.
- Each platform-and-name pair occurs exactly once, and its count includes every
  matching input row.
- Result-row order is irrelevant.

### Examples
**Example 1**

For experiments `(IOS, Programming)`, `(IOS, Sports)`,
`(Android, Reading)`, two copies of `(Web, Reading)`, and
`(Web, Programming)`, the output is:

| platform | experiment_name | num_experiments |
|---|---|---:|
| Android | Reading | 1 |
| Android | Sports | 0 |
| Android | Programming | 0 |
| IOS | Reading | 0 |
| IOS | Sports | 1 |
| IOS | Programming | 1 |
| Web | Reading | 2 |
| Web | Sports | 0 |
| Web | Programming | 1 |

**Example 2**

- Input: one `(Android, Sports)` row
- Output: count `1` for `(Android, Sports)` and `0` for the other eight pairs.

**Example 3**

- Input: three `(Web, Programming)` rows
- Output: count `3` for that pair and `0` for every other pair.
