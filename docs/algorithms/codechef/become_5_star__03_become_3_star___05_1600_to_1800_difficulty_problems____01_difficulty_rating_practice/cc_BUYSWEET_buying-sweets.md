# Buying Sweets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BUYSWEET |
| Difficulty Rating | 1706 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [BUYSWEET](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/BUYSWEET) |

---

## Problem Statement

There are $N$ sweets in the store. The cost of the $i^{th}$ sweet is $A_i$ rupees. Chef is a regular customer, so **after** buying the $i^{th}$ sweet, he gets a **cashback** of $B_i$ rupees.

Chef has $R$ rupees. He is fond of all the sweets, so he wants you to calculate the maximum number of sweets he can buy. Note that he can buy the same type of sweet multiple times, as long as he has the money to do so.

---

## Input Format

- The first line of input will contain $T$, the number of test cases.
- Each test case consists of three lines of input.
- The first line of each test case contains two space-separated integers $N$ and $R$ — the number of sweets in the shop and the amount of money Chef has.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line of each test case contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

---

## Output Format

For each query, print on a new line the maximum number of sweets Chef can buy.

---

## Constraints

- $1 \le T \le 2 \cdot 10^5$
- $1 \le N \le 2 \cdot 10^5$
- $1 \le B_i < A_i \le 10^9$
- $1 \le R \leq 10^9$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
3 3
2 3 4
1 1 1
2 4
5 4
1 2
4 10
4 4 5 5
1 2 4 2
```

**Output**

```text
2
1
7
```

**Explanation**

**Test case $1$:** Chef buys the first sweet, which costs $2$ rupees and has a cashback of $1$ rupee. He now has $3 - 2 + 1 = 2$ rupees remaining. He once again buys the first sweet, which leaves him with $1$ rupee, at which point no more sweets can be bought.

**Test case $2$:** Chef buys the second sweet once.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3
2 3 4
1 1 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2 4
5 4
1 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4 10
4 4 5 5
1 2 4 2
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START36A/problems/BUYSWEET)

[Contest Division 2](https://www.codechef.com/START36B/problems/BUYSWEET)

[Contest Division 3](https://www.codechef.com/START36C/problems/BUYSWEET)

[Contest Division 4](https://www.codechef.com/START36D/problems/BUYSWEET)

Setter: [Yash Thakker](https://www.codechef.com/users/yash5507)

Tester: [Felipe Mota](https://www.codechef.com/users/fmota), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1706

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N sweets in the store. The cost of the i^{th} sweet is A_i rupees. Chef is a regular customer, so **after** buying the i^{th} sweet, he gets a **cashback** of B_i rupees.

Chef has R rupees. He is fond of all the sweets, so he wants you to calculate the maximum number of sweets he can buy. Note that he can buy the same type of sweet multiple times, as long as he has the money to do so.

#
[](#explanation-5)EXPLANATION:

The cost of buying a sweet in this case is:

A[i ] -  B[i]

So what we can do is create another array of A[i] - B[i] and sort it in increasing order. Then for each i, we would first check if the A[i] value of the sweet is greater than the money we have left with us. If its greater than R then we cannot buy that sweet and we skip to the next one otherwise we can buy the sweet i. At this point the i_{th} sweet is also the cheapest sweet we can buy so we should buy as much of i_{th} sweet as possible. Thus we need to calculate for amount R, how many sweets of type i, we can buy. We can buy sweets till R is greater than or equal to A[i].

sweets\_count = \frac{R - B[i]}{A[i] - B[i]}

we would add this to our answer and move on to the next sweet. Also we would reduce our R by sweet\_count \times (A[i]-B[i]), i.e

R = R - sweet\_count \times (A[i]-B[i])

#
[](#time-complexity-6)TIME COMPLEXITY:

O(NlogN) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/m_Hr)

[Setter’s Solution](https://p.ip.fi/p1ma)

[Tester-1’s Solution](https://p.ip.fi/JYJF)

[Tester-2’s Solution](https://p.ip.fi/_vBc)

</details>
