# Largest Odd Substring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LARGODDSTRIN |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [LARGODDSTRIN](https://www.codechef.com/practice/course/strings/STRINGS/problems/LARGODDSTRIN) |

---

## Problem Statement

You are given a string $nums$ consisting of digits representing a large integer. Your task is to find the largest-valued **odd integer** (as a substring of $nums$) that can be obtained.

A **substring** is a contiguous sequence of characters within the string.

## Function Declaration

### Function Name

$findLargestOddSubstring$ – This function finds the largest-valued odd integer that can be obtained as a substring of the given numeric string.

### Parameters

* $num$ : A string representing a large integer, consisting only of digits ($0–9$).

### Return Value

* This function **prints**:

  * The largest odd integer substring if it exists.
  * $-1$ if no odd integer substring can be formed.

## Constraints

* $1 \le |num| \le 10^5$
* The string $num$ contains only digits $0–9$
* The string does **not** contain leading zeros
* There is no limit on the size of the integer represented by the substring

---

## Input Format

* The first line contains a single string `num`.

---

## Output Format

* Print a single line:

  * The largest odd integer substring of `num`
  * Or `-1` if no odd substring exists

---

## Constraints

- $1 \le |S| \le 10^{5}$
- $S \text{ contains only digits } (0\text{--}9)$
- $S \text{ does not contain leading zeros}$

---

## Examples

**Example 1**

**Input**

```text
128764
```

**Output**

```text
1287
```

**Explanation**

The largest odd substring ends at the first odd digit from the right, which is '7'.

**Example 2**

**Input**

```text
60042
```

**Output**

```text
-1
```

**Explanation**

There are no odd digits in the string, so no odd substring exists.

**Example 3**

**Input**

```text
987654321
```

**Output**

```text
987654321
```

**Explanation**

The last digit is '1', which is odd, so the entire number is the largest odd substring.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given a numeric string `S` representing a large integer.\
Your task is to find the **largest-valued odd integer substring** that can be obtained from `S`.

A **substring** is a contiguous sequence of characters from the string.

If there is no odd digit in `S`, print `-1`.

---

## Key Observations

A substring ending at the ** odd digit** from the right will always be the largest **odd substring**.

This is because removing any trailing even digits still keeps the number as large as possible (preserving prefix digits).

If the string contains **no odd digits**, then no odd substring can exist.

---

## Approach

- **Traverse the string from right to left**.

- Find the first odd digit (1, 3, 5, 7, or 9).

- **Return the substring** from the start of the string up to (and including) that odd digit.

- If no odd digit is found, print `-1`.

This approach ensures the substring is **maximal and odd**.

---

## Complexity Analysis

**Time Complexity**: O(n) – we make a single pass through the string.\
**Space Complexity**: O(1) – only a few variables are used.

</details>
