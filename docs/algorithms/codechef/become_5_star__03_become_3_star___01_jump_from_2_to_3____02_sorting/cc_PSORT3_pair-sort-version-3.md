# Pair Sort Version 3

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PSORT3 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [PSORT3](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/PSORT3) |

---

## Problem Statement

You are given two arrays $A$ and $B$ of size $N$. We define a pair as $(A_i$, $B_i)$ where $0 \le i \le N - 1$.

The task is to sort these pairs in **decreasing** order of the second elements of the pairs i.e $B_i$. If both the second elements are equal sort according to **increasing** order of the first elements of the pairs.

Output the sorted pairs in a single line with a space separating the pairs. Each pair is printed with first element followed by a space and second element. See Explanation Section for better understanding.

### Input:

- First line will contain a single integer $N$.
- Second line contains $N$ space separated integers $A_0$, $A_1$, $...$ $A_{N - 1}$ denoting the elements of array $A$.
- Third line contains $N$ space separated integers $B_0$, $B_1$, $...$ $B_{N - 1}$ denoting the elements of array $B$.

### Output:
Output in a single line $2 * N$ space separated integers. Output the pairs in sorted order, where the first element of a pair is from $A_j$ and second element is from $B_j$ with a space in between.

### Constraints
- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^{18}$

### Subtasks
- 30 points : $1 \leq N \leq 1000$
- 70 points : Original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2 2 3
6 3 3
```

**Output**

```text
2 6 2 3 3 3
```

**Explanation**

The pairs are:
- $(2, 6)$
- $(2, 3)$
- $(3, 3)$

We are required to sort these pairs in decreasing order of second elements and then increasing order of first elements. Therefore, pairs sorted:
- $(2, 6)$
- $(2, 3)$
- $(3, 3)$

You can clearly see that the **second elements are in decreasing order from top to bottom** and when second elements of two pairs are equal they are **sorted in increasing order of first elements from top to bottom**. We print the pairs as follows:

$2\ 6\ 2\ 3\ 3\ 3$

The first two elements correspond to pair 1 in sorted list. The next two elements correspond to pair 2 in sorted list. The last two elements correspond to pair 3 from sorted list.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Pair Sort Version 3 Practice Problem in Jump from 2* to 3*](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/PSORT3)

### [](#problem-statement-1)Problem Statement:

To solve this problem, we need to sort pairs of two arrays, A and B, based on specific conditions:

- **Primary Sort**: Sort the pairs in decreasing order based on the second element (i.e., the corresponding element from array B).

- **Secondary Sort**: If the second elements are the same, sort those pairs by the first element (i.e., the corresponding element from array A) in increasing order.

### [](#approach-2)Approach:

**Understanding the Sorting Criteria:**

- The first thing to understand is that we need a custom sorting order for these pairs.

- Given that sorting based on the second element is the primary requirement, we will prioritize sorting by B_i first, ensuring that the pairs with higher values of B_i come before the ones with lower values.

- If two pairs have the same second element, then the first element A_i should be considered, and we sort those pairs in increasing order based on A_i.

**Data Representation:**

- We will create pairs of (A_i,B_i), where `i` ranges from `0` to `N−1`. These pairs will be stored as a vector of **pair<int, int>**, which is a standard C++ data structure for representing pairs of integers.

**Sorting Using Custom Comparator:**

- C++ allows us to define custom sorting criteria by passing a comparison function to the sort function. In this case, the comparator should compare the second elements of the pairs in descending order, and in case of a tie, it should compare the first elements in ascending order.

### [](#complexity-3)Complexity:

- **Time Complexity:** The time complexity is `O(N log N)`, where `N` is the number of pairs. This is because the main operation is sorting the pairs, which takes `O(N log N)`.

- **Space Complexity:** The space complexity is `O(N)` due to the storage required for the vector of pairs.

</details>
