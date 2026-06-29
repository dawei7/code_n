# Chef Builds Subsets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BWFPF01 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [BWFPF01](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/BWFPF01) |

---

## Problem Statement

Chef has a list of integers $inputNumbers$ that may contain duplicates. \
Chef wants to find all possible subsets of this list, including the empty subset, but without any duplicate subsets in the final collection. \
Help Chef generate the complete power set of the list such that each subset is unique. Chef does not mind the order in which the subsets appear, but each subset must be represented as a list of integers.

## Function Declaration

### Function Name
$findSubsetsWithDuplicates$

### Parameters
- $inputNumbers$: A reference to a array containing Chef's list of integers, which may include duplicates.

### Return Value
- Returns an array of arrays , where each inner array represents a unique subset of Chef's input list.
- The output includes all possible subsets without any duplicate subsets.
- Subsets can be in any order.

## Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 10$
- $-10 \leq \text{inputNumbers}[i] \leq 10$

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* Each test case consists of:
  * A line containing an integer $N$ — the size of the array.
  * A line containing $N$ integers — the elements of the array.

---

## Output Format

* For each test case, print all unique subsets of the array.
* Each subset should be printed on a new line
* Print the empty subset as an empty line.
* The order of subsets and the order of integers inside a subset do not matter, but no duplicate subsets should be printed.

---

## Examples

**Example 1**

**Input**

```text
2
3
1 1 2
4
2 2 2 3
```

**Output**

```text
[]
[1]
[1 1]
[1 1 2]
[1 2]
[2]
[]
[2]
[2 2]
[2 2 2]
[2 2 2 3]
[2 2 3]
[2 3]
[3]
```

**Explanation**

- For the first test case, input [1,1,2]: subsets include empty set, single elements [1], [2], duplicates handled by including [1,1], and combinations like [1,2], [1,1,2].
- For the second test case, input [2,2,2,3]: subsets start from empty, single [2], multiple [2,2], [2,2,2], then add [3] in combinations like [2,3], [2,2,3], [2,2,2,3], and [3] alone.

**Example 2**

**Input**

```text
1
5
-1 0 0 1 1
```

**Output**

```text
[]
[-1]
[-1 0]
[-1 0 0]
[-1 0 0 1]
[-1 0 0 1 1]
[-1 0 1]
[-1 0 1 1]
[-1 1]
[-1 1 1]
[0]
[0 0]
[0 0 1]
[0 0 1 1]
[0 1]
[0 1 1]
[1]
[1 1]
```

**Explanation**

- For the array [-1, 0, 0, 1, 1], we generate all unique subsets by including or excluding each element, ensuring duplicates like [0,0] or [1,1] appear only once.
- Start with empty subset [], then add elements stepwise: [-1], [-1,0], [-1,0,0], and so forth, skipping repeated subsets caused by duplicate 0s and 1s.
- The output lists all distinct combinations, including subsets with duplicates only when they appear in the input, like [0,0] and [1,1].

**Example 3**

**Input**

```text
1
1
5
```

**Output**

```text
[]
[5]
```

**Explanation**

- For the input [5], the subsets are the empty set [] and the set containing 5 itself [5].

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Understanding

The problem asks us to generate **all unique subsets** (the power set) of a given list of integers, which may contain duplicates. The key points are:

1. **Subsets include the empty subset.**
2. **Subsets can contain repeated numbers** if they appear in the input, but duplicate subsets must not appear in the output.
3. **Order of subsets and order of numbers within a subset does not matter.**

Example:

* Input: `[1,1,2]`
* Unique subsets: `[]`, `[1]`, `[1,1]`, `[1,2]`, `[1,1,2]`, `[2]`

---

### Approach

1. **Sort the input array**

   * Sorting ensures that duplicates are consecutive.
   * This allows us to easily skip duplicates when generating subsets.

2. **Use backtracking / recursive exploration**

   * Start with an empty subset.
   * At each step, either **include** the current number or **skip** it.
   * After including a number, recurse to the next index.
   * Keep track of the current subset in progress.

3. **Handle duplicates carefully**

   * If the current number is the same as the previous one **and** we did not include the previous one in this recursive path, skip it.
   * This ensures that subsets like `[1,1]` are generated once, not multiple times.

4. **Add every generated subset to the result**

   * This includes the empty subset.

5. **Print or return the subsets**

   * Each subset should be formatted in square brackets with space-separated numbers.
   * The empty subset should appear as `[]`.

---

### Steps of the Algorithm

1. Sort the input array.
2. Initialize an empty list to store the current subset.
3. Start backtracking from index 0:

   * Add the current subset to the result.
   * Loop over the remaining numbers starting from the current index:

     * Skip numbers that are the same as the previous one to avoid duplicates.
     * Include the number in the current subset and recurse.
     * Remove the number (backtrack) before moving to the next number.
4. Continue until all numbers are processed.
5. Return or print the result list of subsets.

---

### Complexity Analysis

* **Time Complexity:**

  * In the worst case, there are `2^N` subsets for a list of size `N`.
  * Sorting takes `O(N log N)`.
  * Generating subsets takes `O(N * 2^N)` because each subset can have up to `N` elements.
  * Overall: `O(N log N + N * 2^N)`

* **Space Complexity:**

  * Space for storing the current subset (`O(N)`) and the result (`O(N * 2^N)`).
  * Recursion stack also uses up to `O(N)` space.

---

### Key Insights

1. Sorting the input is crucial to **handle duplicates efficiently**.
2. Backtracking allows systematic exploration of **all combinations**.
3. Skipping consecutive duplicates ensures **unique subsets** only.
4. The empty subset is always part of the power set.
5. This approach works efficiently for small input sizes (up to around N = 10).

---

This method is general and can be implemented in any programming language using recursion or iterative approaches with careful handling of duplicates.

</details>
