# Traffic Light Controlled Intersection

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1279 |
| Difficulty | Easy |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/traffic-light-controlled-intersection/) |

## Problem Description

### Goal

Road A and Road B cross at one intersection. Directions $1$ and $2$ travel on Road A, while directions $3$ and $4$ travel on Road B. Each road has a traffic light, and exactly one road is green at a time. Initially Road A is green and Road B is red. Cars on different roads must never cross simultaneously.

Implement a deadlock-free `TrafficLight` controller whose `carArrived` method may be called concurrently whenever a car reaches the intersection. If the arriving car's road is already green, let it cross without changing the light. Otherwise call `turnGreen` exactly once to give that road the green light, then call `crossCar`. Calling `turnGreen` for a road that is already green is invalid.

### Function Contract

**Inputs**

- Construct one `TrafficLight` instance for an intersection that begins with Road A, identified by `1`, green.
- `carArrived(carId, roadId, direction, turnGreen, crossCar)` receives a unique car identifier, its road (`1` or `2`), its direction from $1$ through $4$, and two judge callbacks.
- The judge invokes the method concurrently for between $1$ and $20$ cars. Arrival times are non-decreasing, and equal times may create simultaneous calls.

**Return value**

- `carArrived` returns no value. It must invoke `crossCar` once for its car, invoke `turnGreen` only when switching roads, prevent cars from different roads from crossing together, and allow all calls to finish without deadlock.

### Examples

**Example 1**

- Input: `cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrival_times = [10,20,30,40,50]`
- Output: cars `1,3,5` cross on Road A; the light changes to Road B; then cars `2,4` cross.

**Example 2**

- Input: `cars = [1,2,3,4,5], directions = [2,4,3,3,1], arrival_times = [10,20,30,40,40]`
- Output: every car crosses once, with a light change before any car uses the currently red road and no cross-road overlap.

**Example 3**

- Input: `cars = [7], directions = [3], arrival_times = [0]`
- Output: the light changes from Road A to Road B, then car `7` crosses.
