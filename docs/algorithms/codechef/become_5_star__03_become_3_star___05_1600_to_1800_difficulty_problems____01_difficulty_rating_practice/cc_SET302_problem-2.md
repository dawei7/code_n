# Problem-2

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SET302 |
| Difficulty Rating | 1781 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [SET302](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SET302) |

---

## Problem Statement

Hrishi's daughters likes to eat laddoos a lot.

There are **N** sets of laddoos prepared for Diwali; for each **i** (1 ≤ **i** ≤ **N**), the **i**-th set contains **Ai** laddoos.

Hrishi will come home in **H** hours and his daughters want to finish all the laddoos before he returns.

His daughters can eat **K** laddoos per hour.
Each hour, they will choose some set of laddoos.
- If this set contains at least **K** laddoos, then they will eat exactly **K** ladoos from it.
- Otherwise, they eat the whole set but they wont eat from any other set during this hour.

What is the **minimum** **K** such that they are able to eat all the laddoos in **H** hours.

---

## Input Format

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains two space-separated integers **N** and **H** denoting the number of sets and the number of hours after which Hrishi will come home.

- The second line contains **N** space-separated integers **A1, A2, ..., AN**.

### Output

For each test case, print a single line containing one integer — the minimum possible value of **K**.

---

## Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 105

- **N** ≤ **H** ≤ 109

- 1 ≤ **Ai** ≤ 109 for each valid **i**

---

## Examples

**Example 1**

**Input**

```text
3
3 3
1 2 3
3 4
1 2 3
4 5
4 3 2 7
```

**Output**

```text
3
2
4
```

**Explanation**

**Test case $1$:** Daughters can choose $K = 3$ laddoos per hour. This way,
- In the first hour, they eat the set $1$ as the number of laddoos in the set is less than equal to $3$.
- In the second hour, they eat the set $2$ as the number of laddoos in the set is less than equal to $3$.
- In the third hour, they eat the set $3$ as the number of laddoos in the set is less than equal to $3$.

 They can finish eating all the laddoos in $3$ hours. It can be shown that $3$ laddoos per hour is the minimum possible speed with which they can finish all laddoos in $3$ hours.

**Test case $2$:** they can choose $K = 2$ laddoos per hour. This way,
- In the first hour, they eats the set $1$ as the number of laddoos in the set is less than equal to $2$.
- In the second hour, they eat the set $2$ as the number of laddoos in the set is less than equal to $2$.
- In the third hour, they eats the $2$ laddoos from set $3$. $1$ laddoo is left in pile $3$.
- In the fourth hour, they eats the remaining laddoo from pile $3$ as the number of laddoos in the set is less than equal to $2$.

 They can finish eating all the laddoos in $4$ hours. It can be shown that $2$ laddoos per hour is the minimum possible speed with which they can finish all laddoos in $4$ hours.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3
1 2 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3 4
1 2 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 5
4 3 2 7
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Problem-2 Practice Problem in 1600 to 1800 difficulty problems](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SET302)

### [](#problem-statement-1)Problem Statement:

The problem asks us to find the minimum number of laddoos `K` that Hrishi’s daughters can eat per hour such that they can finish all the laddoos from `N` sets within `H` hours.

### [](#approach-2)Approach:

- **Basic Insight**:

- For each set of laddoos A_i , if the daughters eat `K` laddoos per hour, the number of hours required to finish this set can be computed as: hours_needed (A_i)=(A_i+K−1)/K (integer division).The reason we use the formula is that they cannot eat a fraction of a laddoo set.

- **Binary Search for the Minimum K**:

- To find the minimum `K`, we can perform binary search over possible values of `K`.

- For each `K` in this range, we compute the total number of hours required to finish all laddoos, and check if it is less than or equal to `H`.

### [](#algorithm-3)Algorithm:

-

**Feasibility Check**: Calculate the total hours needed for a given `K`: total_hours =  \sum_{i=1}^{N} \frac{A_i + K - 1}{K} the total hours is less than or equal to `H`, then the value `K` is feasible.

-

**Binary Search**:

- Set `l=1`and `r=max⁡(A)`.

- For each midpoint ‘mid’ in the binary search range, check if it is feasible using the `check` function.

- If it’s feasible, try smaller values of `K` by setting `r=mid−1`.

- If it’s not feasible, try larger values by setting `l=mid+1`.

### [](#complexity-4)Complexity:

- **Time Complexity:** The binary search operates over the range of possible values for `K`, which is between `1` and the maximum number of laddoos in any set `O(log(max_laddoos))`. For each middle value `K` tested in the binary search, the check function iterates through the array `A`, which takes `O(N)` time. Total time complexity:  `O(N⋅log(max_laddoos))`.

- **Space Complexity:** `O(1)` No extra space required.

</details>
