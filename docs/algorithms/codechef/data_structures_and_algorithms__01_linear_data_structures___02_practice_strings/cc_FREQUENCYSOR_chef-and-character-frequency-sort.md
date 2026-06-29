# Chef and Character Frequency Sort

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FREQUENCYSOR |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [FREQUENCYSOR](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/FREQUENCYSOR) |

---

## Problem Statement

Chef is experimenting with strings. He wants to rearrange all the characters of a given string **$S$** in decreasing order of their frequency.

If two characters have the same frequency, Chef sorts them in **lexicographical (ASCII) order**.

Help Chef by printing the final rearranged string.

---

### Function Declaration

* **Function Name:**

  * **$sortByFrequency$**

* **Parameters:**

  * **$s$** ($string$) \
    A string consisting of uppercase and lowercase English letters and digits.

* **Return Value:**

  * Returns a $string$ representing the rearranged string after sorting by the given rules.

---

---

## Input Format

- The first and only line contains a string **S**.
- The string consists of uppercase and lowercase English letters and digits.

---

## Output Format

Print the rearranged string after sorting by the given rules.

---

## Constraints

- $1 \le |S| \le 5 \times 10^{5}$

---

## Examples

**Example 1**

**Input**

```text
CookBook
```

**Output**

```text
ooookkBC
```

**Explanation**

**Input:** `CookBook`

The character frequencies are:

* `o` $\rightarrow$ 3
* `B` $\rightarrow$ 1
* `C` $\rightarrow$ 1
* `k` $\rightarrow$ 1
* `u` $\rightarrow$ 1

Chef first places characters in **decreasing frequency** order, so `o` comes first as `ooo`.
The remaining characters all have the same frequency **1**, so they are arranged in **ASCII (lexicographical) order**:

`B < C < k < u`

So the final rearranged string is:

```
oooBCku
```
---

**Example 2**

**Input**

```text
aabbbcddd
```

**Output**

```text
bbbdddaac
```

**Explanation**

**Input:** `aabbbcddd`

The character frequencies are:

* `b` $\rightarrow$ 3
* `d` $\rightarrow$ 3
* `a` $\rightarrow$ 2
* `c` $\rightarrow$ 1

Characters with frequency **3** are `b` and `d`, and since `b < d`, they appear as:
`bbbddd`

Then `a` appears twice:
`aa`

Finally, `c` appears once:
`c`

So the final rearranged string is:

```
bbbdddaac
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Statement

You are given a string S and must rearrange all characters such that:

- Characters with **higher frequency appear before** lower frequency characters

- For characters with **equal frequency**, sort them in **lexicographical (ASCII) order**

- Output the final rearranged string.

---

# Understanding with Examples

Input:\
CookBook

Character count:\
o → 4\
k → 2\
B → 1\
C → 1

Order decision:\
1st: o (highest frequency)\
2nd: k\
3rd: B & C (same freq → ASCII comparison → 'B' comes before 'C')\

Output:\
ooookkBC

---

# Approach

| Step | Description                                              |
| ---- | -------------------------------------------------------- |
| 1    | Count frequency of each character                        |
| 2    | Sort characters primarily by **frequency (descending)**  |
| 3    | For equal frequency, sort by **ASCII value (ascending)** |
| 4    | Build and print the final string                         |
--------------------------------------------------------

# Complexity

| Operation           | Cost                                           |   |         |
| ------------------- | ---------------------------------------------- | - | ------- |
| Frequency counting  | `O(N)`                                         |   |         |
| Sorting characters  | `O(K log K)` (K ≤ 62 for typical alphanumeric) |   |         |
| Constructing output | `O(N)`                                         |   |         |
| **Total**           | `O(N + K log K)` — fast enough for             | S | ≤ 5×10⁵ |

</details>
