# String to Integer Conversion

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECURIMPLEM |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECURIMPLEM](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECURIMPLEM) |

---

## Problem Statement

You are given a string $s$, and your task is to convert it into a 32-bit signed integer (similar to the `atoi` function).

Implement the function according to the following rules:

**Ignore leading whitespaces** (spaces `' '`).

**Check for sign**:
- If the next character is `'-'`, the result should be negative.
- If the next character is `'+'`, the result should be positive.
- Otherwise, assume the number is positive.

**Read digits** until a non-digit character is found or the end of the string is reached.
- Ignore any **leading zeros**.
- If no digits are read, return 0.

**Clamp to 32-bit signed integer range**:
- If the number is less than **-2³¹**, return `-2147483648`.
- If the number is **greater than 2³¹ - 1**, return `2147483647`.

## Function Declaration

### Function Name
$myAtoi$ – This function converts a given string into a 32-bit signed integer.

### Parameters

* $s$ : A string that may contain leading whitespaces, optional sign (`+` or `-`), digits, and other non-digit characters.

### Return Value

* Returns the converted integer after applying all the above rules.

## Constraints

- $1 \leq T \leq 10^4$
- $0 \leq |s| \leq 200$
- $s$ consists of:
  - English letters (`a–z`, `A–Z`)
  - Digits (`0–9`)
  - Spaces `' '`
  - Symbols `'+'`, `'-'`, `'.'`

---

## Input Format

- The first line contains an integer $T$ — the number of test cases.
- Each of the next $T$ lines contains a string $s$.

---

## Output Format

- For each test case, print the converted integer on a new line.

---

## Constraints

0 <= |S| <= 200\
S consists of English letters (`a–z`, `A–Z`), digits (`0–9`), spaces, `'+'`, `'-'`, and `'.'`.

---

## Examples

**Example 1**

**Input**

```text
5
42
   -042
1337c0d3
0-1
words and 987
```

**Output**

```text
42
-42
1337
0
0
```

**Explanation**

**Test 1**:\
Input `"42"` has no spaces or signs, so it directly converts to `42`.

**Test 2**:\
Input `" -042"` ignores spaces, detects `-` sign, then converts digits to `42`, resulting in `-42`.

**Test 3**:\
Input `"1337c0d3"` reads `1337` until the first non-digit, so output is `1337`.

**Test 4**:\
Input `"0-1"` reads only `0` before `'-'`, so output is `0`.

**Test 5**:\
Input `"words and 987"` starts with non-digit, so result is `0`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
42
```

**Output for this case**

```text
42
```



#### Test case 2

**Input for this case**

```text
-042
```

**Output for this case**

```text
-42
```



#### Test case 3

**Input for this case**

```text
1337c0d3
```

**Output for this case**

```text
1337
```



#### Test case 4

**Input for this case**

```text
0-1
```

**Output for this case**

```text
0
```



#### Test case 5

**Input for this case**

```text
words and 987
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Summary

Given a string `S`, convert it to a **32-bit signed integer** following rules similar to `atoi`:

1. Ignore leading spaces.
2. Handle an optional sign (`+` or `-`).
3. Read consecutive digits.
4. Stop at the first non-digit.
5. Ignore leading zeros.
6. If no digits are read, return `0`.
7. Clamp the result to the range
   `[-2^31, 2^31 - 1]`.

---

## Key Observations

* The input may contain letters, symbols, and spaces.
* Parsing must stop immediately when a non-digit is encountered.
* Overflow must be handled explicitly.
* The maximum input size is small (≤ 200), but the digit count may still exceed 32-bit limits.

---

## Approach 1: Brute Force with Conversion

### Idea

1. Trim leading spaces.
2. Extract sign.
3. Extract a numeric substring.
4. Convert it to an integer.
5. Clamp the result.

### Issues

* Direct conversion can overflow.
* Unsafe in languages without arbitrary-precision integers.
* Not suitable for interview or competitive environments.

### Verdict

Not recommended.

---

## Approach 2: Iterative Digit Parsing (Recommended)

### Idea

Simulate manual number construction digit by digit.

Steps:

1. Skip leading spaces.
2. Detect sign.
3. Initialize result = 0.
4. For each digit:

   * Check if adding this digit would overflow.
   * Update result = result × 10 + digit.
5. Apply sign and clamp.

### Overflow Handling

Before multiplying by 10:

```
if result > INT_MAX / 10
or (result == INT_MAX / 10 and digit > 7)
```

Overflow is guaranteed.

### Advantages

* Efficient and safe.
* Industry-standard solution.
* No recursion overhead.

### Complexity

* Time: O(n)
* Space: O(1)

---

## Approach 3: Recursive Digit Parsing

### Idea

Use recursion to parse digits one by one.

Steps:

1. Handle spaces and sign iteratively.
2. Use a recursive function to:

   * Stop at end or non-digit.
   * Check overflow before multiplication.
   * Accumulate the number.
3. Return the signed result.

### Advantages

* Clean separation of concerns.
* Easy to reason about digit parsing.

### Drawbacks

* Extra stack space.
* Less preferred in strict performance environments.

### Complexity

* Time: O(n)
* Space: O(n) due to recursion stack.

---

## Approach 4: Finite State Machine (FSM)

### Idea

Model parsing as a state machine.

States:

* Start
* Signed
* Number
* End

Transitions depend on:

* Space
* Sign
* Digit
* Other characters

### Advantages

* Very robust.
* Excellent for complex parsing rules.
* Clear formal structure.

### Drawbacks

* Overkill for this problem.
* More code.

### Complexity

* Time: O(n)
* Space: O(1)

---

## Common Edge Cases

| Input             | Expected Output |
| ----------------- | --------------- |
| `"   "`           | `0`             |
| `"+"`             | `0`             |
| `"-"`             | `0`             |
| `"0-1"`           | `0`             |
| `"words and 987"` | `0`             |
| `"1337c0d3"`      | `1337`          |
| `"2147483648"`    | `2147483647`    |
| `"-91283472332"`  | `-2147483648`   |

---

## Important Pitfalls

1. **Overflow after multiplication**
   Overflow must be detected *before* multiplying by 10.

2. **Stopping at first non-digit**
   Characters after digits must be ignored.

3. **Handling empty or space-only strings**

4. **Negative zero (language-specific)**
   Some environments may represent `-0`. Normalize to `0`.

</details>
