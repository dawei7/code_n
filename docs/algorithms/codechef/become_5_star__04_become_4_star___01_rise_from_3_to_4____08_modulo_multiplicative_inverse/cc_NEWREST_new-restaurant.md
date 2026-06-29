# New Restaurant

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NEWREST |
| Difficulty Rating | 1800 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Modulo Multiplicative Inverse |
| Official Link | [NEWREST](https://www.codechef.com/practice/course/3to4stars/LP3TO408/problems/NEWREST) |

---

## Problem Statement

Chef Dengklek will open a new restaurant in the city. The restaurant will be open for N days. He can cook M different types of dish. He would like to cook a single dish every day, such that for the entire N days, he only cook at most K distinct types of dishes.

In how many ways can he do that?

### Input

The first line contains a single integer T, the number of test cases. T test cases follow. Each test case consists of a single line consisting of three integers N, M, K.

### Output

For each test case, output a single line consisting the number of different ways he can cook for the entire N days, modulo 1000000007.

### Constraints

- 1 ≤ T ≤ 100

- 1 ≤ N ≤ 1000

- 1 ≤ M ≤ 1000000

- 1 ≤ K ≤ 1000

---

## Examples

**Example 1**

**Input**

```text
4
1 1 1
2 2 2
4 3 2
5 7 3
```

**Output**

```text
1
4
45
5887
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 2 2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
4 3 2
```

**Output for this case**

```text
45
```



#### Test case 4

**Input for this case**

```text
5 7 3
```

**Output for this case**

```text
5887
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/NEWREST)

[Contest](http://www.codechef.com/NOV11/problems/NEWREST)

### DIFFICULTY

MEDIUM

### EXPLANATION

This problem is to be solved using dynamic programming approach plus some combinatorics.

First, define dp[i][j] as the number of ways to cook exactly j different types of dish for i days. As the base case, it is obvious that dp[0][0] = 1, dp[0][x] = 0 for x > 0.

Suppose we know the value of dp[i][j] for some pair (i, j). Now, consider the (i+1)th day. There are two options for us:

- Cook a dish which has been cooked before. There are j types of such dishes. We can update dp[i+1][j]:

dp[i+1][j] += j * dp[i][j]

- Cook a new type of dish. Note that we don’t care which type of dish it is; we only care that its type is different from all j types. We can update dp[i+1][j+1]:dp[i+1][j+1] += dp[i][j]

After that, we’ll take the actual types of dish into account. There are M available types of dish. There are P(M, j) ways to choose j types from M types (the order is important). So, the number of ways to cook exactly j different types of dish for i days is P(M, j) * dp[i][j] = (M! / (M-j)!) * dp[i][j] = M! * (M-j)!-1 * dp[i][j]. Of course, all calculations are performed modulo MOD = 1000000007.

We can precompute all values of k! for all 1  ?  k  ?  M. The value of k!-1 (mod MOD) can be calculated using Euler’s Theorem: k!-1 = k!MOD-2 (mod MOD). Also, the DP values can be computed only once for all T test cases.

Since the original problem asks for the number of ways to cook at most K different types of dish in N days, the final answer is: sum {M! * (M-j)!-1 * dp[N][j]} for all 1  ?   j  ?   min(M, K).

The complexity of this solution is O(N(M+K) + M log MOD + T(M+K)).

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/November/Setter/NEWREST.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/November/Tester/NEWREST.cpp).

</details>
