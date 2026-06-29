# Admins and Shopping

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADMINSHOP |
| Difficulty Rating | 1529 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [ADMINSHOP](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/ADMINSHOP) |

---

## Problem Statement

CodeChef admins went on shopping at a shopping mall.

There are $N$ shops in the mall where the $i^{th}$ shop has a capacity of $A_i$ people. In other words, at any point in time, there can be **at most** $A_i$ number of people in the $i^{th}$ shop.

There are $X$ admins. Each admin wants to visit each of the $N$ shops **exactly once**. It is known that an admin takes exactly **one** hour for shopping at any particular shop. Find the **minimum** time (in hours) in which all the admins can complete their shopping.

**Note:**
1. An admin can visit the shops in any order.
2. It is possible that at some point in time, an admin sits idle and does not visit any shop while others are shopping.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $X$ - the number of shops and the number of admins.
- The second line of each test case contains $N$ integers $A_1, A_2, \ldots, A_N$ - the capacity of the shops.

---

## Output Format

For each test case, output in a single line the **minimum** time (in hours) in which all the admins can complete their shopping.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq X, A_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2 3
3 3
4 2
1 2 3 4
1 6
2
```

**Output**

```text
2
4
3
```

**Explanation**

**Test case $1$:** Minimum time required to complete the shopping is two hours. A possible way to complete shopping in $2$ hours is :
- **$1^{st}$ hour:** All $3$ admins visit shop $1$. This is possible as the capacity of the shop is $3 \geq 3$.
- **$2^{nd}$ hour:** All $3$ admins visit shop $2$. This is possible as the capacity of the shop is $3 \geq 3$.

**Test case $2$:** Minimum time required to complete the shopping is $4$ hours. A possible way to complete shopping in $4$ hours is :
- **$1^{st}$ hour:** Admin $1$ visits shop $1$ and admin $2$ visits shop $4$.
- **$2^{nd}$ hour:** Admin $1$ visits shop $2$ and admin $2$ visits shop $3$.
- **$3^{rd}$ hour:** Admin $1$ visits shop $3$ and admin $2$ visits shop $2$.
- **$4^{th}$ hour:** Admin $1$ visits shop $4$ and admin $2$ visits shop $1$.

**Test case $3$:** Minimum time required to complete the shopping is $3$ hours. A possible way to complete shopping in $3$ hours is :
- **$1^{st}$ hour:** Admins $1$ and $2$ visits shop $1$. All other admins sit idle.
- **$2^{nd}$ hour:** Admins $3$ and $4$ visits shop $1$. All other admins sit idle.
- **$3^{rd}$ hour:** Admins $5$ and $6$ visits shop $1$. All other admins sit idle.
Note that, since the capacity of shop is $2$, maximum $2$ admins visit the shop at once.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3
3 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4 2
1 2 3 4
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
1 6
2
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START35A/problems/ADMINSHOP)

[Contest Division 2](https://www.codechef.com/START35B/problems/ADMINSHOP)

[Contest Division 3](https://www.codechef.com/START35C/problems/ADMINSHOP)

[Contest Division 4](https://www.codechef.com/START35D/problems/ADMINSHOP)

Setter: [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

Tester: [Felipe Mota](https://www.codechef.com/users/fmota), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1529

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

CodeChef admins went on shopping at a shopping mall.

There are N shops in the mall where the i^{th} shop has a capacity of A_i people. In other words, at any point in time, there can be **at most** A_i number of people in the i^{th} shop.

There are X admins. Each admin wants to visit each of the N shops **exactly once**. It is known that an admin takes exactly **one** hour for shopping at any particular shop. Find the **minimum** time (in hours) in which all the admins can complete their shopping.

**Note:**

- An admin can visit the shops in any order.

- It is possible that at some point in time, an admin sits idle and does not visit any shop while others are shopping

#
[](#explanation-5)EXPLANATION:

For each test case, we are given the number of shops N, the number of admins X and the **maximum** people that can shop at a particular store simultaneously.

Since each Admin **must necessarily visit all the N shops** once, so clearly the minimum time required in case of no restrictions is N.

When the maximum number of admins are limited for the shops, we first find the shop which allows for the **minimum** number of admins at the same time. This shop will tell us about the minimum time *in case the shifts **are more than** N* otherwise the answer will remain N.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/yJKx)

[Setter’s Solution](http://p.ip.fi/qqvn)

[Tester-1’s Solution](http://p.ip.fi/mD3S)

[Tester-2’s Solution](http://p.ip.fi/_NQV)

</details>
