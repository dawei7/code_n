# Car Fleet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 853 |
| Difficulty | Medium |
| Topics | Array, Stack, Sorting, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/car-fleet/) |

## Problem Description
### Goal
There are $n$ cars traveling from distinct starting positions toward mile `target`. Arrays `position` and `speed` give each car's starting mile and constant speed. No car may pass another car. When a faster car catches a car or fleet ahead, they continue together at the minimum speed among their members.

A car fleet is either one car or cars traveling together. A catch that occurs exactly at `target` still joins the cars into one fleet. Return the number of distinct fleets that reach the destination.

### Function Contract
**Inputs**

- `target`: the destination mile, where $0 < \texttt{target} \leq 10^6$.
- `position`: $n$ unique starting positions satisfying $0 \leq \texttt{position[i]} < \texttt{target}$.
- `speed`: $n$ positive speeds paired by index with `position`, where $1 \leq n \leq 10^5$ and $0 < \texttt{speed[i]} \leq 10^6$.

**Return value**

Return the number of car fleets that arrive at `target`.

### Examples
**Example 1**

- Input: `target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]`
- Output: `3`

The cars at positions `10` and `8` meet at the target, the cars at `5` and `3` merge earlier, and the car at `0` remains alone.

**Example 2**

- Input: `target = 10, position = [3], speed = [3]`
- Output: `1`

**Example 3**

- Input: `target = 100, position = [0,2,4], speed = [4,2,1]`
- Output: `1`

The rear cars successively catch the slower car ahead.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Process cars in road order, not input order**

Sort paired positions and speeds by position from closest to farthest from `target`. For a car at position $p$ with speed $v$, its unobstructed arrival time is

$$
t = \frac{\texttt{target}-p}{v}.
$$

The closest car begins the first fleet. While moving backward through the sorted cars, compare each arrival time with the arrival time of the nearest fleet ahead.

If the rear car's time is less than or equal to the fleet's time, it catches that fleet before or exactly at the destination and contributes no new fleet. If its time is greater, it cannot catch the fleet ahead, so it begins another fleet and becomes the new comparison time for still farther cars.

**Compare arrival times exactly**

Store the fleet time as a distance numerator and speed denominator. To test whether a car's time is greater, compare `distance * fleet_speed` with `fleet_distance * car_speed`. All quantities are positive, so cross multiplication preserves the inequality and avoids floating-point rounding near equal arrival times.

After processing the closest prefix, the stored fleet time is the slowest effective arrival boundary visible to the next rear car. The no-passing rule means that car can affect only that nearest fleet first. Thus each strict increase in arrival time identifies exactly one fleet, while every non-increase merges into the fleet ahead.

#### Complexity detail

Sorting the $n$ cars takes $O(n\log n)$ time, and the subsequent scan is $O(n)$. The sorted list of position-speed pairs uses $O(n)$ space.

#### Alternatives and edge cases

- **Monotonic stack of arrival times:** Push times in position order and merge non-increasing rear times; it expresses the same rule in $O(n\log n)$ time after sorting.
- **Floating-point times:** Usually convenient, but exact cross multiplication handles simultaneous arrivals without precision concerns.
- **Quadratic comparison sorting:** Selection or bubble sort preserves correctness but raises the total time to $O(n^2)$.
- **Single car:** It forms one fleet by itself.
- **Catch at the destination:** Equal arrival times count as one fleet, so only a strictly greater rear time starts another.
- **Faster rear car:** A smaller unobstructed arrival time means it must slow to the fleet ahead.
- **Slower rear car:** A larger arrival time means it never catches that fleet and remains separate.
- **Cascading merges:** Once a car joins a fleet, the fleet ahead's arrival time remains the comparison boundary for farther cars.
- **Unsorted input:** Position and speed must remain paired during sorting.
- **Unique positions:** No two cars begin side by side, as guaranteed by the contract.

</details>
