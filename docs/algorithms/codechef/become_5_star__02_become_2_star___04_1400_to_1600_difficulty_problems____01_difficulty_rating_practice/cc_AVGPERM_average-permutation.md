# Average Permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AVGPERM |
| Difficulty Rating | 1401 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [AVGPERM](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/AVGPERM) |

---

## Problem Statement

You are given an integer $N$.

Find a permutation $P = [P_1, P_2, \ldots, P_N]$ of the integers $\{1, 2, \ldots, N\}$ such that sum of averages of all consecutive triplets is minimized, i.e.

$$
\sum_{i=1}^{N-2} \frac{P_i + P_{i+1} + P_{i+2}}{3}
$$

is minimized.

If multiple permutations are possible, print any of them.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains an integer N, the size of the permutation.

---

## Output Format

For each test case, output on a new line a permutation which satisfies the above conditions.

---

## Constraints

- $1 \leq T \leq 1000$
- $3 \leq N \leq 10^5$
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
4
3
```

**Output**

```text
3 2 1 4
3 2 1
```

**Explanation**

**Test case $1$:** The sum is $\frac{P_1 + P_2 + P_3}{3} + \frac{P_2 + P_3 + P_4}{3} = \frac{3 + 2 + 1}{3} + \frac{2 + 1 + 4}{3} = 6/3 + 7/3 = 4.333\ldots$ Among all possible permutations of $\{1, 2, 3, 4\}$, this is one of the permutations which provides the minimum result.

**Test case $2$:** The sum is $\frac{3+2+1}{3} = 6/3 = 2$. Every permutation of size $3$ will have this value, hence it is the minimum possible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
```

**Output for this case**

```text
3 2 1 4
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
3 2 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START50A/problems/AVGPERM)

[Contest Division 2](https://www.codechef.com/START50B/problems/AVGPERM)

[Contest Division 3](https://www.codechef.com/START50C/problems/AVGPERM)

[Contest Division 4](https://www.codechef.com/START50D/problems/AVGPERM)

Setter: [Shanu Singroha](https://www.codechef.com/users/shanu_singroha)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1401

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an integer N.

Find a permutation P = [P_1, P_2, \ldots, P_N] of the integers \{1, 2, \ldots, N\} such that sum of averages of all consecutive triplets is minimized, i.e.

\sum_{i=1}^{N-2} \frac{P_i + P_{i+1} + P_{i+2}}{3}

is minimized.

If multiple permutations are possible, print any of them.

#
[](#explanation-5)EXPLANATION:

We are given the following sum to compute

\sum_{i=1}^{N-2} \frac{P_i + P_{i+1} + P_{i+2}}{3}

This can be simplified as:

\frac{P_1 + 2 \times P_2 + 3 \times (P_3 + P_4.....P_{n-2}) + 2 \times P_{n-1} + P_n}{3}

Since P_1 and P_n is not repeated and P_{n-1} and P_2 is repeated twice so it makes sense to assign maximum values to P_1 and P_n, followed by the next largest values to P_{n-1} and P_2. Rest of the values we can assign randomly since rest all of them are in multiples of 3. Thus we can have one of the possible permutations as follows:

N,N-2,1,2,3.....N-3,N-1

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/ef2J)

[Setter’s Solution](http://p.ip.fi/vy7m)

[Tester1’s Solution](http://p.ip.fi/r19Q)

[Tester2’s Solution](http://p.ip.fi/yXjx)

</details>
