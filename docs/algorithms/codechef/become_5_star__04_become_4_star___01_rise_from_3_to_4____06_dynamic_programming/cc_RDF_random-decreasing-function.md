# Random decreasing function

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RDF |
| Difficulty Rating | 1975 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [RDF](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/RDF) |

---

## Problem Statement

Andriy and Serhiy are little students from the Lyceum of Kremenchuk. Yesterday there was a great party in the city - Chef's birthday. There were a lot of famous programmers at the party and, of course, everybody gave a gift to Chef. Andriy and Serhiy also didn't come empty-handed. Andriy gave Chef two integer numbers **N** and **K**. Serhiy was more inventive and gave Chef a strange function called "Random-Decreasing-Function", or "**RDF**" abbreviated. The function has the following form:

``RDF(N, K)
    **for** i = 1 **to** K
        **do** N = random(N)
    **return** N``

In above language function **random(N)** returns any integer in the range **[0, N)** with equal probability. Let's consider that **random(0) = 0**. Chef likes both gifts very much and he plays with them every day, let alone that he forgot about his restaurant. Chef runs this function plenty times a day. The only trouble is that results are too unexpected for Chef. Now he asks you to find the expected result of **RDF(N, K)**.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. The only line of each test case contains two space-separated integers **N** and **K**.

### Output

For each test case, output a single line containing the expected result of **RDF(N, K)**. Your answer will be considered as correct if it has an absolute or relative error less than **10−6**. More formally if the expected output is **A** and your output is **B**, your output will be considered as correct if and only if
**|A − B| ≤ 10−6 * max{|A|, |B|, 1}**.

### Constrains

- **1** ≤ **T** ≤ **500000** (**5 * 105**)

- **1** ≤ **N** < **100000** (**105**)

- **0** ≤ **K** < **100000** (**105**)

---

## Examples

**Example 1**

**Input**

```text
3
6 1
4 2
4 3
```

**Output**

```text
2.5
0.3750
0.0416667
```

**Explanation**

**Example case 1.** **RDF(6, 1)** returns each of the numbers **0, 1, 2, 3, 4, 5** with probability **1/6**. Hence the expected value is
**(0 + 1 + 2 + 3 + 4 + 5) / 6 = 2.5**.

**Example case 2.** Value of **N** when **RDF(4, 2)** is called may change by one of the following scenarios:

- **4 ? 0 ? 0** with probability **1/4**.

- **4 ? 1 ? 0** with probability **1/4**.

- **4 ? 2 ? 0** with probability **1/8**.

- **4 ? 2 ? 1** with probability **1/8**.

- **4 ? 3 ? 0** with probability **1/12**.

- **4 ? 3 ? 1** with probability **1/12**.

- **4 ? 3 ? 2** with probability **1/12**.

Hence the expected value is
**0 * 1/4 + 0 * 1/4 + 0 * 1/8 + 1 * 1/8 + 0 * 1/12 + 1 * 1/12 + 2 * 1/12 = 1/8 + 1/12 + 1/6 = 3/8 = 0.375**.

**Example case 3.** You should figure it out by yourself.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 1
```

**Output for this case**

```text
2.5
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
0.3750
```



#### Test case 3

**Input for this case**

```text
4 3
```

**Output for this case**

```text
0.0416667
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/RDF)

[Contest](http://www.codechef.com/MARCH13/problems/RDF)

### DIFFICULTY

EASY

### PREREQUISITES

Simple Math, Dynamic Programming

### PROBLEM

You are given a function random(N), that returns a uniform random integer between 0 and N-1.

You are also given a function RDF defined as follows

`
RDF(N,K)
    repeat K times
        N = random(N)
    return N
`

Now, given N and K, find the expected value of RDF(N,K).

### QUICK EXPLANATION

Let **F(N,K)** be the expected value of **RDF(N,K).**

From the definition of **RDF,** we can derive the following

-
**F(N,0)** = N

-
**F(N,K)** = ( **F(0,K-1)** + **F(1,K-1)** … + **F(N-1,K-1)** ) / N

Thus, we can write a quick **DP** to solve the problem

`
F = Array [0 ... 99999] [0 ... 99999]
for i = 0 to 99999
    F[i,0] = i

for j = 1 to K
    sum = 0
    for i = 1 to N
        sum += F[i-1,j-1]
        F[i,j] = sum / i
`

Of course this solution will not work. There is neither enough memory and nor enough time. But, if you tried to implement this approach for smaller values of K, you would get an interesting insight.

**The value of DP[n,k] falls exponentially as k rises.**

In fact, the value of **DP[n,k]** is well below the required level of precision, when k > 35. Now, you can run the above for

``DP = Array [0 ... 99999] [0 ... 36]
``

and then print the values from the **DP** table if K ? 36. For all other cases you can print 0.

### EXPLANATION

Let us prove this formally. [ Thanks to Anton  ]

We will prove by induction that

`F(N,K) <= N / 2``K`

## Base Case
``F(N,0) <= N
``

This is given.

## Induction
`
F(N,K+1) =
    ( F(0,K) + F(1,K) ... + F(N-1,K) ) / N

Since F(j, K) <= j / 2K for j = 0, 1, ..., N-1

F(N,K+1) <=
    ( 0/2K + 1/2K ... + (N-1)/2K ) / N
    = ( 0 + 1 ... + N-1 ) / N / 2K
    = N*(N-1)/2 / N / 2K
    = (N-1) / 2K+1
    <= N / 2K+1
`

Hence Proved.

## Consequence

`F(N,K) <= N / 2``K`

- F(N,K) increases as N increases.

- F(N,K) decreases as K increases.

We can only increase **N** up to **99999.** At **N** = **99999,** let us find the value of **K,** beyond which **F(99999,K)** will be less than our precision goal.

`
99999 / 2K < 10-6
2K > 1011
K > log2 1011

or, K > 36.54
`

Thus, at **K** = **37,** already all the values of **F(N,K)** are less than **10-6.**

We can simply calculate the **DP** till **K** = **36.** Print the values from the **DP** table if **K** ? **36,** or **0** otherwise.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/March/Setter/RDF.pas).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/March/Tester/RDF.cpp).

</details>
