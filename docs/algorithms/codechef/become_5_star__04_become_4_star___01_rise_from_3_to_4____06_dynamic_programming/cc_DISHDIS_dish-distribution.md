# Dish Distribution

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISHDIS |
| Difficulty Rating | 1596 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [DISHDIS](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/DISHDIS) |

---

## Problem Statement

Chef feels that being the Head Chef is a very difficult job. More than cooking, managing the kitchen and distributing the work between various cooks proves to be a tiring task. There are many dishes to be prepared. And he has a team of talented cooks to do this for him. But the Chef always has a problem distributing tasks among them. For a cook i, the Chef wants to give him *atleast* xi dishes to prepare in a day. But different cooks have different capacities. Any cook i can cook *atmost* yi number of dishes in a single day. Chef is very aware of every cook's capability and will not give anyone more work than his maximum capacity. Now, he wants you to help him out here.

Your task will be simple: Tell him the number of ways in which he can distribute the given number of dishes among his team.

### Input:

First line contains T, number of tests.
Each test begins with a single line containing 2 space separated integers: n and m, the number of dishes to be prepared and the number of cooks in Chef's team.

Then follow m lines. The ith line contains 2 space separater integers which are the corresponding xi and yi.

### Output:

For every test case, output a single integer: the number of ways of distributing the work mod 1000000007.

### Constraints:
1<=T<=50

1<=n,m<=100

0<=xi,yi<=100

---

## Examples

**Example 1**

**Input**

```text
1
3 2
0 3
1 3
```

**Output**

```text
3
```

**Explanation**

**Test case $1$:** Chef can distribute the dishes in the following three ways:
- $0$ dishes for the first cook and $3$ dishes for the second cook.
- $1$ dish for the first cook and $2$ dishes for the second cook.
- $2$ dishes for the first cook and $1$ dish for the second cook.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/DISHDIS/)

[Contest](http://www.codechef.com/OCT11/problems/DISHDIS/)

### DIFFICULTY

EASY

### EXPLANATION

This was the Easy problem for this month. The problem is a standard combinatorics problem which asks us to find the number of solutions possible for:

x1 + x2 + x3 + … + xm = n

with the constraints ai<=xi<=bi

Though the problem can be solved using combinatorics, the constraints and the time limit of the problem allow a simple O(n3) dp solution to pass. The recurrence is straight-forward. Let dp[x][y] denote the number of ways of preparing y dishes by the first x cooks. Clearly, our answer will be dp[m][n]. The recurrence is as follows:

dp[i][j]=?dp[i-1][j-k]      where x[i]<=k<=y[i]

A lot of people had a problem passing the time limit with a recursive solution. It’s always better to write an iterative code for your solution, especially if the recurrence is simple.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/October/Setter/DishDis.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/October/Tester/DishDis.java).

</details>
