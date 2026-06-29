# Distinct Codes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISTCODE |
| Difficulty Rating | 1234 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [DISTCODE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/DISTCODE) |

---

## Problem Statement

Sergey recently learned about **country codes** - two letter strings, denoting countries. For example, **BY** stands for Belarus and **IN** stands for India. Mesmerized by this new discovery, Sergey now looks for country codes everywhere!

Sergey has recently found a string **S** consisting of uppercase Latin letters. He wants to find the number of different country codes that appear in **S** as contiguous substrings. For the purpose of this problem, consider that every **2**-letter uppercase string is a valid country code.

### Input

The first line of input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first and only line of each test case contains a string **S**, consisting of uppercase Latin letters.

### Output

For each test case, output a single line containing the number of different country codes appearing in the given string.

### Constraints

- **1** ≤ **T** ≤ **100**

- Subtask 1 (35 points): **2** ≤ **|S|** ≤ **3**

- Subtask 2 (65 points): **2** ≤ **|S|** ≤ **104**

---

## Examples

**Example 1**

**Input**

```text
2
INBY
BYBY
```

**Output**

```text
3
2
```

**Explanation**

**Example case 1.** The codes are **IN**, **NB** and **BY**.

**Example case 2.** The codes are **BY** and **YB**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
INBY
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
BYBY
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/DISTCODE)

[Contest](http://www.codechef.com/LTIME31/problems/DISTCODE/)

# Difficulty:

CakeWalk

# Pre-requisites:

Basic Language Constructions

# Problem:

Find the number of distinct consecutive 2-letter substrings of the string S.

# Explanation:

## Solution for the subtask 1 (35 points):

If |S| = 2, then there is only one possible substring - the string S. So, the answer is 1.

If |S| = 3, then if all letters in the string are the same, then the answer is 1, otherwise there are 2 distinct consecutive 2-letter substrings, so, the answer is then 2.

## Solution for all subtasks:

Consider a boolean array A[][] of $26$x$ 26$ elements.

Let A[i,j] be **true** if there is a substring of S with first letter - the ith Latin alphabet letter and the second letter - the jth Latin alphabet letter.

Initially all elements of A[][] are false.

Let’s iterate through the symbols of the string S and set true all elements of A for the corresponding substrings. Note, that S is 1-indexed in the given pseudocode.

The pseudocode for the same follows:

``For k := 2 to |S|
	A[S[k-1], S[k]] = true;

``

The last step is to iterate through the array A and calculate the number of elements A[i,j] such that A[i,j] is **true**.

The complexity is O(|S|) for a single test case.

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/LTIME31/Setter/DISTCODE.cpp)

# Tester’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/LTIME31/Tester/DISTCODE.cpp)

</details>
