# Strange Function

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ABX01 |
| Difficulty Rating | 1789 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [ABX01](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/ABX01) |

---

## Problem Statement

As New Year is approaching, Salik is studying functions in order to sharpen his math skills. Instead of regular functions, he is studying a strange function **F** which operates on non-negative integers. The value of **F**(**A**) is obtained by the following process:

- Compute the sum of digits of **A**; let's denote this sum by **S**.

- If **S** is a single-digit integer, then **F**(**A**) = **S**.

- Otherwise, **F**(**A**) = **F**(**S**).

It's guaranteed that this process correctly defines the function **F**.

Since this problem was pretty straightforward, he invented a new problem: Given two integers **A** and **N**, compute **F**(**AN**). Can you help him solve this task?

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first and only line of each test case contains two space-separated integers **A** and **N**.

### Output

For each test case, print a single line containing one integer — the value of **F**(**AN**).

### Constraints

- 1 ≤ **T** ≤ 105

- 1 ≤ **A**, **N** ≤ 1018

### Subtasks

**Subtask #1 (10 points):**

- 1 ≤ **N** ≤ 3

- 1 ≤ **A** ≤ 105

**Subtask #2 (20 points):**

- 1 ≤ **N** ≤ 100

- 1 ≤ **A** ≤ 105

**Subtask #3 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 2
7 2
127 1
```

**Output**

```text
7
4
1
```

**Explanation**

**Example case 1:** F(5 · 5) = F(25) = F(2+5) = F(7) = 7

**Example case 2:** F(7 · 7) = F(49) = F(4+9) = F(13) = F(1+3) = F(4) = 4

**Example case 3:** F(127) = F(1+2+7) = F(10) = F(1+0) = F(1) = 1

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
7 2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
127 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/ABX01)

[Contest](http://www.codechef.com/LTIME55/problems/ABX01)

**Setter :** [Mohammad Salik](https://www.codechef.com/users/abx_2109)

**Tester :** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Editorialist :** [Mohammad Salik](https://www.codechef.com/users/abx_2109)

## Difficulty

Simple/Easy

## Prerequisites

Fast modular exponentiation, Observation skills

## Problem

You are given two integers A and N. The task is to compute F(A^N) where F(X) is a function which results in a non-negative single digit integer obtained by a process of summing digits,and on each iteration using the result from the previous iteration to compute a digit sum untill single digit number is reached.

## Explanation

### For Subtask 1

We can simply find A^N as it doesn’t exceed 10^{15} and then evaluate F(A^N) by the recursive process mentioned in the definition of this function.Note that we can evaluate F(A^N) in less than 5 iterations.

### For Subtask 2 and 3

Let us first observe the function F first.What will be F(X) for a single digit integer X ? It will simply be the number itself.Or we can say for a single digit integer X ,F(X)=X\%9 for X!=9 and F(X)=9 for X=9.Combining these two we can write F(X)=X\%9 + 9*(X\%9==0) for a single digit integer X where X\%9==0 will return 1 only when X is 9. Now what will be F(X) for a two digit integer X. For a two digit integer X which is a multiple of 9 observe that F(X)=9 and for X not a multiple of 9 , F(X)= X\%9. Generalising this we can define F(X) as follows : F(X)= X\%9 + 9*(X\%9==0) for any non negative integer X where (X\%9==0) will return 1 only when X is a multiple of 9.

Now lets try to find out F(X*X). Consider two Cases :

-

When X is a multiple of 9 i.e F(X)=9 then X*X is also a multiple of 9 and consequently F(X*X)=9. Also see here that F(F(X)*F(X))= F(9*9)=F(81)=9.Hence when X is a multiple of 9 then F(X*X)=F(F(X)*F(X)).

-

When X is not a multiple of 9 then F(X)=X\%9 . Hence, we have F(F(X)*F(X))=F((X\%9)*(X\%9))=((X\%9)*(X\%9))\%9 = (X*X)\%9 = F(X*X) .Hence in this case also F(X*X)=F(F(X)*F(X)).

So lets generalise this. F(X^2)=F(F(X)*F(X)). Similarly, F(X^4)=F( (F(F(X)*F(X)))^2 ).

Now for **SUBTASK #2** where N<=100 we can evaluate F(A^N) by iterating from 1 to N and taking F at each step while multiplying.The following code evaluates this in N steps :

`
    ll Res=1;
    for(int i=1;i<=N;i++)
    {
            Res=Res*A;
            Res=F(Res);
    }
`

For **Subtask #3** we have N<=10^{18} and hence we cannot take N steps as it will timeout. we can write a function similar to a fast modular exponentiation to evaluate F(A^N) which evaluates this in logN steps.The following code evaluates this :

`
int solve(long long A,long long N)
{
   long long res=1;
   while(N)
   {
        if(N%2==1)
        {
            res=res*F(A);
            res=F(res);
        }
        A=F(F(A)*F(A));
        N/=2;
   }
   return res;
}
`

The function F(A) for an integer A can be computed in O(1) easily as we have already defined this function.

## Time Complexity

O(logN) per testcase

## Space Complexity

O(1)

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME55/Setter/ABX01.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME55/Tester/ABX01.cpp).

</details>
