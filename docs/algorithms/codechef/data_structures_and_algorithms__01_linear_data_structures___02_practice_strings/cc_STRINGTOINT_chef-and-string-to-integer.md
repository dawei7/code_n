# Chef and String to Integer

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRINGTOINT |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [STRINGTOINT](https://www.codechef.com/practice/course/strings/STRINGS/problems/STRINGTOINT) |

---

## Problem Statement

Chef has found a strange string that may contain spaces, signs, numbers, and letters.
He wants to **convert this string into an integer** by following a few simple rules.

You need to help Chef by writing a program that performs this conversion carefully.

**Conversion Rules**
- **Ignore spaces**:
   - Skip all leading spaces before any character.

- **Check the sign**:
   - If the next character is `'-'`, the number is negative.
   - If the next character is `'+'`, the number is positive.
   - If no sign is given, assume it is positive.

- **Read digits only**:
   - Read all consecutive digits and stop when a non-digit character is found.
   - If no digits are found, the result is **0**.

- **Clamp within range**:
   - If the number is smaller than **-2147483648**, return **-2147483648**.
   - If the number is larger than **2147483647**, return **2147483647**.
---
## Function Declaration

### Function Name

$myAtoi$ – This function converts a given string into a 32-bit signed integer by following specific conversion rules similar to the standard `atoi` function.

### Parameters

* $s$ : A string that may contain leading spaces, optional sign characters (`+` or `-`), digits, and other non-digit characters.

### Return Value

* Returns an integer obtained after converting the string according to the given rules.
* If no valid number can be formed, the function returns `0`.
* If the converted number is smaller than `-2147483648`, it returns `-2147483648`.
* If the converted number is larger than `2147483647`, it returns `2147483647`.
---

---

## Input Format

- The first line contains an integer $T$ — the number of test cases.
- Each of the next $T$ lines contains one string $S$.
---

---

## Output Format

- For each test case, print the converted integer on a new line.
---

---

## Constraints

- $1 \le T \le 100$
- $0 \le |S| \le 200$
- $\texttt{S may contain letters, digits, spaces, '+' , '-' , and '.'}$

---

## Examples

**Example 1**

**Input**

```text
5
   98hello
-00456
+45abc23
word123
  -91283472332
```

**Output**

```text
98
-456
45
0
-2147483648
```

**Explanation**

**Test case 1**:\
`" 98hello"` -> ignore spaces -> read digits `98` -> result = **98**

**Test case 2**:\
`"-00456"` -> negative sign -> read digits `456` -> result = **-456**

**Test case 3**:\
`"+45abc23"` -> sign `+` -> read digits `45` -> result = **45**

**Test case 4**:\
`"word123"` -> starts with non-digit ? no number found -> result = **0**

**Test case 5**:\
`"-91283472332"` -> number is too small -> clamp to **-2147483648**

**Separated test cases**

#### Test case 1

**Input for this case**

```text
98hello
```

**Output for this case**

```text
98
```



#### Test case 2

**Input for this case**

```text
-00456
```

**Output for this case**

```text
-456
```



#### Test case 3

**Input for this case**

```text
+45abc23
```

**Output for this case**

```text
45
```



#### Test case 4

**Input for this case**

```text
word123
```

**Output for this case**

```text
0
```



#### Test case 5

**Input for this case**

```text
-91283472332
```

**Output for this case**

```text
-2147483648
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

Chef needs to convert a string into an integer — just like the behavior of the standard `atoi()` function — but with certain rules and safe handling of invalid input, signs, and overflow conditions.

The string can include:
- Leading spaces
- Optional `+` or `-` sign
- Digits (0–9)
- Random letters or symbols after the digits

You must:

- **Skip leading spaces**
- **Check for a sign** (`+` or `-`)
- **Read digits until a non-digit**
- **Stop reading at the first non-digit**
- **Clamp the result** to 32-bit signed integer range
   - Minimum: -2147483648 (`INT_MIN`)

Maximum: 2147483647 (`INT_MAX`)

---

# Intuition

We simulate manual parsing from left to right:

- Ignore spaces first.
- Detect sign.
- Convert subsequent digits to a number.
- Stop conversion on encountering a non-digit.
- Handle overflow before multiplying by 10 or adding the next digit.

This mimics how C’s `atoi()` works, but adds safety for overflow and underflow.

---

# Algorithm

**Skip leading spaces**\
Move the pointer forward while encountering spaces.

**Detect sign**
If the current character is `'-'`, set `sign = -1`.

If `'+'`, set `sign = 1`.

If neither, assume positive

**Initialize result = 0**

**Iterate through digits**
- For each digit `d`, check if adding it would overflow 32-bit integer bounds.
- If overflow is possible, return `INT_MAX` or `INT_MIN` based on the sign.

**Stop reading**

As soon as a non-digit character is found, break out of the loop.

Return `sign * result`

---

# Edge Cases

Input has **no digits** → output `0`

Input starts with **letters** → output `0`

Input exceeds integer range → clamp to min/max

Input contains **leading zeros** (e.g., `-00456`) → handled naturally

Empty string or only spaces → output `0`

---

# Complexity Analysis

**Time Complexity**: `O(N)` — scans each character once

**Space Complexity**: `O(1)` — only uses a few variables

Both are optimal since the problem requires parsing the full string.

---

# Key Insights

Overflow must be handled **before** multiplication and addition.

Use **long long (C/C++)** or **long (Java)** or Python’s native int to handle intermediate overflows.

Stopping early on the first invalid character avoids unnecessary processing.

The clamping ensures consistent 32-bit integer output.

</details>
