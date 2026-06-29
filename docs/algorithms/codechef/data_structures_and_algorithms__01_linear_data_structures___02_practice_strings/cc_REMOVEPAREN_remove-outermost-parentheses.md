# Remove Outermost Parentheses

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REMOVEPAREN |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [REMOVEPAREN](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/REMOVEPAREN) |

---

## Problem Statement

You are given a valid parentheses string $s$.\
A valid parentheses string is composed of `'('` and `')'` that are properly balanced.

A valid parentheses string is called **primitive** if it cannot be split into two smaller valid parentheses strings.

Your task is to **remove the outermost parentheses** from every primitive part of $s$ and print the final result.

## Function Declaration

### Function Name

$removeOuterParentheses$ – This function removes the outermost parentheses from every primitive substring of a valid parentheses string.

### Parameters

* $s$: A valid parentheses string consisting only of the characters `‘(’` and `‘)’`.
  The string may contain multiple primitive valid parentheses substrings concatenated together.

### Return Value

* Returns a new string formed by removing the outermost parentheses from every primitive part of the input string.
* The returned string preserves the internal structure of the parentheses inside each primitive substring.

## Constraints

- $1 \le T \le 100$
- $1 \le |s| \le 10^{5}$
- $ {s} \text{ contains only the characters `(' and `)'.}$
- $ {s} \text{ is guaranteed to be a valid parentheses string.}$

---

## Input Format

The first line contains an integer $T$, the number of test cases.

Each test case consists of a single line containing the string $s$.

---

## Output Format

For each test case, print the modified string after removing the outermost parentheses.

---

## Examples

**Example 1**

**Input**

```text
4
((()))
(()(()))
()()
((())())(()(()))
```

**Output**

```text
(())
()(())
 
(())()()(())
```

**Explanation**

**Test Case 1**:\
`s = ((()))`\
Primitive decomposition = `"((()))"`\
After removing the outermost parentheses -> `(())`

**Test Case 2:**\
`s = (()(()))`
Primitive decomposition = `"(()(()))"`
After removing the outermost -> `()(())`

**Test Case 3:**\
`s = ()()`\
Primitive decomposition = `"()" + "()"`\
After removing the outermost from each -> `"" + "" = ""`

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given a valid parentheses string `s`.\
A valid parentheses string is composed only of `'('` and `')'`, arranged so that they are **properly balanced**.

A primitive parentheses string is one that **cannot be divided** into two non-empty valid parentheses strings.

Your task is to **remove the outermost parentheses** from every primitive substring in `s` and print the resulting string.

---

## Key Observations

Every time the parentheses are **balanced back to zero depth**, it indicates the end of a primitive substring.

The **outermost parentheses** are the first `'('` when depth goes from `0 → 1` and the last `')'` when depth goes from `1 → 0`.

We must **skip adding** these outermost parentheses to the result.

---

## Approach

We use a **depth counter** to track how deeply nested we are.

- Initialize an empty string or list `result` and set `depth = 0`.

- Iterate over each character `ch` in `s`:

   - If ch == '(':

      - If depth > 0, add '(' to result (not outermost).

      - Increase `depth`.

   - Else (`ch == ')'`):

      - Decrease `depth`.

      - If `depth > 0`, add `')'` to result (not outermost).

After the loop, `result` contains the string with all outermost parentheses removed.

---

## Complexity Analysis

**Time Complexity**: O(n) – one pass through the string.\
**Space Complexity**: O(n) – for storing the result string.

</details>
