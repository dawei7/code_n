# Minimum Insertions to Make Parentheses Valid

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VALIDPAREN |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [VALIDPAREN](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/VALIDPAREN) |

---

## Problem Statement

Chef is given a string **$S$** consisting only of the characters **`(`** and **`)`**. Chef wants to make this parentheses string valid by performing the **minimum number of insertions**.

A parentheses string is considered **valid** if and only if one of the following conditions holds:

* It is an empty string, or
* It can be written as **$AB$**, where both **$A$** and **$B$** are valid parentheses strings, or
* It can be written as **$(A)$**, where **$A$** is a valid parentheses string.

In one move, Chef is allowed to **insert one parenthesis**, either **`(`** or **`)`**, at **any position** in the string.

Chef wants to know the **minimum number of insertions** required to make the given string valid.

Your task is to help Chef compute this minimum number for each test case.

---

### Function Declaration

* **Function Name:**

  * **$minAddToMakeValidNaive$**

* **Parameters:**

  * **$s$** (`string`)
    A string consisting only of the characters **`(`** and **`)`**.

* **Return Value:**

  * Returns an `int` representing the **minimum number of insertions** required to make the parentheses string valid.
---

## Input Format

The first line contains a single integer **$T$** — the number of test cases.

Each of the next **$T$** lines contains a string **$S$**, consisting only of the characters **`(`** and **`)`**.

---

## Output Format

For each test case, print a single integer — the **minimum number of insertions** required to make the parentheses string valid.

---

## Constraints

* $1 \le T \le 100$
* $1 \le |S| \le 1000$
* $S[i] \in { '(', ')' }$

---

## Input Format

The first line contains an integer **T**, the number of test cases.

Each of the next **T** lines contains a string **S**, consisting only of `'('` and `')'`.

---

## Output Format

For each test case, print a single integer —
the **minimum number of insertions** required to make the parentheses string valid.

---

## Constraints

- $1 \le T \le 100$
- $1 \le |S| \le 1000$
- $\texttt S[i] ∈ $ { '(', ')' }

---

## Examples

**Example 1**

**Input**

```text
4
())(
((((
)()())
(())
```

**Output**

```text
2
4
2
0
```

**Explanation**

**Test Case 1 :** Input String: `())(`

Chef scans the string from left to right:

* The first `'('` is matched correctly.
* The second `')'` is extra and needs one `'('` to match.
* The last `'('` is unmatched and needs one `')'`.

So, **2 insertions** are required to make the string valid.

**Test Case 2 :** Input String: `((((`

All characters are `'('` and none of them are closed.

Each `'('` requires a corresponding `')'` to form a valid pair.
So, **4 insertions** of `')'` are needed.

**Test Case 3 :** Input String: `)()())`

* The first `')'` has no matching `'('`, so one `'('` must be inserted.
* Later, there is one extra `')'` that remains unmatched.
In total, **2 insertions** are required to make the string valid.

**Test Case 4 :** All opening parentheses have matching closing parentheses, and the structure is already valid.

So, **no insertions** are required.

Hence, the output is **`0`**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
())(
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
((((
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
)()())
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
(())
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

You are given a string **S** consisting of only `'('` and `')'`.\
A parentheses string is **valid** if:

- It’s empty `""`, or
- It can be written as **AB**, where both **A** and **B** are valid, or
- It can be written as **(A)**, where **A** is valid.

Your task is to find the **minimum number of insertions** required to make the string valid.

You can insert '(' or ')' anywhere in the string.

 ---

 # Approach

 We can simulate **removing valid pairs** `'()'` until no more exist.\
The remaining unmatched parentheses count = number of insertions needed.

---

# Algorithm:

Loop through the string:

- Whenever `'()'` is found, remove it.

Repeat until no `'()'` pairs remain.

The leftover length = **number of insertions required **.

---

# Time Complexity:

Worst case: O(N²) because each removal shifts characters.

Works fine for small strings.

</details>
