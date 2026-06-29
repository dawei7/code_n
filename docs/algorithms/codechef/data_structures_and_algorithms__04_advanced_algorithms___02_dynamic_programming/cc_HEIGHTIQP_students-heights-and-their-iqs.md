# Students, heights and their IQs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEIGHTIQP |
| Difficulty Band | Dynamic programming |
| Path | Data Structures and Algorithms |
| Lesson | Different types of dynamic programming problems |
| Official Link | [HEIGHTIQP](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA08/problems/HEIGHTIQP) |

---

## Problem Statement

In the school morning assembly, $n$ students are standing in a line. You, being the principal of the school know the heights and IQ levels of the students. This information is provided to you by an array $h$ and $iq$, where $h_i, iq_i$ denotes the height and the IQ of the $i$-th student, respectively.

You want to find the longest subsequence of the students such that their heights are in strictly increasing order, whereas their IQ levels are in strictly decreasing order. Note that a subsequence is gotten by removing some (possibly zero) students from the line from any position.

Find out the length of the longest such subsequence.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $n$.
- The second line contains $n$ space-separated integers $h_1, h_2, \dots, h_n$.
- The third line contains $n$ space-separated integers $iq_1, iq_2, \dots, iq_n$.

---

## Output Format

For each test case, print a single line containing one integer — the answer to the problem.

---

## Constraints

- $1 \le T \le 5$
- $1 \le n \le 10^3$
- $1 \le h_i, iq_i \le 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
3
1 2 3
3 2 1
4
1 3 2 4
5 6 4 4
```

**Output**

```text
3
2
```

**Explanation**

**Example case $1$:** You can choose the subsequence $\{1, 2, 3\}$ of the students. You can see the heights of the students are increasing from left to right, whereas the IQ levels are decreasing.

**Example case $2$:** You can choose the subsequence $\{2, 4\}$ of students. You can see the height of $4$-th student is $4$, which is greater than the height of $2$-nd student which is $3$. The IQ level of $4$-th student which is $4$ is less than the $2$-nd student which is $6$. Hence, the answer is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
3 2 1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
1 3 2 4
5 6 4 4
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Students, heights and their IQs](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA08/problems/HEIGHTIQP)

### [](#problem-statement-1)Problem Statement:

In the school morning assembly, there are **n** students standing in a line, each with a height and IQ level. The task is to find the longest subsequence of students with strictly increasing heights and strictly decreasing IQ levels. A subsequence can be formed by removing some (or no) students.

### [](#approach-2)Approach:

The solution uses **dynamic programming** to find the longest valid subsequence. We maintain an array `DP` where `DP[i]` represents the length of the longest subsequence ending at student `i`.

- **Dynamic Programming Initialization**: Initialize the `DP` array with all values set to 1, indicating each student can be a subsequence by themselves.

- **Building the DP Array**: For each student `i`, check previous students `j`:

-

Skip if `H[j] >= H[i]` (not strictly increasing) or `IQ[j] <= IQ[i]` (not strictly decreasing).

-

Update `DP[i]` to be the maximum of its current value or `1 + DP[j]` if both conditions are satisfied.

- **Finding the Maximum Length**: After populating the `DP` array, find the maximum value, representing the longest valid subsequence.

This method efficiently calculates the longest subsequence using relationships between students based on their heights and IQ levels.

### [](#time-complexity-3)Time Complexity:

- O(n²) for each test case, where n is the number of students.

### [](#space-complexity-4)Space Complexity:

- O(n) due to the `DP` array used to store subsequence lengths.

</details>
