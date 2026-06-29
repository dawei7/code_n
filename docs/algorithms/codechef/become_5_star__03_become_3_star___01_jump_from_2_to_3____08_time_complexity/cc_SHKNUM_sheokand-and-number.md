# Sheokand and Number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SHKNUM |
| Difficulty Rating | 1534 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [SHKNUM](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/SHKNUM) |

---

## Problem Statement

Sheokand is good at mathematics. One day, to test his math skills, Kaali gave him an integer $N$. To impress Kaali, Sheokand has to convert $N$ into an integer $M$ that can be represented in the form $2^x + 2^y$ (where $x$ and $y$ are non-negative integers such that $x \neq y$). In order to do that, he can perform two types of operations:
- add $1$ to $N$
- subtract $1$ from $N$

However, Sheokand is preparing for his exams. Can you help him find the minimum number of operations required to convert $N$ into a valid integer $M$?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each testcase contains a single integer $N$.

### Output
For each test case, print a single line containing one integer — the minimum required number of operations.

### Constraints
- $1 \le T \le 100,000$
- $1 \le N \le 10^9$

### Subtasks
**Subtask #1 (30 points):** $1 \le T \le 1,000$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
10
22
4
```

**Output**

```text
0
2
1
```

**Explanation**

**Example case 1:** $N=10$ is already in the form $2^x + 2^y$, with $x=3$ and $y=1$.

**Example case 2:** $N=22$ can be converted into $M=20=2^2+2^4$ or $M=24=2^3+2^4$ in two operations.

**Example case 3:** $N=4$ can be converted into $M=3=2^0+2^1$ or $M=5=2^0+2^2$ in one operation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
22
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](https://www.codechef.com/problems/SHKNUM)

[Contest](https://www.codechef.com/AUG18B/problems/SHKNUM)

**Author:** [Jitender Sheora](https://www.codechef.com/users/jitendersheora)

**Tester:** [Mark Mikhno](https://www.codechef.com/users/famafka)

**Editorialist:** [Bhuvnesh Jain](https://www.codechef.com/users/likecs)

# Difficulty

SIMPLE

# Prerequisites

Pre-computation, Binary-search

# Problem

You are given a number N and you can apply 2 type of operations:

- Add 1 to the number.

- Subtract 1 from the number.

Find the minimum number of operations to be carried such that the resulting number can be represented as 2^x + 2^y, where x and y are non-negative and x != y.

# Explanation

The first thing to note is the optimal answer requires us to apply the only operation of either type. Since the operations negate the effect of each other, we should either only add or subtract from our initial number N.

Suppose, if we have a **sorted list** of all possible final numbers which can be represented in the form, 2^x + 2^y, then we can simply find the number nearest to N. For the smaller number, we can simply apply subtraction operation and for the greater number, we can simply apply the addition operation.

For finding the nearest number greater than or smaller than a given number, we can simply binary search. If you are not familiar with this, you can read [topcoder tutorial](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/). There are also inbuilt-functions like “lower_bound” and “upper_bound” in C++ which do your job. (But remember your list should be sorted.)

We can now pre-computate all possible numbers which can be represented in the form 2^x + 2^y. Below is a pseudo-code for it:

``
    vals = []
    for i in [0, 30]:
        for j in [i+1, 30]:
            x = (1 << i) + (1 << j)
            vals.append(x)

``

Note that the maximum possible exponent of 2 in answer can be ceil(\log{{10}^9}) = 30. This is because, for the minimum operation, we need to find the nearest possible number closest to N.

The size of vals will be (31 * 30) / 2) = 465. Since the size is not large, even iterating through all numbers, instead of applying binary search will pass for the full solution.

Once, you are clear with the above idea, you can see the author or editorialist implementation below for help.

Feel free to share your approach, if it was somewhat different.

# Time Complexity

O({\log}^2{N}) for pre-computation.

O({\log{|vals|}}) per test case.

# Space Complexity

O({\log}^2{N})

# SOLUTIONS:

Author’s solution can be found [here](https://www.codechef.com/download/Solutions/AUG18/setter/SHKNUM.cpp).

Tester’s solution can be found [here](https://www.codechef.com/download/Solutions/AUG18/tester/SHKNUM.cpp).

Editorialist’s solution can be found [here](https://www.codechef.com/download/Solutions/AUG18/editorialist/SHKNUM.cpp).

</details>
