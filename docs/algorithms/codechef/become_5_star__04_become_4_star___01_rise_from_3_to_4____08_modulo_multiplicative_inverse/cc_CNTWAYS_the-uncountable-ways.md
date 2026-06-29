# The Uncountable Ways

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNTWAYS |
| Difficulty Rating | 1992 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Modulo Multiplicative Inverse |
| Official Link | [CNTWAYS](https://www.codechef.com/practice/course/3to4stars/LP3TO408/problems/CNTWAYS) |

---

## Problem Statement

Little Chef loves mathematics.Every day, he solves some mathematical problems to improve his skill.

A few days ago, he found a popular problem about turtles. The problem is as follows. Little Chef is given **R** rectangles, numbered 1 through **R**. The width and height of the **i**-th rectangle are **Ni** and **Mi** unit respectively. There is a turtle located on the top-left corner of each rectangle. For each rectangle, count the number of ways the turtle can reach the bottom-right corner, if each turtle can only move right or down 1 unit at any time.The turtle is not allowed to move outside the rectangle, but, of course, the turtle can move on the boundary of the rectangle.

In less than one second, this problem was solved for all rectangles.He felt that the problem was too easy. This morning, Little Chef wanted more challenges. Thus, for each rectangle **i**, he cut and removed a rectangle of **Ai** × **Bi** unit from the top-right corner. See the following figure for detail.

He could not solve this new version of the problem easily. Help him count the number of ways each turtle can reach the bottom-right corner using the same rule as before.

### Input

The first line of the input contains a single integer **R**. The description of **R** rectangles follows. Each description consists of a single line containing four space-separated integers **Ni**, **Mi**, **Ai**, and **Bi**.

### Output

For each rectangle, output a single line containing the number of ways, modulo 1,000,000,007.

### Constraints

1 ≤ **R** ≤ 10
 2 ≤ **Ni**, **Mi** ≤ 400,000
1 ≤ **Ai** < **Ni**
1 ≤ **Bi** < **Mi**

---

## Examples

**Example 1**

**Input**

```text
1
2 2 1 1
```

**Output**

```text
5
```

**Explanation**

In the sample case, there are 5 ways the turtle can reach the bottom right corner as follows:

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINKS

[Practice](http://www.codechef.com/problems/CNTWAYS)

[Contest](http://www.codechef.com/DEC12/problems/CNTWAYS)

## DIFFICULTY

EASY-MEDIUM

## PREREQUISITES

Combinatorics, Modular Multiplicative Inverse

## PROBLEM

There is a rectangle of N × M units. Another rectangle of A × B units is cut off from the upper right corner. Count the number of ways an ant can reach the bottom right corner starting from the top left corner, if it can only move right or down.

## QUICK EXPLANATION

Split the path into 3 subpaths: (0, 0) -> (p, B-1) -> (p, B) -> (N, M). The answer is the sum of (number of ways to go from (0, 0) to (p, B-1)) × (number of ways to go from (p, B) to (N, M)) over all possible values of p.

## EXPLANATION

### A = B = 0

First, let’s consider a simpler version of the problem where A = B = 0, i.e. the rectangle is intact. This becomes a traditional problem. To reach the bottom right corner, the ant needs to move right N times and move down M times. The order of moves does not matter. In other words, the ant needs to move N+M times, N of which the ant moves right. The number of ways, by combinatorics, is:

(N+M) choose N = C(N+M, N) = (N+M)! / (N! × M!)

Note that (N+M) choose N = (N+M) choose M.

### Calculating C(N+M, N)

Since we have to calculate the answer modulo MOD = 1,000,000,007, the above formula have to be rewritten to

C(N+M, M) = ((N+M)! × N!-1 × M!-1) mod MOD

Here, x-1 is the modular multiplicative inverse of x modulo MOD. Since MOD is a prime number, we can calculate it using Fermat’s little theorem: x-1 = xMOD-2 (mod MOD). We can calculate xMOD-2 in O(lg MOD) time using exponentiation by squaring. Because we will use factorials many times in this solution, we can precompute all factorials and their inverses (modulo MOD) for all integers from 0 through 800,000, inclusive.

`
fact[0] = ifact[0] = 1
for i = 1; i ? 800000; i++:
    fact[i] = (i × fact[i-1]) mod MOD
    ifact[i] = (fact[i]MOD-2) mod MOD
`

Therefore the function C(X, Y) can be calculated in constant time as follows. For convenience, we also introduce function ways(N, M) that returns the number of ways an ant can reach the bottom right corner of an N × M intact rectangle.

`
function C(X, Y):
    return (fact[X] × ifact[X-Y] × ifact[Y]) mod MOD

function ways(N, M):
    return C(N+M, M)
`

### A, B > 0

Consider this ASCII art picture of a typical input rectangle. Assume that the top left corner is (0, 0) and the bottom right corner is (N, M).

`
  +---------+
  |         |
  |         | B
  |         |       A
M +         +-------------+
  |                       |
  |                       |
  |                       |
  +-----------------------+
             N
`

We can split the ant’s journey from the top left corner to the bottom right in 3 phases:

Phase 1. The ant moves from top left corner to point (p, B-1):

`
  +---------+
  |\        |
  | \       | B
  |  p      |       A
M +         +-------------+
  |                       |
  |                       |
  |                       |
  +-----------------------+
             N
`

Phase 2. The ant moves down from point (p, B-1) to point (p, B):

`
  +---------+
  |\        |
  | \       | B
  |  p      |       A
M +  |      +-------------+
  |                       |
  |                       |
  |                       |
  +-----------------------+
             N
`

Phase 3. Finally, the ant moves from point (p, B) to point (N, M):

`
  +---------+
  |\        |
  | \       | B
  |  p      |       A
M +  |      +-------------+
  |  \                    |
  |   ------------------\ |
  |                      \|
  +-----------------------+
             N
`

Note that the phases are actually subproblems of the simpler problem mentioned before. The number of ways to perform Phase 1 is ways(p, B-1). The number of ways to perform Phase 2 is of course 1. Finally, the number of ways to perform Phase 3 is ways(N-p, M-B). Therefore, the number of ways if the ant passes point (p, B-1) and then point (p, B) is:

`
ways(p, B-1) × ways(N-p, M-B)
`

It is important to note that we do need an intermediate Phase 2 so that we do not count a path more than once.

To obtain the final answer, iterate over all possible values of p and sum the results. Here is a pseudocode of this solution.

`
read(N, M, A, B)
res = 0
for p = 0; p ? N-A; p++:
    res += ways(p, B-1) × ways(N-p, M-B)
println(res)
`

## SETTER’S SOLUTION

Will be provided soon.

## TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/December/Tester/CNTWAYS.c).

</details>
