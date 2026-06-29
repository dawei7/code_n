# Flatten String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR30 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR30](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR30) |

---

## Problem Statement

You are given a string that may contain nested parentheses, each with inner strings. The goal is to write a recursive function, **flatten_string**, that flattens the given string by removing all parentheses and concatenating the characters in the nested structure.

---

## Input Format

- The only line of input contains a single string which consists of lowercase english alphabets and parentheses.

---

## Output Format

- Output the flattened string.

---

## Constraints

- $1 \leq n \leq 200000$, where n = size of string
- String contains only lowercase latin letters and parentheses.

---

## Examples

**Example 1**

**Input**

```text
abc(def(ghi(jkl(mn))))op
```

**Output**

```text
abcdefghijklmnop
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Flatten String in Recursion](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR30)

### [](#problem-statement-1)Problem Statement:

You are given a string that may contain nested parentheses, each with inner strings. The goal is to write a recursive function, **flatten_string**, that flattens the given string by removing all parentheses and concatenating the characters in the nested structure.

### [](#approach-2)Approach:

**1. Character by Character Traversal**:

- We traverse the string one character at a time.

- For each character, we check whether it’s an opening parenthesis `(`, closing parenthesis `)`, or just a regular letter.

**2. Handling Parentheses**:

- **Opening Parenthesis `(`**:

- When we find `(`, it means we’re entering a nested section.

- We then **recursively** call our function to handle everything inside this new section, until we hit the closing parenthesis `)`.

- The result from the nested section is **appended** to our main result.

- **Closing Parenthesis `)`**:

- When we find `)`, it means we’re done with this section, so we **stop the current recursive call** and return the result we’ve collected so far.

**3. Regular Characters**: Any letter that’s not inside parentheses is added directly to our result string.

**4. Edge Case**: If there are **no parentheses**, the function will just go through the string and return it unchanged.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(n)` where `n` is the length of the string. Each character is processed exactly once.

- **Space Complexity:** `O(n)` due to the recursion stack, especially for deeply nested parentheses.

</details>
