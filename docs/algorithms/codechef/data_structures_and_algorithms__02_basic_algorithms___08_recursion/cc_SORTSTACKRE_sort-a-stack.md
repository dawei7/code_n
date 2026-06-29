# Sort a Stack

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SORTSTACKRE |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [SORTSTACKRE](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/SORTSTACKRE) |

---

## Problem Statement

You are given a stack of integers.\
Your task is to sort the stack in **descending order** using **recursion**, such that the **top of the stack contains the greatest element**.

You are **not allowed to use any loop-based sorting algorithms** (like bubble sort, merge sort, quicksort, etc.).\
You may only use recursion and standard stack operations:\
`push`, `pop`, `top/peek`, and `isEmpty`.

## Function Declaration

### Function Name

$sortStack$ – This function sorts a stack of integers in **descending order** using **recursion only**, such that the **top of the stack contains the greatest element**.

### Parameters

* $st$ : A reference to a stack of integers that needs to be sorted.

### Return Value

* The function does **not return anything**.
* It modifies the given stack in-place so that it becomes sorted in **descending order**.

## Constraints

* $1 \leq T \leq 10$
* $1 \leq N \leq 100$
* $-10^4 \leq \text{elements of stack} \leq 10^4$

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* For each test case:

  * The first line contains a single integer $N$, the number of elements in the stack.
  * The second line contains **N space-separated integers**, representing the stack elements **from top to bottom**.

---

## Output Format

* For each test case, print the stack elements **from top to bottom** after sorting the stack in **descending order**.

---

## Constraints

1 ≤ T ≤ 10\
1 ≤ N ≤ 100\
-10⁴ ≤ stack[i] ≤ 10⁴

---

## Examples

**Example 1**

**Input**

```text
2
4
4 1 3 2
5
10 20 -5 7 15
```

**Output**

```text
4 3 2 1
20 15 10 7 -5
```

**Explanation**

**Test Case 1**:\
Original Stack: [4, 1, 3, 2]\
Sorted (Descending): [4, 3, 2, 1]

**Test Case 2**:\
Original Stack: [10, 20, -5, 7, 15]\
Sorted (Descending): [20, 15, 10, 7, -5]

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
4 1 3 2
```

**Output for this case**

```text
4 3 2 1
```



#### Test case 2

**Input for this case**

```text
5
10 20 -5 7 15
```

**Output for this case**

```text
20 15 10 7 -5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Restatement

Sorting a stack without loops is a little like teaching a tower of stones to arrange itself one pebble at a time.
The only moves allowed:

- `push`
- `pop`
- `peek / top`
- `isEmpty`

And the constraint:\
**top of the stack must hold the greatest element**.

The goal is to use **recursion itself as the workspace**.

---

# Core Idea

To sort a stack using recursion:

**Step 1 (sortStack)**:

Take the top out → sort what remains → insert the top back in its correct (descending) place.

**Step 2 (sortedInsert)**:

Insert a value into an already sorted (descending) stack so that the descending order is preserved.

These two functions together create a self-correcting system.

---

# Example Walkthrough

**Input stack (top → bottom):**

4 1 3 2

**Step-by-step**:

- Pop `4`, sort `[1,3,2]`
- Pop `1`, sort `[3,2]`
- Pop `3`, sort `[2]`
- Pop `2`, hit empty → start inserting back

Now inserting in descending order:

- Insert 2 → stack: `[2]`
- Insert 3 → stack: `[3, 2]`
- Insert 1 → stack: `[3, 2, 1]`
- Insert 4 → stack: `[4, 3, 2, 1]`

**Result:**

4 3 2 1

---

# Time & Space Complexity

**Time**:

O(N²)
Because each insertion into the stack may traverse N items, and we do this N times.

**Space**:

O(N) recursion depth.

</details>
