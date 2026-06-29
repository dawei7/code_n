# Sereja and Arrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEARRAYS |
| Difficulty Rating | 1999 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [SEARRAYS](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/SEARRAYS) |

---

## Problem Statement

### Sereja and Arrays

Sereja have an array that consist of *n* integers *a*1, *a*2, ..., *a**n* (0 ≤ *a**i* ≤ 1). Sereja can make next operation:

-  fix some integer *i* (1 ≤ *i* ≤ *n* - *k* + 1)

-

subtract *1* from values: *a**i*, *a**i* + 1, ..., *a**i* + *k* - 1

Sereja call array *a* *good* if it is possible to make some operations, that he can and get array that contain only zeros. Now Sereja interested in next question: how many good arrays *a* with length *n* exist?

### Input

First line contain integer *T* — number of testcases. *T* tests follow. Each testcase is given by two integers *n* and *k*.

### Constraints
-  1 ≤ *T* ≤ 10

-  1 ≤ *k* ≤ *n* ≤ 105

### Output

For each testcase output answer modulo 109 + 7.

### Note

**Test #0-1(25 points) n  ≤ **15

**Test #2(25 points) n  ≤ **100

**Test #3(50 points) n  ≤ **100000

---

## Examples

**Example 1**

**Input**

```text
3
3 3
5 2
5 1
```

**Output**

```text
2
8
32
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 2
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
5 1
```

**Output for this case**

```text
32
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Problem Link:** [contest](http://www.codechef.com/LTIME09/problems/SEARRAYS), [practice](http://www.codechef.com/problems/SEARRAYS)

**Difficulty:** Easy

**Pre-requisites:** DP, Implementation

**Problem:**

We need to count the number of **01**-strings of **N** chars, such that any continuous section of ones of them have a length which is a multiple of **K**.

I.e, if **K** = 2, then string **00011001111** is good, while **0011100** is not.

**Explanation:**

This problem is a dynamic programming(DP) problem. As far as it’s so, we need to think about the parameters we should use for DP.

Let’s consider the following function **F[i]**, denoting the number of **01**-strings of **i** chars, such that any continuous section of ones of them have a length which is a multiple of **K**.

It’s a quite obvious observation, that the answer for the problem is **F[N]**.

Let’s consider some border cases.

**F[0]** = 1.

It is quite obvious, since there is an empty string which fully satisfies to our conditions.

**F[1]** = 2, in case **K** = 1, otherwise 1.

If **K** = 1, then strings **0** and **1** both satisfy to out conditions, otherwise string **1** doesn’t satisfy.

Well, it’s time to present the recurrent formula.

**F[i]** = **F[i - 1]** + **F[i - K - 1]** + … + **F[i - c * K - 1]** (**i - c * K - 1** is non-negative, while **i - (c + 1) * K - 1** is negative).

Also, in case **i** is a multiple of **K**, we should increase **F[i]** by 1.

The logic of the formula is the following:

Let’s consider the continuous section of ones, which ends in the position i. It may have a length equal to 0, **K**, **2 * K** and so on. For better understanding, let’s assume that it’s length equals to **3 * K**.

Then, all the positions from the range **[i - 3 * K + 1 … i]** are ones and **(i - 3 * k)'th** position is a zero.

We know how do the positions **[i - 3 * k … i]** look, but we don’t know what’s going on before them. That’s why we need to add summand **F[i - 3 * k - 1]** to **F[i]**.

In case, when **i** is a multiple of **K**, we add 1, because we can’t use the logic described above.

So, here is a pseudocode, which shows the implementation of this DP:

``F[0] = 1
for i from 1 to N do
begin
	F[i] = 0
	if ( i is a multiple of K )
	begin
		F[i] = 1
	end
	loop_pointer = i - 1
	while ( loop_pointer is non-negative ) do
	begin
		F[i] = ( F[i] + F[ loop_pointer ] ) modulo 1000000007
		loop_pointer = loop_pointer - K
	end
end
``

Well, we have a working polynomial solution, which runs in **O(N ^ 2 / K)** time. In case **K** is a quite big number, this solution works fast, but for smaller values of **K** it’s getting TLE.

Let’s improve it!

The key observation is, that the loop for counting current **F[]** is needless.

Formally, **F[i] = G[(i - 1) modulo K]**, where **G[(i - 1) modulo K]** is the sum of all previous **F[x]**, such that **(i - x - 1)** is a multiple of **K**.

We should maintain **G[]** while counting **F[]**. As before, in case **i** is a multiple of **K**, we should increase **F[i]** by 1.

Here is a pseudocode, which shows the implementation of the linear-time algorithm:

``F[0] = 1
G[0] = 1
for i from 1 to N do
begin
	F[i] = 0
	if ( i is a multiple of K )
	begin
		F[i] = 1
	end
	F[i] = ( F[i] + G[(i - 1) modulo K] ) modulo 1000000007
	G[i modulo K] = ( G[i modulo K] + F[i] ) modulo 1000000007
end
``

**Setter’s Solution:** [link](http://www.codechef.com/download/Solutions/LTIME09/Setter/SEARRAYS.cpp)

**Tester’s Solution:** [link](http://www.codechef.com/download/Solutions/LTIME09/Tester/SEARRAYS.cpp)

</details>
