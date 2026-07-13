# Heaters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 475 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/heaters/) |

## Problem Description
### Goal
Houses and heaters occupy integer coordinates on a one-dimensional number line. Every heater uses the same nonnegative radius `r` and covers all houses whose absolute coordinate distance from it is at most `r`.

Return the smallest common radius that ensures every house is covered by at least one heater. Each house may use its nearest heater independently, and heaters do not need to cover one another. Input coordinates may be unordered and may contain repeated locations. A house at a heater needs distance zero. The function returns only the radius, not house-to-heater assignments or coverage intervals.

### Function Contract
**Inputs**

- `houses`: house coordinates
- `heaters`: heater coordinates

**Return value**

- The minimum nonnegative integer radius shared by all heaters that covers every house

### Examples
**Example 1**

- Input: `houses = [1, 2, 3], heaters = [2]`
- Output: `1`

**Example 2**

- Input: `houses = [1, 2, 3, 4], heaters = [1, 4]`
- Output: `1`

**Example 3**

- Input: `houses = [1, 5], heaters = [2]`
- Output: `3`

### Required Complexity

- **Time:** $O((h + t) \log(h + t))$
- **Space:** $O(t)$

<details>
<summary>Approach</summary>

#### General

**Reduce the global radius to nearest-heater distances**

For each house, the smallest radius that covers it is its distance to the nearest heater. A common radius covers every house exactly when it is at least all of those local distances, so the answer is their maximum.

**Find neighboring heaters by binary search**

Sort heater positions. For a house, binary-search the first heater not left of it. Only that heater and its immediate predecessor can be nearest; every other heater lies still farther in the same direction. Take the smaller available distance and update the maximum.

**Why the maximum is both necessary and sufficient**

Any radius below the largest nearest-heater distance leaves that particular house uncovered. Choosing the largest distance covers each house by the heater that established its local minimum, so no larger radius is necessary.

#### Complexity detail

Sorting `t` heaters costs $O(t \log t)$, and `h` binary searches cost $O(h \log t)$, within $O((h + t) \log(h + t))$. The sorted copy uses $O(t)$ space.

#### Alternatives and edge cases

- **Sort houses and use two pointers:** advances a heater pointer toward the nearest position in $O(h \log h + t \log t)$ total time.
- **Binary-search the radius:** checks coverage for each candidate but adds a coordinate-range logarithm.
- **Scan every heater per house:** is correct but costs $O(h \cdot t)$ time.
- **House on a heater:** contributes distance zero.
- **House outside heater range:** only the nearest endpoint heater is available.
- **Duplicate coordinates:** do not affect nearest distances.
- **One heater:** the answer is the farther distance to the extreme houses.

</details>
