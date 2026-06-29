# Chef and String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XYSTRP |
| Difficulty Rating | 1124 |
| Difficulty Band | Greedy Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Greedy Algorithms |
| Official Link | [XYSTRP](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA01/problems/XYSTRP) |

---

## Problem Statement

There are $N$ students standing in a row and numbered $1$ through $N$ from left to right. You are given a string $S$ with length $N$, where for each valid $i$, the $i$-th character of $S$ is 'x' if the $i$-th student is a girl or 'y' if this student is a boy. Students standing next to each other in the row are friends.

The students are asked to form pairs for a dance competition. Each pair must consist of a boy and a girl. Two students can only form a pair if they are friends. Each student can only be part of at most one pair. What is the maximum number of pairs that can be formed?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$.

### Output
For each test case, print a single line containing one integer ― the maximum number of pairs.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $|S| = N$
- $S$ contains only characters 'x' and 'y'
- the sum of $N$ over all test cases does not exceed $3 \cdot 10^5$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
xy
xyxxy
yy
```

**Output**

```text
1
2
0
```

**Explanation**

**Example case 1:** There is only one possible pair: (first student, second student).

**Example case 2:** One of the ways to form two pairs is: (first student, second student) and (fourth student, fifth student).

Another way to form two pairs is: (second student, third student) and (fourth student, fifth student).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
xy
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
xyxxy
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
yy
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Chef and String in Greedy Algorithms](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA01/problems/XYSTRP)

### [](#problem-statement-1)Problem Statement:

There are N students standing in a row and numbered 1 through N from left to right. You are given a string S with length N, where for each valid i, the i-th character of S is ‘x’ if the i-th student is a girl or ‘y’ if this student is a boy. Students standing next to each other in the row are friends.

The students are asked to form pairs for a dance competition. Each pair must consist of a boy and a girl. Two students can only form a pair if they are friends. Each student can only be part of at most one pair. What is the maximum number of pairs that can be formed?

### [](#approach-2)Approach:

- Traverse the string from left to right, checking adjacent characters.

- If the current character is different from the previous one (`s[i] != s[i-1]`), it indicates a potential pair, so you increment the counter and skip to the next character.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)` Iterate through the whole string as all the pairs are considered.

- **Space Complexity:** `O(1)` No extra space is needed to store the result.

</details>
