# Count of Maximum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXCOUNT |
| Difficulty Rating | 1180 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MAXCOUNT](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MAXCOUNT) |

---

## Problem Statement

Given an array $A$ of length $N$, your task is to find the element which repeats in the array the maximum number of times, along with its exact frequency count.

If there is a tie (i.e multiple elements have the same maximum frequency), you must choose the **smallest** element among them.

---

## Function Declaration

### Function Name
$mostFrequent$ – This function processes the array and finds the required element and its count.

### Parameters
$N$ : An integer representing the length of the array $A$.
$A$ : An array (or list) of $N$ integers.

### Return Value
Returns an array/pair of two integers:
1. The most frequent element (the smallest one in case of a tie).
2. Its corresponding frequency count.

---

### Constraints:
* $1 \le T \le 100$
* $1 \le N \le 10^5$
* $1 \le A[i] \le 10^9$
* The sum of $N$ over all test cases does not exceed $2 \times 10^5$.

*The input and output formats provided below are only for testing with custom inputs. You only need to complete the logic function. The parsing of inputs, looping over test cases, and final printing are handled automatically by the platform.*

---

## Input Format

- The first line contains a single integer $T$, representing the number of test cases.
- For each test case:
  - The first line contains a single integer $N$, representing the length of the array.
  - The second line contains $N$ space-separated integers representing the elements of array $A$.

---

## Output Format

- For each test case, print two space-separated integers on a new line: the chosen element followed by its frequency count.

---

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $1 \le A[i] \le 10^9$
- The sum of $N$ over all test cases does not exceed $2 \times 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5
1 2 3 2 5
6
1 2 2 1 1 2
```

**Output**

```text
2 2
1 3
```

**Explanation**

In first case 2 occurs twice whereas all other elements occur only once.
In second case, both 1 and 2 occur 3 times but 1 is smaller than 2.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 2 5
```

**Output for this case**

```text
2 2
```



#### Test case 2

**Input for this case**

```text
6
1 2 2 1 1 2
```

**Output for this case**

```text
1 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/MAXCOUNT/)

[Contest](http://www.codechef.com/FEB12/problems/MAXCOUNT/)

### DIFFICULTY

EASY

### EXPLANATION

This was supposed to be a problem that anyone who knows basic programming could solve and I’m glad that it’s satisfied our expectations.

For the given constraints there were two easy approaches that one could use to solve this problem:

**Approach 1:**

The number of elements in the array bounded just by 100. For each element check how many other elements are equal to this one and hence find out what is the corresponding count. This would take time **O(N****2**). Since **N <= 100** here this solution would fit easily into the time limit.

**Approach 2:**

The range of elements is small - all elements are between **1** and **10000**. One could create a frequency map for the array. I.e. create an array **FREQ** of size **10000** such that **FREQ****[x]** gives the number of times the number x appears in the array. Initially all values in **FREQ** are zeros. When you start reading input and say you read a number **x**, you should add **1** to **FREQ**[x]. It takes **O(N)** time to build this array after initialization. When all input values have been scanned, one could make iteration at the FREQ array to find the smallest element with the largest count.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/February/Setter/MAXCOUNT.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/February/Tester/MAXCOUNT.cpp).

</details>
