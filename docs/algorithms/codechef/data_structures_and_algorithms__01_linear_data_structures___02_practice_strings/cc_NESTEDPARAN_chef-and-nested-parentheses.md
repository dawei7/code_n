# Chef and Nested Parentheses

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NESTEDPARAN |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [NESTEDPARAN](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/NESTEDPARAN) |

---

## Problem Statement

Chef is playing with a string **$s$** that contains digits, arithmetic operators, and parentheses. He wants to find the **maximum nesting depth** of parentheses in the string.

The nesting depth is the maximum number of parentheses that are open at the same time. Chef wants you to help him calculate this value.

---

### Function Declaration

* **Function Name:**

  * **$maxNestingDepth$**

* **Parameters:**

  * **$s$** (`string`)
    A string that may contain digits, arithmetic operators **`+`**, **`-`**, **`*`**, **`/`**, and parentheses **`(`**, **`)`**.

* **Return Value:**

  * Returns an `int` representing the **maximum nesting depth** of parentheses in the string.

---
## Constraints

* $1 \le T \le 100$
* $1 \le |s| \le 100$
* **$s$** consists of digits **$0$–$9$**, arithmetic operators **`+`**, **`-`**, **`*`**, **`/`**, and parentheses **`(`**, **`)`**
* **$s$** is guaranteed to be a valid parentheses string (**VPS**)
---

---

## Input Format

- The first line contains an integer $T$ — the number of test cases.
- Each of the next $T$ lines contains a string $s$ — a valid parentheses string (VPS).
---

---

## Output Format

- For each test case, print a single integer — the maximum nesting depth of parentheses in the string.
---

---

## Constraints

- $1 \le T \le 100$
- $1 \le |s| \le 100$
- $\texttt{s} \text{ consists of digits } 0\text{--}9 \text{ and the characters } +,\ -,\ *,\ /,\ ),\ \text{and }\ ($.
- $\texttt{s} \text{ is guaranteed to be a valid parentheses string (VPS).}$

---

## Examples

**Example 1**

**Input**

```text
4
((1+2)+3)
(5+(6*7))
(1+(2*(3+4)))
()()()
```

**Output**

```text
2
2
3
1
```

**Explanation**

**Test case 1**: Maximum nesting depth is 2.\
**Test case 2**: Maximum nesting depth is 2.\
**Test case 3**: Maximum nesting depth is 3 (inside `2*(3+4)`).\
**Test case 4**: Maximum nesting depth is 1 (no nested parentheses).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
((1+2)+3)
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
(5+(6*7))
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
(1+(2*(3+4)))
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
()()()
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

We are given a string `s` containing digits, arithmetic operators, and parentheses.\
The goal is to compute the **maximum nesting depth** of parentheses in the string.

A **nesting depth** is defined as the maximum number of parentheses that are simultaneously open at any point in the string.\
The string is guaranteed to be a valid parentheses string (VPS).

---

# Intuition

- Every time we encounter `'('`, the current depth increases by 1.
- Every time we encounter `')'`, the current depth decreases by 1.
- The maximum value reached by the current depth during the traversal is the **maximum nesting depth**.

This approach ensures that we correctly count nested parentheses while ignoring digits and operators.

---

# Algorithm

Initialize `maxDepth = 0` and `currentDepth = 0`.

Traverse the string character by character:
- If the character is `'('`, increment `currentDepth`.
- If the character is `')'`, decrement `currentDepth`.
- Update `maxDepth` as the maximum of maxDepth and currentDepth.

After traversing the string, maxDepth is the maximum nesting depth.

---

# Complexity Analysis

**Time Complexity**: `O(N)` per test case, where `N` is the length of the string, since we process each character once.

**Space Complexity**: `O(1)`, only two integer variables are used.

---

# Key Takeaways

This problem can be solved using a **single pass** and a **simple counter**.

There is no need for stacks or recursion, as the input is guaranteed to be a valid parentheses string.

The approach efficiently tracks depth while ignoring irrelevant characters.

</details>
