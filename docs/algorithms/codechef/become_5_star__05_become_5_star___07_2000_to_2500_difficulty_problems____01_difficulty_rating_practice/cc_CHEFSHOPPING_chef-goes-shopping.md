# Chef Goes Shopping

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSHOPPING |
| Difficulty Rating | 2164 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CHEFSHOPPING](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CHEFSHOPPING) |

---

## Problem Statement

MoEngage goes shopping with Chef. There are $N$ ingredients placed on a line, numbered $1$ to $N$ from left to right.

At any point in time, MoEngage can choose the ingredient numbered $x$ and do **one** of the following operations:
- If the chosen ingredient is not the leftmost amongst the remaining ingredients, **remove the left neighbor**. This operation costs $L_x$ coins.
- If the chosen ingredient is not the rightmost amongst the remaining ingredients, **remove the right neighbor**. This operation costs $R_x$ coins.

**Note:** MoEngage can perform **at most one** operation of one type on a particular ingredient. For example, you can't remove elements from the left of ingredient $x$ two times. However, you can remove one ingredient each from the left and from the right of ingredient $x$.

MoEngage performs the operations until only one ingredient is left.
Find the **minimum** number of coins he needs to pay so that only one ingredient is left.

---

## Input Format

- The first line contains a positive integer $T$ - the number of test cases. Then $T$ test cases follow.
- The first line of each test case contains a single integer $N$ - the number of ingredients.
- The second line of each test case contains $N$ integers $L_1, L_2, \ldots, L_N$ - the number of coins required to remove the ingredient from the left of an ingredient.
- The third line of each test case contains $N$ integers $R_1, R_2, \ldots, R_N$ - the number of coins required to remove the ingredient from the right of an ingredient.

---

## Output Format

For each test case, output in a new line, one integer - the **minimum** number of coins MoEngage needs to pay so that only one ingredient is left.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \le L_i, R_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
1
3
4
4
2 1 3 2
4 2 4 3
7
3 10 5 2 8 3 9
8 6 11 5 9 13 7
```

**Output**

```text
0
5
32
```

**Explanation**

- **Test case 1:** The number of ingredients is already $1$. Thus, MoEngage has to spend $0$ coins.
- **Test case 2:** Initially, the list of ingredients is $[1, 2, 3, 4]$. MoEngage can apply the operations in the following way:
    - Apply the first operation on ingredient $4$. Coins required for this are $L_4 = 2$. The updated list of ingredients is $[1, 2, 4]$.
    - Apply the second operation on ingredient $2$. Coins required for this are $R_2 = 2$. The updated list of ingredients is $[1, 2]$.
    - Apply the first operation on ingredient $2$. Coins required for this are $L_2 = 1$. The updated list of ingredients is $[2]$.

Thus, the total number of coins required is $2+2+1 = 5$. It can be shown that MoEngage cannot achieve a single ingredient in less than $5$ coins.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
3
4
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4
2 1 3 2
4 2 4 3
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
7
3 10 5 2 8 3 9
8 6 11 5 9 13 7
```

**Output for this case**

```text
32
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Chef Goes Shopping](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CHEFSHOPPING)

### [](#problem-statement-1)Problem Statement

MoEngage goes shopping with Chef. There are N ingredients placed on a line, numbered 1 to N from left to right.

At any point in time, MoEngage can choose the ingredient numbered x and do **one** of the following operations:

- If the chosen ingredient is not the leftmost amongst the remaining ingredients, **remove the left neighbor**. This operation costs L_x coins.

- If the chosen ingredient is not the rightmost amongst the remaining ingredients, **remove the right neighbor**. This operation costs R_x coins.

**Note:** MoEngage can perform **at most one** operation of one type on a particular ingredient. For example, you can’t remove elements from the left of ingredient x two times. However, you can remove one ingredient each from the left and from the right of ingredient x.

MoEngage performs the operations until only one ingredient is left.

Find the **minimum** number of coins he needs to pay so that only one ingredient is left.

### [](#approach-2)Approach

To solve the problem, the logic is to minimize the cost of operations needed to reduce the number of ingredients to one. Each ingredient x has two potential costs associated with it: removing the left neighbor at a cost of L_x and removing the right neighbor at a cost of R_x. Since we can only remove one neighbor at a time, the strategy should be to choose the minimum of the two possible operations for each pair of adjacent ingredients. Specifically, for each pair of adjacent ingredients, we will add the minimum of the cost to remove the left neighbor of the next ingredient and the right neighbor of the current ingredient. We continue this process for all ingredients except the first and the last one because they don’t have both left and right neighbors. The total cost is the sum of all these minimal costs.

### [](#time-complexity-3)Time Complexity

The time complexity of the solution is O(N), where N is the number of ingredients, because we are simply iterating through the list of ingredients once.

### [](#space-complexity-4)Space Complexity

The space complexity is O(N) due to the storage used for the two arrays that hold the costs for removing neighbors on the left and right for each ingredient.

</details>
