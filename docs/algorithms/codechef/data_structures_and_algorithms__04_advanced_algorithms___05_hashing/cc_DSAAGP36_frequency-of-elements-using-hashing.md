# Frequency of elements using Hashing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAAGP36 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Hashing |
| Official Link | [DSAAGP36](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP36) |

---

## Problem Statement

You are given an integer $N$ and an array containing $N$ integers.
For each element in the array, you have to output its frequency in the array using Hashing.
The frequency of an element in the array tells how many times it occurs in the array.

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

- $1 \leq N \leq 10^5$
- $1 \leq max(A) \leq 100$

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

Problem Link - [Frequency of elements using Hashing in Hashing](https://www.codechef.com/learn/course/hashing/HASH01/problems/DSAAGP36)

### [](#problem-statement-1)Problem Statement:

You are given an integer N and an array A containing N integers. For each element in the array, you have to output its frequency in the array using Hashing.

### [](#approach-2)Approach:

- Find the maximum element in the array.

- Declare a Hash array of size `max_element + 1`, and initialize all elements to `0`.

- Iterate through the array and for each element increment the corresponding index in the Hash array.

### [](#complexity-3)Complexity:

- **Time Complexity:** We are finding the maximum element by iterating through the whole array `O(N)`. Then we add the array values to their corresponding indexes into the hash array which takes `O(N)` time. Total time complexity comes as `2*O(N) -> O(N)`

- **Space Complexity:** The hash array is created which is of size `max_element+1`. If max_element is `M`, then this array requires `O(M)` space.

</details>
