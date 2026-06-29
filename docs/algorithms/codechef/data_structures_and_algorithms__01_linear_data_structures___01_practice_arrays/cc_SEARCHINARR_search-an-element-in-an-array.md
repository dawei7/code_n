# Search an element in an array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEARCHINARR |
| Difficulty Rating | 600 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [SEARCHINARR](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/SEARCHINARR) |

---

## Problem Statement

You are given an array $A$ of size $N$ and an element $X$. Your task is to find whether the array $A$ contains the element $X$ or not.

## **Function Declaration**

### **Function Name**

$solve$ – This function checks whether a given element **X** is present in the array **A**.

### **Parameters**

* $N$ : An integer representing the number of elements in the array.
* $X$ : An integer representing the element to be searched.
* $A$ : A list/array of integers of length **N**, representing the input array.

### **Return Value**

* Returns a **string**:

  * `"YES"` if the element $X$ exists in the array $A$.
  * `"NO"` if the element $X$ is not present in the array.

---

## Input Format

- The first line contains two space-separated integers $N$ and $X$ — the size of array and the element to be searched.
- The second line contains all the elements of array $A$

---

## Output Format

Output "YES" if the element $X$ is present in $A$, otherwise output "NO".

---

## Constraints

- $1 \leq N , X \leq 10^5$
- $1 \leq A_i \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
5 3
7 3 5 2 1
```

**Output**

```text
YES
```

**Example 2**

**Input**

```text
5 10
7 3 5 2 1
```

**Output**

```text
NO
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Search an element in an array in Arrays](https://www.codechef.com/learn/course/arrays/ARRAYS02/problems/SEARCHINARR)

### [](#problem-statement-1)Problem Statement:

You are given an array A of size N and an element X. Your task is to find whether the array A contains the element X or not.

### [](#approach-2)Approach:

- We iterate through the array and check whether any element in the array is equal to X.

- If we find X in the array, we can stop the search and output “YES”.

- If we complete the iteration without finding X, we output “NO”.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)` Iterated through the whole array.

- **Space Complexity:** `O(1)` No extra space is used.

</details>
