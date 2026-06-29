# Color Sorting Challenge

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SORTARRAYS |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [SORTARRAYS](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/SORTARRAYS) |

---

## Problem Statement

Chef has an array $nums$ of `N` balls, where each ball is painted **red**, **white**, or **blue**. The balls are represented by integers:
- `0` → Red
- `1` → White
- `2` → Blue\
Chef wants to arrange the balls so that balls of the same color are together in the order:\
**Red**, **White**, then **Blue**.

Help Chef sort the array **in-place**, without using any built-in sorting functions.

## **Function Declaration**

### **Function Name**

$sortColors$ – This function rearranges an array of balls painted Red $0$, White $1$, or Blue $2$ so that all balls of the same colour are grouped together in the order **Red → White → Blue**.

### **Parameters**

* $N$ : The number of balls in the array.
* $nums$ : A reference to an array of $N$ integers, where each integer represents the color of a ball.

### **Return Value**

* The function does **not** return anything.
* It modifies the array **in-place**, rearranging the balls so that:

  * All $0$s appear first
  * Followed by all $1$s
  * Followed by all $2$s

## **Constraints**

* $1 \leq T \leq 10$
* $1 \leq N \leq 300$
* $nums[i] \in {0, 1, 2}$

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* For each test case:

  * The first line contains an integer $N$ — the number of balls.
  * The next line contains $N$ space-separated integers representing the ball colors.

---

## Output Format

* For each test case, print the sorted array on a new line, where all $0$s come first, followed by all $1$s, then all $2$s.

---

## Constraints

* $ 1 \leq N \leq 300 $
* $\text{nums}[i] \in \{0, 1, 2\} $

---

## Examples

**Example 1**

**Input**

```text
7
0 2 1 2 0 1 0
```

**Output**

```text
0 0 0 1 1 2 2
```

**Explanation**

All red (0) balls come first, followed by white (1), then blue (2).

**Example 2**

**Input**

```text
5
1 1 2 0 2
```

**Output**

```text
0 1 1 2 2
```

**Explanation**

Array is rearranged so that `0`’s come first, followed by 1’s, then 2’s.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

Chef has an array of **N balls**, where each ball is painted **red**, **white**, or **blue**.\
The balls are represented by integers:
`0 → Red`\
`1 → White`\
`2 → Blue`

Chef wants to arrange the balls so that balls of the same color are together in the order:\
**Red (0)**, **White (1)**, then **Blue (2)**.

Your task is to help Chef **sort the array in-place**, without using any built-in sorting functions.

---

## Key Observations

- This is a classic **Dutch National Flag Problem**.
-We need to partition the array into three groups: `0s`, `1s`, and `2s`.
- Instead of counting and reconstructing, we can do it in a **single traversal** by maintaining three pointers.

---

## Approach
- Maintain three pointers:
   - `low` → the boundary where the next `0` should go.
   - `mid` → the current element under consideration.
   - `high` → the boundary where the next `2` should go.

- Traverse the array:
   - If `nums[mid] == 0`: swap it with `nums[low]``, then move both `low` and `mid` forward.
   - If `nums[mid] == 1`: leave it in place, move `mid` forward.
   - If `nums[mid] == 2`: swap it with `nums[high]`, move `high` backward (but do not increment `mid`).

Continue until `mid > high`.

---

## Complexity Analysis
**Time Complexity**:
- We make a single pass through the array.
- Each element is swapped at most once.
- Therefore, time complexity = `O(N)`.

**Space Complexity**:
- We sort in-place using only three extra pointers (`low`, `mid`, `high`).
- Therefore, space complexity = **O(1)**.

</details>
