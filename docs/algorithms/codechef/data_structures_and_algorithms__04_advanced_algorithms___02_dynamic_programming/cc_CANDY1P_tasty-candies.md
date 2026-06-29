# Tasty Candies

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CANDY1P |
| Difficulty Band | Dynamic programming |
| Path | Data Structures and Algorithms |
| Lesson | Different types of dynamic programming problems |
| Official Link | [CANDY1P](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA07/problems/CANDY1P) |

---

## Problem Statement

Misha LOVES candies. And today she snuck into Chef's kitchen to have some :) . Chef, being very fond of Misha, has arranged the candies in form of an array. The candy at index $i$ has tastiness $A_i$. Each candy further has a type $T_i$ which is either $0$ or $1$.

Chef says that Misha can chose a subarray of the entire array **(Sub-array cannot be of size $0$. Also, sub-array can span the entire length of array.)** and the type of candy to eat. She then eats all the candies inside that sub-array **of the chosen type**. She defines happiness has **sum of tastiness of all candies she eats**. She is wondering on what is the maximum happiness she can obtain, please help her find it!

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each test case has an integer $N$ which denotes number of candies.
- Next line has $N$ integers $A_i$ denoting tastiness of the candy.
- Third line has $N$ integers denoting $T_i$- type of each candy.

---

## Output Format

For each testcase, output in a single line answer the maximum happiness possible.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $-10^6 \leq A_i \leq 10^6$
- $0 \leq T_i \leq 1$

---

## Examples

**Example 1**

**Input**

```text
2  
8  
5 -6 7 8 9 13 -12 1  
1 1 1 1 1 1 0 1  
2   
5 6  
1 0
```

**Output**

```text
38    
6
```

**Explanation**

In first example, we pick the sub-array from index $[3,8]$ and decide to eat candies of type $1$  which gives $7+8+9+13+1=38$. Note that the candy at index $7$ with tastiness $-12$ isnt eaten as its of different type.

In second example, Misha will eat candy with tastiness $6$. Note that she cannot eat both candies even if she chooses the entire array as both are of different types.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8
5 -6 7 8 9 13 -12 1
1 1 1 1 1 1 0 1
```

**Output for this case**

```text
38
```



#### Test case 2

**Input for this case**

```text
2
5 6
1 0
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Tasty Candies](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA07/problems/CANDY1P)

### [](#problem-statement-1)Problem Statement:

Misha LOVES candies, and she wants to maximize her happiness by selecting a subarray of candies, each with a tastiness value and a type (`0` or `1`). The goal is to find the maximum sum of tastiness from a contiguous subarray of candies of the same type.

### [](#approach-2)Approach:

The key idea of this solution is to use dynamic programming to find the maximum sum of tastiness for two types of candies (0 and 1). We maintain an array `DP`, where `DP[i]` represents the maximum sum of tastiness for subarrays ending at index `i`.

-

**Input Reading**: We read the number of test cases and for each, the number of candies along with their tastiness values and types.

-

**Subarray Separation**: Two vectors, `V0` and `V1`, store tastiness values based on types (0 and 1) to handle them separately.

-

**Dynamic Programming Calculation**: The function `MaxSumSubarray` calculates the maximum sum for a vector:

-

If empty, return a very small number.

-

Initialize `DP[0]` with the first element. Iterate through the vector, updating `DP[i]` to reflect the best subarray sum by either starting fresh or adding to the previous sum.

-

Return the maximum from `DP`.

-

**Final Output**: Compute maximum happiness for both types and output the larger value.

### [](#time-complexity-3)Time Complexity:

- **O(n)** per test case, processing each candy once.

### [](#space-complexity-4)Space Complexity:

- **O(n)** for the DP array and type vectors.

</details>
