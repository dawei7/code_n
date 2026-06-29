# Linear Search in array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO03 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Searching |
| Official Link | [SESO03](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH1/problems/SESO03) |

---

## Problem Statement

Write a program to search for a specific element in an array and print "**Yes**" if the element is present, otherwise print "**No**".

---

## Input Format

- The first line contains an integer $n$, the length of the array and $k$, the element to be search.
- The second line contains $n$ space-separated integers representing the elements of the array.

---

## Output Format

- Print "**Yes**" if the element $k$ is present in the array.
- Print "**No**" if the element $k$ is not present in the array.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
8 1
3 5 1 4 5 6 5 6
```

**Output**

```text
Yes
```

**Example 2**

**Input**

```text
3 4
1 2 3
```

**Output**

```text
No
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH1/problems/SESO03)

#### [](#problem-understanding-1)Problem Understanding

The problem requires us to search for a specific element in an array. Given an array of integers and a target element, we need to determine whether the target element is present in the array. If it is found, we should print “Yes”; otherwise, we should print “No”.

#### [](#approach-2)Approach

The problem can be solved using a straightforward linear search algorithm.

- We iterate through the array elements using a loop.

- For each element in the array, we check if it matches the target element `k`.

- If we find a match, we set a flag (`found`) to `true` and break out of the loop since we no longer need to check the remaining elements.

- If the loop completes without finding the element, the flag remains `false`.

- After completing the search, we print “Yes” if the flag is `true`, indicating that the element was found.

- Otherwise, we print “No” if the flag is `false`, indicating that the element was not found.

#### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity of the solution is O(n), where `n` is the number of elements in the array. In the worst case, we may need to check every element of the array, which results in linear time complexity.

-

**Space Complexity**: The space complexity is O(1) for the extra space used for variables like `k`, `found`, and the loop counter. The space used by the array itself is O(n), but this is considered part of the input rather than additional space used by the algorithm.

</details>
