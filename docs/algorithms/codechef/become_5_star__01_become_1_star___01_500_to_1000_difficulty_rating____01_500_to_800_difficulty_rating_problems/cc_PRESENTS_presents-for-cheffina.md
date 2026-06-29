# Presents for Cheffina

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRESENTS |
| Difficulty Rating | 757 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [PRESENTS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/PRESENTS) |

---

## Problem Statement

Chef has fallen in love with Cheffina, and wants to buy $N$ gifts for her. On reaching the gift shop, Chef got to know the following two things:
- The cost of each gift is $1$ coin.
- On the purchase of every $4^{th}$ gift, Chef gets the $5^{th}$ gift free of cost.

What is the minimum number of coins that Chef will require in order to come out of the shop carrying $N$ gifts?

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains an integer $N$, the number of gifts in the shop.

---

## Output Format

For each test case, output on a new line the minimum number of coins that Chef will require to obtain all $N$ gifts.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
5
4
```

**Output**

```text
4
4
```

**Explanation**

**Test case $1$**: After purchasing $4$ gifts, Chef will get the $5^{th}$ gift free of cost. Hence Chef only requires $4$ coins in order to get $5$ gifts.

**Test case $2$**: Chef will require $4$ coins in order to get $4$ gifts.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
4
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

[Contest Division 1](https://www.codechef.com/START36A/problems/PRESENTS)

[Contest Division 2](https://www.codechef.com/START36B/problems/PRESENTS)

[Contest Division 3](https://www.codechef.com/START36C/problems/PRESENTS)

[Contest Division 4](https://www.codechef.com/START36D/problems/PRESENTS)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Tester: [Felipe Mota](https://www.codechef.com/users/fmota), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

757

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has fallen in love with Cheffina, and wants to buy N gifts for her. On reaching the gift shop, Chef got to know the following two things:

- The cost of each gift is 1 coin.

- On the purchase of every 4^{th} gift, Chef gets the 5^{th} gift free of cost.

What is the minimum number of coins that Chef will require in order to come out of the shop carrying N gifts?

#
[](#explanation-5)EXPLANATION:

For every fifth gift that Chef buys, it will be free of cost. So from given N gifts if we take a sets of 5 gifts then one gift from each set would be free. So the total number of gifts that would be free of cost would be the number of sets that can be made from N gifts. This would be nothing but \frac{N}{5}. Thus total money spent would be total number of gifts minus the number of gifts that would be free.

answer = N - \frac{N}{5}

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/Ig2j)

[Setter’s Solution](https://p.ip.fi/X6w0)

[Tester-1’s Solution](https://p.ip.fi/c8PH)

[Tester-2’s Solution](https://p.ip.fi/HRLd)

</details>
