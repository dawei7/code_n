# Investments in 2016

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 585 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/investments-in-2016/) |

## Problem Description
### Goal
Given an `Insurance` table of policy identifiers, total investment values for 2015 and 2016, and geographic coordinates, report the sum of `tiv_2016` for policies satisfying two conditions. A qualifying policy's `tiv_2015` must be shared by at least one other policyholder, while its exact `(lat, lon)` location must not be shared by any other policyholder.

Sum only the 2016 values of rows meeting both conditions and return the result as `tiv_2016`, rounded to two decimal places. Sharing only a latitude or only a longitude does not make a location duplicate; the coordinate pair is the location key.

### Function Contract
**Inputs**

- `Insurance(pid, tiv_2015, tiv_2016, lat, lon)`: insurance policy values and coordinates

**Return value**

- A one-row result grid with column `tiv_2016`
- Include a policy only when its `tiv_2015` appears more than once and its exact `(lat, lon)` pair appears once
- Round the qualifying 2016-value sum to two decimal places

### Examples
**Example 1**

- Input: two policies share `tiv_2015 = 10` and occupy different unique locations
- Output: the sum of both `tiv_2016` values

**Example 2**

- Input: a policy shares its 2015 value but also shares its location
- Output: that policy is excluded

**Example 3**

- Input: a policy has a unique location but a unique 2015 value
- Output: that policy is excluded
