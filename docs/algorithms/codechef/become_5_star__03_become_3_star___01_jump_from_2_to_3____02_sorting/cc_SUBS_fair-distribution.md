# Fair distribution

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBS |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [SUBS](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/SUBS) |

---

## Problem Statement

Given an array  $A_1, A_2, .., A_N$  of size $N$ and an integer $K$.
You want to choose $K$ elements from array $A$ such that difference between maximum and minimum element ( from chosen elements) is minimum.

### Input
- The first line of input contains one integer $T$.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line of each test case contains $N$ space-separated integers $A_i$.

### Output
For each test case, print a single line containing one integer —  difference between maximum and minimum element.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $1 \le K \le N$
- $0 \le A_i \le 10^9$
- Sum of $N$ over all test cases doesn't exceed $2*10^6$

### Subtasks
**Subtask #1 (10 points):**
- $1 \le N \le 20$

**Subtask #2 (30 points):**
- $1 \le N \le 1000$

**Subtask #3 (60 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
4 3
1 2 4 7
4 2
2 4 1 7
5 4
1 5 44 20 40
```

**Output**

```text
3
1
39
```

**Explanation**

**Example case 1:**
All possible ways of choosing are,
$(1,2,4) = 4-1 =3$
$(1,2,7) = 7-1 =6$
$(1,4,7) = 7-1 =6$
$(2,4,7) = 7-2 =5$ .
Hence answer is $3$

**Example case 2:**
All possible ways of choosing are,
$(2,4) = 4-2 = 2$
$(2,1) = 2-1 = 1$
$(2,7) = 7-2 = 5$
$(4,1) = 4-1 = 3$
$(4,7) = 7-4 = 2$
$(1,7) = 7-1 = 6$
Hence answer is $1$

**Example case 3:**
Optimal way to choose is  $( 5, 44, 20, 40) = 44-5 = 39$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 3
1 2 4 7
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4 2
2 4 1 7
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5 4
1 5 44 20 40
```

**Output for this case**

```text
39
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Fair distribution Practice Problem in Jump from 2* to 3*](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/SUBS)

### [](#problem-statement-1)Problem Statement:

Given an array A_1,A_2,..,A_N of size N and an integer K. You want to choose K elements from array A such that difference between maximum and minimum element ( from chosen elements) is minimum.

### [](#approach-2)Approach:

- **Sort the array**: Sorting arranges the elements in increasing order, and consecutive elements in this sorted array are more likely to have the smallest differences.

- **Sliding Window of Size K**: Once the array is sorted, the problem reduces to finding the minimum difference between the first and last elements of any consecutive subsequence of length `K`.

- **Iterate through the array**: For each possible starting index `i`, calculate the difference between the `i-th` element and the `(i + K - 1)-th` element (the `K-th` element in the subsequence).

- **Minimize the Difference**: Track the minimum of these differences.

### [](#algorithm-3)Algorithm:

- Sort the array.

- For each index `i` from `0` to `N - K`, calculate the difference between `A[i+K-1]` and `A[i]`.

- Return the minimum of these differences.

### [](#complexity-4)Complexity:

- **Time Complexity:** Sorting the array takes `O(N log N)`. The sliding window loop takes `O(N - K)` iterations, which is essentially `O(N)` in the worst case.

- **Space Complexity:**  O(1) No extra space used.

</details>
