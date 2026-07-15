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

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Store the identifier of the road whose light is currently green, initialized to Road A. Protect both that state and the complete crossing operation with one mutual-exclusion lock.

When a car arrives, acquire the lock before examining the green-road state. If the car belongs to the other road, invoke `turnGreen` and update the stored road. Then invoke `crossCar` while still holding the lock and release the lock afterward. A context-managed lock ensures release even if a callback raises.

Because only the lock holder can inspect or change the light, two calls cannot both decide to perform the same switch. Holding that same lock through `crossCar` also prevents any other road from changing the light or entering the intersection during a crossing. Every holder performs only finite callback work and releases the single lock without waiting for another resource, so cyclic waiting and deadlock cannot occur.

#### Complexity detail

Each arrival performs one lock acquisition, one road comparison, at most one light callback, and one crossing callback, all $O(1)$ work with $O(1)$ stored state. A thread may wait for earlier cars, but the controller's own work per call remains constant.

The source contract fixes the workload at no more than $20$ concurrent calls. Correctness depends on mutual exclusion, callback semantics, and progress rather than asymptotic runtime, so the package uses a bounded-concurrency certificate with scheduler and deadlock regression.

#### Alternatives and edge cases

- **Separate light and crossing locks:** Releasing one before acquiring the other creates a window in which the light can change while a car is crossing.
- **Check the road outside the lock:** Concurrent cars can observe stale state and redundantly call `turnGreen`.
- **Busy waiting on a shared flag:** It wastes CPU and still needs synchronization for visibility and atomicity.
- **First car on Road B:** It must switch the initially green Road A light before crossing.
- **Consecutive cars on one road:** Only the first after a road change calls `turnGreen`; later cars cross under the existing green light.
- **Simultaneous arrivals:** Their precise order may vary, but each car must cross exactly once without different roads occupying the intersection together.

</details>
