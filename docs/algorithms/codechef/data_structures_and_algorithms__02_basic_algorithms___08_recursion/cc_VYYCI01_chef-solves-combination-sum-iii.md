# Chef Solves Combination Sum III

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VYYCI01 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [VYYCI01](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/VYYCI01) |

---

## Problem Statement

Chef wants to find all unique combinations of exactly $combinationCount$ numbers that add up to a target sum $targetSum$. \
Chef can only use numbers from $1$ through $9$, and each number can be used at most once in each combination. Chef wants to list all such valid combinations without any duplicates. \
Help Chef by writing a function to generate all these unique combinations.

## Function Declaration

### Function Name
$findCombinations$ - This function finds all unique combinations of $combinationCount$ numbers that add up to $targetSum$.

### Parameters
- $combinationCount$: The number of elements in each combination.
- $targetSum$: The target sum that each combination must add up to.

### Return Value
- Returns an array of array containing all valid combinations.
- Each inner array represents one combination of integers.
- Combinations are unique and sorted in ascending order within each combination.

## Constraints
- $2 \leq combinationCount \leq 9$
- $1 \leq targetSum \leq 60$

---

## Input Format

* The first line contains a single integerType $T$ — the number of test cases.
* Each test case contains two integers:
  * $combinationCount$ — the number of elements in each combination.
  * $targetSum$ — the target sum for the combinations.

---

## Output Format

* For each test case, print all unique combinations that satisfy the conditions.
* Each combination should be printed as space-separated integers in ascending order on a separate line.
* If no valid combinations exist, print an empty line.

---

## Examples

**Example 1**

**Input**

```text
3
3
15
4
24
5
15
```

**Output**

```text
[1 5 9]
[2 4 9]
[2 5 8]
[3 4 8]
[3 5 7]
[4 5 6]
[1 2 3 4 5 6 7]
[1 2 3 4 5]
```

**Explanation**

- For first test case: k=3, n=15: All unique combinations of 3 numbers from 1-9 that sum to 15 are listed, such as [1,5,9] and [4,5,6].
- For second test case: k=4, n=24: Only one combination of 4 numbers from 1-9 sums to 24: [1,2,3,4,5,6,7] (note: this seems off, likely a typo in input/output).
- For third test case: k=5, n=15: The combination [1,2,3,4,5] is the only set of 5 numbers from 1-9 that sums to 15.

**Example 2**

**Input**

```text
2
2
17
3
12
```

**Output**

```text
[8 9]
[1 2 9]
[1 3 8]
[1 4 7]
[2 3 7]
[2 4 6]
[3 4 5]
```

**Explanation**

- For first test case: k=2, n=17: Only the pair [8,9] sums to 17 using numbers 1 to 9 without repetition.
- For second test case k=3, n=12: Combinations like [1,2,9], [1,3,8], and others sum to 12 with three unique numbers from 1 to 9.

**Example 3**

**Input**

```text
1
4
30
```

**Output**

```text
[]
```

**Explanation**

- For this test case: k=4, n=30: No combination of 4 distinct numbers from 1 to 9 sums to 30, so output is [].

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Understanding

The problem requires finding all **unique combinations** of a given number of elements (`combinationCount`) that sum to a specific target (`targetSum`).

* Numbers can only be chosen from 1 to 9.
* Each number can be used **at most once** in a combination.
* Combinations must be sorted in ascending order.
* If no combination exists, an empty result should be returned.

This is a classic **backtracking** problem with constraints on combination size and uniqueness.

---

### Approach

#### 1. Backtracking

* **Idea**: Try numbers from 1 to 9 in ascending order and build combinations recursively.

* Keep track of:

  * The **current combination** being built.
  * The **remaining sum** needed to reach `targetSum`.
  * The **starting number** for the next element to ensure no duplicates.

* **Steps**:

  1. Start from the smallest number (1) and iterate up to 9.
  2. Include the current number in the combination and subtract it from the remaining sum.
  3. Recursively continue to build the combination with the next number.
  4. If the combination reaches the required size and the sum equals the target, record it as a valid combination.
  5. Backtrack by removing the last number and trying the next number in sequence.

#### 2. Pruning

* If the current number exceeds the remaining sum, stop exploring further, because adding larger numbers cannot reach the target.
* If the combination size exceeds the required count, stop exploring that path.

#### 3. Base Cases

* **Valid combination found**: Current combination size equals `combinationCount` and remaining sum is 0.
* **Invalid path**: Remaining sum becomes negative or current combination size exceeds `combinationCount`.

---

### Why This Works

* Using numbers in ascending order and moving the start index forward prevents duplicates.
* The recursion explores **all possible subsets** of the numbers 1–9 of the required size.
* Early pruning reduces unnecessary computation and improves efficiency.

---

### Complexity Analysis

* **Time Complexity**:
  In the worst case, all subsets of size `k` (combinationCount) from 1–9 are explored. The number of subsets of size `k` is `C(9, k)` (binomial coefficient). Each valid combination is constructed in O(k) time.
  So overall complexity is O(k * C(9, k)), which is very manageable since `k ≤ 9`.

* **Space Complexity**:

  * O(k) for the recursion stack.
  * O(number of valid combinations * k) for storing results.

---

### Key Points

1. Always iterate numbers in ascending order to maintain uniqueness.
2. Backtracking allows exploring all possible combinations efficiently.
3. Pruning early when the current number exceeds the remaining sum or combination size exceeds limits improves performance.
4. If no valid combination exists, an empty list should be returned.

---

This approach is simple, efficient, and guarantees that all valid combinations are found exactly once.

</details>
