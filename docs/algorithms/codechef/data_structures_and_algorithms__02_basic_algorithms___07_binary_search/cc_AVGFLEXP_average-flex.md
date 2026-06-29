# Average Flex

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AVGFLEXP |
| Difficulty Rating | 1442 |
| Difficulty Band | Binary Search |
| Path | Data Structures and Algorithms |
| Lesson | More Problems |
| Official Link | [AVGFLEXP](https://www.codechef.com/learn/course/binary-search/LIBSDSA04/problems/AVGFLEXP) |

---

## Problem Statement

There are $N$ students in a class, where the $i$-th student has a score of $A_i$.

The $i$-th student will *boast* if and only if the number of students scoring less than or equal $A_i$ is greater than the number of students scoring greater than $A_i$.

Find the number of students who will boast.

---

## Input Format

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ - the number of students.
- The second line of each test case contains $N$ integers $A_1, A_2, \dots, A_N$ - the scores of the students.

---

## Output Format

For each test case, output in a single line the number of students who will boast.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $0 \leq A_i \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
3
100 100 100
3
2 1 3
4
30 1 30 30
```

**Output**

```text
3
2
3
```

**Explanation**

- **Test case $1$:** All three students got the highest score. So all three of them will boast.
- **Test case $2$:** Only the student with score $1$ will not be able to boast.
- **Test case $3$:** Only the student with score $1$ will not be able to boast.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
100 100 100
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
2 1 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4
30 1 30 30
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Average Flex in Binary Search](https://www.codechef.com/learn/course/binary-search/LIBSDSA04/problems/AVGFLEXP)

### [](#problem-statement-1)Problem Statement:

There are N students in a class, where the i-th student has a score of A_i. The i-th student will boast if and only if the number of students scoring less than or equal to A_i is greater than the number of students scoring greater than A_i. Find the number of students who will boast.

### [](#approach-2)Approach:

- To efficiently count the number of scores less than or equal to a particular score, we sort the array of scores.

- Using upper_bound: For each student’s score $A[i]4, we find the position where A[i] would fit in the sorted array (using *upper_bound*). The distance from the beginning of the array to this iterator gives us the count of elements that are less than or equal to A[i].

- Specifically, **upper_bound(v, v+n, v[i]) - v** computes the number of students who have a score less than or equal to A[i].

- Calculate the number of students scoring greater than A[i] as n−d (where d is the count of students scoring less than or equal to A[i]).

### [](#complexity-3)Complexity:

- **Time Complexity:** The main operations include sorting the array, which is `O(NlogN)`, and iterating through the array to calculate boasting students, which is `O(N)`. The overall complexity is `O(NlogN)`.

- **Space Complexity:** `O(1)`.

</details>
