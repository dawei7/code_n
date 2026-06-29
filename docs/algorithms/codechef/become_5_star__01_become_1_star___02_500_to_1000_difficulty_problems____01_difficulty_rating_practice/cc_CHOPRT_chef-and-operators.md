# Chef And Operators

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHOPRT |
| Difficulty Rating | 770 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHOPRT](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHOPRT) |

---

## Problem Statement

Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational Operators.

Relational Operators are operators which check relationship between two values. Given two numerical values **A** and **B** you need to help chef in finding the relationship between them that is,

First one is greater than second or,
First one is less than second or,
First and second one are equal.

### Input

First line contains an integer **T**, which denotes the number of testcases. Each of the **T** lines contain two integers **A** and **B**.

### Output

For each line of input produce one line of output. This line contains any one of the relational operators

'<' , '>' , '='.

### Constraints

1 ≤ **T** ≤ 10000
1 ≤ **A**, **B** ≤ 1000000001

---

## Examples

**Example 1**

**Input**

```text
3
10 20
20 10
10 10
```

**Output**

```text
<
>
=
```

**Explanation**

In this example 1 as 10 is lesser than 20

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 20
```

**Output for this case**

```text
<
```



#### Test case 2

**Input for this case**

```text
20 10
```

**Output for this case**

```text
>
```



#### Test case 3

**Input for this case**

```text
10 10
```

**Output for this case**

```text
=
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Chef And Operators Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHOPRT)

### [](#problem-statement-1)Problem Statement:

Chef is learning about relational operators, which are used to compare two numerical values. The task is to determine the relationship between two given integers A and B. For each pair of numbers, you need to output one of the following:

- ‘<’ if A is less than B

- ‘>’ if A is greater than B

- ‘=’ if A is equal to B

### [](#approach-2)Approach:

The problem can be solved by a straightforward comparison using conditional statements.

- Compare A and B using basic conditional checks:

- If A<B, print `'<'`.

- If A>B, print `'>'`.

- If A==B, print `'='`.

### [](#complexity-3)Complexity:

- **Time Complexity**: `O(1)` using the conditional statements.

- **Space Complexity**: `O(1)` No extra space is used.

</details>
