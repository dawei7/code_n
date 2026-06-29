# Chef and Roman Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFROMAN |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [CHEFROMAN](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/CHEFROMAN) |

---

## Problem Statement

Chef has found an ancient Roman numeral and wants to know its integer value.

Roman numerals use the following symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Normally, symbols are added from left to right.\
For example:\
**III = 3**, **VIII = 8**, **XII = 12**

However, if a smaller value comes before a larger one, it is subtracted:

- I before V (5) or X (10) → 4 or 9
- X before L (50) or C (100) → 40 or 90
- C before D (500) or M (1000) → 400 or 900

Your task is to help Chef convert the given Roman numeral string S into its integer value.

## Function Declaration

### Function Name

$romanToInt$ – This function converts a given Roman numeral string into its corresponding integer value.

### Parameters

* $s$ : A string representing a valid Roman numeral.
  The string contains only the characters `I`, `V`, `X`, `L`, `C`, `D`, and `M`.

### Return Value

* Returns an integer representing the decimal (base-10) value of the given Roman numeral string.

## Constraints
- $1 \le |S| \le 15$
- $S \text{ contains only the characters } I, V, X, L, C, D, \text{ and } M$.
- $\text{It is guaranteed that } S \text{ is valid and represents a number between } 1 \text{ and } 3999$.

---

## Input Format

* The input consists of a single line containing a string `S`, which represents a Roman numeral.

---

## Output Format

* Print a single integer — the decimal value of the Roman numeral.

---

## Examples

**Example 1**

**Input**

```text
XLII
```

**Output**

```text
42
```

**Example 2**

**Input**

```text
CMXLIV
```

**Output**

```text
944
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

We are given a string `S` representing a **valid Roman numeral**.
The task is to convert this Roman numeral into its **integer value**.

Roman numerals have specific rules:

- Symbols are usually added left to right: `III = 3`, `VIII = 8`, `XII = 12`.
- If a smaller value appears before a larger value, it is subtracted:
`IV = 4`, `IX = 9`, `XL = 40`, `CM = 900`.

We need to process the string according to these rules to compute the integer equivalent.

---

# Intuition

- Traverse the Roman numeral from left to right.

- For each character:

   - Get its integer value.

   - If the next character represents a larger value, subtract the current value from the result.

   - Otherwise, add the current value to the result.

- This approach works because Roman numerals are guaranteed to follow the subtraction rule in valid sequences.

---

# Algorithm

Initialize `result = 0`.

For each character `s[i]` in the string:

- Get `current = value(s[i])`.
- If `i + 1 < n` and `value(s[i+1]) > current`, then `result -= current`.
- Else, `result += current`.

Return `result` after processing all characters.

`value(c)` is a utility function that maps Roman symbols to integers (`I = 1`, `V = 5`, etc.).

---

# Complexity Analysis

**Time Complexity**: `O(N)`\
Each character is processed exactly once, and a constant-time lookup is used for each symbol.

**Space Complexity**: `O(1)`\
Only a few integer variables are used; no additional data structures are needed.

---

# Key Takeaways

The key insight is to **compare each character with the next one** to determine whether to add or subtract.

Using a **utility function** for symbol values keeps the code clean.

Since the input is guaranteed to be valid, there is no need for error checking.

</details>
