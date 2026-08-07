### Approach 1: Brute Force Enumeration + Classification Discussion

#### Intuition

Enumerate all possible combinations of land and water activities. We can either perform a land activity first and then a water activity, or perform a water activity first and then a land activity. To find the earliest completion time, we compute the optimal result for both orders and take the minimum.

Consider the order **"land first, then water"**:

* For a land activity, its completion time is:

$\textit{landStartTime}[i] + \textit{landDuration}[i]$

* When starting the water activity, there are two possible cases:

  * If the water activity is already available, we can start it immediately. The completion time is:

$\textit{finishLand} + \textit{waterDuration}[j]$

* If the water activity is not yet available, we must wait until its start time. The completion time is:

$\textit{waterStartTime}[j] + \textit{waterDuration}[j]$

These two cases can be unified as:

$\max(\textit{finishLand}, \textit{waterStartTime}[j]) + \textit{waterDuration}[j]$

We then repeat the same process for the order **"water first, then land"**.

By enumerating all possible combinations and both execution orders, we can return the minimum completion time.

#### Implementation

```python
class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        res = inf
        for i in range(n):
            for j in range(m):
                land = landStartTime[i] + landDuration[i]
                land_water = max(land, waterStartTime[j]) + waterDuration[j]
                res = min(res, land_water)

                water = waterStartTime[j] + waterDuration[j]
                water_land = max(water, landStartTime[i]) + landDuration[i]
                res = min(res, water_land)
        return res
```

#### Complexity Analysis

Let $n$ and $m$ be the lengths of the input arrays.

- Time complexity: $O(n \times m)$.

- Space complexity: $O(1)$.

---

### Approach 2: Linear Enumeration + Classification Discussion

#### Intuition

We can either perform a land activity first and then a water activity, or vice versa. To find the earliest completion time, we compute the optimal result for both orders and take the minimum.

Suppose the second activity is fixed. The final completion time is:

$\max(\textit{finish1}, \textit{start2}) + \textit{duration2}$

where:

* $\textit{finish1}$ is the completion time of the first activity.
* $\textit{start2}$ is the start time of the second activity.

Notice that this expression is non-decreasing with respect to $\textit{finish1}$. Therefore, to minimize the final completion time, we only need to consider the earliest possible completion time among all choices for the first activity.

Assume we perform a land activity first. We first find the earliest completion time among all land activities. Then, using this completion time, we traverse all water activities and compute the earliest possible overall completion time.

Finally, we reverse the order and repeat the same process for **"water first, then land"**. The smaller of the two results is the answer.

#### Implementation

```python
class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        def solve(start1, duration1, start2, duration2):
            finish1 = inf
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])
            finish2 = inf
            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1) + duration2[i])
            return finish2

        land_water = solve(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        water_land = solve(
            waterStartTime, waterDuration, landStartTime, landDuration
        )
        return min(land_water, water_land)
```

#### Complexity Analysis

Let $n$ and $m$ be the lengths of the input arrays.

- Time complexity: $O(n + m)$.

- Space complexity: $O(1)$.

---