# Buy1-Get1

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BUY1GET1 |
| Difficulty Rating | 1191 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [BUY1GET1](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/BUY1GET1) |

---

## Problem Statement

One day Alice visited Byteland to purchase jewels for her upcoming wedding anniversary.

In Byteland, every Jewelry shop has their own discount methods to attract the customers. One discount method called **Buy1-Get1** caught Alice's attention. That is, Alice buys one jewel, then she can get one additional jewel with the same color without charge by **Buy1-Get1**.

Alice lists the needed jewels as a string **S**, each letter denotes one jewel, and the same letters denote the same colors of jewels, and the different letters denote the different colors of jewels. The cost of each jewel is **1**. Your task is to calculate the minimum cost for getting all the jewels Alice listed.

### Input

The first line of input contains a single line **T**, which represents the number of test cases. Then **T** lines will follow, and each contains a string **S**, which represents the jewels Alice needed.

### Output

Output the minimum cost for each test case.

### Constraints

**1 ≤ T ≤ 100**
**1 ≤ |S| ≤ 200**, where **|S|** represents the length of the string **S**.
 The string **S** is case sensitive, and will contain only English characters in the range **[a-z], [A-Z]**.

---

## Examples

**Example 1**

**Input**

```text
4
ssss
ssas
sa
s
```

**Output**

```text
2
3
2
1
```

**Explanation**

In the first sample case, Alice needs **4** jewel of color **s**. One of the optimal way is the following:
 Buy the first **s** with cost **1**, and she can get the second **s** without charge. Then buy the third **s** with cost **1**, and she can get the last **s** without charge. In this case, she get **4** jewels with only cost **2**.

In the second sample case, Alice needs **3** jewels of color **s** and **1** jewel of color **a**. One of the optimal way is the following:
 Buy the second **s** with cost **1**, and she can get the last **s** without charge. Then buy the **a** and the first **s** with cost **2**. In this case, she get **4** jewels with only cost **3**.

In the third and fourth sample cases, she cannot save her money by using **Buy1-Get1**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
ssss
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
ssas
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
sa
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
s
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/BUY1GET1)

[Contest](http://www.codechef.com/FEB13/problems/BUY1GET1)

# Difficulty:

CAKEWALK

# Pre-requisites:

Ad-hoc

# Problem:

You are given a set of jewels of different colors that you need to purchase. Buying a jewel of color **k** makes you eligible to get another jewel of color **k** for free, by availing of the Buy1-Get1 offer. All jewels, irrespective of color, cost 1. Find the minimum cost you pay by using Buy1-Get1.

# Explanation:

Consider a frequency array where each element stores how many jewels of that particular color are there. There are only 52 colors (from the constraint that each color is denoted by a case-sensitive latin character).

Now, the answer = sum ceil(f[i]/2).

Lets argue this using a necessary-and-sufficient-condition argument.

Q. Why do we need at least sum ceil(f[i]/2)?

A. To acquire the jewels of color ‘i’, lets say we pay ‘k’ amount of money. So the rest has been got for free, i.e. f[i] - k times we have used Buy1Get1 for this color. But we can use only k times the Buy1-Get1 offer (on this color). So k >= f[i]-k, which gives us that the minimum required amount to be paid for acquiring all f[i] jewels of color i is at least f[i]/2.

Hence, to acquire all jewels, we need at least sum ceil(f[i]/2) money.

Q. Why is sum ceil(f[i]/2) sufficient?

A. It is in fact true, that ceil(f[i]/2) is sufficient to acquire all f[i] jewels of color i. For this, lets arrange the f[i] jewels in a row, and then, for each one we buy, the next one we take for free. In this way, we are saving the cost of every alternate jewel. Hence, this takes ceil(f[i]/2) amount of money. The total is thus, overall sum ceil(f[i]/2).

Time Complexity: O(T * |S|). |S| per test-case to update the frequency array.

# Author’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/February/Setter/BUY1GET1.c)

# Tester’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/February/Tester/BUY1GET1.cpp)

</details>
