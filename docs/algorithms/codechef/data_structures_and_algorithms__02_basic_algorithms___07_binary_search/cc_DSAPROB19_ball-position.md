# Ball Position

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAPROB19 |
| Difficulty Band | Binary Search |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to binary search |
| Official Link | [DSAPROB19](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSAPROB19) |

---

## Problem Statement

You are given $K$ electromagnetic balls that need to be placed on $N$ coordinates on a number line. These balls attract each other, so you need to place them as far apart as possible.

Your task is to determine the maximum possible value of the minimum distance between any two balls after placing all $K$ balls optimally on the given coordinates.

For example, given the coordinates [1, 2, 8, 4, 9] and $K=3$ balls, you need to place the balls in such a way that they are as far apart as possible. By sorting the coordinates, we get [1, 2, 4, 8, 9]. Placing the balls at positions 1, 4, and 8 maximizes the minimum distance between any two balls, which is 3. Hence, the maximum possible value of the minimum distance between any two balls is 3.

Return the minimum distance between any two balls.

---

## Input Format

- The first line contains two integers $N$ and $K$.
- The second line contains $N$ unique integers $pos[i]$, the coordinates on the number line.

---

## Output Format

- Output a single integer representing the maximum minimum distance between any two balls.

---

## Constraints

- $ 2 \leq K \leq N $
- $ 2 \leq N \leq 10^5 $
- $ -10^9 \leq pos[i] \leq 10^9 $

---

## Examples

**Example 1**

**Input**

```text
6 4
1 2 4 8 9 12
```

**Output**

```text
3
```

**Explanation**

The optimal placement of the balls is at positions 1, 4, 8, and 12. The minimum distance between any two balls is 3.

**Example 2**

**Input**

```text
5 3
1 2 8 4 9
```

**Output**

```text
3
```

**Explanation**

The optimal placement of the balls is at positions 1, 4, and 8. The minimum distance between any two balls is 3.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Ball Position](https://www.codechef.com/learn/course/undefined/TCTESTJULY/problems/DSAPROB19)

**Problem Statement:**

You are given `K` electromagnetic balls that need to be placed on `N` coordinates on a number line. These balls attract each other, so the goal is to place them as far apart as possible.

Your task is to find the maximum possible value of the minimum distance between any two balls after placing all `K` balls on the given coordinates optimally.

**Approach:**

The key idea is to maximize the minimum distance between `K` electromagnetic balls placed on `N` sorted coordinates. The solution leverages binary search on possible distances combined with a greedy placement strategy to determine if the placement of balls is feasible for a given minimum distance.

-

**Sorting:** First, sort the coordinates so that we can attempt placing balls sequentially in increasing order.

-

**Binary Search on Minimum Distance:** Perform binary search on the possible minimum distances between balls, ranging from `0` to the maximum distance (difference between the smallest and largest coordinates).

-

**Greedy Placement Check:** For each midpoint `mid` (in the binary search), use a greedy method to check if we can place all `K` balls such that the distance between any two consecutive balls is at least `mid`. Start placing the first ball at the first position and place subsequent balls at the next available position that maintains at least mid distance from the last placed ball.

-

**Adjust Search:** If the placement is successful for `mid`, try for a larger distance by moving the left boundary of the search to `mid + 1`.

If unsuccessful, reduce the right boundary to `mid - 1` to check for smaller distances.

-

**Final Result:** The largest `mid` for which the placement is feasible gives the maximum possible minimum distance.

**Time Complexity:**

The overall time complexity is `O(Nlog⁡(N) + Nlog(⁡maxDistance))`, where sorting positions takes `O(Nlog⁡(N))`, the binary search runs in `O(log⁡(maxDistance))`, and the helper function check runs in `O(N)` for each binary search step.

**Space Complexity:**

The space complexity is `O(N)`, since we are using an additional array to store the positions

</details>
