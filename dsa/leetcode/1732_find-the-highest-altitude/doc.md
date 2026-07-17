# Find the Highest Altitude

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1732 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-highest-altitude/) |

## Problem Description

### Goal

A biker travels through $n + 1$ points whose altitudes may differ. Point $0$ is the start of the trip and has altitude $0$.

The length-$n$ integer array `gain` describes the route: `gain[i]` is the net altitude change from point $i$ to point $i + 1$. Apply these changes in route order and return the highest altitude attained at any point, including the initial altitude of $0$.

### Function Contract

**Inputs**

- `gain`: an integer list of length $n$, where `gain[i]` is the net altitude change along one route segment.
- The contract guarantees $1 \le n \le 100$ and $-100 \le \texttt{gain[i]} \le 100$.

**Return value**

- Return the maximum altitude among all $n + 1$ route points, with the starting altitude included.

### Examples

**Example 1**

- Input: `gain = [-5,1,5,0,-7]`
- Output: `1`
- Explanation: The point altitudes are `0,-5,-4,1,1,-6`, whose maximum is $1$.

**Example 2**

- Input: `gain = [-4,-3,-2,-1,4,3,2]`
- Output: `0`
- Explanation: Every later altitude is below the initial altitude.

**Example 3**

- Input: `gain = [3,-1,2,-2]`
- Output: `4`
- Explanation: The altitudes are `0,3,2,4,2`, so the peak occurs before the trip ends.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Interpret altitude as a prefix sum**

After processing the first $i$ gains, the current altitude is the sum of those $i$ values. There is no need to materialize every prefix sum: keep one running altitude and add each gain as its segment is traversed.

**Include the starting point in the maximum**

Initialize the best altitude to $0$, not to the first gain. After every update, compare the new running altitude with the best value. This ensures the answer remains $0$ when the entire route stays below its starting height, while still capturing a peak at any later point.

#### Complexity detail

The scan performs one addition and one maximum comparison for each of the $n$ gains, taking $O(n)$ time. The running altitude and best altitude are the only additional values, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Build every prefix sum:** Storing all $n + 1$ altitudes and taking their maximum is correct but uses $O(n)$ extra space unnecessarily.
- **Recompute each prefix:** Summing `gain[:i]` separately for every point is correct but takes $O(n^2)$ time.
- **All negative gains:** The starting altitude $0$ is the answer because every later point is lower.
- **Zero gains:** Repeated equal altitudes remain valid candidates for the maximum.
- **Peak before the endpoint:** Tracking only the final altitude misses routes that climb and then descend.
- **Single segment:** Compare that one resulting altitude with the starting altitude.

</details>
