# Frequency of each element in the array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAAGP35 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Hashing |
| Official Link | [DSAAGP35](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP35) |

---

## Problem Statement

You are given an integer $N$ and an array containing $N$ integers.
For each element in the array you have to output it's frequency in the array.
Frequency of an element in the array tells how many times it occurs in the array.

Iterate over each element in the array and count the frequency of that element using another loop then print the frequency for each element in the array.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains one integer $N$ denoting the number of elements in the array.
    - The next line contains $N$ space separated integers, denoting the elements in the array.

---

## Output Format

For each test case, output $N$ space separated integers denoting the frequency of each element of the array.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq A_i \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
10
1 2 1 2 1 3 4 1 2 3
5 
1 1 1 1 1
5
1 2 1 2 1
```

**Output**

```text
4 3 4 3 4 2 1 4 3 2
5 5 5 5 5
3 2 3 2 3
```

**Explanation**

**Test Case 1**: In this array $1$ occurs $4$ times, $2$ occurs $3$ times, $3$ occurs $2$ times and $4$ occurs $1$ times.
**Test Case 2**: In this array $1$ occurs $5$ times.
**Test Case 3**: In this array $1$ occurs $3$ times and $2$ occurs $2$ times.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
1 2 1 2 1 3 4 1 2 3
```

**Output for this case**

```text
4 3 4 3 4 2 1 4 3 2
```



#### Test case 2

**Input for this case**

```text
5
1 1 1 1 1
```

**Output for this case**

```text
5 5 5 5 5
```



#### Test case 3

**Input for this case**

```text
5
1 2 1 2 1
```

**Output for this case**

```text
3 2 3 2 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Frequency of each element in the array in Hashing](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP35)

### [](#problem-statement-1)Problem Statement:

You are given an integer N and an array containing N integers. For each element in the array, you have to output its frequency in the array.

### [](#approach-2)Approach:

For each element in the array:

- Use an inner loop to go through the entire array again and count how many times the current element appears.

- We print the frequency for each element as we process it.

### [](#complexity-3)Complexity:

- **Time Complexity:** For each test case, we have an array of size `N`. The outer loop runs `N` times, and for each element, the inner loop also runs `N` times. Thus, the time complexity for each test case is `O(N^2)`.

- **Space Complexity:** `O(1)` No extra space needed to store output.

</details>
