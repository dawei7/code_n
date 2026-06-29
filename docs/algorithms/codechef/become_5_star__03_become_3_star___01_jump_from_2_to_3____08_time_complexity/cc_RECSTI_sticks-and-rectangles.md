# Sticks and Rectangles

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECSTI |
| Difficulty Rating | 1555 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [RECSTI](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/RECSTI) |

---

## Problem Statement

MoEngage has a bundle of $N$ sticks. The $i^{th}$ stick has a length $L_i$ meters.

Find the **minimum** number of sticks (of any length) you need to add to the bundle such that you can construct some [rectangles](https://en.wikipedia.org/wiki/Rectangle) where **each** stick of the bundle belongs to **exactly one** rectangle and **each** side of a rectangle should be formed with **exactly one** stick.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, denoting the number of given sticks.
- The second line of each test case contains $N$ space-separated integers $L_1, L_2, \dots, L_N$, denoting the length of the sticks.

---

## Output Format

For each test case, output in a single line, the minimum number of sticks you need to add to the bundle to satisfy the given conditions.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \leq L_i \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
1
1
2
2 5
4
2 2 3 3
7
1 3 5 7 1 7 5
```

**Output**

```text
3
2
0
1
```

**Explanation**

**Test case $1$:** One possible way is to add $3$ sticks with lengths $1, 2,$ and $2$. Now, it is possible to construct a rectangle with one pair of opposite sides having a length of $1$ and another pair of opposite sides having a length of $2$.

**Test case $2$:** The optimal way is to add $2$ sticks with lengths $2$ and $5$. Now, it is possible to construct a rectangle with one pair of opposite sides having a length of $2$ and another pair of opposite sides having a length of $5$.

**Test case $3$:** There is no need to add more sticks to the bundle as it is possible to construct a rectangle using the given sticks.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
2
2 5
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4
2 2 3 3
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
7
1 3 5 7 1 7 5
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK140A/problems/RECSTI)

[Contest Division 2](https://www.codechef.com/COOK140B/problems/RECSTI)

[Contest Division 3](https://www.codechef.com/COOK140C/problems/RECSTI)

[Contest Division 4](https://www.codechef.com/COOK140D/problems/RECSTI)

Setter: [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

Tester: [Harris Leung](https://www.codechef.com/users/gamegame)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7), [Jakub Safin](https://www.codechef.com/users/xellos)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

Basic Arithmetic

#
[](#problem-4)PROBLEM:

You have a bundle of N sticks, the ith stick has a length Li meters. Find the minimum number of sticks you need to add to the bundle such that you can construct some rectangles and each stick of the bundle belongs to exactly one rectangle.

#
[](#explanation-5)EXPLANATION:

Think of the problem as a combination of 2 tasks:

- Pairing every length Li with an equal length.

- Ensuring that the total number of sticks after adding the requisite number to complete all the pairs is a multiple of 4.

A rectangle contains pairs of equal and opposite sides. So every length should be present even number of times. Once every length is paired, it has to be ensured that the total number of sides are a multiple of 4. This can be done by simply adding the required number of pairs.

#
[](#time-complexity-6)TIME COMPLEXITY:

The above solution required the program to iterate over the given array atleast once. Hence, the solution has a time complexity of O(N) where N is the size of the array.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://pastebin.com/YKGWiPLk)

[Setter’s Solution](http://p.ip.fi/dOfh)

[Tester’s Solution](http://p.ip.fi/uU6m)

</details>
