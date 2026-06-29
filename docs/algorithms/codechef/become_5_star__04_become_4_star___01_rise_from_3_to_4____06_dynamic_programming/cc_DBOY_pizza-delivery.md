# Pizza Delivery

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DBOY |
| Difficulty Rating | 1666 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [DBOY](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/DBOY) |

---

## Problem Statement

Chef Po had recently started home delivery service for pizzas. Po has only a single delivery boy that delivers the orders by riding his motorcycle. The motorcycle has an unlimited capacity of fuel tank. However, it is too old and can only ride 1 km for each 1 liter of fuel.

There are $N$ fuel stations near the restaurant. The $i^{th}$ fuel station can fill a fuel tank exactly $K_{i}$ litres; not more and not less. Filling a fuel tank with any amount of fuel in those stations tends to take a long time. Since the fuel stations are placed near the restaurant, no fuel is needed to go to a fuel station.

Today Chef Po received $N$ pizza orders, which is the same number of fuel stations fortuitously. The house of the person that ordered the $i^{th}$ order is $H_{i}$ km away from the restaurant. The delivery boy cannot deliver more than one order at a time. Therefore, after delivering an order, he must return back to the restaurant to take the next order.

The delivery boy is an efficient person and thus he wants to fill the fuel tank with the exact amount of fuel required to deliver an order and return back. He also does not want to spends much time filling the tank, so he wants to minimize the number of times he fills the tank. Help him determine the minimum number of times he must fill the tank to deliver all orders.

---

## Input Format

- The first line contains a single integer $T$ denoting the number test cases. The description of $T$ test cases follows.
- For each test case, the first line contains a single integer $N$.
- The second line contains $N$ space-separated integers $H_{i}$.
- The third line contains $N$ space-separated integers $K_{i}$.

---

## Output Format

For each test case, output a single line containing the minimum number of times the delivery boy must fill the tank.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq N \leq 500$
- $1 \leq H_{i} \leq 500$
- $1 \leq K_{i} \leq 500$
- There is at least one way for completing the deliveries. That is, the delivery boy  always can fill a fuel tank exactly $2 * H_{i}$ litres for $1 \leq i \leq N.$

---

## Examples

**Example 1**

**Input**

```text
1
4
1 2 3 4
1 4 5 3
```

**Output**

```text
7
```

**Explanation**

Here is one possible solution.

For the first order, the delivery boy must ride 1 + 1 = 2 km long. Fill the tank twice in the first fuel station.

For the second order, the delivery boy must ride 2 + 2 = 4 km long. Fill the tank once in the second fuel station.

For the third order, the delivery boy must ride 3 + 3 = 6 km long. Fill the tank twice in the fourth fuel station.

For the fourth order, the delivery boy must ride 4 + 4 = 8 km long. Fill the tank in the third and fourth fuel stations.

In total, the delivery boy must fill the tank 7 times. There is no way to fill the tank less than 7 times.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINKS

[Practice](http://www.codechef.com/problems/DBOY)

[Contest](http://www.codechef.com/DEC12/problems/DBOY)

## DIFFICULTY

SIMPLE

## PREREQUISITES

Dynamic Programming

## PROBLEM

There are N fuel stations numbered 1 through N. The i-th fuel station can fill exactly Ki liters at any time. You have N days. On the i-th day, you must have exactly 2 × Hi liters in your fuel tank. After that, you will have a round trip and the tank will become empty again. Determine the minimum number of times you must fill your fuel tank on the whole N days.

## QUICK EXPLANATION

Use dynamic programming approach. Let dp[i][j] = the minimum number of times to fill exactly j liters using only fuel stations 1 through i. The answer to the problem is dp[N][2 × H1] + dp[N][2 × H2] + … dp[N][2 × HN].

## EXPLANATION

This is problem can be reduced to the traditional coin change problem. We have N types of coin, each having value K1, K2, …, and KN. We want to make changes for N days, each for 2 × H1, 2 × H2, …, and 2 × HN. What is the minimum number of coins needed?

Note that since each day is independent, we can minimize the number of coins on each day, and sum the results over N days.

Mathematically, for each day i, we want to minimize the value of

X1 + X2 + … + XN

subject to

X1K1 + X2K2 + … + XNKN = 2 × Hi

Xk ? 0 for 1 ? k ? N

We will use dynamic programming to solve this problem. Let dp[i][j] = the minimum number of coins needed to make changes for j, using only coins of types 1 through i. The base case is:

- dp[0][0] = 0 (no coins needed)

- dp[0][j] = infinity; for j ? 0 (it is impossible to make changes for j with no coins)

We can use a very large number such as 1,000,000,000 as infinity in our code.

We need to setup a recurrence relation. For each state dp[i][j], there are two possibilities:

- We do not use any coin of type i. The minimum number of coins needed is then dp[i - 1][j].

- We use at least one coin of type i. The minimum number of coins needed is then 1 + dp[i][j - Ki].

Therefore, we have

dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - Ki])

Both time and space complexity of this solution are in O(N × max{Hi}).

Here is a pseudocode of this solution.

`
read(N)
for i = 1; i ? N; i++:
    read(H[i])
for i = 1; i ? N; i++:
    read(K[i])

dp[0][0] = 0
for j = 1; j ? max{2 × H[i]}; j++:
    dp[0][j] = 1000000000

for i = 1; i ? N; i++:
    for j = 0; j ? max{2 × H[i]}; j++:
        dp[i][j] = dp[i-1][j]
        if K[i] ? j:
            dp[i][j] = min(dp[i][j], 1 + dp[i][j-K[i])

int res = 0
for i = 1; i ? N; i++:
    res = res + dp[N][2*H[i]]
println(res)
`

There is a solution that only uses O(max{Hi}) memory for the dp table. This solution uses the facts that:

- dp[i][?] only refers dp[i-1][?]. So instead of keeping N rows in the DP table, we can store only the last two rows.

- Furthermore, dp[i][x] only refers dp[i][y] for y < x. So we can store only the current row and fill the current row of the DP table from right to left.

`
read(N)
for i = 1; i ? N; i++:
    read(H[i])
for i = 1; i ? N; i++:
    read(K[i])

dp[0] = 0
for j = 1; j ? max{2 × H[i]}; j++:
    dp[j] = 1000000000

for i = 1; i ? N; i++:
    for j = K[i]; j < max{2 × H[i]}; j++:
        dp[j] = min(dp[j], 1 + dp[j-K[i])

int res = 0
for i = 1; i ? N; i++:
    res = res + dp[2*H[i]]
println(res)
`

Note that for the i-th row we fill the table from K[i] instead from 0. This is because for j < K[i] the DP values will not change.

Another solution is to use the so-called “forward DP”, i.e. filling the latter entries of the DP table using the values of the current entry. This is just a matter of style.

`
read(N)
for i = 1; i ? N; i++:
    read(H[i])
for i = 1; i ? N; i++:
    read(K[i])

dp[0] = 0
for j = 1; j ? max{2 × H[i]}; j++:
    dp[j] = 1000000000

for i = 1; i ? N; i++:
    for j = 0; j+K[i] < max{2 × H[i]}; j++:
        dp[j+K[i]] = min(dp[j+K[i]], 1 + dp[j])

int res = 0
for i = 1; i ? N; i++:
    res = res + dp[2*H[i]]
println(res)
`

In all solutions above, we do not remove duplicate coin types as they do not affect the answer, although they will make us recompute the same coin types in the DP table.

## SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/December/Setter/DBOY.cc).

## TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/December/Tester/DBOY.c).

</details>
