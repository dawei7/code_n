# Put fruits into basket

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FRUITBASKET |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [FRUITBASKET](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/FRUITBASKET) |

---

## Problem Statement

You have a row of fruit trees planted in a straight line, from left to right. An integer array $fruits$ represents the trees, where $fruits[i]$ denotes the type of fruit produced by the $i^\text{th}$ tree.

You have **two baskets**, and each basket can carry **only one type of fruit**, but there is no limit on the quantity of fruit in each basket. You want to collect the **maximum number of fruits** by following these rules:

1. You can start picking fruits from **any tree** and must move to the **right**.
2. You pick exactly **one fruit from each tree** you visit.
3. You can only pick fruits that fit into your two baskets. Once you encounter a fruit type that **doesn’t match the two types already in your baskets**, you must stop collecting.

Return the **maximum number of fruits** you can collect for each test case.

## Function Declaration

### Function Name
$totalFruits$ – This function determines the maximum number of fruits that can be collected using at most two baskets, where each basket can hold only one type of fruit.

### Parameters

* $fruits$ : A reference to an integer array where $fruits[i]$ represents the type of fruit on the $i^{th}$ tree.

### Return Value

* Returns an integer representing the maximum number of fruits that can be collected following the given rules.

## Constraints

- $1 \leq t \leq 10^5$
- $1 \leq n \leq 10^5$
- The total number of elements across all test cases will not exceed $10^5$.

---

## Input Format

- The first line contains a single integer $t$ — the number of test cases.
- For each test case:
  - The first line contains an integer $n$ — the number of trees.
  - The second line contains $n$ integers representing the array $fruits$.

---

## Output Format

- For each test case, print a single integer — the maximum number of fruits that can be collected.

---

## Constraints

- $1 \leq t \leq 10^5$
- $1 \leq n \leq 10^5$
- $0 \leq \text{fruits}[i] < n$

Additionally, the total number of elements across all test cases will not exceed (10^5).

---

## Examples

**Example 1**

**Input**

```text
2
5
3 3 2 1 3
4
1 2 1 2
```

**Output**

```text
3
4
```

**Explanation**

**Test case 1:** `[3, 3, 2, 1, 3]`

* Start at the first tree: baskets can hold `3` and `2`.
* You can pick `3, 3, 2` before encountering `1`, which doesn’t fit.
* Maximum fruits collected: **3**.

**Test case 2:** `[1, 2, 1, 2]`

* Start at the first tree: baskets hold `1` and `2`.
* You can pick all four fruits `1, 2, 1, 2`.
* Maximum fruits collected: **4**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
3 3 2 1 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
1 2 1 2
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Understanding

You are given a row of trees, each producing a type of fruit. You have **two baskets**, and each basket can only hold **one type of fruit**, but there is no limit on the quantity. You want to collect as many fruits as possible by moving **rightward from any starting tree** and picking **exactly one fruit per tree**. Once a tree produces a fruit type that cannot fit into your baskets, you must stop.

The goal is to **maximize the number of fruits collected**.

---

## Key Observations

1. You are essentially looking for the **longest contiguous subarray** containing **at most 2 distinct values**.
2. You can start at any tree, but since only the rightward path matters, you can consider **every subarray** starting from the left.
3. The problem reduces to **sliding window / two-pointer technique**:

   * Maintain a window of consecutive trees that contains **at most 2 distinct fruit types**.
   * Track the **count of each fruit type** in the current window.
   * When a third fruit type is encountered, shrink the window from the left until there are only 2 types.

---

## Approach

1. Initialize two pointers, `left` and `right`, to define a sliding window.
2. Use a data structure (e.g., map, dictionary, or array) to store the **count of each fruit type** in the current window.
3. Iterate over the trees with the `right` pointer:

   * Add the current fruit to the window (increment its count).
   * If the number of distinct fruit types exceeds 2:

     * Shrink the window from the left by decrementing the count of the fruit at `left`.
     * If its count becomes zero, remove it from the window.
     * Move `left` forward.
4. After each step, calculate the current window size (`right - left + 1`) and update the maximum.
5. After processing all trees, the maximum window size is the **maximum number of fruits that can be collected**.

---

## Time and Space Complexity

* **Time Complexity:** O(n) per test case, because each tree is visited at most twice (once when entering the window, once when leaving).
* **Space Complexity:** O(1) in theory, because the window can hold at most 2 fruit types, though using a map may take up to O(n) in some implementations.

---

## Edge Cases to Consider

1. **Single tree** → maximum fruits = 1.
2. **All fruits are the same** → maximum fruits = length of the array.
3. **All fruits are unique** → maximum fruits = 2, since only two types can be collected.
4. **Alternating two types** → the window can extend across the entire array.
5. **Random patterns with multiple switches** → test the sliding window correctly shrinks and expands.

---

## Conclusion

The problem is a classic **sliding window problem** where you track the longest subarray with at most 2 distinct elements. The key is to **efficiently maintain the counts of fruit types** and adjust the window when the constraint is violated.

This approach works efficiently even for large arrays, as it processes each element only a constant number of times.

</details>
