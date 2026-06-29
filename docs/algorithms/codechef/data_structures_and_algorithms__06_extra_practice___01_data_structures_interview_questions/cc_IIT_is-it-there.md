# Is It There

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | IIT |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [IIT](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/IIT) |

---

## Problem Statement

The Chef gives you a non-decreasing sorted array $A$ of $N$ integers and ask you $Q$ queries. Each query contains an integer $X$ and your task is to determine whether this element is in the array.

First, complete the function "init" in the code snippet (with no returning value) that takes two arguments - an integer $N$ and the array of integers $A$ of size $N$. This function is called only once per test case, at the beginning of the test case. The function of "init" is to help you initialize values that you need to use later in the queries.

Complete the function "isItThere" in the code snippet, returning string either "Found" or "Not Found" - depending on whether the element $X$, given as the only argument of the function, is in the array. This function will be called $Q$ times after the function "init" is called.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each testcase contains two integers $N, Q$.
- The second line of each testcase contains $N$ elements - representing the array $A$.
- The next $Q$ lines of each testcase contain an integer $X$

Note: You need to complete the functions in the submit solution tab:

void init(int n, int a[]){...}

string isItThere(int x){...}

---

## Output Format

For each testcase, the single line of output will contain a string passed by the function isItThere and it should be either "Found" or "Not Found".

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N, Q \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $1 \leq X \leq 10^9$
- Sum of $N$ and $Q$ over all test cases does not exceed $2\cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
1
3 2
1 5 10
2
10
```

**Output**

```text
Not Found
Found
```

**Explanation**

Integer 2 is not an element of the array, while 10 is.
