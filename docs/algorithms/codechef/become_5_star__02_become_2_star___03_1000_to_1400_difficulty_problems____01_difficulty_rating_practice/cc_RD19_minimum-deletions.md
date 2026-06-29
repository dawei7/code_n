# Minimum Deletions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RD19 |
| Difficulty Rating | 1267 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [RD19](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/RD19) |

---

## Problem Statement

The *greatest common divisor* (GCD) of a sequence is the greatest positive integer which divides each element of this sequence.

You are given a sequence $A$ of positive integers with size $N$. You are allowed to delete up to $N-1$ elements from this sequence. (I.e., you may delete any number of elements, including zero, as long as the resulting sequence is non-empty.)

Please find the minimum number of elements which have to be deleted so that the GCD of the resulting sequence would be equal to $1$, or determine that it is impossible.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

### Output
For each test case, print a single line containing one integer — the minimum number of elements to delete, or $-1$ if it is impossible to make the GCD equal to $1$.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 1,000$
- $1 \le A_i \le 50,000$ for each valid $i$

### Subtasks
**Subtask #1 (20 points):** $2 \le N \le 3$

**Subtask #2 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
2
2 3
2
2 4
```

**Output**

```text
0
-1
```

**Explanation**

**Example case 1:** The GCD is already equal to $1$, so the answer is $0$.

**Example case 2:** It is impossible to make the GCD equal to $1$, so the answer is $-1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
2 3
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
2 4
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RD19)

[Contest](https://www.codechef.com/MAY18B/problems/RD19)

**Author:**  [nileshjha19](https://www.codechef.com/users/nileshjha19)

**Tester:**  [Suchan Park](https://www.codechef.com/users/tncks0121)

**Editorialist:**  [Suchan Park](https://www.codechef.com/users/tncks0121)

# DIFFICULTY:

Very Easy

# PREREQUISITES:

How to compute GCD (Euclidean Algorithm)

# PROBLEM:

You are given a sequence of integers of length N. You are allowed to delete up to N-1 elements in this sequence. Your goal is to make the GCD of the resulting sequence 1. Find whether it is possible, and if it’s possible, find the minimum number of deletions.

### QUICK EXPLANATION:

It makes no sense to remove any elements, since any such operation doesn’t decrease the GCD and increase the number of deletions. Therefore the answer is 0 if the GCD of the original array is 1, -1 otherwise.

### EXPLANATION:

From the definition of GCD, we know that

\texttt{gcd}(a, b) \le \texttt{min}(a,b)

This means whenever we apply the GCD operation, the value does not increase. Therefore, the longer the sequence is, the smaller the GCD becomes.

Since we want to *minimize* the GCD and the number of deletions, we can see the best strategy is not deleting any of the elements!

If the GCD of the given sequence is 1, we are done. Otherwise, the GCD will not be 1 even if we delete some elements (since the GCD will not decrease), it is impossible to make the GCD 1.

Therefore the answer is 0 if the GCD of the original array is 1, -1 otherwise.

We can compute the GCD of the whole array by:

\texttt{gcd}(A_1,\texttt{gcd}(A_2,\texttt{gcd}(A_3,\cdots,\texttt{gcd}(A_{n-1}, A_{n})\cdots))

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/MAY18/setter/RD19.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/MAY18/tester/RD19.cpp).

Editorialist’s solution can be found [here](http://www.codechef.com/download/Solutions/MAY18/editorialist/RD19.cpp).

</details>
