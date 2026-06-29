# Second Largest

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOW017 |
| Difficulty Rating | 730 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FLOW017](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW017) |

---

## Problem Statement

Three numbers **A**, **B** and **C** are the inputs. Write a program to find second largest among them.

---

## Input Format

The first line contains an integer **T**, the total number of testcases. Then **T** lines follow, each line contains three integers **A**, **B** and **C**.

---

## Output Format

For each test case, display the second largest among **A**, **B** and **C**, in a new line.

---

## Constraints

- 1 **≤** **T** **≤** 1000

- 1 **≤** **A,B,C** **≤** 1000000

---

## Examples

**Example 1**

**Input**

```text
3 
120 11 400
10213 312 10
10 3 450
```

**Output**

```text
120
312
10
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
120 11 400
```

**Output for this case**

```text
120
```



#### Test case 2

**Input for this case**

```text
10213 312 10
```

**Output for this case**

```text
312
```



#### Test case 3

**Input for this case**

```text
10 3 450
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Second Largest Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW017)

### [](#problem-statement-1)Problem Statement:

Three numbers **A**, **B** and **C** are the inputs. Write a program to find second largest among them.

### [](#approach-2)Approach:

**Approach 1:**

This approach directly compares the three integers using conditional statements to find the second largest number.

**Steps:**

- Compare A,B, and C using conditional checks:

- If A is greater than B and less than C, or A is greater than C and less than B, A is the second largest.

- Similarly, check B and C with the same logic.

- Print the number that satisfies the condition for each test case.

**Approach 2:**

This approach involves storing the numbers in an array and using the `sort` function to find the second largest.

**Steps:**

- Store the integers A,B,C in an array.

- Sort the array in ascending order.

- Print the second element in the sorted array, which will be the second largest.

### [](#complexity-3)Complexity:

- **Time Complexity**: For both the approaches we have time complexity of `O(1)`. Using simple if-else and sorting three integers requires `O(1)`.

- **Space Complexity**: `O(1)` No extra space used.

</details>
