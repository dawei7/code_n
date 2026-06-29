# Chef Finds Combination Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FRXUX01 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [FRXUX01](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/FRXUX01) |

---

## Problem Statement

Chef has a collection of numbers of candidates $candidateNumbers$ and a number $targetSum$. Chef wants to find all unique combinations of these $candidateNumbers$ where the sum equals the $targetSum$. \
Each candidateNumber can be used only once in each combination. Help Chef find all such unique combinations without any duplicates.

Chef needs your help to implement a function that returns all these unique combinations.

## Function Declaration

### Function Name
$findCombinationSum2$ - This function finds all unique combinations of $candidateNumbers$ that sum up to the $targetSum$.

### Parameters
- $candidateNumbers$: A vector of integers representing the numbers of candidates available for combinations.
- $targetSum$: The target integer sum for which combinations are to be found.

### Return Value
- Returns an array of array of integers.
- Each inner array represents a unique combination of $candidateNumbers$ that add up to $targetSum$.
- The combinations are returned in no particular order, and duplicates are excluded.

## Constraints
- $1 \leq \text{candidateNumbers.length} \leq 100$
- $1 \leq \text{candidateNumbers}[i] \leq 50$
- $1 \leq \text{targetSum} \leq 30$

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* Each test case contains:
  * First line: integers representing Chef's candidateNumbers.
  * Second line: An integer $targetSum$ — the target sum Chef wants to achieve.

---

## Output Format

* For each test case, print all unique combinations of candidateNumbers that sum up to targetSum.
* The order of combinations and the order of integers within a combination do not matter.
* If no combination is found, print an empty line.

---

## Examples

**Example 1**

**Input**

```text
1
[2, 5, 2, 1, 2]
5
```

**Output**

```text
[1 2 2]
[5]
```

**Explanation**

- For the input array [2, 5, 2, 1, 2] with target 5, the unique combinations that sum to 5 are [1, 2, 2] and [5].
- [1, 2, 2] is formed by picking 1 and two 2's; [5] is a single element equal to the target.

**Example 2**

**Input**

```text
2
[4, 3, 2, 7, 3, 5]
6
[1, 1, 2, 5, 6, 7, 10]
9
```

**Output**

```text
[2 4]
[3 3]
[1 1 2 5]
[1 1 7]
[1 2 6]
[2 7]
```

**Explanation**

- For the first test case (target=6, candidates=[4,3,2,7,3,5]):
  Combinations that sum to 6 are [2 4] (2+4=6), [3 3] (3+3=6), and [4 5] (4+5=9 no, ignore). Correct sums are [3 3] and [2 4].

- For the second test case (target=9, candidates=[1,1,2,5,6,7,10]):
  Combinations summing to 9 are [1 1 2 5] (1+1+2+5=9), [2 7] (1+1+7=9), [1 2 6] (1+2+6=9), and [2 7] (2+7=9). These are the output lines matching sum 9.

**Example 3**

**Input**

```text
1
[1, 1, 1, 2, 2, 3, 4, 5]
8
```

**Output**

```text
[1 1 1 2 3]
[1 1 1 5]
[1 1 2 4]
[1 2 2 3]
[1 2 5]
[1 3 4]
[2 2 4]
[3 5]
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## 1. Problem Breakdown

Imagine you have a list of numbers called `candidateNumbers` and a `targetSum`. Your goal is to find all unique combinations of numbers from `candidateNumbers` that add up exactly to `targetSum`. Each number in `candidateNumbers` can only be used once in each combination. Also, the list might have duplicates, but the combinations you return should not repeat the same set of numbers.

For example, if `candidateNumbers` is `[10, 1, 2, 7, 6, 1, 5]` and `targetSum` is `8`, some valid combinations are `[1, 7]`, `[1, 2, 5]`, `[2, 6]`, and `[1, 1, 6]`. Notice that `[1, 7]` appears only once, even though there are two `1`s in the list.

## 2. Approach 1 — Brute Force

### Idea

A straightforward way to solve this problem is to try every possible combination of numbers and check if their sum equals `targetSum`. This means:

- Start from the first number.
- For each number, decide to either include it in the current combination or skip it.
- Move to the next number and repeat.
- If the sum of the current combination equals `targetSum`, save it.
- If the sum exceeds `targetSum`, stop exploring that path.

This approach explores all subsets of `candidateNumbers`.

### Step-by-step reasoning

1. Begin with an empty combination and the full `targetSum`.
2. At each step, pick the current number and try two things:
   - Include it in the combination and reduce the `targetSum` accordingly.
   - Exclude it and move on.
3. Recursively do this for all numbers.
4. Whenever the `targetSum` becomes zero, record the current combination.
5. If the `targetSum` becomes negative, backtrack immediately since no further numbers can fix it.

### Dry-run example

Suppose `candidateNumbers = [2, 3]` and `targetSum = 5`.

- Start with empty combination, targetSum=5.
- Include 2:
  - Combination: [2], targetSum=3.
  - Include 3:
    - Combination: [2, 3], targetSum=0 → save [2, 3].
  - Exclude 3:
    - Combination: [2], targetSum=3 → no more numbers, backtrack.
- Exclude 2:
  - Combination: [], targetSum=5.
  - Include 3:
    - Combination: [3], targetSum=2 → no more numbers, backtrack.
  - Exclude 3:
    - Combination: [], targetSum=5 → no more numbers.

The only valid combination found is `[2, 3]`.

### Downsides

- This method tries all subsets, which can be very large (exponential time).
- It does not handle duplicates well, so it might return repeated combinations.

## 3. Approach 2 — Better Approach

### Optimization idea

To avoid duplicate combinations, first **sort** the `candidateNumbers`. Sorting groups identical numbers together, making it easier to skip duplicates.

When iterating through the sorted array:

- If the current number is the same as the previous number and the previous number was not chosen in this recursion level, skip it.
- This ensures that you don't generate the same combination multiple times.

### Why this helps

By sorting and skipping duplicates, you prevent exploring branches that would lead to the same combination. This reduces unnecessary work and avoids duplicate results.

### Complexity

- Sorting takes O(n log n), where n is the number of `candidateNumbers`.
- Backtracking still explores many subsets, but skipping duplicates prunes the search space.
- Overall complexity is better than brute force but still exponential in the worst case.

## 4. Approach 3 — Most Efficient Solution

### How it works

This approach builds on the previous one with a refined backtracking method that:

1. Sorts the `candidateNumbers`.
2. Uses a recursive function to build combinations.
3. At each recursion, iterates over the remaining numbers starting from a given index.
4. Skips any number that is the same as the previous number at the same recursion level to avoid duplicates.
5. Includes the current number if it does not exceed the remaining `targetSum`.
6. Recurses with the updated `targetSum` and next index.
7. When `targetSum` reaches zero, adds the current combination to the results.

### Why it works

- Sorting ensures duplicates are adjacent.
- Skipping duplicates at the same recursion depth prevents repeated combinations.
- Using the index to move forward ensures each number is used at most once per combination.
- Backtracking explores only valid paths, pruning early when the sum exceeds `targetSum`.

### When it might fail or constraints

- Works best when `candidateNumbers` are non-negative. Negative numbers could complicate pruning since sums might decrease unpredictably.
- The solution may still be slow for very large inputs due to exponential nature of combinations.
- Memory usage grows with the number of valid combinations found.

### Time and space complexity

- Time complexity: O(2^n) in the worst case, since each number can be chosen or not.
- Space complexity: O(n) for the recursion stack and temporary combination storage, plus space for storing results.

---

By following this efficient backtracking approach with sorting and duplicate skipping, you can find all unique combinations that add up to `targetSum` without redundant work.

</details>
