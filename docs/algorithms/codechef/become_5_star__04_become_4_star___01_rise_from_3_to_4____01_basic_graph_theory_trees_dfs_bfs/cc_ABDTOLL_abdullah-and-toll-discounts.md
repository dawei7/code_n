# Abdullah and Toll Discounts

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ABDTOLL |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [ABDTOLL](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/ABDTOLL) |

---

## Problem Statement

Abdullah has recently moved to Tolland. In Tolland, there are $N$ cities (numbered $1$ through $N$) connected by $N-1$ bidirectional roads such that it is possible to visit any city from any other city. For each city $i$, there is a *toll value* $TL_i$.

Abdullah lives in city $X$. He has planned a tour of Tolland lasting for $2N$ days. For each $i$ ($1 \le i \le N$), on the $2i-1$-th day, he travels from city $X$ to city $i$, and on the $2i$-th day, he travels from city $i$ back to city $X$.

In Tolland, there are also special discount coupons. For each city $c$ and positive integer $v$, there is a discount coupon for city $c$ with *value* $v$. All discount coupons may be bought anywhere in Tolland; the cost of each discount coupon is twice its value.

When travelling from any city $i$ to any (not necessarily different) city $j$, Abdullah must pay a toll exactly once in each city on the path between them (including $i$ and $j$); even if he passed through some cities before, he must pay the toll in these cities as well. For any city $i$, the toll is $TL_i$ when not using any discount coupons; however, if Abdullah bought some discount coupons for city $i$, he may use some or all of them to decrease this toll to $\mathrm{max}\,(0, TL_i-V)$, where $V$ is the sum of values of coupons for city $i$ used by Abdullah. Each coupon may be used at most once per day, but they do not expire when used and the same coupon may be used on multiple days. On each day, Abdullah may use any coupons he wants, but a coupon for city $i$ may only be used to decrease the toll in city $i$.

Abdullah has a travel budget: on each day, he must not spend more than $K$ units of money on paying tolls. Before the start of the tour, he may choose to buy any number of discount coupons, for any cities and with any values (possibly different ones for different cities); the cost of coupons is not included in the budget for any day of the tour. Help Abdullah find the minimum total amount of money he must spend on discount coupons so that on each day during the tour, he will be able to stay within his budget by using the coupons he bought.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $X$ and $K$.
- The second line contains $N$ space-separated integers $TL_1, TL_2, \ldots, TL_N$.
- Each of the next $N-1$ lines contains two space-separated integers $U$ and $V$ denoting that cities $U$ and $V$ are connected by a bidirectional road.

### Output
For each test case, print a single line containing one integer ― the minimum amount of money Abdullah should spend on coupons.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10^4$
- $1 \le K \le 10^{13}$
- $1 \le X, U, V \le N$
- $1 \le TL_i \le 10^9$ for each valid $i$

### Subtasks
**Subtask #1 (40 points):**
- each city is directly connected to at most two other cities
- city $X$ is directly connected to at most one city

**Subtask #2 (60 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
4 2 6
4 7 6 2
2 1
2 3
2 4
3 1 8
2 3 1
1 2
2 3
```

**Output**

```text
14
0
```

**Explanation**

**Example case 1:** The total costs of tolls on each day without purchasing any discount coupons would be $[11, 11, 7, 7, 13, 13, 9, 9]$.

The budget $6$ is exceeded on each day of the tour. However, Abdullah can buy a discount coupon with value $5$ for city $2$ and a discount coupon with value $2$ for city $3$. The total cost of these coupons is $5 \cdot 2 + 2 \cdot 2 = 14$. Now, the costs of tolls on each day are $[6, 6, 2, 2, 6, 6, 4, 4]$, and the budget is never exceeded.

**Example case 2:** The costs of tolls on each day without purchasing any discount coupons would be $[2, 2, 5, 5, 6, 6]$. Since the budget is already never exceeded, there is no need to buy any discount coupons.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link -  [Abdullah and Toll Discounts](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/ABDTOLL)

### [](#problem-statement-1)Problem Statement -

Abdullah has recently moved to Tolland. In Tolland, there are N cities (numbered 1 through N) connected by N-1 bidirectional roads such that it is possible to visit any city from any other city. For each city i, there is a *toll value* TL_i.

Abdullah lives in city X. He has planned a tour of Tolland lasting for 2N days. For each i (1 \le i \le N), on the 2i-1-th day, he travels from city X to city i, and on the 2i-th day, he travels from city i back to city X.

In Tolland, there are also special discount coupons. For each city c and positive integer v, there is a discount coupon for city c with *value* v. All discount coupons may be bought anywhere in Tolland; the cost of each discount coupon is twice its value.

When travelling from any city i to any (not necessarily different) city j, Abdullah must pay a toll exactly once in each city on the path between them (including i and j); even if he passed through some cities before, he must pay the toll in these cities as well. For any city i, the toll is TL_i when not using any discount coupons; however, if Abdullah bought some discount coupons for city i, he may use some or all of them to decrease this toll to \mathrm{max}\,(0, TL_i-V), where V is the sum of values of coupons for city i used by Abdullah. Each coupon may be used at most once per day, but they do not expire when used and the same coupon may be used on multiple days. On each day, Abdullah may use any coupons he wants, but a coupon for city i may only be used to decrease the toll in city i.

Abdullah has a travel budget: on each day, he must not spend more than K units of money on paying tolls. Before the start of the tour, he may choose to buy any number of discount coupons, for any cities and with any values (possibly different ones for different cities); the cost of coupons is not included in the budget for any day of the tour. Help Abdullah find the minimum total amount of money he must spend on discount coupons so that on each day during the tour, he will be able to stay within his budget by using the coupons he bought.

### [](#approach-2)Approach -

The solution is based on exploring each city starting from Abdullah’s city X, using a Depth-First Search (DFS) to evaluate toll costs and determine the minimum coupon expenses required. We begin by defining each city’s toll requirements and the connections between cities. The DFS recursively traverses each city and calculates the toll costs Abdullah would incur when traveling from city X to any destination. During traversal, for each node (city), the algorithm evaluates the toll costs of its child nodes and determines if the toll exceeds the allowed budget K. If so, discount coupons are considered to reduce the toll to fit within the budget, ensuring the minimum number of coupons is purchased by reducing the toll just enough to stay within K. The algorithm computes the cumulative tolls, adjusting them with coupons as needed and aggregating the cost of these coupons to reach the minimum spending for Abdullah’s journey.

### [](#time-complexity-3)Time Complexity -

O(N), where N is the number of cities, as each city is visited once during the DFS.

### [](#space-complexity-4)Space Complexity -

O(N), due to storage requirements for the adjacency list and toll data.

</details>
