# Push Dominoes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 838 |
| Difficulty | Medium |
| Topics | Two Pointers, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/push-dominoes/) |

## Problem Description
### Goal
A line contains `n` upright dominoes. Initially, some are pushed left and some are pushed right at the same time. After each second, every domino falling left pushes its adjacent upright neighbor on the left, and every domino falling right similarly pushes the adjacent upright neighbor on the right.

If an upright domino receives equal falling forces from both sides, it stays upright. A falling domino exerts no additional force on a domino that is already falling or has fallen. The input string uses `L` for an initial left push, `R` for an initial right push, and `.` for no push. Return the final state after all effects finish.

### Function Contract
**Inputs**

- `dominoes`: a string of length $n$ containing only `L`, `R`, and `.`, where $1 \leq n \leq 10^5$.

**Return value**

Return a string of the same length describing every domino's final left-fallen, right-fallen, or upright state.

### Examples
**Example 1**

- Input: `dominoes = "RR.L"`
- Output: `"RR.L"`

The rightward force has no additional effect on a domino already falling right, and the middle upright domino is balanced.

**Example 2**

- Input: `dominoes = ".L.R...LR..L.."`
- Output: `"LL.RR.LLRRLL.."`

**Example 3**

- Input: `dominoes = "R...L"`
- Output: `"RR.LL"`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Only neighboring explicit forces govern a gap**

Add a virtual `L` just before the string and a virtual `R` just after it. These sentinels express that dots before the first `L` fall left, dots after the last `R` fall right, and otherwise no outside force enters the line. Scan consecutive non-dot symbols and resolve the dots between them as one independent segment.

For boundary forces `L...L` or `R...R`, every intervening domino falls in that shared direction. Between `L...R`, the forces point away from the gap, so every dot stays upright. Between `R...L`, forces move inward at equal speed: fill the left half with `R`, the right half with `L`, and retain one central `.` exactly when the gap length is odd.

The initially pushed symbols themselves never change. Every dot lies in exactly one segment between consecutive forces, and the four boundary-direction combinations exhaust all possibilities. The segment rule matches the arrival time and direction of the nearest possible forces, including equal-time cancellation, so concatenating the resolved segments yields the unique final state.

#### Complexity detail

The scan visits every input symbol once, and the total number of generated output characters is $n$. This gives $O(n)$ time. The sentinel string and output pieces together use $O(n)$ space.

#### Alternatives and edge cases

- **Simulate one second at a time:** Applying simultaneous updates across the whole line until stable is correct, but a single force crossing a long dot run can require $O(n)$ rounds of $O(n)$ scanning, for $O(n^2)$ time.
- **Two directional force arrays:** Left-to-right and right-to-left passes can record arrival distances and compare them at each domino, also achieving $O(n)$ time with $O(n)$ space.
- **All upright:** With no real force, the virtual `L...R` pair leaves every domino as `.`.
- **Outward forces:** A segment `L...R` remains upright because neither force enters the gap.
- **Odd inward gap:** In `R...L`, the middle domino receives both forces simultaneously and stays upright.
- **Already falling neighbor:** A force does not pass through as an extra instantaneous push; propagation still advances only one adjacent upright domino per second.

</details>
