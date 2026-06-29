# Chef and Easy Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XXOR |
| Difficulty Rating | 1810 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Bit Manipulation |
| Official Link | [XXOR](https://www.codechef.com/practice/course/2to3stars/LP2TO305/problems/XXOR) |

---

## Problem Statement

You are given a sequence **A1, A2, ..., AN** and **Q** queries. In each query, you are given two parameters **L** and **R**; you have to find the smallest integer **X** such that 0 ≤ **X** < 231 and the value of (**AL** xor **X**) + (**AL+1** xor **X**) + ... + (**AR** xor **X**) is maximum possible.

Note: xor denotes the [bitwise xor operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

### Input

- The first line of the input contains two space-separated integers **N** and **Q** denoting the number of elements in **A** and the number of queries respectively.

- The second line contains **N** space-separated integers **A1, A2, ..., AN**.

- Each of the next **Q** lines contains two space-separated integers **L** and **R** describing one query.

### Output

For each query, print a single line containing one integer — the minimum value of **X**.

### Constraints

- 1 ≤ **N** ≤ 105

- 1 ≤ **Q** ≤ 105

- 0 ≤ **Ai** < 231 for each valid **i**

### Subtasks

**Subtask #1 (18 points):**

- 1 ≤ **N** ≤ 103

- 1 ≤ **Q** ≤ 103

- 0 ≤ **Ai** < 210 for each valid **i**

**Subtask #2 (82 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
5 3
20 11 18 2 13
1 3
3 5
2 4
```

**Output**

```text
2147483629
2147483645
2147483645
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINK:

[Div1](http://www.codechef.com/MARCH18A/problems/XXOR), [Div2](http://www.codechef.com/MARCH18B/problems/XXOR)

[Practice](http://www.codechef.com/problems/XXOR)

**Author:** [Hruday Pabbisetty](http://www.codechef.com/users/hruday968)

**Tester:** [Triveni Mahatha](http://www.codechef.com/users/triveni)

**Editorialist:** [Adarsh Kumar](http://www.codechef.com/users/adkroxx)

## DIFFICULTY:

Easy-Medium

## PREREQUISITES:

Prefix Sum

## PROBLEM:

You are given an array with N elements. You need to answer Q queries. In each query, you are given two parameters L and R, and you have to find the smallest integer X such that 0 \le X < 2^{31} and the value of \sum \limits_{i=L}^R (A[i]\text{ xor }X) is maximum possible.

## EXPLANATION:

Lets focus on the binary representation of each A[i]'s and X. You can observe that each bit are independent, i.e. you can solve the same problem by iterating over each bit. Basically, for each bit you can reduce the problem to simpler one.

Given a **binary array** P of length N. And in each query, you need to find minimum X where 0 \le X \le 1 and the value of G(L,R) = \sum\limits_{i=L}^R (P[i]\text{ xor }X) is maximum possible. Lets see, if we take X = 0, value of G(L,R) will be equal to number of occurences of 1 in range (L,R). If we take X=1, value of G(L,R) will be equal to number of occurences of 0 in range (L,R). Hence, we can conclude that if the number of occurences of 1 is greater than or equal to number of occurences of 0 in range we will take X as 0 else we will take X as 1.

For each query, we just need to answer number of bits that are 1 at j^{th} bit in the range (L,R) for all 0 \le j < 31. For doing the same we will maintain prefix sum for each of the bit position. The pre-processing part can be done in O(N.log(MAX)). We can answer each of the query in O(log(MAX)) now, i.e. O(1) for each of the bit position. For more implementation details, you can have a look at attached solutions.

## Time Complexity:

O((Q+N).log(MAX))

## AUTHOR’S AND TESTER’S SOLUTIONS

[Setter’s solution](http://www.codechef.com/download/Solutions/MARCH18/Setter/XXOR.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/MARCH18/Tester/XXOR.cpp)

</details>
