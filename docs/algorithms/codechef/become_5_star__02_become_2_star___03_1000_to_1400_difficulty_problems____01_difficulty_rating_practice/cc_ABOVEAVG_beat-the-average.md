# Beat the Average

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ABOVEAVG |
| Difficulty Rating | 1278 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [ABOVEAVG](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/ABOVEAVG) |

---

## Problem Statement

There are $N$ students in a class. Recently, an exam on Advanced Algorithms was conducted with maximum score $M$ and minimum score $0$. The average score of the class was found out to be **exactly** $X$.

Given that a student having score **strictly greater** than the average receives an `A` grade, find the **maximum** number of students that can receive an `A` grade.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- The only line of each test case consists of three integers $N, M, X$ - the number of students, the maximum score and the average score respectively.

---

## Output Format

For each test case, output in a single line, the **maximum** number of students who can receive `A` grade.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^7$
- $1 \leq X \leq M \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
2 100 50
3 100 50
5 40 40
10 50 49
```

**Output**

```text
1
2
0
9
```

**Explanation**

**Test case $1$:** There are $2$ students in the class. One of the possible values of scores is $[99, 1]$. Here, the average score is $\frac{99+1}{2} = \frac{100}{2} = 50$. Only the first student receives an `A` grade. It can be shown that the maximum number of students receiving an `A` grade is not more than $1$.

**Test case $2$:** There are $3$ students in the class. One of the possible values of the scores is $[60, 20, 70]$. Here, the average score is $\frac{60+20+70}{3} = \frac{150}{3} = 50$. The students receiving an `A` grade are students $1$ and $3$. It can be shown that the maximum number of students receiving an `A` grade is not more than $2$.

**Test case $3$:** There are $5$ students in the class. The average score and the maximum score is $40$. Thus, the scores of all the students is $40$. Since the score of all the students is equal to the average, none of them receive an `A` grade.

**Test case $4$:** It can be shown that the maximum number of students receiving an `A` grade does not exceed $9$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 100 50
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 100 50
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5 40 40
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
10 50 49
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START37A/problems/ABOVEAVG)

[Contest Division 2](https://www.codechef.com/START37B/problems/ABOVEAVG)

[Contest Division 3](https://www.codechef.com/START37C/problems/ABOVEAVG)

[Contest Division 4](https://www.codechef.com/START37D/problems/ABOVEAVG)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Jakub Safin](https://www.codechef.com/users/xellos0), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1278

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N students in a class. Recently, an exam on Advanced Algorithms was conducted with maximum score M and minimum score 0. The average score of the class was found out to be **exactly** X.

Given that a student having score **strictly greater** than the average receives an `A` grade, find the **maximum** number of students that can receive an `A` grade.

#
[](#explanation-5)EXPLANATION:

Let us look at the two cases for this problem:

-
X=M: Here it implies that every single student has scored M marks and since no student can score more than M marks. Thus in this case no student would receive A grade.

-
X < M: Let us take a variable sum as the sum of marks of all students. Then

sum = N \times X

Now to maximise students who score more than average marks we assign (X+1) marks to as many students as possible, which would be our answer.

answer = \lfloor \frac{sum}{X+1} \rfloor

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/13x9)

[Setter’s Solution](http://p.ip.fi/2AH3)

[Tester1’s Solution](http://p.ip.fi/SsHo)

[Tester2’s Solution](http://p.ip.fi/X90D)

</details>
