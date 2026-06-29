# Finding Square Roots

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FSQRT |
| Difficulty Rating | 668 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FSQRT](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FSQRT) |

---

## Problem Statement

*In olden days finding square roots seemed to be difficult but nowadays it can be easily done using in-built functions available across many languages *
.

Assume that you happen to hear the above words and you want to give a try in finding the square root of any given integer using in-built functions. So here's your chance.

### Input

The first line of the input contains an integer T, the number of test cases. T lines follow. Each line contains an integer N whose square root needs to be computed.

### Output

For each line of the input, output the square root of the input integer, rounded down to the nearest integer, in a new line.

### Constraints

1<=T<=20

1<=N<=10000

---

## Examples

**Example 1**

**Input**

```text
3
10
5
10000
```

**Output**

```text
3
2
100
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
10000
```

**Output for this case**

```text
100
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Finding Square Roots Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FSQRT)

### [](#problem-statement-1)Problem Statement:

Finding Square root of a number using in-built square-root function.

### [](#approach-2)Approach:

- Use a built-in function (e.g., `sqrt()` in C++ or Python) to compute the square root of `N`.

- Round the result down to the nearest integer using functions like `floor()` or by casting to an integer (e.g., `int(sqrt(N))`).

### [](#complexity-3)Complexity:

- **Time Complexity**: `O(1)` The `sqrt()` function runs in `O(1)` for each `N`

- **Space Complexity**: `O(1)` Not using any extra space.

</details>
