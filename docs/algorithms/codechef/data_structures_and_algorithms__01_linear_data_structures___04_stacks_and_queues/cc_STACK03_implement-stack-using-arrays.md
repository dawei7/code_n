# Implement Stack using Arrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STACK03 |
| Difficulty Rating | 932 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [STACK03](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS/problems/STACK03) |

---

## Problem Statement

Here's a simple exercise that involves implementing a stack. \
In this exercise, you'll implement a basic stack to reverse a string using the stack's LIFO property.

### Task
Update the functions `push()` and `pop()` within the class stack to output the reverses string.

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
Hello, World!
```

**Output**

```text
!dlroW ,olleH
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Implement Stack using Arrays](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS/problems/STACK03)

### [](#problem-statement-1)Problem Statement:

Here’s a simple exercise that involves implementing a stack.

In this exercise, you’ll implement a basic stack to reverse a string using the stack’s LIFO property.

***Task***

Update the functions `push()` and `pop()` within the class stack to output the reverses string.

### [](#approach-2)Approach:

The key idea behind this code is to use a stack to reverse the characters of a given string. A stack works by adding elements to the top, and when elements are removed, they are popped from the top. This property is perfect for reversing a string because by pushing the characters onto the stack and then popping them off, we reverse the order.

Here’s how the code works:

- **Pushing Characters**:

- We first push each character of the input string onto the stack, one by one.

- The `pushToStack` function places each character at the top of the stack. Since stacks follow LIFO, the last character pushed will be the first to come out when we pop.

- **Popping Characters**:

- After all characters are on the stack, we begin popping them off one by one. Each character popped from the stack is added to a new string (`reversedString`).

- This process continues until the stack is empty. Since the stack pops characters in reverse order, the `reversedString` will hold the input string in reverse.

### [](#time-complexity-3)Time Complexity:

The time complexity is **O(n)** because we push and pop each character of the string once.

### [](#space-complexity-4)Space Complexity:

The space complexity is **O(n)** due to the stack and reversed string, both requiring space proportional to the input length.

</details>
