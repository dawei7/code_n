# Generate Binary Strings Without Consecutive 1s

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GENBIN1 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [GENBIN1](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/GENBIN1) |

---

## Problem Statement

You are given an integer $n$, and your task is to generate all binary strings of length $n$ that **do not contain consecutive `1`s**.

The strings must be printed in **lexicographically increasing order** (sorted order).

A binary string is a string that contains only the characters `'0'` and `'1'`.

## Function Declaration

### Function Name

$generate$ – This function generates all binary strings of length **`n`** that do not contain consecutive `1`s using **recursion**, and prints them in lexicographically increasing order.

### Parameters

* $n$ : A number representing the required length of the binary strings.

### Return Value

* The function **does not return anything**.
* It prints all valid binary strings of length $n$, each on a new line.

## Constraints

* $1 \le n \le 20$
* The string contains only characters $0$ and $1$
* No binary string may contain $11$ as a substring

---

## Input Format

* The first line contains a single integer $n$ — the length of the binary string.

---

## Output Format

* Print all valid binary strings of length $n$ that do **not contain consecutive $1$s**.
* Each string must be printed on a **new line**.
* Strings must appear in **lexicographically increasing order**.

---

## Constraints

1 ≤ n ≤ 20

---

## Examples

**Example 1**

**Input**

```text
4
```

**Output**

```text
0000
0001
0010
0100
0101
1000
1001
1010
```

**Example 2**

**Input**

```text
3
```

**Output**

```text
000
001
010
100
101
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Summary

You are given an integer **n**.
Your task is to generate **all binary strings of length n** such that:

* Each string contains only `'0'` and `'1'`
* No string contains `"11"` as a substring (no consecutive `1`s)
* The output must be in **lexicographically increasing order**

---

## Key Observation

A binary string is valid if and only if **every `1` is either the first character or is preceded by `0`**.

This means:

* `'0'` can always be placed
* `'1'` can be placed **only if the previous character is not `1`**

---

## Approach 1: Recursive Backtracking (Most Common & Recommended)

### Idea

Build the binary string **character by character** using recursion:

* At each step:

  * Always try adding `'0'`
  * Try adding `'1'` **only if the previous character is `'0'` or the string is empty**
* When the string reaches length `n`, print it

### Why It Works

* Recursion explores all valid combinations
* Invalid strings with `"11"` are never generated
* Trying `'0'` before `'1'` ensures lexicographical order

### Time Complexity

* Number of valid strings follows Fibonacci sequence
* Time Complexity: **O(F(n))**, where `F(n)` is the nth Fibonacci number
* Upper bound is less than `2^n`

### Space Complexity

* **O(n)** for recursion stack and current string

---

## Approach 2: Dynamic Programming (Count Only)

### Idea

Instead of generating strings, count them:

Let:

* `dp[i][0]` = number of valid strings of length `i` ending with `0`
* `dp[i][1]` = number of valid strings of length `i` ending with `1`

Recurrence:

* `dp[i][0] = dp[i-1][0] + dp[i-1][1]`
* `dp[i][1] = dp[i-1][0]`

Total strings = `dp[n][0] + dp[n][1]`

### Use Case

* Useful when **only the count is required**
* Not suitable when actual strings must be printed

### Time Complexity

* **O(n)**

### Space Complexity

* **O(n)** (can be optimized to O(1))

---

## Approach 3: Iterative Construction (BFS / Queue)

### Idea

Start with valid base strings and expand them iteratively:

* Start with `"0"` and `"1"`
* For each string:

  * Always append `'0'`
  * Append `'1'` only if last character is `'0'`
* Stop when strings reach length `n`

### Characteristics

* Avoids recursion
* Uses a queue or list to store intermediate strings

### Time Complexity

* Same as recursive approach: **O(F(n))**

### Space Complexity

* Higher than recursion due to storing all partial strings

---

## Approach 4: Bitmasking with Validation (Brute Force)

### Idea

* Iterate from `0` to `2^n - 1`
* Convert each number to a binary string of length `n`
* Check if the string contains `"11"`

### Drawbacks

* Inefficient for larger `n`
* Generates many invalid strings

### Time Complexity

* **O(n × 2^n)**

### Space Complexity

* **O(n)**

---

## Lexicographical Order Guarantee

To ensure sorted output:

* Always generate or expand `'0'` before `'1'`
* This applies naturally in recursive and BFS approaches

---

## Edge Cases

* `n = 1` → Output: `0`, `1`
* `n = 2` → Output: `00`, `01`, `10`
* `n = 20` → Maximum allowed size, recursion still safe

---

## Final Recommendation

* **Use Recursive Backtracking** when strings must be printed
* **Use Dynamic Programming** when only the count is needed
* Avoid brute force except for learning or very small `n`

</details>
