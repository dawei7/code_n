# Fruit Basket

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COMB09 |
| Difficulty Rating | 932 |
| Difficulty Band | Combinatorics |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Combinatronics |
| Official Link | [COMB09](https://www.codechef.com/learn/course/combinatorics/COMBI01/problems/COMB09) |

---

## Problem Statement

Chef is preparing a fruit basket for Cheffina, he has $N$ varieties of fruits. \
In particular, he has $A_i$ number of fruits of the $i$-th varity.

In how many ways he can prepare the fruit basket? \
Chef can add no more than $A_i$ number of the $i$-th fruit in the basket. \
Chef can prepare an empty fruit basket.

### Note
- Since the output can be very large, output it modulo $10^9 + 7$.
- Beware of overflows while using 32-bit datatypes.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

For each test case, output on a new line the number of ways Chef can prepare the fruit basket. \
Since the output can be very large, output it modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
4 
2 1 3 5
1
1
2
1 2
```

**Output**

```text
144
2
6
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
2 1 3 5
```

**Output for this case**

```text
144
```



#### Test case 2

**Input for this case**

```text
1
1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Fruit Basket in Combinatorics](https://www.codechef.com/learn/course/combinatorics/COMBI01/problems/COMB09)

### [](#problem-statement-1)Problem Statement:

Chef is preparing a fruit basket for Cheffina, he has N varieties of fruits. In particular, he has A_i number of fruits of the i-th varity.

In how many ways he can prepare the fruit basket?

Chef can add no more than A_i number of the i-th fruit in the basket. Chef can prepare an empty fruit basket.

### [](#approach-2)Approach:

- **Understanding the Combinations**:

- For each variety of fruit i, Chef can choose from 0 to A[i] fruits. This gives A[i]+1 options (including choosing none).

- The total number of ways to prepare the fruit basket is the product of choices for all fruit varieties.

- **Formula**:

- Total Ways = ∏(A[i]+1) from i=1 to N. Here, N is the number of fruit varieties, and A[i] is the number of fruits of the i-th variety.

- Since the result can be very large, we will take the result modulo 10^9 + 7.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)` For traversing the array once.

- **Space Complexity:** `O(1)` No extra space required.

</details>
