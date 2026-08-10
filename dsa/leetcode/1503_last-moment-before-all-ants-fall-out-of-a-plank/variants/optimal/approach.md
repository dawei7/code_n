## General

**Why collisions look more complicated than they are**

At first, simulating positions, collision times, and direction changes seems necessary. The key simplification is that every ant moves at the same speed and ants are indistinguishable for the requested answer.

When a right-moving ant meets a left-moving ant, both reverse direction. Geometrically, this produces the same occupied positions over time as allowing the two ants to pass through each other. In the collision interpretation, the physical ants exchange velocities. In the pass-through interpretation, each velocity continues straight. If the ants have no identity-dependent properties, these descriptions differ only in which label is attached to each trajectory.

The question asks only when the last ant falls, not which original ant falls at that time. Swapping identities at collisions cannot change the multiset of fall times. Therefore, every initial direction can be treated as continuing straight to its corresponding edge with no collision simulation.

**Time for each straight trajectory**

An ant at position `x` moving left travels distance `x` to coordinate zero. At speed one unit per second, its fall time is `x` seconds.

An ant at position `x` moving right travels distance `n - x` to the right endpoint at coordinate `n`. Its fall time is `n - x` seconds.

The last moment is simply the maximum of all these individual straight-line times.

The stored solution initializes `ans = 0`. It scans `left` and updates `ans = max(ans, x)`. It then scans `right` and updates `ans = max(ans, n - x)`. At least one ant exists, so some candidate is considered, although zero is also a valid fall time for an ant already at the endpoint and moving outward.

**A more formal collision equivalence**

Consider the spacetime trajectories of all ants if they pass through one another. At any meeting of opposite trajectories, the physical collision rule makes the incoming ant on one line leave along the other line. This is equivalent to swapping the identities assigned to the two continuous lines.

Apply that relabeling at every collision. The set of occupied positions at every time remains identical to the pass-through system. In particular, ants reach the plank endpoints at exactly the same collection of times in both systems.

Since taking a maximum ignores identities, the largest endpoint time from the pass-through trajectories is exactly the actual last fall time.

**Why simultaneous and repeated collisions cause no issue**

The equivalence is local to every meeting and does not consume time. Repeated collisions merely perform additional identity swaps. Even if several interactions occur over an execution, no trajectory is delayed or accelerated because speed magnitude stays one.

The source therefore needs neither position updates nor event ordering. Initial location and initial direction alone determine each straight trajectory's endpoint time.

**Understanding the examples**

For a plank of length four, a left-moving ant at position four has straight fall time four. A right-moving ant at position zero also has fall time four. Other ants can collide, but no trajectory lasts longer than four seconds, so the answer is four.

If every ant moves right on a length-seven plank, the ant starting at zero has the longest distance, seven. If every ant moves left, the ant starting at seven similarly determines the answer.

**Why taking maxima separately is sufficient**

The largest left-moving time is the largest starting coordinate in `left`. The largest right-moving time is obtained from the smallest starting coordinate in `right` because `n - x` decreases as `x` grows. The code scans rather than calling `max` or `min` directly, which naturally handles either list being empty.

Finally, the maximum across both groups is the last of all fall events.

## Complexity detail

Let $L$ be the number of initially left-moving ants and $R$ the number of initially right-moving ants. The two loops inspect each ant exactly once and perform constant work, so time is $O(L+R)$.

If $A=L+R$ denotes the total number of ants, this is the manifest's $O(A)$ time. The algorithm stores only `ans` and one loop variable, using $O(1)$ auxiliary space.

No cost depends on the number of collisions, which could be much larger than the number of ants. Avoiding collision simulation is what makes the solution linear in input size.

Coordinates and times are integers because starting positions, endpoint positions, and speed are integral. The instantaneous collision assumption avoids any pause that would change travel time.

## Alternatives and edge cases

- **Event simulation:** Computing the next collision or fall repeatedly is much more complex and can be quadratic or worse; identities are irrelevant to the answer.
- **Pass-through trajectory view:** This is the essential optimal model because direction swaps between identical equal-speed ants are equivalent to identity swaps.
- **Only left-moving ants:** The answer is the maximum value in `left`.
- **Only right-moving ants:** The answer is `n` minus the minimum value in `right`.
- **Ant at coordinate zero moving left:** It falls immediately at time zero.
- **Ant at coordinate n moving right:** It also falls immediately at time zero.
- **Ants at both endpoints moving inward:** Their straight trajectories can last the full plank length, regardless of later collisions.
- **Simultaneous collisions:** They do not change the set of unlabeled trajectories or fall times.
- **Last fall shared by several ants:** Returning the common moment still satisfies the question.
- **At least one ant:** The contract guarantees the combined arrays are nonempty, so the maximum concept is defined.
- **Unique starting positions:** No two ants begin at the same coordinate, avoiding an ambiguous initial collision.
