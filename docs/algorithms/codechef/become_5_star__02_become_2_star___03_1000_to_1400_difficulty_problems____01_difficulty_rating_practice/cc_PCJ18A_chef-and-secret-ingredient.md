# Chef and Secret Ingredient

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PCJ18A |
| Difficulty Rating | 1244 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [PCJ18A](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/PCJ18A) |

---

## Problem Statement

Today Chef wants to evaluate the dishes of his $N$ students. He asks each one to cook a dish and present it to him.

Chef loves his secret ingredient, and only likes dishes with at least $X$ grams of it.
Given $N$, $X$ and the amount of secret ingredient used by each student $A_i$, find out whether Chef will like at least one dish.

###Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each testcase contains two integers $N$
 (number of students) and $X$ (minimum amount of secret ingredient that a dish must contain for Chef to like it).
- The next line contains $N$ space separated integers, $A_i$ denoting the amount of secret ingredient used by the students in their dishes.

###Output:
For each testcase, print a single string "YES" if Chef likes at least one dish. Otherwise, print "NO". (Without quotes).

###Constraints:
- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$
- $1 \leq X \leq 1000000$
- $1 \leq A_i \leq 1000000$

---

## Examples

**Example 1**

**Input**

```text
3
5 100
11 22 33 44 55
5 50
10 20 30 40 50
5 45
12 24 36 48 60
```

**Output**

```text
NO
YES
YES
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 100
11 22 33 44 55
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
5 50
10 20 30 40 50
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
5 45
12 24 36 48 60
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/PCJ18A)

[Contest](https://www.codechef.com/PCJ2018/problems/PCJ18A)

**Author:** [Madhav Sainanee](http://www.codechef.com/users/madhav_1999)

**Tester:** [Prakhar Gupta](http://www.codechef.com/users/prakhar17252)

**Editorialist:** [Prakhar Gupta](http://www.codechef.com/users/prakhar17252)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

None

### PROBLEM:

Given N dishes, find out if there is atleast one dish with amount of secret ingredient \geq X

### EXPLANATION:

We go over the amount of secret ingredient in all the N dishes. If we find a dish which has amount of secret ingredient more than or equal to X, we print ‘YES’.

One mistake participants did was break from the input loop once they found an A_i \geq X. This led to the remaining input of the current test case to be transferred to the next test case, leading to a Wrong Answer, or sometimes a Runtime Error verdict.

**Complexity:** The time complexity is O(N) per test case.

### AUTHOR’S SOLUTION:

Author’s solution can be found [here](https://www.codechef.com/viewsolution/19718279).

</details>
