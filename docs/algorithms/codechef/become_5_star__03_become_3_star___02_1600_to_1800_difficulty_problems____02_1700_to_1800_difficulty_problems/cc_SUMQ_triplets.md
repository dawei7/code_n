# Triplets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUMQ |
| Difficulty Rating | 1772 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [SUMQ](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SUMQ) |

---

## Problem Statement

Given a triplet of integers (X , Y , Z), such that X ≤ Y and Y ≥ Z, we define f(X , Y , Z) to be (X + Y) * (Y + Z). If either X > Y or Y < Z, or both, then f(X , Y , Z) is defined to be 0.

You are provided three arrays ** A , B** and **C **  of any length (their lengths may or may not be equal).

Your task is to find the sum of f(X , Y , Z) over all triplets (X, Y , Z) where  ** X, Y** and **Z ** belong to ** A**, **B** and **C** respectively.

 Output your sum for each test case modulo **1000000007**.

### Input

- The first line contains a single integer, **T**, which is the number of test cases. The description of each testcase follows:

- The first line of each testcase contains **3** integers: **p, q** and **r**. These denote the lengths of **A**,**B** and **C** respectively.

- The second line contains **p** integers, which are the elements of **A**

- The third line contains **q** integers, which are the elements of **B**

- The fourth line contains **r** integers, which are the elements of **C**

### Output

 Output the required sum modulo ** 1000000007 ** for each test case in a new line.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **p**, **q**, **r** ≤ 100000

- 1 ≤ every array element ≤ 1000000000

### Subtasks

- Subtask #1 (30 points): 1 ≤ **p**,**q**,**r**  ≤ 100

- Subtask #2 (70 points): 1 ≤** p**,**q**,**r**  ≤ 100000

---

## Examples

**Example 1**

**Input**

```text
1 
3 1 3
1 2 3
5
4 5 6
```

**Output**

```text
399
```

**Explanation**

As there is only one choice for Y which equals to 5, to get a non-zero function value,we can choose any element for X from the set { 1 , 2 , 3 } and for Z from the set { 4  , 5 }

So triplets which give non-zero function values are:

 { 1 , 5  , 4 } :  ( 1 + 5 ) * ( 5 + 4 )  = 54

{ 1 , 5  , 5 } :  ( 1 + 5 ) * ( 5 + 5 )  = 60

{ 2 , 5  , 4 } :  ( 2 + 5 ) * ( 5 + 4 )  = 63

{ 2 , 5  , 5 } :  ( 2 + 5 ) * ( 5 + 5 )  = 70

{ 3 , 5  , 4 } :  ( 3 + 5 ) * ( 5 + 4 )  = 72

{ 3 , 5  , 5 } :  ( 3 + 5 ) * ( 5 + 5 )  = 80

Final answer : 54 + 60 + 63 + 70 + 72 + 80  = 399

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/SUMQ)

[Contest](http://www.codechef.com/JUNE17/problems/SUMQ)

**Author:** [Vipul Sharma](http://www.codechef.com/users/vipsharmavip)

**Tester:** [Prateek Gupta](http://www.codechef.com/users/prateekg603)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

### DIFFICULTY:

MEDIUM

### PREREQUISITES:

None

### PROBLEM:

You are given three arrays A, B and C. You have to sum up (A_i+B_j)(B_j+C_k) for all i, j, k such that A_i \leq B_j \geq C_k.

### QUICK EXPLANATION:

Over all B_j's, sum up \left(\sum\limits_{A_i \leq B_j}(A_i+B_j)\right)\times\left(\sum\limits_{C_k \geq B_j}(B_j+C_k)\right).

### EXPLANATION:

Let’s bruteforce B_j. If we fix some j, then we can choose A_i \leq B_j and C_k \geq B_j independently. Let’s sort A in ascending order and C in descending order. Then suitable A_i as well as suitable C_k will form prefix of A and C correspondingly which size can be found by binary search. Let the sizes of these prefixes will be k_1 and k_2. Then from triples with this B_j we will have contribution of \sum\limits_{i=1}^{k_1}\sum\limits_{k=1}^{k_2}(A_i+B_j)(B_j+C_k)=\sum\limits_{i=1}^{k_1}(A_i+B_j)\left(k_2 B_j+\sum\limits_{k=1}^{k_2}C_k\right)=\left(k_1 B_j+\sum\limits_{i=1}^{k_1}A_i\right)\times \left(k_2 B_j+\sum\limits_{k=1}^{k_2}C_k\right) which can be quickly calculated using prefix sums. Thus we have O(n \log n) solution.

We can optimize this solution to \mathcal{O}(n) by making the following observation. Let us sort the B in increasing order. The values of k_1 and k_2 can only increase when we go from left to right in the array B. This technique’s standard name is “two pointers” approach.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be updated soon.

Tester’s solution will be updated soon.

### RELATED PROBLEMS:

</details>
