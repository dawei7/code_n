# Generate All Well-Formed Parentheses

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GENPAREN |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [GENPAREN](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/GENPAREN) |

---

## Problem Statement

You are given an integer **n**, representing the number of pairs of parentheses.
Your task is to **generate all possible combinations** of well-formed (balanced) parentheses using exactly **n pairs**.

A parentheses string is considered **well-formed** if:
- Every opening bracket `'('` has a corresponding closing bracket `')'`.
- The brackets are correctly nested.

Return all valid combinations **in lexicographical order**.

### Lexicographical order:
Lexicographical order is the **dictionary order** of strings.

* Characters are compared **left to right**
* `'('` comes **before** `')'` in ASCII

  ```
  '(' = ASCII 40
  ')' = ASCII 41
  ```
* So **any string with '(' at an earlier position is smaller**

## Function Declaration

### Function Name
$generate$ – This function generates all possible combinations of well-formed (balanced) parentheses using exactly $n$ pairs and returns them in lexicographical order.

### Parameters

* $n$ : A number representing the number of pairs of parentheses.

### Return Value

* Returns a collection (array) of strings.
* Each string represents a valid well-formed parentheses combination using exactly $n$ pairs.
* The returned collection is sorted in **lexicographical order**.

## Constraints

- $1 \leq n \leq 8$
- Only characters '(' and ')' are allowed
- All valid combinations must be generated exactly once

---

## Input Format

* The first line contains a single integer $n$ — the number of pairs of parentheses.

---

## Output Format

* Print all valid parentheses combinations.
* Each combination should be printed on a new line.
* Output must be in **lexicographical order**.

---

## Constraints

1 ≤ n ≤ 8

---

## Examples

**Example 1**

**Input**

```text
2
```

**Output**

```text
(())
()()
```

**Example 2**

**Input**

```text
3
```

**Output**

```text
((()))
(()())
(())()
()(())
()()()
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Restatement

You are given an integer n, representing the number of pairs of parentheses.

Your task is to **generate all possible well-formed** (balanced) parentheses strings using exactly **n pairs**, and print them in **lexicographical order**.

A string is considered well-formed when:

Every `(` has a matching `)`

Parentheses are correctly nested (no early closing)

Example

For `n = 3`, valid combinations include:

((()))\
(()())\
(())()\
()(())\
()()()

---

# Approach

Generating balanced parentheses is like building a fragile little tower — each `(` invites a matching `)` later, and the pattern must always stay structurally sound.

To construct all such strings, we use recursion, guided by two counts:
- `open` → how many `(` we’ve placed so far
- `close` → how many `)` we’ve placed so far

And one strict rule:

**You can never close more than you’ve opened**.

---

# Core Idea

We build the string **character by character**, deciding at each step whether to add:

- An opening bracket `(`\
Allowed when `open < n`

- **A closing bracket** `)`\
Allowed when close < open

This ensures:
- We never exceed `n` opening brackets
- We never close prematurely
- All final strings are balanced

Once `close == n`, the string is complete and printed.

---

# Why This Order Produces Lexicographical Output

Because the recursion always tries:

Add `(` (lexicographically smaller)

Add `)` (later in dictionary order)

…every generated string naturally appears in sorted order, no post-sorting needed.

It’s like always exploring the left corridor of a maze before the right one.

---

# Step-By-Step Explanation

1.**Begin with an empty string**

`curr = ""`, `open = 0`, `close = 0`

2. **Branch 1 — Add** `(`

If `open < n`, we place another `(` and continue.

This grows the string deeper, parenthesis roots reaching upward like vines.

3. **Branch 2 — Add** `)`

We add `)` only if `close < open`.\
This ensures balance: you never close more than you opened.

4. **Base Condition**

If `close == n`, all pairs are closed → print the string.

---

# Time Complexity

**O(Cₙ)**

Where `Cₙ` is the n-th Catalan number:

`Cₙ = (1 / (n+1)) * (2n choose n)`

This represents the exact number of balanced bracket sequences.

Growth is exponential but optimal — you only generate valid strings.

# Space Complexity

**O(n) (recursion depth)**

---

# Why This Recursion Works Beautifully

No backtracking arrays

No stack structures

No validation after building
(invalid sequences are never created)

It grows only legal sequences — the recursion tree prunes itself whenever an imbalance might occur.

---

# Summary

To generate well-formed parentheses:

Use recursion with two counters: `open`, `close`.

Add `(` when `open < n`.

Add `)` when `close < open`.

When both reach `n`, print the string.

Recursive left-branch-first ordering yields lexicographically sorted output automatically.

</details>
