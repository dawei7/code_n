# Last Moment Before All Ants Fall Out of a Plank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1503 |
| Difficulty | Medium |
| Topics | Array, Brainteaser, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/) |

## Problem Description
### Goal

A wooden plank occupies the interval from position $0$ through position $n$. Every ant walks at one unit per second. Positions in `left` identify ants initially moving toward $0$, while positions in `right` identify ants initially moving toward $n$.

When two ants moving in opposite directions meet, both reverse direction immediately without spending additional time. An ant falls as soon as it reaches either end of the plank. Determine the time at which the final ant or ants fall. Initial positions are unique across both direction arrays, but either array may be empty.

### Function Contract
**Inputs**

Let $A=\lvert\texttt{left}\rvert+\lvert\texttt{right}\rvert$.

- `n`: the plank length, with $1 \le n \le 10^4$.
- `left`: distinct positions in $[0,n]$ for ants initially moving left.
- `right`: distinct positions in $[0,n]$ for ants initially moving right.
- A position appears in at most one array, and $1 \le A \le n+1$.

**Return value**

Return the integer time when the last ant reaches an end and falls immediately.

### Examples
**Example 1**

- Input: `n = 4, left = [4,3], right = [0,1]`
- Output: `4`
- Explanation: Although collisions exchange directions, some trajectory remains on the plank until time $4$.

**Example 2**

- Input: `n = 7, left = [], right = [0,1,2,3,4,5,6,7]`
- Output: `7`
- Explanation: The right-moving ant starting at $0$ crosses the full plank; the ant at $7$ falls immediately.

**Example 3**

- Input: `n = 7, left = [0,1,2,3,4,5,6,7], right = []`
- Output: `7`
- Explanation: The left-moving ant starting at $7$ needs seven seconds to reach $0$.

### Required Complexity
- **Time:** $O(A)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Remove identities from a collision**

At a meeting, two identical-speed ants reverse directions. If the ants are indistinguishable, the same two outgoing trajectories result when they simply continue through one another: one path proceeds left and the other proceeds right. Only which physical ant follows which path changes.

The requested answer depends on the last occupied trajectory, not on ant identity. Replacing every collision by a pass-through therefore preserves the multiset of endpoint arrival times. This avoids tracking encounter order, half-integer meeting positions, or chains of collisions.

**Measure each uninterrupted trajectory**

After applying the pass-through interpretation, a left-moving trajectory from position $x$ travels distance $x$ to endpoint $0$, so it falls at time $x$. A right-moving trajectory from $x$ travels distance $n-x$ to endpoint $n$, so it falls at time $n-x$.

The latest left-moving fall is consequently `max(left)`. The latest right-moving fall is produced by the smallest starting position in `right`, equivalently `n - min(right)`. Empty direction arrays contribute zero so that the other side determines the result.

Return the larger of those two times. An ant already at the endpoint toward which it moves contributes zero, correctly representing an immediate fall.

**Why the maximum is the last real fall**

Every original ant starts one trajectory. At each collision, exchanging the ants assigned to the two continuing trajectories does not create, delete, delay, or accelerate either path. Inductively, after all collisions, the real system and pass-through model have exactly the same endpoint arrival times.

The formula computes every pass-through trajectory's remaining distance at unit speed and takes their maximum. That value is therefore both attained by at least one real ant and no smaller than any other real fall time, so it is exactly the requested last moment.

#### Complexity detail

Finding the maximum of `left` and minimum of `right` scans all $A$ ant positions once, taking $O(A)$ time. The calculation stores only a constant number of extrema and uses $O(1)$ auxiliary space.

No simulation time depends on $n$, and neither input array is modified.

#### Alternatives and edge cases

- **Second-by-second simulation:** Move every remaining ant, detect encounters, reverse directions, and remove fallen ants. It can require $O(nA)$ work and collision handling is easy to get wrong.
- **Event-driven collision simulation:** Sort ants and process meetings and endpoint events. This is more efficient than time stepping but still unnecessary because identities do not affect fall times.
- **Treat ants as passing through:** This is the chosen equivalence, not a change to the physical rule; it preserves unlabeled trajectories and endpoint arrival times exactly.
- **Only left-moving ants:** The answer is `max(left)` because each fall time equals its starting position.
- **Only right-moving ants:** The answer is `n - min(right)` because the farthest path begins closest to $0$.
- **Ant already at an outward endpoint:** Position $0$ in `left` or position $n$ in `right` contributes time zero.
- **Ant at the opposite endpoint:** Position $n$ in `left` or position $0$ in `right` requires the full $n$ seconds.
- **Several ants fall last:** Return their shared time once; ant identities and counts are not requested.
- **Meetings at half-integer times:** The trajectory equivalence avoids numerical simulation, so no floating-point representation is needed.
- **Dense occupancy:** At most one ant begins at each integer position, and a single scan still suffices.

</details>
