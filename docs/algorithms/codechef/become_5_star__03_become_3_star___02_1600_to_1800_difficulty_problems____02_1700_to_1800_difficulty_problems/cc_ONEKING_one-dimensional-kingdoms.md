# One Dimensional Kingdoms

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ONEKING |
| Difficulty Rating | 1743 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [ONEKING](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/ONEKING) |

---

## Problem Statement

**N** one dimensional kingdoms are represented as intervals of the form **[ai , bi]** on the real line.
A kingdom of the form **[L, R]** can be destroyed completely by placing a bomb at a point **x** on the real line if **L
≤ x ≤ R**.

Your task is to determine minimum number of bombs required to destroy all the one dimensional kingdoms.

### Input

-
First line of the input contains **T** denoting number of test cases.

-
For each test case, first line contains **N** denoting the number of one dimensional kingdoms.

-
For each next **N** lines, each line contains two space separated integers **ai** and **bi**.

### Output

For each test case , output an integer denoting the minimum  number of bombs required.

### Constraints

Subtask 1 (20 points) : **1 ≤ T ≤ 100 , 1 ≤ N ≤ 100 , 0 ≤ ai ≤ bi ≤500 **

Subtask 2 (30 points) : **1 ≤ T ≤ 100 , 1 ≤ N ≤ 1000 , 0 ≤ ai ≤ bi ≤ 1000  **

Subtask 3 (50 points) : **1 ≤ T ≤ 20 , 1 ≤ N ≤ 105, 0 ≤ ai ≤ bi ≤ 2000**

---

## Examples

**Example 1**

**Input**

```text
1
3
1 3
2 5
6 9
```

**Output**

```text
2
```

**Explanation**

There are three kingdoms [1,3] ,[2,5] and [6,9]. You will need at least 2 bombs
to destroy the kingdoms. In one of the possible solutions, you can place two bombs at x = 2 and x = 6 .

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/ONEKING)

[Contest](http://www.codechef.com/JAN15/problems/ONEKING)

**Author:** [Snigdha Chanda](http://www.codechef.com/users/nssprogrammer)

**Tester:** [Shiplu Hawlader](http://www.codechef.com/users/shiplu)

**Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

### DIFFICULTY:

EASY-MEDIUM

### PRE-REQUISITES:

Greedy

### PROBLEM:

Given **N (?100000)** intervals **[Ai, Bi]**, one such interval can be deleted by placing a bomb at **x** if **Ai ? x ? Bi**. Find minimum number of bombs required to delete all intervals.

### EXPLANATION:

First we sort all intervals according to increasing **Bi**.

Now, let’s say we have placed a bomb at position **x** on the line. All intervals such that their starting point **Ai ? x** will get destroyed. So we’ll greedily place the bombs when required.

Pseudo code:

``n,a,b = input
ar=[]    //ar[i] denotes maximum starting point for intervals ending at i

for i=1 to N:
    ar[b[i]]=max(ar[b[i]], a[i])

ans=0
max=-1  //denotes the latest value of x where we placed a bomb

for i=0 to 2000:
    //we need a bomb to all intervals ending at i'th position
    if max < ar[i]:
        ans += 1
        max = i
print ans
``

Complexity: **O(N+2000)**.

### SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/JAN15/Setter/ONEKING.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/JAN15/Tester/ONEKING.cpp)

</details>
