# Reverse The Number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOW007 |
| Difficulty Rating | 588 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FLOW007](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW007) |

---

## Problem Statement

Given an Integer **N**, write a program to reverse it.

### Input

The first line contains an integer **T**, total number of testcases. Then follow **T** lines, each line contains an integer **N**.

### Output

 For each test case, display the reverse of the given number **N**, in a new line.

### Constraints

- 1 **≤** **T** **≤** 1000

- 1 **≤** **N** **≤** 1000000

---

## Examples

**Example 1**

**Input**

```text
4
12345
31203
2123
2300
```

**Output**

```text
54321
30213
3212
32
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
12345
```

**Output for this case**

```text
54321
```



#### Test case 2

**Input for this case**

```text
31203
```

**Output for this case**

```text
30213
```



#### Test case 3

**Input for this case**

```text
2123
```

**Output for this case**

```text
3212
```



#### Test case 4

**Input for this case**

```text
2300
```

**Output for this case**

```text
32
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Reverse The Number Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW007)

### [](#problem-statement-1)Problem Statement:

Given an Integer **N**, write a program to reverse it.

### [](#approach-2)Approach:

**Reverse the integer**:

- Use mathematical operations to reverse the digits of the integer:

- Initialize a variable `reversedNumber` to store the reversed result, initially set to `0`.

- Use a loop to extract the last digit of `N` using `N%10`, add it to `reversedNumber`, and then remove the last digit from `N` using integer division `N//10`.

- Continue until `N` becomes `0`.

- Alternatively, convert the integer to a string, reverse the string, and convert it back to an integer for simplicity.

**Edge Cases**:

- Single-digit numbers: The reverse should be the number itself.

- Numbers with trailing zeros (e.g., `2300`): The reverse should remove leading zeros (e.g., `32`).

- Maximum constraint `N=1,000,000`: Ensure the program can handle up to `7-digit` numbers efficiently.

### [](#complexity-3)Complexity:

- **Time Complexity**: `O(D)` where `D` is the number of digits in `N`. Reversing each number runs in linear time relative to the number of digits.

- **Space Complexity**: `O(1)` for the mathematical approach or `O(D)` for the string approach.

</details>
