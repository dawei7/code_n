## General

**Replace collisions with pass-through motion.** When two identical-speed robots collide and reverse, the occupied trajectories are the same as if the robots passed through one another; only their identities are exchanged. Pairwise distance depends on occupied coordinates, not robot labels. Therefore compute each endpoint independently as `nums[i] - d` for `L` or `nums[i] + d` for `R` and ignore collision simulation entirely.

**Sum distances after sorting.** Sort the final coordinates. For a coordinate `positions[i]`, every earlier coordinate is no larger, so its total distance to those $i$ coordinates is

$$
i\cdot\texttt{positions}[i]-\sum_{j=0}^{i-1}\texttt{positions}[j].
$$

Maintain the preceding sum as `prefix`, add this contribution for each index, and then extend the prefix. Every unordered pair is counted exactly once, when its right endpoint is processed. Apply the modulus to the final sum; arbitrary-precision arithmetic in the app-local Python implementation safely holds the intermediate total.

## Complexity detail

Computing endpoints takes $O(n)$ time, sorting takes $O(n\log n)$, and the prefix pass takes $O(n)$, for $O(n\log n)$ total time. The final-coordinate array and sorting storage use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Simulate collisions:** Event simulation is unnecessary and substantially more complex, especially for simultaneous and half-step collisions.
- **Direct pair enumeration:** Computing every absolute difference is correct but takes $O(n^2)$ time.
- **Ordered multiset of trajectories:** Tracking robot identities through swaps does not change the coordinate multiset used by the answer.
- When `d = 0`, the method correctly sums distances between the original positions.
- Robots moving in the same direction undergo a common translation, which preserves their mutual distances.
- Initial `nums` need not be sorted; only computed endpoints are sorted.
- Endpoint coordinates and the unreduced pair sum may exceed 32-bit ranges, so intermediate arithmetic must be wide enough.
- Each unordered pair contributes once, never once per ordering.
