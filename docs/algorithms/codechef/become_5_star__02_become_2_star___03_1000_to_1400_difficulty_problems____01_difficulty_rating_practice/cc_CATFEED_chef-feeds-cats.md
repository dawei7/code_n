# Chef Feeds Cats

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CATFEED |
| Difficulty Rating | 1343 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CATFEED](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CATFEED) |

---

## Problem Statement

Chef owns $N$ cats (numbered $1$ through $N$) and he wants to feed them. There are $M$ identical cans of cat food; each can must be used to feed exactly one cat and Chef can only feed one cat at a time. Chef wrote down the order in which he wants to feed the cats: a sequence $A_1, A_2, \ldots, A_M$.

An order of feeding cats is *fair* if there is no moment where Chef feeds a cat that has already been fed strictly more times than some other cat. Help Chef — tell him if the order in which he wants to feed the cats is fair.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $M$ space-separated integers $A_1, A_2, \ldots, A_M$.

### Output
For each test case, print a single line containing the string `"YES"` if the order is fair or `"NO"` if it is unfair.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $1 \le M \le 10^3$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
7
3 9
1 2 3 1 2 3 1 2 3
3 9
1 2 3 3 2 1 1 2 3
3 5
2 3 1 1 2
3 6
2 1 1 3 2 3
2 8
1 2 1 2 1 2 1 1
5 3
5 3 1
4 5
1 2 3 1 4
```

**Output**

```text
YES
YES
YES
NO
NO
YES
NO
```

**Explanation**

**Example case 4:** Cat $1$ will eat twice before cat $3$ eats even once, so the order is unfair.

**Example case 5:** The order is unfair because cat $1$ will eat its fifth can before cat $2$ eats its fourth can.

**Example case 7:** The order is unfair because cat $1$ will eat twice before cat $4$ eats even once.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 9
1 2 3 1 2 3 1 2 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3 9
1 2 3 3 2 1 1 2 3
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
3 5
2 3 1 1 2
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
3 6
2 1 1 3 2 3
```

**Output for this case**

```text
NO
```



#### Test case 5

**Input for this case**

```text
2 8
1 2 1 2 1 2 1 1
```

**Output for this case**

```text
NO
```



#### Test case 6

**Input for this case**

```text
5 3
5 3 1
```

**Output for this case**

```text
YES
```



#### Test case 7

**Input for this case**

```text
4 5
1 2 3 1 4
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CATFEED)

[Contest](https://www.codechef.com/LTIME76B/problems/CATFEED)

**Author:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Tester & Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### PROBLEM EXPLANATION

Chef owns N cats (numbered 1 through N) and he wants to feed them. There are M identical cans of cat food; each can must be used to feed exactly one cat and Chef can only feed one cat at a time. Chef wrote down the order in which he wants to feed the cats: a sequence A_1,A_2,…,A_M.

An order of feeding cats is *fair* if there is no moment where Chef feeds a cat that has already been fed strictly more times than some other cat. Help Chef — tell him if the order in which he wants to feed the cats is fair.

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### EXPLANATION:

This was the easiest problem of the contest. Because of very low limits a brute-force solution gets an easy AC.

Keep a counter for each cat recording how many times you had fed it before. Before feeding the next cat just loop over all other cats and check if it was fed fewer times than (or equal to) each of them.  It’s better to check out my implementation. It runs in O(M*N)

A solution that runs in O(M \, log M) works as follows:

Strip the operations into consecutive blocks of N feeding operations (starting from the first one). Each of these blocks must be a permutation of length N (distinct elements). For each block, you can sort the numbers and verify. The last block may have less than N elements, it would be enough to check that all numbers inside it are distinct.

### AUTHOR’S AND TESTER’S SOLUTIONS:

**EDITORIALIST’s solution**: Can be found [here](https://pastebin.com/m5T1i2cN)

**EDITORIALIST’s 2nd solution**: Can be found [here](http://www.codechef.com/download/Solutions/AUG17/Tester2/RAINBOWA.cpp)

</details>
