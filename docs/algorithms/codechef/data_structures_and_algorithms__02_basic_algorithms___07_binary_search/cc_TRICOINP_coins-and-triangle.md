# Coins And Triangle

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRICOINP |
| Difficulty Rating | 1075 |
| Difficulty Band | Binary Search |
| Path | Data Structures and Algorithms |
| Lesson | More Problems |
| Official Link | [TRICOINP](https://www.codechef.com/learn/course/binary-search/LIBSDSA07/problems/TRICOINP) |

---

## Problem Statement

Chef belongs to a very rich family which owns many gold mines. Today, he brought **N** gold coins and decided to form a triangle using these coins. Isn't it strange?

Chef has a unusual way of forming a triangle using gold coins, which is described as follows:

- He puts **1** coin in the **1st** row.

- then puts **2** coins in the **2nd** row.

- then puts **3** coins in the **3rd** row.

-  and so on as shown in the given figure.

Chef is interested in forming a triangle with maximum possible height using at most **N** coins. Can you tell him the maximum possible height of the triangle?

### Input

The first line of input contains a single integer **T** denoting the number of test cases.

The first and the only line of each test case contains an integer **N** denoting the number of gold coins Chef has.

### Output

For each test case, output a single line containing an integer corresponding to the maximum possible height of the triangle that Chef can get.

### Constraints

- **1 ≤ T ≤ 100**

- **1 ≤ N ≤ 109**

### Subtasks

- Subtask 1 (48 points) : **1 ≤ N ≤ 105**

- Subtask 2 (52 points) : **1 ≤ N ≤ 109**

---

## Examples

**Example 1**

**Input**

```text
3
3
5
7
```

**Output**

```text
2
2
3
```

**Explanation**

**Test 1:** Chef can't form a triangle with height > 2 as it requires atleast 6 gold coins.
**Test 2:** Chef can't form a triangle with height > 2 as it requires atleast 6 gold coins.
**Test 3:** Chef can't form a triangle with height > 3 as it requires atleast 10 gold coins.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
7
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Coins And Triangle in Binary Search](https://www.codechef.com/learn/course/binary-search/LIBSDSA07/problems/TRICOINP)

### [](#problem-statement-1)Problem Statement:

Chef belongs to a very rich family which owns many gold mines. Today, he brought N gold coins and decided to form a triangle using these coins. Isn’t it strange? Chef has a unusual way of forming a triangle using gold coins, which is described as follows:

He puts **1** coin in the **1st** row, then puts **2** coins in the **2nd** row, then puts **3** coins in the **3rd** row, and so on.

Chef is interested in forming a triangle with maximum possible height using at most **N** coins. Can you tell him the maximum possible height of the triangle?

### [](#approach-2)Approach:

To form a triangle of height h, the total number of coins required is the sum of the first h natural numbers:

Total coins for height h=1+2+3+⋯+h=h(h+1)/2

- **Using Binary Search:**

- Initialize two pointers one with 1 and other with number of coins.

- Calculate the midpoint. Compute the total number of coins required for a triangle of height `mid` using the formula mid(mid+1)/2.

- Check if the total number of coins for height `mid` is less than or equal to N

- Update the answer to `mid` (as it is a valid height).

- Move the `lower_bound` to `mid+1` to check if a larger height is possible.

- If the total number of coins for height `mid` exceeds N, reduce the `upper bound` to `mid−1` to try for a smaller height.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(log N)` for binary search

- **Space Complexity:** `O(1)` No extra space used.

</details>
