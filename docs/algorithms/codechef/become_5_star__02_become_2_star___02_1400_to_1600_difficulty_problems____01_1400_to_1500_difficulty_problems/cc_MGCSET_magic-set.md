# Magic Set

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MGCSET |
| Difficulty Rating | 1472 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [MGCSET](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/MGCSET) |

---

## Problem Statement

Katya has a sequence of integers $a_1, a_2, \dots, a_n$ and an integer $m$.

She defines a *good* sequence of integers as a non-empty sequence such that the sum of the elements in each of its non-empty subsequences is divisible by $m$.

Katya wants to know the number of good subsequences of the sequence $a$. Can you help her?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $n$ and $m$.
- The second line contains $n$ space-separated integers $a_1, a_2, \dots, a_n$.

### Output
For each test case, print a single line containing one integer — the number of good subsequences.

### Constraints
- $1 \le T \le 1,000$
- $1 \le n \le 30$
- $1 \le m \le 1,000$
- $1 \le a_i \le 1,000$ for each valid $i$

### Subtasks
**Subtask #1 (30 points):** $1 \le n \le 5$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
2 3
1 2
2 3
1 3
```

**Output**

```text
0
1
```

**Explanation**

**Example case 1:** There are no good subsequences.

**Example case 2:** There is exactly one good subsequence of $a$: $[3]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3
1 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2 3
1 3
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div 1](http://www.codechef.com/JULY18A/problems/MGCSET)

[Div 2](http://www.codechef.com/JULY18B/problems/MGCSET)

[Practice](http://www.codechef.com/problems/MGCSET)

**Author:** [Full name](http://www.codechef.com/users/author_nick)

**Tester:** [Full name](http://www.codechef.com/users/tester_nick)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

### DIFFICULTY:

SIMPLE

### PREREQUISITES:

Basic combinatorics

### PROBLEM:

You have a sequence of integers a_1,a_2,\dots,a_n and an integer m.

Good sequence is an integer sequence such that sum of elements in each of its subsequences is divisible by m.

You have to calculate number of good subsequences of a.

### QUICK EXPLANATION:

Output 2^k-1 where k is number of a_i divisible by m.

### EXPLANATION:

Sequence is good \iff all of its elements are divisible by m. Both implications are obvious: \Longleftarrow  follows from the fact that if a and b are divisible by m than a+b is also divisible by m and \implies follows directly from definition of the good sequence. Thus if a_{i_1}, \dots, a_{i_k} is subsequence of all numbers divisible by m, you can use any its subsequence except for the empty one. Thus the answer is 2^k-1 because for each element of this subsequence you will either take it or not and we subtract 1 to not count the case when we don’t take anything.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/JULY18/setter/MGCSET.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/JULY18/tester/MGCSET.cpp).

### RELATED PROBLEMS:

</details>
