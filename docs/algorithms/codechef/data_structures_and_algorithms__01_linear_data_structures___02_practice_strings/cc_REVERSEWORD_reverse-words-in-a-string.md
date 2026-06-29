# Reverse Words in a String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REVERSEWORD |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [REVERSEWORD](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/REVERSEWORD) |

---

## Problem Statement

You are given a string $s$ consisting of English letters, digits, and spaces `' '`.\
Your task is to **reverse the order of the words** in the string.

A word is defined as a sequence of non-space characters.\
The words in $s$ are separated by one or more spaces.

You must:

- Return the words in **reverse order**, separated by a **single space**.

- Remove any **leading**, **trailing**, or **multiple spaces** between words.

### Function Declaration

### Function Name
$reverseWords$ – This function reverses the order of words in a given string while removing extra spaces.

### Parameters

* $s$ : A reference to a string consisting of English letters (uppercase and lowercase), digits, and spaces.

### Return Value

* Returns a string where:
  * The order of words is reversed.
  * Words are separated by a single space.
  * Leading, trailing, and multiple spaces are removed.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |s| \leq 10^4$
- The string contains English letters (uppercase and lowercase), digits, and spaces.
- There is at least one word in the string.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases.
- Each of the next $T$ lines contains a string $s$.

---

## Output Format

- For each test case, print a single line containing the string with words in reverse order, separated by a single space.

---

## Constraints

- $1 \le T \le 100$
- $1 \le |S| \le 10^{4}$
- $\texttt{S contains English letters (uppercase and lowercase), digits, and spaces ' '}$
- $\texttt{There is at least one word in S}$

---

## Examples

**Example 1**

**Input**

```text
4
codechef is awesome
  java   and   python  
123 test case
   learn   data   structures
```

**Output**

```text
awesome is codechef
python and java
case test 123
structures data learn
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
codechef is awesome
```

**Output for this case**

```text
awesome is codechef
```



#### Test case 2

**Input for this case**

```text
java   and   python
```

**Output for this case**

```text
python and java
```



#### Test case 3

**Input for this case**

```text
123 test case
```

**Output for this case**

```text
case test 123
```



#### Test case 4

**Input for this case**

```text
learn   data   structures
```

**Output for this case**

```text
structures data learn
```



**Example 2**

**Input**

```text
1
Roses are red
```

**Output**

```text
red are Roses
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

You are given a string **S** containing letters, digits, and spaces.\
You need to **reverse the order of words**, ensuring that:
- Words are separated by a single space.
- All extra spaces (leading, trailing, or between words) are removed.

A word is a sequence of non-space characters.

---

# Approach

To reverse the words properly, we must:

- **Split** the string into words — ignoring multiple spaces.
- **Reverse** the list of words.
- **Join** them back together with a **single space**.

---

# Step-by-Step Explanation

**Step 1: Trim spaces**

- Remove leading and trailing spaces since they don’t contribute to words.

**Step 2: Split into words**

- Break the string into a list of words by splitting using one or more spaces.

**Step 3: Reverse the list**

- Reverse the order of the words array/list.

**Step 4: Join words**

-Join the reversed words with a single space `" "`.

---

# Time Complexity

- **O(N)** – Traversing the entire string once.
- **O(N)** space for storing the words.

Total: **O(N)** time and **O(N)** space.

</details>
