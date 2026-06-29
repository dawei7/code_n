# Remove Duplicates

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REMDUP |
| Difficulty Rating | 1100 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [REMDUP](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/REMDUP) |

---

## Problem Statement

Chef gave you the $head$ of a sorted linked list which may contain duplicate values. You've to remove all the duplicate values and return the sorted linked list such that it does not contain any duplicates.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the length of array.
- The second line of every test case contains $N$ integers - $ A_1,A_2,..,A_N$ denoting the integers in the array.
- It is guaranteed that the array is sorted
- You don't need to read or print anything. Just complete the function removeDuplicates() which takes the head of the linked list as input.

---

## Output Format

Return the head of the sorted linked list without duplicates.

---

## Constraints

- $ 1\leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $\sum N \leq 5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
4
6 15 22 22
5
13 17 17 17 20
4
5 6 6 6
2
9 9
```

**Output**

```text
6 15 22 
13 17 20 
5 6 
9
```

**Explanation**

**Test Case 1:** It is easy to see that the linked list without duplicates is $[6, 15, 22]$

**Test Case 4:** The is only a single value in the entire linked list

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
6 15 22 22
```

**Output for this case**

```text
6 15 22
```



#### Test case 2

**Input for this case**

```text
5
13 17 17 17 20
```

**Output for this case**

```text
13 17 20
```



#### Test case 3

**Input for this case**

```text
4
5 6 6 6
```

**Output for this case**

```text
5 6
```



#### Test case 4

**Input for this case**

```text
2
9 9
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## [](#problem-explanation-1)Problem Explanation

We are given a sorted linked list and we have to remove all the duplicates from the linked list and return the sorted linked list with unique values.

## [](#approach-2)Approach

Since the linked list is sorted, the duplicate values will be right next to one another. We can iterate over the linked list and if the next value is equal to the current value we delete the next node. To delete the node we set the current’s next pointer to the next of the next node. and then delete the next node.

</details>
