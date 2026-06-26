# String to Integer (atoi)

| | |
|---|---|
| **ID** | `string_12` |
| **Category** | strings |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) |

## Problem statement

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).
The algorithm must follow these strict rules:
1. **Whitespace:** Ignore any leading whitespace (`" "`).
2. **Sign:** Determine the sign by checking if the next character is `'-'` or `'+'`. Assume `+` if neither is present.
3. **Conversion:** Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored. Convert these digits into an integer.
4. **Rounding:** If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then clamp the integer so that it remains in the range.

**Input:** A string `s`.
**Output:** A 32-bit clamped integer.

## When to use it

- To safely parse user input (which is always a String) into a mathematical number, handling all edge cases gracefully without throwing an exception.
- One of the most infamous interview questions to test your attention to detail and edge-case handling.

## Approach

**1. The Four-Step Deterministic Parsing:**
This problem doesn't require a clever algorithm; it requires a perfectly disciplined State Machine execution.
- **Step 1: Trim.** Strip leading whitespaces.
- **Step 2: Sign.** Check index 0 for `+` or `-`. If found, record the sign and move the pointer forward.
- **Step 3: Digits.** Iterate through the string. While the character is a digit (`'0'`-`'9'`), multiply our running total by 10 and add the new digit. If we hit a non-digit (like a letter or a space), STOP instantly.
- **Step 4: Overflow.** If the running total exceeds the maximum 32-bit integer, clamp it and return immediately.

**2. The Mathematical Digit Conversion:**
How do we turn the character `'7'` into the integer `7` without using a built-in `int()` function?
Characters are just ASCII integers under the hood!
`'0'` is ASCII 48. `'7'` is ASCII 55.
Therefore, the integer value is simply `ASCII('7') - ASCII('0') = 55 - 48 = 7`!

**3. Handling Overflow in Strictly Typed Languages:**
In Python, integers have arbitrary precision, so you can just let the number grow huge and clamp it at the end.
In C++ or Java, `total * 10 + digit` will physically crash the memory space (Overflow Exception) BEFORE you have a chance to clamp it!
To fix this, before we multiply by 10, we check: `if total > MAX_INT / 10`. If it is, the multiplication is guaranteed to overflow! Clamp and return immediately!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_12: String to Integer (atoi).

Parse a string as a 32-bit signed integer. Skip leading
whitespace, handle an optional +/- sign, read digits
until a non-digit. Clamp to the int32 range.
"""


def solve(s, n):
    if n == 0:
        return 0
    i = 0
    while i < n and s[i] == " ":
        i += 1
    if i == n:
        return 0
    sign = 1
    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        sign = -1
        i += 1
    result = 0
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    while i < n and s[i].isdigit():
        digit = int(s[i])
        new_result = result * 10 + digit
        if sign == 1 and new_result > INT_MAX:
            return INT_MAX
        if sign == -1 and -new_result < INT_MIN:
            return INT_MIN
        result = new_result
        i += 1
    return sign * result
```

</details>

## Walk-through

`s = "   -42"`
1. **Trim:** `i` advances past three spaces to index `3`.
2. **Sign:** `s[3] == '-'`. `sign = -1`. `i` advances to `4`.
3. **Digits:**
   - `i = 4`: `s[4] = '4'`. `digit = 4`. `result = 0 * 10 + 4 = 4`.
   - `i = 5`: `s[5] = '2'`. `digit = 2`. `result = 4 * 10 + 2 = 42`.
4. End of string. Return `sign * result = -42`. ✓

`s = "4193 with words"`
1. **Trim:** No leading spaces. `i = 0`.
2. **Sign:** No sign. `sign = 1`.
3. **Digits:**
   - `i = 0`: `'4'`. `result = 4`.
   - `i = 1`: `'1'`. `result = 41`.
   - `i = 2`: `'9'`. `result = 419`.
   - `i = 3`: `'3'`. `result = 4193`.
   - `i = 4`: `' '`. `s[i].isdigit()` is False! Loop instantly breaks.
4. Return `4193`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

We iterate through the string exactly once from left to right.
Time complexity is strictly $O(N)$ where N is the length of the string.
Space complexity is strictly $O(1)$ constant time as we only store a few integer variables (`i`, `sign`, `result`).

## Variants & optimizations

- **Valid Number / IsNumeric (`string_04`?):** A much harder variation where you must strictly validate if a string mathematically represents ANY valid number (including decimals, scientific `e` notation, and leading zeroes) using a complex Deterministic Finite Automaton (DFA) state machine.

## Real-world applications

- **Standard Libraries:** This is literally the exact implementation of C's `<stdlib.h>` `atoi()` function, which is the foundational bedrock for parsing human-inputted configurations, JSON numbers, and HTTP headers across the entire internet.

## Related algorithms in cOde(n)

- **[string_12 - String to Integer (atoi)](#)** — Wait, this is it!
- **[math_05 - Reverse Integer](../math/math_05_reverse-integer.md)** — The sister problem that requires the exact same `result > MAX_INT // 10` overflow check logic, but applying modulo `% 10` to strip digits instead of adding them!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
