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

### Required Complexity
- **Time:** $O(q)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Let $q$ be the number of `addCar` calls.

**Store one counter per exact type.** Keep the remaining capacities in positions `1`, `2`, and `3` of a fixed four-element array. The unused zero position lets `carType` index its own counter directly and avoids any mapping or conditional type conversion.

For an arrival, inspect only its matching counter. Zero means the request must fail without mutation. A positive value means one correct-size space can be reserved, so decrement it and return `true`. Spaces of other sizes are never considered or changed.

Initially, each counter equals its constructor capacity. After every call, a successful arrival reduces exactly the corresponding remaining count, while a failed arrival changes none. Induction over the calls shows that each counter always equals initial spaces minus successfully parked cars of that type. The method therefore returns `true` exactly when the required matching space exists.

**Adapting the operation sequence locally.** The app creates one `ParkingSystem` and applies every value in `carTypes` to that same object, collecting the resulting Booleans. This preserves the stateful platform behavior without including a constructor placeholder in the returned trace.

#### Complexity detail

Every `addCar` performs one indexed lookup and at most one decrement, so each call is $O(1)$ and $q$ calls take $O(q)$ time. The fixed counter array uses $O(1)$ space regardless of capacity or call count; the Boolean list is required output.

#### Alternatives and edge cases

- **Store every individual space:** Searching a list for an available matching slot is correct but can take linear time per car and quadratic time over many arrivals.
- **Use one total-capacity counter:** This is incorrect because a car cannot occupy a different-sized space.
- A type may start with zero capacity, making every arrival of that type fail.
- Failed calls do not consume spaces and do not affect later calls.
- Once a type's last slot is occupied, all subsequent cars of that type fail independently of other capacities.
- Capacities and usage counts for the three types evolve independently.

</details>
