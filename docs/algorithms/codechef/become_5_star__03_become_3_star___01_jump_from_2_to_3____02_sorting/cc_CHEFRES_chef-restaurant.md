# Chef Restaurant 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFRES |
| Difficulty Rating | 1776 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [CHEFRES](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/CHEFRES) |

---

## Problem Statement

Chef is a cook and he has recently opened a restaurant.

The restaurant is open during $N$ time intervals $[L_1, R_1), [L_2, R_2), \dots, [L_N, R_N)$. No two of these intervals overlap — formally, for each valid $i$, $j$ such that $i \neq j$, either $R_i \lt L_j$ or $R_j \lt L_i$.

$M$ people (numbered $1$ through $M$) are planning to eat at the restaurant; let's denote the time when the $i$-th person arrives by $P_i$. If the restaurant is open at that time, this person does not have to wait, but if it is closed, this person will wait until it is open. Note that if this person arrives at an exact time when the restaurant is closing, they have to wait for the next opening time.

For each person, calculate how long they have to wait (possibly $0$ time), or determine that they will wait forever for the restaurant to open.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of the input contains two space-separated integers $N$ and $M$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $L_i$ and $R_i$.
- $M$ lines follow. For each valid $i$, the $i$-th of these lines contains a single integer $P_i$.

### Output
For each test case, print $M$ lines. For each valid $i$, the $i$-th of these lines should contain a single integer — the time person $i$ has to wait, or $-1$ if person $i$ has to wait forever.

### Constraints
- $1 \le T \le 100$
- $1 \le N, M \le 10^5$
- $1 \le L_i \lt R_i \le 10^9$ for each valid $i$
- $1 \le P_i \le 10^9$ for each valid $i$
- the intervals are pairwise disjoint
- the sum of $N$ for all test cases does not exceed $3 \cdot 10^5$
- the sum of $M$ for all test cases does not exceed $3 \cdot 10^5$

### Subtasks
**Subtask #1 (30 points):**
- the sum of $N$ for all test cases does not exceed $1,000$
- the sum of $M$ for all test cases does not exceed $1,000$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
4 5
5 7
9 10
2 3
20 30
5
6
7
35
1
```

**Output**

```text
0
0
2
-1
1
```

**Explanation**

**Query $1$:** The person coming at time $5$ does not have to wait as the restaurant is open in $[5,7)$ slot.

**Query $2$:** The person coming at time $6$ does not have to wait as the restaurant is open in $[5,7)$ slot.

**Query $3$:** The person coming at time $7$ has to wait since the restaurant is closed at time $7$. The next slot in which the restaurant opens is $[9,10)$. Thus, the person waits for $2$ units of time.

**Query $4$:** The person coming at time $35$ has to wait forever as the restaurant does not open after time $30$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFRES)

[Contest: Division 1](https://www.codechef.com/LTIME64A/problems/CHEFRES)

[Contest: Division 2](https://www.codechef.com/LTIME64B/problems/CHEFRES)

**Setter:** [Hasan](https://www.codechef.com/users/kingofnumbers)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Taranpreet Singh](http://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Simple

### PREREQUISITES:

Maps, Binary search or ordering queries would do fine.

### PROBLEM:

Given N disjoint intervals [L_i, R_i) and M query times P_i, we need to print the minimum waiting time from query point to any time belonging to any interval, at or after query time.

### SUPER QUICK EXPLANATION

-
``  Sort intervals as well as query time, maintain two pointers and for every interval, iterate from earliest query time $X$ and answer is $L_i - T_i$ if query time is before interval, otherwise $0$ for every query time such that $R_{i-1} \leq X < R_i$.
``

-
``  Alternate online solution is  for every query $X$, to use binary search to find earliest interval such that $X < R_i$. If query time lies in interval, Wait time is zero, else $L_i-X$.
``

- Query times at or after R_n will wait forever (if possible without food :D)

### EXPLANATION

Since intervals are disjoint, every query point can belong to at most one interval, which we need to find, in order to find out the waiting time. Suppose we know that for query time X, the required interval is [L, R). How to calculate waiting time?

See the secret box.

Click to view

If X belong to [L, R), Food is delivered immediately and thus, waiting time is zero.

Otherwise, we will have to wait for Interval to begin, that is, wait from time X up to time L, resulting in waiting time L-X.

This is enough to solve sub task 1, since we can check for every query time, waiting time for all intervals ending after query time and print the minimum of all waiting times, but this results in O(N*M) complexity, which is too slow for sub task 2.

We need to find this interval fast. We know that the interval we are seeking is in fact the  earliest interval which ends after query time.

It is ideal to sort the intervals, whenever we need to find such  earliest, first, last intervals. Sorting is almost used in every problem which involves intervals.

Anyways, after sorting, if interval j is required interval, we know that either j==1 of R_{j-1} \leq X < R_j. This can be used as condition for binary search, since all interval before jth interval has R_i \leq X and all intervals after jth interval has R_i < X.

Otherwise, we can sort the query points and use two pointers, one for query points and one for interval index. For every interval, assign minimum times to all query points which are before R_i, not assigned answer yet.

In case answer is not assigned to query, customer has to survive without food forever.

### Time Complexity

For binary search solution, Time complexity is O((M+N)*logN).

For Offline solution, Time complexity is O(N*logN +M*logM).

Proving complexity is not hard for this problem, though may be referred in secret box.

Click to view

In binary search solution, sorting cost O(N*logN) and each query take O(logN) time, thus total time O((M+N)*logN)

For offline solution, sorting dominates time complexity. After sorting, rest part takes only O(M+N) time.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/LTIME64/setter/CHEFRES.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/LTIME64/tester/CHEFRES.cpp)

[Editorialist’s solution](http://www.codechef.com/download/Solutions/LTIME64/editorialist/CHEFRES.java)

**Edit:** Until above links are not working, You may refer solution [here](https://ideone.com/Ls5gd5).

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
