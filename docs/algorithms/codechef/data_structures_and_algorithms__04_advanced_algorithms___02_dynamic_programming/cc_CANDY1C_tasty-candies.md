# Tasty Candies

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CANDY1C |
| Difficulty Band | Dynamic programming |
| Path | Data Structures and Algorithms |
| Lesson | Different types of dynamic programming problems |
| Official Link | [CANDY1C](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA07/problems/CANDY1C) |

---

## Problem Statement

Misha LOVES candies. And today she snuck into Chef's kitchen to have some :) . Chef, being very fond of Misha, has arranged the candies in form of an array. The candy at index $i$ has tastiness $A_i$. Each candy further has a type $T_i$ which is either $0$ or $1$.

Chef says that Misha can chose a subarray of the entire array **(Sub-array cannot be of size $0$. Also, sub-array can span the entire length of array.)** and the type of candy to eat. She then eats all the candies inside that sub-array **of the chosen type**. She defines happiness has **sum of tastiness of all candies she eats**. She is wondering on what is the maximum happiness she can obtain, please help her find it!

**Just read the statement and think about it for now. We'll be solving this over the next few pages.**

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each test case has an integer $N$ which denotes number of candies.
- Next line has $N$ integers $A_i$ denoting tastiness of the candy.
- Third line has $N$ integers denoting $T_i$- type of each candy.

---

## Output Format

For each testcase, output in a single line answer the maximum happiness possible.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $-10^6 \leq A_i \leq 10^6$
- $0 \leq T_i \leq 1$

---

## Examples

**Example 1**

**Input**

```text
2  
8  
5 -6 7 8 9 13 -12 1  
1 1 1 1 1 1 0 1  
2   
5 6  
1 0
```

**Output**

```text
38    
6
```

**Explanation**

In first example, we pick the sub-array from index $[3,8]$ and decide to eat candies of type $1$  which gives $7+8+9+13+1=38$. Note that the candy at index $7$ with tastiness $-12$ isnt eaten as its of different type.

In second example, Misha will eat candy with tastiness $6$. Note that she cannot eat both candies even if she chooses the entire array as both are of different types.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8
5 -6 7 8 9 13 -12 1
1 1 1 1 1 1 0 1
```

**Output for this case**

```text
38
```



#### Test case 2

**Input for this case**

```text
2
5 6
1 0
```

**Output for this case**

```text
6
```


