# Maximum Unique Segment

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXSEGM |
| Difficulty Rating | 1791 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [MAXSEGM](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/MAXSEGM) |

---

## Problem Statement

You are given 2 arrays **W** =  (**W1**, **W2**, .., **WN**) and **C** =  (**C1**, **C2**, .., **CN**) with **N** elements each. A range [l, r] is *unique* if all the elements **Cl**, **Cl+1**, .., **Cr** are unique (ie. no duplicates). The *sum* of the range is **Wl** +  **Wl+1** + ... + **Wr**.

You want to find an *unique* range with the maximum *sum* possible, and output this sum.

### Input

- The first line of the input contains an integer **T**, denoting the number of test cases. The description of each testcase follows.

- The first line of each test case contains a single integer **N**, denoting the size of the arrays.

- The second line contains **N** space-separated integers : **C1**, **C2**, .., **CN**.

- The third line contains **N** space-separated integers : **W1**, **W2**, .., **WN**.

### Output

For each testcase, output a single integer in a new line, which should be the maximum possible *sum* of an *unique* range.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N** ≤ **1000000**

- **0** ≤ **Ci** < **N**

- **0** ≤ **Wi** ≤ **1000000000**

- **1** ≤ Sum of **N** over all test cases ≤ **1000000**

### Subtasks

- Subtask #1 (30 points): Sum of **N** over all test cases ≤ **10000**

- Subtask #2 (70 points): Original constraints

---

## Examples

**Example 1**

**Input**

```text
1
5
0 1 2 0 2
5 6 7 8 2
```

**Output**

```text
21
```

**Explanation**

The range [2, 4] is an *unique* range because (1, 2, 0) has no duplicates. Its *sum* is 6 + 7 + 8 = 21. This is the maximum possible, and hence is the answer.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXSEGM)

[Contest](https://www.codechef.com/LTIME49/problems/MAXSEGM)

**Author:** [Ramazan Rakhmatullin](https://www.codechef.com/users/grumpy_gordon)

**Testers:** [Lewin Gan](https://www.codechef.com/users/lg5293), [Marek Sommer](https://www.codechef.com/users/mareksom)

**Editorialist:** [Pawel Kacprzak](https://www.codechef.com/users/pkacprzak)

### DIFFICULTY:

Easy

### PREREQUISITES:

Two pointers

### PROBLEM:

You are given 2 arrays W = [W_1, W_2, \ldots, W_N] and C = [C_1, C_2, \ldots, C_N] with N elements each. We say that a range [L, R] is unique if all the elements C_L, C_{L+1}, \ldots, C_R are unique. The goal is to find the maximum possible sum W_L + W_{L+1} + \ldots + W_R for a unique range [L, R].

### EXPLANATION:

First of all, notice that in both subtasks, values of W are up to 10^9, which means that the final sum can exceed 32-bit integer range, so you should use 64-bit integers to represent the sums.

### Subtask 1

In the first subtask, there are up to 100 test cases to solve, but we know that the sum of N over all these test cases doesn’t exceed 10^4, so we can apply the following quadratic time approach. For all L = 1, 2, \ldots, N, let’s iterate over all R \geq L such that a range [L, R] is unique and update the result during this iteration. The key observation here is that if for some A, the range [L, A] is not unique, i.e. there exists two indices L \leq i < j \leq A, such that C_i = C_j, then any range [L, B] for B > A is also not unique. In order to track uniqueness of elements in a range during iterations, we can use a hash-table, or even better, after noticing that values in C are non-negative integers less than N, we can use a simple boolean array for this purpose.

The following pseudocode illustrates the above appraoch:

``result = 0
for L = 1 to N:
    for i = 0 to N-1:
        seen[i] = False # initially all are unseen
    currentSum = 0
    for R = L to N:
        if seen[C[R]]:
            break
        currentSum += W[R]
        result = max(result, currentSum)
        seen[C[R]] = True
print result
``

The total time complexity of this method is clearly O(N^2) for a single test case, which is sufficient in this subtask.

### Subtask 2

In the second subtask, there are also up to 100 test cases to solve, but now the sum over N over these test cases doesn’t exceed 10^6. Thus we need a faster approach, ideally a linear one.

The key observation is to notice that values in the array W are non-negative, which means that if a range [L, R] is unique, and we can extend it in any direction, then we can always do that. It follows, that if we have a unique range [L, R], we want to extend in both directions as much as it stays unique. This leads to the following approach:

Let’s start with L = 1. We are going to use a boolean array for tracking already seen elements in the current range - similarly as in the solution for the first subtask. Now, let’s find maximum R such that the range [L, R] is unique. It means that either R = N or value C[R+1] appears in range [L, R] in array C. We do this by simply iterating from R = L until we find this maximum R. Now we know that [L, R] is a unique range and we can update the result with its sum, which can be computed while iterating. Now comes the second key observation. If R = N we are done, because there are no remaining elements to the right. Otherwise, in order to extend the current range to the right, we have to find the minimum i \geq L, such that C[i] = C[R+1], update L to i+1 and start extending the right endpoint of the range from R while it remains unique. We repeat this process until R becomes N. The following pseudocode illustrates this approach:

``result = 0
currentSum = 0
L = 1
R = 1
for i = 0 to N-1:
    seen[i] = False # initially all are unseen
while True:
    while R <= N and not seen[C[R]]:
        currentSum += W[R]
        seen[C[R]] = True
        R += 1
    result = max(result, currentSum)
    if R == N+1:
        break
    while seen[C[R]]:
        seen[C[L]] = False
        currentSum -= W[L]
        L += 1
print result
``

The time complexity of this approach is O(N) for a single test case because both L and R can be updated at most N times in the loops and the total complexity is dominated by the loops where these values are updated in every iteration. This method is often called “Two pointers” approach and it’s useful in approaching many problems, even very advanced ones.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Setter’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME49/Setter/MAXSEGM.cpp).

First tester’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME49/Tester1/MAXSEGM.py).

Second tester’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME49/Tester2/MAXSEGM.cpp).

Editorialist’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME49/Editorialist/MAXSEGM.py).

</details>
