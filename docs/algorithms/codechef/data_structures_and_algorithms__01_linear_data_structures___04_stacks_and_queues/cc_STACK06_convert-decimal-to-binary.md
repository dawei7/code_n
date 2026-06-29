# Convert Decimal to Binary

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STACK06 |
| Difficulty Rating | 932 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [STACK06](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/STACK06) |

---

## Problem Statement

Let's implement a stack using arrays to solve a classic problem: converting an integer from decimal to binary using the "divisor-remainder" method.

In this method, you repeatedly divide the decimal number by 2 and keep track of the remainders. \
The remainders, when read from bottom to top, give you the binary representation of the number.

Update the code given in the IDE to solve this problem.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

For each test case, output on a new line the maximum value of $A_1+A_N$ you can get after several right rotations.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
10
15
18
```

**Output**

```text
1010
1111
10010
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
```

**Output for this case**

```text
1010
```



#### Test case 2

**Input for this case**

```text
15
```

**Output for this case**

```text
1111
```



#### Test case 3

**Input for this case**

```text
18
```

**Output for this case**

```text
10010
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Convert Decimal to Binary](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/STACK06)

### [](#problem-statement-1)Problem Statement:

Let’s implement a stack using arrays to solve a classic problem: converting an integer from decimal to binary using the “divisor-remainder” method.

In this method, you repeatedly divide the decimal number by 2 and keep track of the remainders.

The remainders, when read from bottom to top, give you the binary representation of the number.

### [](#approach-2)Approach:

The key idea behind this code is to use a stack to reverse the binary digits generated from a decimal number.

-

**Stack Implementation**: We use an array `a[]` and a variable `top` to implement the stack, where `push()` adds an element and `pop()` removes an element from the stack. The stack stores the binary digits (remainder when dividing by 2) of the decimal number in reverse order.

-

**Decimal to Binary Conversion**:

- For each decimal number, we repeatedly divide it by 2, storing the remainder in the stack. This remainder represents the binary digits in reverse order (Least Significant Bit first).

- After converting all digits, the binary digits are popped from the stack and printed, giving the correct order for binary representation.

-

**Edge Case**: If the input decimal number is 0, the binary representation is directly printed as **0**.

-

**Multiple Test Cases**: The program reads multiple test cases and performs the decimal to binary conversion for each one, printing the binary result.

### [](#time-complexity-3)Time Complexity:

The time complexity is **O(log₂(decimal))** for each decimal number because we divide the decimal number by 2 in each iteration, which reduces its size logarithmically.

### [](#space-complexity-4)Space Complexity:

The space complexity is **O(log₂(decimal))** because the stack stores the binary digits, which are proportional to the number of digits in the binary representation of the decimal number.

</details>
