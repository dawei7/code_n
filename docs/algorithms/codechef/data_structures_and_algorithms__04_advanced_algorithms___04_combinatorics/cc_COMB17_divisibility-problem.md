# Divisibility Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COMB17 |
| Difficulty Rating | 932 |
| Difficulty Band | Combinatorics |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Combinatronics |
| Official Link | [COMB17](https://www.codechef.com/learn/course/combinatorics/COMBI02/problems/COMB17) |

---

## Problem Statement

Chef has three numbers $A$, $B$ and $C$. \
He gives you the following task calculate the number of positive integers smaller than or equal to $N$, which are divisible by at least of of $A$, $B$ and $C$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a three integers $N$, $A$, $B$, $C$.

---

## Output Format

Output on $T$ new lines (for each test case):
 - Number of positive integers smaller than or equal to $N$, which are divisible by at least of of $A$, $B$ and $C$

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^9$
- $1 \leq A, B, C \leq min(10^3, N)$

---

## Examples

**Example 1**

**Input**

```text
5
10 2 3 2
5 3 2 4
6 3 3 3
24 12 2 12
20 3 20 3
```

**Output**

```text
7
3
2
12
7
```

**Explanation**

For the second test case: $N$ = $5$, $A$ = $3$, $B$ = $2$ and $C$ = $4$. \
Numbers less than or equal to $N$, which are divisible by either $A$, $B$ or $C$ = {$2$, $3$, $4$}

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 2 3 2
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
5 3 2 4
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
6 3 3 3
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
24 12 2 12
```

**Output for this case**

```text
12
```



#### Test case 5

**Input for this case**

```text
20 3 20 3
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

Given a positive integer **N** and three positive integers **A**,  **B**, and **C** , the task is to count the number of positive integers smaller than or equal to  **N**  that are divisible by at least one of **A**,  **B**, or **C**.

### [](#approach-2)Approach:

To solve this problem, we can use the principle of Inclusion-Exclusion. We first count the multiples of each individual number **A**, **B**, and **C** less than or equal to **N**. Then, we subtract the multiples that are common between pairs of numbers and add back the multiples that are common to all three numbers.

### [](#steps-3)Steps:
[](#h-1-count-multiples-of-each-number-4)1. Count Multiples of Each Number:

We start by counting the multiples of each individual number **A**, **B**, and **C** that are less than or equal to **N** because these are the numbers that are divisible by at least one of the given numbers.

For example:

- S_a represents the count of numbers that are divisible by **A** and are less than or equal to **N**.

- S_b represents the count of numbers that are divisible by **B** and are less than or equal to **N**.

- S_c represents the count of numbers that are divisible by **C** and are less than or equal to **N**.

[](#h-2-count-multiples-of-pairs-5)2. Count Multiples of Pairs:

Next, we calculate the counts of multiples of pairs of numbers. This step is crucial to correct the double counting of numbers that are divisible by more than one of the given numbers.

For example:

- S_{ab} represents the count of numbers that are divisible by both **A** and **B** and are less than or equal to **N**.

- S_{bc} represents the count of numbers that are divisible by both **B** and **C** and are less than or equal to ( N ).

- S_{ac} represents the count of numbers that are divisible by both **A** and **C** and are less than or equal to **N**.

[](#h-3-count-multiples-of-all-three-numbers-6)3. Count Multiples of All Three Numbers:

In this step, we calculate the count of multiples of all three numbers, which are divisible by **A**, **B**, and **C** simultaneously. This count is subtracted in the next step to correct for the triple counting of numbers that are divisible by all three numbers.

For example:

- S_{abc} represents the count of numbers that are divisible by **A**, **B**, and **C** and are less than or equal to **N**.

[](#h-4-apply-inclusion-exclusion-principle-7)4. Apply Inclusion-Exclusion Principle:

The Inclusion-Exclusion principle is applied to find the total count of numbers that are divisible by at least one of the given numbers. This principle helps to correct the counts calculated in the previous steps to avoid overcounting or undercounting.

The formula used is:

S = S_a + S_b + S_c - S_{ab} - S_{bc} - S_{ac} + S_{abc}

- We add the counts of multiples of individual numbers S_a, S_b, and S_c.

- We subtract the counts of multiples of pairs of numbers S_{ab}, S_{bc}, and S_{ac}.

- We add back the count of multiples of all three numbers S_{abc} to correct for the triple counting.

This approach ensures that each number is counted exactly once if it is divisible by at least one of the given numbers.

#### [](#time-complexity-8)Time Complexity:

- Calculating S_a, S_b, and S_c:  **O(1)**

- Calculating S_{ab}, S_{bc}, and S_{ac}: **O(log(min(A, B, C)))**

- Calculating S_{abc}: **O(log(min(A, B, C)))**

- Total time complexity : **O(Tlog(min(A, B, C)))**

#### [](#space-complexity-9)Space Complexity:

- Constant extra space is required for storing the input and output variables, therefore, the space complexity is **O(1)** for each test case.

</details>
