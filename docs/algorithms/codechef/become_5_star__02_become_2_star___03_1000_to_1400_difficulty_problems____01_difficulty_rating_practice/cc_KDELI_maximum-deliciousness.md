# Maximum Deliciousness

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KDELI |
| Difficulty Rating | 1263 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [KDELI](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/KDELI) |

---

## Problem Statement

A new patisserie has opened up to rave reviews. You, in your quest for deliciousness, are going to visit it.

The patisserie has $N$ pastries. With your trained eye, you judge that the $i$-th of them has *deliciousness* $A_i$.
Of course, you want to eat pastries whose total deliciousness is as high as possible. Unfortunately, you can't just buy everything out.

There are $K$ customers in the store, including you. They form a queue to order pastries, of which you're the $L$-th person.
Each customer, including you, will do the following:
- Among the remaining pastries, buy the one with the **highest** deliciousness
- Then, move to the back of the queue

This will repeat till all the pastries are sold out.
What's the total deliciousness of the pastries you buy?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains three space-separated integers $N$, $K$, and $L$ — the number of pastries, the number of people, and your initial position in the queue.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the deliciousness of the pastries.

---

## Output Format

For each test case, output on a new line the answer: the total deliciousness of the pastries you buy.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq L \leq K \leq N \leq 2\cdot 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all tests won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4 2 1
3 8 6 14
4 2 2
3 8 6 14
5 3 3
8 5 9 11 49
4 1 1
9 30 1 18
```

**Output**

```text
20
11
9
58
```

**Explanation**

**Test case $1$:** There are $4$ pastries, and $2$ people in the queue. You're first among them. The process is as follows:
- First, you buy the most delicious pastry, which is $14$. You move to the back of the queue.
- Next, the other person buys the most delicious remaining pastry, which is $8$. They move to the back of the queue, so you're in front again.
- You buy the most delicious remaining pastry, $6$, and move to the back.
- The other person buys the only remaining pastry, and the process ends.

The total deliciousness of the pastries you bought is $14 + 6 = 20$.

**Test case $2$:** This is the same as test case $1$, but you start second instead. This means you get the other two pastries this time, for a total of $3 + 8 = 11$.

**Test case $3$:** You're third in line. The first two people will buy the pastries with deliciousness $49$ and $11$ respectively, so your best choice is to buy the one with $9$.
The other two people then buy the remaining pastries.

**Test case $4$:** You're the only person in line, so you can buy everything.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 1
3 8 6 14
```

**Output for this case**

```text
20
```



#### Test case 2

**Input for this case**

```text
4 2 2
3 8 6 14
```

**Output for this case**

```text
11
```



#### Test case 3

**Input for this case**

```text
5 3 3
8 5 9 11 49
```

**Output for this case**

```text
9
```



#### Test case 4

**Input for this case**

```text
4 1 1
9 30 1 18
```

**Output for this case**

```text
58
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/KDELI)

[Contest: Division 1](https://www.codechef.com/AUG23A/problems/KDELI)

[Contest: Division 2](https://www.codechef.com/AUG23B/problems/KDELI)

[Contest: Division 3](https://www.codechef.com/AUG23C/problems/KDELI)

[Contest: Division 4](https://www.codechef.com/AUG23D/problems/KDELI)

***Author, Tester, and Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Sorting

# [](#problem-4)PROBLEM:

K people line up to buy N pastries from a shop. You’re L-th in line.

The pastries have deliciousness values A_1, A_2, \ldots, A_N.

On their turn, a person will always pick the most delicious remaining pastry; then move to the back of the line.

Find the total deliciousness of pastries you buy.

# [](#explanation-5)EXPLANATION:

Let’s sort the array A, so that A_1 \geq A_2 \geq \ldots \geq A_N.

Then, notice that:

- The first person will choose A_1

- The second person will choose A_2

- The third person will choose A_3

\vdots

- The K-th person will choose A_K

- Then, it’s the first person’s turn again, who will pick A_{K+1}

- The second person gets another turn, and picks A_{K+2}

\vdots

In general, the i-th person in line will pick A_i, A_{i+K}, A_{i+2K}, \ldots.

You’re L-th in line, so you’ll pick A_L, A_{L+K}, A_{L+2K}, \ldots

Simply print the sum of these numbers.

Since N can be as large as 2\cdot 10^5 in this task, sorting A needs to be done in \mathcal{O}(N\log N) using an efficient algorithm, such as mergesort or quicksort; \mathcal{O}(N^2) sort algorithms such as bubble sort and insertion sort won’t be fast enough.

The simplest way is to just use your language’s built-in sort function.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k, l = map(int, input().split())
    a = sorted(list(map(int, input().split())))[::-1]
    print(sum(a[l-1::k]))
``

</details>
