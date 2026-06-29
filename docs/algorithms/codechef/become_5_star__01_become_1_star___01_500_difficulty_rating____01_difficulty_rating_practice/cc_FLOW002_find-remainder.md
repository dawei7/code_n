# Find Remainder

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOW002 |
| Difficulty Rating | 421 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [FLOW002](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW002) |

---

## Problem Statement

Write a program to find the remainder when an integer **A** is divided by an integer **B**.

### Input

The first line contains an integer **T**, the total number of test cases. Then **T** lines follow, each line contains two Integers **A** and **B**.

### Output

For each test case, find the remainder when **A** is divided by  **B**, and display it in a new line.

### Constraints

- 1 **≤** **T** **≤** 1000

- 1 **≤** **A,B** **≤** 10000

---

## Examples

**Example 1**

**Input**

```text
3 
1 2
100 200
40 15
```

**Output**

```text
1
100
10
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
100 200
```

**Output for this case**

```text
100
```



#### Test case 3

**Input for this case**

```text
40 15
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Find Remainder Practice Problem in 500 difficulty rating](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW002)

### [](#problem-statement-1)Problem Statement:

Write a program to find the remainder when an integer **A** is divided by an integer **B** .

### [](#approach-2)Approach:

- The problem is simple and can be solved using the modulus operator `%` in most programming languages. The modulus operator returns the remainder after division.

- Print the result of `A % B`.

### [](#complexity-3)Complexity:

- **Time Complexity**: `O(1)`. Simple output is done

- **Space Complexity**: `O(1)`. No extra space required.

</details>
