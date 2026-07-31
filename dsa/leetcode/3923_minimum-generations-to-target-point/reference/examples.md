## Examples

**Example 1**

- Input: `points = [[0,0,0],[6,6,6]], target = [3,3,3]`
- Output: `1`
- **Explanation:**
  - Generation $0$ contains `[[0,0,0],[6,6,6]]`, not the target.
  - In generation $1$, the only pair produces `[3,3,3]`.
  - The available points are then `[[0,0,0],[6,6,6],[3,3,3]]`, so the first target generation is $1$.

**Example 2**

- Input: `points = [[0,0,0],[5,5,5]], target = [1,1,1]`
- Output: `2`
- **Explanation:**
  - Generation $0$ is `[[0,0,0],[5,5,5]]`; it does not contain the target.
  - Their generation-$1$ midpoint is `[2,2,2]`, leaving `[[0,0,0],[5,5,5],[2,2,2]]` available.
  - Generation $2$ considers all three pairs. They produce `[2,2,2]`, `[1,1,1]`, and `[3,3,3]`, respectively.
  - After adding the new points, the available list is `[[0,0,0],[5,5,5],[2,2,2],[1,1,1],[3,3,3]]`. The target first appears in generation $2$.

**Example 3**

- Input: `points = [[0,0,0],[2,2,2],[3,3,3]], target = [2,2,2]`
- Output: `0`
- **Explanation:** The target is one of the initial generation-$0$ points, so no generated midpoint is needed.

**Example 4**

- Input: `points = [[1,2,3]], target = [5,5,5]`
- Output: `-1`
- **Explanation:** A single initial point provides no pair of distinct points. No later generation can contain anything new, so the target is impossible.
