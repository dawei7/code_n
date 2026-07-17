# Car Fleet II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1776 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Stack, Heap (Priority Queue), Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/car-fleet-ii/) |

## Problem Description

### Goal

There are $n$ cars moving in the same direction on a one-lane road. `cars[i] = [position_i, speed_i]` gives car $i$'s initial position in meters and speed in meters per second. Positions are strictly increasing, so the array lists cars from back to front.

Treat every car as a point. When cars occupy the same position, they form one fleet at that position and continue at the initial speed of the slowest car in the fleet. For every original car, return the time at which it first collides with the next car or fleet ahead. Use `-1` if that collision never occurs. A returned time within $10^{-5}$ of the exact value is accepted.

### Function Contract

**Inputs**

- `cars`: an array of $n$ pairs `[position, speed]`.
- Positions are strictly increasing.
- The constraints guarantee $1 \le n \le 10^5$ and $1 \le \text{position}, \text{speed} \le 10^6$.

**Return value**

Return an array of $n$ floating-point collision times. Entry $i$ is car $i$'s first collision time, or `-1.0` when it never catches a car or fleet ahead.

### Examples

**Example 1**

- Input: `cars = [[1,2],[2,1],[4,3],[7,2]]`
- Output: `[1.0,-1.0,3.0,-1.0]`
- Explanation: Cars `0` and `2` catch their respective next cars after one and three seconds.

**Example 2**

- Input: `cars = [[3,4],[5,4],[6,3],[9,1]]`
- Output: `[2.0,1.0,1.5,-1.0]`
- Explanation: The collision schedule accounts for fleets that form before a car farther back arrives.

**Example 3**

- Input: `cars = [[1,1],[2,2],[3,3]]`
- Output: `[-1.0,-1.0,-1.0]`
- Explanation: Every car ahead is faster, so no car catches another.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Process known futures from front to back**

Scan indices from right to left. At that point, collision times for every car ahead are already known. Maintain a stack of indices that can still be the first relevant target for a car farther back. The top is the nearest surviving candidate.

**Discard candidates that cannot be reached as themselves**

For current car $i$ and candidate $j$, a collision is impossible while both keep their present speeds if `speed_i <= speed_j`; candidate $j$ can be removed. Otherwise their direct meeting time is

$$
t = \frac{\text{position}_j-\text{position}_i}
         {\text{speed}_i-\text{speed}_j}.
$$

If $j$ never collides, this meeting is valid. If $j$ does collide, the meeting is valid only when $t$ is no later than $j$'s own collision time. When $t$ is later, $j$ will already have joined a slower fleet, so it cannot be car $i$'s first target in its current form; remove it and test the next stack candidate.

**Why the first survivor gives the answer**

Every popped candidate is unusable: it is either not slower or disappears into a fleet before the current car could reach it. The first candidate not satisfying either rejection condition remains present until the computed meeting time, so the current car really collides then. If no candidate survives, the car never collides. Pushing the current index preserves exactly the candidates needed by cars farther back.

#### Complexity detail

Each index is pushed once and popped at most once. Although one iteration may pop several candidates, the total number of stack operations is $O(n)$, giving $O(n)$ time. The answer and stack arrays each use $O(n)$ space.

#### Alternatives and edge cases

- **Quadratic forward search:** For each car, examine every car ahead and use already-computed collision times to find the first valid target. It follows the same collision condition but takes $O(n^2)$ time.
- **Event priority queue:** Schedule adjacent fleet collisions and update neighboring events after every merge. This can achieve $O(n\log n)$ time but requires careful stale-event handling.
- Equal speeds never produce a future collision unless the cars are already together, which strict initial positions exclude.
- Several cars can collide at exactly the same time; the comparison must allow `t == collision_times[j]`.
- A candidate that collides earlier than the current car could reach it must be skipped even if its current speed is lower.
- The frontmost car always has answer `-1.0`.

</details>
