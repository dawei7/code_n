# Large Square

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XLSQUARE |
| Difficulty Rating | 1160 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [XLSQUARE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/XLSQUARE) |

---

## Problem Statement

You are given $N$ identical squares, each with side length $A$. All the squares have their sides parallel to the $x-axis$ and $y-axis$. That is, the squares are not tilted. You have to take several (possibly, zero or all) squares and rearrange them to obtain a mega square. The mega square can't have any gap in the enclosed region or have overlapping squares. Also, you cannot rotate any square.

Output the side length of the largest mega square that you can obtain.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N, A$.

---

## Output Format

For each test case, print a single line containing one integer - the side length of the largest square you can obtain.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
5
3 2
5 3
16 18
11 8
8 6
```

**Output**

```text
2
6
72
24
12
```

**Explanation**

**Test case $1$:**  You can choose just one square to form the mega square. So the side length will be $2$.

**Test case $2$:**  You can choose $4$ squares to form a mega square with side-length $2 \cdot A$ $= 6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 3
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
16 18
```

**Output for this case**

```text
72
```



#### Test case 4

**Input for this case**

```text
11 8
```

**Output for this case**

```text
24
```



#### Test case 5

**Input for this case**

```text
8 6
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/START9C/problems/XLSQUARE)

[Contest - Division 2](https://www.codechef.com/START9B/problems/XLSQUARE)

[Contest - Division 1](https://www.codechef.com/START9A/problems/XLSQUARE)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#problem-3)PROBLEM:

Given N squares of side length A, whose sides are parallel to the coordinate axises, calculate the side length of the largest square you can make, whose area is completely covered by a subset of these N squares. You may **not** rotate the squares or overlap them.

#
[](#explanation-4)EXPLANATION:

**Observation:** The side length of the largest square is always a multiple of A.

(This is because we are tiling the area of the square completely with squares of side length A).

Thus, if the side length of the mega square is X*A, we will require X*X squares of length A to cover the area of the mega square. All we are left to find is the largest X such that X*X \le N. This is equivalent to X \le \sqrt{N}. So, the largest valid X would then be \lfloor\sqrt{N}\rfloor.

The side length of the largest mega square is thus \lfloor\sqrt{N}\rfloor*A.

#
[](#time-complexity-5)TIME COMPLEXITY:

O(1) per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/49968231).

*Experimental:* For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
