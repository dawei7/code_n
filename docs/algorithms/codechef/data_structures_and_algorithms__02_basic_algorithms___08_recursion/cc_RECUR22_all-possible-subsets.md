# All Possible Subsets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR22 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR22](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR22) |

---

## Problem Statement

You are given an Array and you have to output all possible subsets of that array.

For Example:
Let the array Arr = [1, 2, 3], It's possible subsets include:
- {}
- {1}
- {2}
- {3}
- {1, 2}
- {2, 3}
- {1, 3}
- {1, 2, 3}

**Note** - Print the subsets in sorted order.

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the number of integers in the array.
- The second line contains $N$ integers.

---

## Output Format

Output All the possible subsets of the given array.

---

## Constraints

- $1 \leq N \leq 10$
- $1 \leq A_i \leq 10^5$
- There are no duplicate values in the array.

---

## Examples

**Example 1**

**Input**

```text
3
1 2 3
```

**Output**

```text
1
1 2
1 2 3
1 3
2
2 3
3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [All Possible Subsets in Recursion](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR22)

### [](#problem-statement-1)Problem Statement:

You are given an Array and you have to output all possible subsets of that array.

You have to print the subarrays in sorted order.

### [](#approach-2)Approach:

- **Recursive Function**: The `allPossibleSubsets` function takes the current index, the original array, the current subset being built, and a reference to all subsets found so far.

- **Base Case**: If the `index` reaches the size of the array, the current subset is added to the list of all subsets.

- **Recursive Cases**:

- First, it explores the case where the current element is not included.

- Then, it includes the current element in the subset and recursively explores further.

- After including the element, it backtracks by removing the last added element to ensure the next iteration starts with the correct state.

- **Backtracking**: The use of backtracking ensures that we explore all combinations without skipping any potential subsets.

- **Sorting**: After generating all subsets, we sort them to maintain the required order in the output.

### [](#complexity-3)Complexity:

- **Time complexity:** The time complexity is `O(2^N)` because there are `2^N` possible subsets for an array of size `N`. Each subset takes `O(N)` time to copy into the result.

- **Space Complexity:** The space complexity is `O(N)` for the recursive call stack at maximum depth and `O(2^N)` for storing the subsets in the result. Thus, the overall space complexity is `O(N+2^N)`.

</details>
