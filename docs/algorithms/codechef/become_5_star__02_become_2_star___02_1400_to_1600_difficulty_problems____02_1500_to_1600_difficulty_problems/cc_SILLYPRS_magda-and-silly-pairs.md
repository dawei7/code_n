# Magda and Silly Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SILLYPRS |
| Difficulty Rating | 1507 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [SILLYPRS](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/SILLYPRS) |

---

## Problem Statement

Chef and his friend Magda have $2N$ mutual friends: $N$ of these friends are chefs and the other $N$ are chefettes. The chefs are numbered $1$ through $N$ and the chefettes are (independently) also numbered $1$ through $N$. Since Magda wants their friends to be as happy as possible and to preserve traditional family values, she wants to pair them up in such a way that each chef is paired with exactly one chefette and each chefette with exactly one chef.

The chefs have heights $A_1, A_2, \ldots, A_N$ and the chefettes have heights $B_1, B_2, \ldots, B_N$. For each valid $i, j$, if the $i$-th chef and the $j$-th chefette are paired, they will have exactly one child with height $\left\lfloor\frac{A_i+B_j}{2}\right\rfloor$. Magda wants to pair up the chefs and chefettes in such a way that the sum of heights of all their children ($N$ children in total) is maximum possible. Please help her do that.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

### Output
Print a single line containing one integer ― the maximum sum of heights of the children.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- $1 \le B_i \le 10^9$ for each valid $i$

### Subtasks
**Subtask #1 (40 points):** $1 \le N \le 100$

**Subtask #2 (60 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
4 5 6
1 2 3
5
4 8 6 4 1
2 5 7 4 7
```

**Output**

```text
10
23
```

**Explanation**

**Example case 1:** One possible solution is to pair the first chef with the second chefette, the second chef with the first chefette and the third chef with the third chefette. Their children will have heights $3$, $3$ and $4$, respectively.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
4 5 6
1 2 3
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
5
4 8 6 4 1
2 5 7 4 7
```

**Output for this case**

```text
23
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Magda and Silly Pairs Practice Problem in 1400 to 1600 difficulty problems](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/SILLYPRS)

### [](#problem-statement-1)Problem Statement:

We need to pair `N` chefs with `N` chefettes to maximize the total sum of heights of their children. The height of the child resulting from the pairing of the `i-th` chef and the `j-th` chefette is given by:

Height of child=⌊A_i+B_j⌋/2. Where A_i is the height of the `i-th` chef and $B_j$​ is the height of the `j-th` chefette.

### [](#approach-2)Approach:

- Read the heights of chefs and add each height to `sum`.

- Check if each height is odd using `x & 1` (bitwise operation to check if `x` is odd). Increment `odd` if it is.

- Read the heights of chefettes, add each height to `sum`, and decrement `odd` if the height is odd.

- After processing both arrays, `odd` holds the net difference in the number of odd numbers between the two arrays.

- The result for the maximum possible sum of heights of the children is calculated as: ans=(sum−∣odd∣)/2.

- This formula ensures the sum is adjusted to balance out the pairing of odd and even numbers to maximize the overall sum.

- Pairing an odd number with another odd or an even with an even results in an integer average. Pairing an odd with an even results in a non-integer average, which, when floored, results in a lower sum.

- By subtracting `abs(odd)`, we ensure that we adjust for these cases to maximize the sum.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(n)` per test case for reading input and calculating `sum` and `odd`.

- **Space Complexity:** `O(1)` for auxiliary space since only variables are used.

</details>
