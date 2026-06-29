# Convert string to number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRTONUM |
| Difficulty Rating | 1200 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [STRTONUM](https://www.codechef.com/practice/course/strings/STRINGS/problems/STRTONUM) |

---

## Problem Statement

You are given a string that represents a positive number. Your task is to write a program that converts this string into its numerical equivalent without using any in-built parsing, conversion libraries, or direct type casting methods. The string will not contain any leading zeros, decimals, or any non-numeric characters.

Complete the function **stringToNumber** in the IDE

---

## Input Format

- The first line contains a single integer, T, the number of test cases.
- The following T lines each contain a single string, S, representing the number.

---

## Output Format

For each test case, print the numerical equivalent of the string.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |S| \leq 10$, where $|S|$ is the length of the string.
- S will only contain digits (0-9) and will not have leading zeros.

---

## Examples

**Example 1**

**Input**

```text
3
123
42
1001
```

**Output**

```text
123
42
1001
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
123
```

**Output for this case**

```text
123
```



#### Test case 2

**Input for this case**

```text
42
```

**Output for this case**

```text
42
```



#### Test case 3

**Input for this case**

```text
1001
```

**Output for this case**

```text
1001
```


