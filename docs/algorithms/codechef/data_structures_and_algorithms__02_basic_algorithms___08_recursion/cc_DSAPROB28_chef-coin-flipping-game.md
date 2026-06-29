# Chef Coin Flipping Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAPROB28 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [DSAPROB28](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/DSAPROB28) |

---

## Problem Statement

The chef is playing a game with a coin that has a $1$ printed on one side and a $2$ printed on the other. He wants to find out how many different ways he can achieve a sum of $S$ by flipping the coin any number of times.

Help Chef determine the total number of ways to get a sum of $S$ using any number of flips of the coin.

---

## Input Format

The input consists of a single integer $S$.

---

## Output Format

Output a single integer representing the number of ways to achieve the sum $S$.

---

## Constraints

- $ 1 \leq S \leq 20 $

---

## Examples

**Example 1**

**Input**

```text
3
```

**Output**

```text
3
```

**Explanation**

To achieve a sum of 3, there are three ways:
- (1, 2)
- (2, 1)
- (1, 1, 1)

**Example 2**

**Input**

```text
2
```

**Output**

```text
2
```

**Explanation**

To achieve a sum of 2, there are two ways:
- (1, 1)
- (2)

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

Chef has a coin with 1 printed on one side and 2 printed on the other. Chef wants to determine how many different ways he can achieve a sum of `S` by flipping the coin any number of times.

#### [](#approach-2)Approach:

This problem can be approached using dynamic programming or recursion, where the goal is to find all possible sequences of coin flips that sum up to `S`. The recursive nature of the problem can be observed by noting that if we know the number of ways to achieve a sum `S-1` and `S-2`, we can easily compute the number of ways to achieve `S`.

### [](#recursive-approach-3)Recursive Approach:

-

**Base Cases**:

- If `S < 0`, there is no valid sequence of flips that can sum to `S`, so we return `0`.

- If `S == 0`, there is exactly one way to achieve the sum `0`—by not flipping the coin at all. So, we return `1`.

-

**Recursive Case**:

- To achieve a sum `S`, the last coin flip must either be `1` or `2`.

- If the last flip is `1`, the problem reduces to finding the number of ways to achieve a sum of `S-1`.

- If the last flip is `2`, the problem reduces to finding the number of ways to achieve a sum of `S-2`.

- Therefore, the total number of ways to achieve `S` is the sum of the ways to achieve `S-1` and `S-2`.

**Note** : For the given constraint, recursive approach is enough to pass the tests.

### [](#complexity-4)Complexity:

- **Time Complexity**: The time complexity of this recursive solution is `O(2^S)`, which is exponential. This is because each call to `countWays(S)` makes two additional calls to smaller subproblems. While simple, this approach can be highly inefficient for large values of `S`.

### [](#space-complexity-5)Space Complexity:

- **Space Complexity**: The space complexity is `O(S)` due to the depth of the recursive call stack.

### [](#optimization-with-dynamic-programming-6)Optimization with Dynamic Programming:

To optimize the solution, we can use dynamic programming to avoid redundant calculations by storing the results of subproblems:

``#include<bits/stdc++.h>
using namespace std;

// Memoization table to store results of subproblems
unordered_map<int, int> dp;

int countWays(int S) {
    // Base cases
    if (S < 0) return 0;  // No way to achieve a negative sum
    if (S == 0) return 1; // One way to achieve sum 0 (by not flipping any coins)

    // Check if the result is already in the memoization table
    if (dp.find(S) != dp.end()) return dp[S];

    // Recursively calculate the number of ways to achieve sum S
    dp[S] = countWays(S - 1) + countWays(S - 2);

    return dp[S];
}

int main() {
    int S;
    cin >> S;
    cout << countWays(S) << endl; // Output the result
    return 0;
}
``

- This top-down approach with memoization is much more efficient than a naive recursive solution. It ensures that each subproblem is solved only once, reducing the time complexity to `O(S)`.

</details>
