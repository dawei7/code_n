# Design Parking System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1603 |
| Difficulty | Easy |
| Topics | Design, Simulation, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/design-parking-system/) |

## Problem Description
### Goal
Design a parking lot with three independent kinds of spaces: big, medium, and small. The constructor receives the fixed number of spaces of each kind. Car types `1`, `2`, and `3` represent big, medium, and small cars respectively.

When `addCar(carType)` is called, the arriving car may use only a space of its matching type. If at least one such space remains, occupy one permanently and return `true`. If none remains, leave the state unchanged and return `false`.

### Function Contract
**Platform interface**

- `ParkingSystem(big, medium, small)` initializes the three capacities.
- `addCar(carType)` attempts one arrival and returns whether it parked.
- Capacities lie in $[0,1000]$, `carType` is in `{1,2,3}`, and at most 1000 additions occur.

**Inputs**

- `big`, `medium`, and `small`: the initial capacities for the corresponding space types.
- `carTypes`: the app-local ordered sequence of car types passed to `addCar`.

**Return value**

Return one Boolean per arrival, preserving call order.

### Examples
**Example 1**

- Input: `big = 1`, `medium = 1`, `small = 0`, `carTypes = [1,2,3,1]`
- Output: `[true,true,false,false]`

**Example 2**

- Input: all capacities are zero and `carTypes = [1,2,3]`.
- Output: `[false,false,false]`

**Example 3**

- Input: `big = 0`, `medium = 0`, `small = 2`, `carTypes = [3,3,3]`
- Output: `[true,true,false]`
