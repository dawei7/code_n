# Trip

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRIP |
| Difficulty Rating | 2005 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [TRIP](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/TRIP) |

---

## Problem Statement

You are starting out on a long (really long) trip. On the way, there are N gas stations, the locations of which are given as a_1,a_2,...,a_N. Initially you are located at the gas station at a_1, and your destination is at location a_N. Your car can only store enough fuel to travel atmost M units without refilling. You can stop at any station and refill the car by any amount. Now you wish to plan your trip such that the number of intermediate stops needed to reach the destination is minimum, and also how many ways are there to plan your trip accordingly.

###
Input :

The first line two space seperated integers N and M. N lines follow, and the ith line has the value a_i (0 <= a_i <= 1000000000). The input will be such that a solution will always exist.

###
Output :

Output two space seperated integers : The least number of stops, and the number of ways to plan the trip which uses the least number of stops. Output this value modulo 1000000007.

###
Constraints :
`
2 <= N <= 1000000
1 <= M <= 1000
a_1 < a_2 < .. < a_N

`

---

## Examples

**Example 1**

**Input**

```text
6 3
0
1
3
4
7
10
```

**Output**

```text
3 2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/TRIP/)

[Contest](http://www.codechef.com/APRIL10/problems/TRIP/)

### DIFFICULTY

EASY

### EXPLANATION

It is easy to see that in order to make the least number of stops, one should cover as much distance as possible each time. We can compute this in linear time, by maintaining two pointers p1 and p2 such that a[p2] - a[p1] <= M, but a[p2+1] - a[p1] > M. We can decrement p1 and adjust p2 accordingly.

Thus we get get for each point i, dp[i], which is the minimum number of steps to reach the destination from location i. To count the number of ways,  we have dp[i] = sum dp[j], such that dp[j] = dp[i+1], and a[j] - a[i] <= M. We can easily compute the dp[] array in linear time as well.

</details>
