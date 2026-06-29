# Add to Subsequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSEQDIST |
| Difficulty Rating | 1737 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [SUBSEQDIST](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SUBSEQDIST) |

---

## Problem Statement

Chef has an array $A$ of length $N$.

In one operation, Chef can choose any [subsequence](https://en.wikipedia.org/wiki/Subsequence) of the array and any integer $X$ and then add $X$ to **all** the elements of the chosen subsequence.

Determine the **minimum** number of operations required to make all the elements of the array **distinct**.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ — the length of Array $A$.
    - Next line contains $N$ space-separated integers $A_1, A_2, A_3, \dots, A_N$ - denoting the array $A$.

---

## Output Format

For each test case, output the **minimum** number of operations required to make all the elements distinct.

---

## Constraints

- $1 \leq T \leq 4000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases do not exceed $3 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
3
3 3 3
6
1 3 2 1 2 2
4
1 2 1 2
5
1 3 2 4 6
```

**Output**

```text
2
2
1
0
```

**Explanation**

**Test case $1$:**
- Operation $1$: Choose the subsequence $\{A_1\}$ and add $X = 1$ to the elements. The array becomes $A = [4, 3, 3]$.
- Operation $2$: Choose the subsequence $\{A_2\}$ and add $X = 2$ to the elements. The array becomes $A = [4, 5, 3]$.

Thus, we require, minimum $2$ operations to make all the elements distinct.

**Test case $2$:**
- Operation $1$: Choose the subsequence $\{A_1, A_6\}$ and add $X = 4$ to the elements. The array becomes $A = [5, 3, 2, 1, 2, 6]$.
- Operation $2$: Choose the subsequence $\{A_3\}$ and add $X = 5$ to the elements. The array becomes $A = [5, 3, 7, 1, 2, 6]$.

Thus, we require, minimum $2$ operations to make all the elements distinct.

**Test case $3$:**
- Operation $1$: Choose the subsequence $\{A_3, A_4\}$ and add $X = 2$ to the elements. The array becomes $A = [1, 2, 3, 4]$.

Thus, we require, minimum $1$ operation to make all the elements distinct.

**Test case $4$:** All the elements are distinct. We need zero operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
3 3 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
6
1 3 2 1 2 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4
1 2 1 2
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
5
1 3 2 4 6
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START58A/problems/)

[Contest Division 2](https://www.codechef.com/START58B/problems/)

[Contest Division 3](https://www.codechef.com/START58C/problems/)

[Contest Division 4](https://www.codechef.com/START58D/problems/)

Setter: [Abhinav Gupta](https://www.codechef.com/users/abhi_inav)

Tester: [Satyam](https://www.codechef.com/users/satyam_343), [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1737

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has an array A of length N.

In one operation, Chef can choose any [subsequence](https://en.wikipedia.org/wiki/Subsequence) of the array and any integer X and then add X to **all** the elements of the chosen subsequence.

Determine the **minimum** number of operations required to make all the elements of the array **distinct**.

#
[](#explanation-5)EXPLANATION:

Suppose in the array there are distinct elements A_1,A_2…A_n, with frequencies f_1,f_2,...,f_n. Then for each element A_i, we will proceed as follows:

Case \;1: f_i = 1

In this case the number is already distinct, so no operation is required.

Case \; 2: f_i > 1

In this case we will select half of elements of A_i and increase it by an arbitrary high number.

We can do the operations for all the distinct elements at the same time.

So in each operation, we will select all the distinct elements A_i, such that f_i > 1 and increase half of the elements to a arbitrary higher value.

Thus in all we just have to calculate the maximum f_i, say f_{max} and in each operation we will reduce the frequency f_{max} by half, thus our answer would be

\lceil
log_{2}{f_{max}}
\rceil

Since operations would be applied to all f_j < f_{max}, at the same time so we just have to calculate for maximum f_i.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/0D5y)

[Setter’s Solution](http://p.ip.fi/JthA)

[Tester1’s Solution](http://p.ip.fi/gyKz)

[Tester2’s Solution](http://p.ip.fi/SjbF)

</details>
