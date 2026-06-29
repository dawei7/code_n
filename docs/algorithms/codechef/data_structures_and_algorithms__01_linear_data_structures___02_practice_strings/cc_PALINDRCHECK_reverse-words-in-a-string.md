# Reverse Words in a String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PALINDRCHECK |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [PALINDRCHECK](https://www.codechef.com/practice/course/strings/STRINGS/problems/PALINDRCHECK) |

---

## Problem Statement

You are given a string $s$ consisting of English letters (uppercase and lowercase), digits, and spaces `' '`. The string may contain leading or trailing spaces, or multiple spaces between words.

Your task is to **reverse the order of the words** in the string. A word is defined as a sequence of non-space characters.

The resulting string should:
- Contain words in reversed order.
- Have only **single spaces** separating words.
- Not contain leading or trailing spaces.

## Function Declaration

### Function Name

$reverseWords$ – This function reverses the order of words in a given string while ensuring that words are separated by exactly one space and there are no leading or trailing spaces.

### Parameters

* $s$ : A string consisting of English letters (uppercase and lowercase), digits, and spaces `' '`.

### Return Value

* Returns a string containing the words of $s$ in reversed order.
* The returned string:
  * Contains words separated by a single space.
  * Has no leading or trailing spaces.

## Constraints

* $1 \le |s| \le 10^4$
* The string $s$ contains:
  * Uppercase English letters ($A–Z$)
  * Lowercase English letters ($a–z$)
  * Digits ($0–9$)
  * Space characters (`' '`)
* The string may contain:
  * Leading spaces
  * Trailing spaces
  * Multiple consecutive spaces between words
* There is **at least one word** in $s$.

---

## Input Format

* The first line contains a single string $s$.

---

## Output Format

* Print a single line containing the words of $s$ in reversed order.
* Words must be separated by exactly one space.
* There must be no leading or trailing spaces in the output.

---

## Constraints

- $1 \le |S| \le 10^{4}$
- **S** contains English letters (both uppercase and lowercase), digits, and spaces ' '.
- There is at least **one word** in **S**.

---

## Examples

**Example 1**

**Input**

```text
OpenAI   creates amazing   AI   models
```

**Output**

```text
models AI amazing creates OpenAI
```

**Example 2**

**Input**

```text
Data   Science is fun
```

**Output**

```text
fun is Science Data
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Statement

Given a string `s` consisting of words and spaces, reverse the **order of words** such that:

* Words are separated by one or more spaces
* The output must have **exactly one space** between words
* There must be **no leading or trailing spaces**

A **word** is defined as a maximal substring consisting of non-space characters.

---

## Approach 1: Using Extra Data Structures (Brute / Straightforward)

### Idea

* Trim leading and trailing spaces
* Split the string into words
* Store words in a container
* Build the result by traversing the container in reverse order

---

### Steps

1. Remove leading spaces
2. Remove trailing spaces
3. Use a string stream or manual parsing to extract words
4. Store words in a vector
5. Append words from last to first with a single space

---

### Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` (stores words + result)

---

### Pros

* Very easy to understand
* Clean and readable

### Cons

* Uses extra memory
* Not optimal for memory-constrained environments

---

## Approach 2: Stack-Based Solution

### Idea

* Parse words from left to right
* Push each word onto a stack
* Pop words to build the reversed string

---

### Steps

1. Traverse the string and extract words
2. Push each word onto a stack
3. Pop words and append them to the result string

---

### Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` (stack + result)

---

### Pros

* Conceptually simple
* Natural reversal logic

### Cons

* Still uses extra space
* No advantage over vector-based approach

---

## Approach 3: Reverse Entire String + Fix Words (Optimal In-place)

### Idea

Use the fact that:

* Reversing the entire string reverses word order
* Each word itself becomes reversed
* Reversing each word again fixes it
* Extra spaces can be cleaned in-place

---

### Steps

1. Reverse the entire string
2. Reverse each word individually
3. Remove extra spaces:

   * Skip leading spaces
   * Reduce multiple spaces to one
   * Remove trailing spaces

---

### Example

Input:

```
"  hello   world  "
```

Process:

```
Reverse whole string → "  dlrow   olleh  "
Reverse each word →  "  world   hello  "
Remove spaces →      "world hello"
```

---

### Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)` (auxiliary)

---

### Pros

* Optimal solution
* No extra memory used
* Industry-standard approach (used in interviews & LeetCode)

### Cons

* Slightly harder to implement
* Requires careful pointer handling

---

## Approach 4: Two-Pointer Backward Scan (Semi In-place)

### Idea

* Traverse the string from the end
* Extract words one by one
* Append them to the result string

---

### Steps

1. Start from the end of the string
2. Skip trailing spaces
3. Capture a word
4. Append it to result
5. Repeat until start of string

---

### Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` (result string)

---

### Pros

* No need to reverse the string
* Easier than full in-place approach

### Cons

* Still uses extra memory for output

---

## Comparison Summary

| Approach                | Time | Space | In-place | Difficulty |
| ----------------------- | ---- | ----- | -------- | ---------- |
| Extra DS (vector)       | O(n) | O(n)  | ❌        | Easy       |
| Stack-based             | O(n) | O(n)  | ❌        | Easy       |
| Reverse + Fix (Optimal) | O(n) | O(1)  | ✅        | Medium     |
| Backward Scan           | O(n) | O(n)  | ❌        | Medium     |

---

## Final Recommendation

* **For interviews / competitive programming:**
  👉 **Approach 3 (In-place reverse)**

* **For readability / production code:**
  👉 **Approach 1 or 4**

---

## Key Takeaways

* Space optimization often comes from **in-place transformations**
* Reversing operations can simplify complex string rearrangements
* Cleaning spaces is as important as reversing words

</details>
