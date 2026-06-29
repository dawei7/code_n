# Remove Bad elements

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REMOVEBAD |
| Difficulty Rating | 1100 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [REMOVEBAD](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/REMOVEBAD) |

---

## Problem Statement

Chef has an array $A$ of length $N$.

In one operation, Chef can remove **any one** element from the array.

Determine the **minimum** number of operations required to make all the elements **same**.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ —the length of Array $A$.
    - Next line contains $N$ space-separated integers $A_1, A_2, A_3, \dots, A_N$ - denoting the array $A$.

---

## Output Format

For each test case, output the **minimum** number of operations required to make all the elements same.

---

## Constraints

- $1 \leq T \leq 4000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
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
1 3 2 4 5
```

**Output**

```text
0
3
2
4
```

**Explanation**

**Test case $1$:** All the elements are already same. Thus we need to perform zero operations.

**Test case $2$:** We remove the elements $A_1, A_2,$ and $A_4$ using three operations. The array becomes $[2, 2, 2]$ where all elements are same.

**Test case $3$:** We remove the elements $A_1$ and $A_3$ using two operations. The array becomes $[2, 2]$ where all elements are same.

**Test case $4$:** We remove the elements $A_1, A_2, A_3,$ and $A_4$ using four operations. The array becomes $[5]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
3 3 3
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
6
1 3 2 1 2 2
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4
1 2 1 2
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
5
1 3 2 4 5
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START58A/problems/REMOVEBAD)

[Contest Division 2](https://www.codechef.com/START58B/problems/REMOVEBAD)

[Contest Division 3](https://www.codechef.com/START58C/problems/REMOVEBAD)

[Contest Division 4](https://www.codechef.com/START58D/problems/REMOVEBAD)

Setter: [Abhinav Gupta](https://www.codechef.com/users/abhi_inav)

Tester: [Satyam](https://www.codechef.com/users/satyam_343), [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1100

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has an array A of length N.

In one operation, Chef can remove **any one** element from the array.

Determine the **minimum** number of operations required to make all the elements **same**.

#
[](#explanation-5)EXPLANATION:

In order to make all the elements same, we will select the element with the maximum frequency and delete all the other elements. Thus we will calculate the frequency of each element and select the element say x with maximum frequency, say f. Then our answer would be:

n - f

where n is the size of the array.

In case there are more than element having same maximum frequency then we can select any one of them and our answer would still be the same.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/zsY-)

[Setter’s Solution](http://p.ip.fi/4aVs)

[Tester1’s Solution](http://p.ip.fi/er0I)

[Tester2’s Solution](http://p.ip.fi/tWWS)

</details>
