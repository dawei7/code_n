# Aggressive Cows

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAAGP1099 |
| Difficulty Rating | 932 |
| Difficulty Band | Binary Search |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to binary search |
| Official Link | [DSAAGP1099](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSAAGP1099) |

---

## Problem Statement

Farmer John has built a new long barn, with $N$ stalls. The stalls are located along a straight line at positions $x_1 ... x_N$.

His $C$ cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, Farmer John wants to assign the cows to stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

### Task
You are given the check function, now you have to use predicate binary search to search for the minimum solution for this problem.

---

## Input Format

- The first line of input contains two space-separated integers $N$ and $K$  denoting the number of elements in the array $A$ and the element to search.
- The second line contains $N$ space-separated integers denoting the elements in the array $A$.

---

## Output Format

- Output position of $K$ or the position where $K$ is to be inserted.

---

## Constraints

- $2 \leq N \leq 10^5$
- $2 \leq C \leq N$
- $0 \leq x_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
5 3
1 2 8 4 9
```

**Output**

```text
3
```

**Explanation**

We can put 3 cows in the stalls at positions 1, 4 and 8,
resulting in a minimum distance of 3.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Aggressive Cows in Binary Search](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSAAGP1099)

### [](#problem-statement-1)Problem Statement:

Farmer John has built a new long barn, with N stalls. The stalls are located along a straight line at positions x_1, ..., x_N.

​His C cows don’t like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, Farmer John wants to assign the cows to stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

### [](#approach-2)Approach:

- **Sorting the Stall Positions**: The array (which contains the stall positions) is sorted in ascending order. This is important because the stalls need to be considered in order to calculate the distance between them.

- **Binary Search Setup**:

- Initialize two pointers: `low` and `high`:

- `low = 0`: This represents the smallest possible distance between two cows.

- `high = 1e9 + 1`: This represents the largest possible distance (just beyond the maximum possible stall position of 10^9).

- **Using Binary Search**:

- The loop performs binary search to find the maximum possible minimum distance between cows:

- `mid` is calculated as the midpoint between `first` and `last`.

- The `check` function is called with `mid` as the target distance, to check if it’s possible to place all cows with at least this distance between them. Refer for check function: [Aggressive Cows in Binary Search](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSAAGP1098)

- If placing cows with this distance is possible (`canplace == true`), the search continues to the right (increasing the minimum distance by setting `first = mid`).

- If not, the search continues to the left by updating `last = mid`.

- Once the binary search completes the value of `first` is printed. This represents the largest minimum distance at which the cows can be placed.

### [](#complexity-3)Complexity:

- **Time Complexity:** Sorting takes `O(n log n)`, Binary search utilizes `O(log n)` and the check function takes `O(n)` for iterating through the stalls. Total time complexity: `O(n log n) + O(log n) + O(n) = O(n log n)`.

- **Space Complexity:** `O(1)` No extra space is used.

</details>
