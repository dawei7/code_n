# Small factorials

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FCTRL2 |
| Difficulty Rating | 648 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FCTRL2](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FCTRL2) |

---

## Problem Statement

You are asked to calculate factorials of some small positive integers.

### Input

An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1 <= n <= 100

### Output

For each integer n given at input, display a line with the value of n!

**Note:** For larger numbers, their factorial can overflows any available numeric data type in C.

---

## Examples

**Example 1**

**Input**

```text
4
1
2
5
3
```

**Output**

```text
1
2
120
6
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5
```

**Output for this case**

```text
120
```



#### Test case 4

**Input for this case**

```text
3
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Small factorials Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FCTRL2)

### [](#problem-statement-1)Problem Statement:

Given an integer `n`, calculate the factorial `n!` for a range of input numbers and print the result.

### [](#approach-2)Approach:

- **Challenges in the Problem**: Handling Large Numbers-

- The value of n! grows extremely fast. For instance, 20! = 2,432,902,008,176,640,000. Standard data types such as `int` or `long long` cannot handle such large values since they exceed their maximum range.

- **Storing and Printing Large Numbers**: To handle the large size of factorial results-

- use an array to store individual digits of the factorial.

- Perform multiplication digit by digit, handling carries like manual multiplication and store the result in reverse order for easier manipulation.

### [](#steps-3)Steps:

- **Use an Array to Store Digits**:

- To handle large results, use an array to store individual digits of the factorial. This avoids overflow issues with traditional data types.

- Each digit of the resulting number is stored in an array in reverse order (least significant digit first) to simplify multiplication.

- **Perform Multiplication Digit-by-Digit**:

- Use a manual multiplication approach, similar to how multiplication is done by hand:

- Multiply each digit in the array by the current number `x` in the iteration.

- Maintain a carry and add it to the next step to handle multi-digit results.

- After multiplication, update the array with the new number and continue until `n` is reached.

- **Print the Result**:

- After all iterations are complete, print the array starting from the highest index down to `0` to display the full factorial.

### [](#complexity-4)Complexity:

- **Time Complexity**: O(n^2 . m), where `m` is the number of digits in the factorial. The approach is efficient for `n` up to `100` due to the manageable size of operations on individual digits.

- **Space Complexity**: O(m), where `m` is the number of digits in the result (maximum for `100!` is `158` digits).

</details>
