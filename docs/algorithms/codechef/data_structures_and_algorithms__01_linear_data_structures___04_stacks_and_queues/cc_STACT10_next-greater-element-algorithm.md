# Next Greater Element Algorithm

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STACT10 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [STACT10](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/STACT10) |

---

## Problem Statement

The algorithm typically uses a stack data structure to keep track of the elements greater than current element.

- **Initialize an empty stack**
- **Iterate through the array from right to left**: Start from the rightmost element of the array and move towards the left.
- **Pop elements from the stack**: For each element in the array, pop elements from the stack until the stack is empty or the element at the top of the stack is greater than the current array element.
- **Find the Next Greater Element (NGE)**: If the stack is empty, there is no NGE for the current element, otherwise the top of the stack is NGE for current element.
- **Push the current element**: Push the current element on the stack as it can be NGE for the remaining elements.

Example:
Consider the array [4, 5, 2, 10, 8].\
Length of the array is 5, thus the last index is 4.

- **Start from the right:**

index = 4\
element = 8\
stack = []

For 8, the stack is empty. So, the NGE for 8 is -1. `nge[4] = -1`\
Push 8 onto the stack.

- **Move to the next element (10):**

index = 3\
element = 10\
stack = [8]

Pop 8 from the stack since 8 is smaller than 10.\
The stack will become empty. NGE for 10 is -1. `nge[3] = -1`\
Push 10 onto the stack.

- **Move to the next element (2):**

index = 2\
element = 2\
stack = [10]

The top of the stack (10) is greater than 2. No need to pop.\
The NGE for 2 is 10. `nge[2] = 10`\
Push 2 onto the stack.

- **Move to the next element (5):**

index = 1\
element = 5\
stack = [10, 2]

Pop 2 from the stack since 2 is smaller than 5.\
The next element in stack is 10, which is greater than 5. No need to pop.\
The NGE for 5 is 10. `nge[1] = 10`\
Push 5 onto the stack.

- **Move to the last element (4):**

index = 0\
element = 4\
stack = [10, 5]

The top of the stack (5) is greater than 4. No need to pop.\
The NGE for 4 is 5. `nge[0] = 5`\
Push 4 onto the stack.

The resulting NGE array is [5, 10, 10, -1, -1]. This array represents the next greater element for each element in the original array.

### Task
- Given the implementation of NGE with some missing blank, fill the missing code.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
4 
4 5 2 25
```

**Output**

```text
5 25 25 -1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Next Greater Element Algorithm](https://www.codechef.com/learn/course/stacks-and-queues/LSTACKS02/problems/STACT10)

### [](#problem-statement-1)Problem Statement:

The algorithm typically uses a stack data structure to keep track of the elements greater than current element.

- **Initialize an empty stack**

- **Iterate through the array from right to left**: Start from the rightmost element of the array and move towards the left.

- **Pop elements from the stack**: For each element in the array, pop elements from the stack until the stack is empty or the element at the top of the stack is greater than the current array element.

- **Find the Next Greater Element (NGE)**: If the stack is empty, there is no NGE for the current element, otherwise the top of the stack is NGE for current element.

- **Push the current element**: Push the current element on the stack as it can be NGE for the remaining elements.

### [](#approach-2)Approach:

The main idea is to use a stack to help us find the Next Greater Element (NGE) for each item in the array by going through the array from the last element to the first. Here’s how it works:

- **Using a Stack**: We use a stack because it allows us to easily keep track of elements and access the most recently added item. This is useful for comparing elements.

- **Right to Left Traversal**: By starting from the end of the array and moving towards the beginning, we can easily find the NGE for each element without needing to check every subsequent element again.

- **Removing Smaller Elements**: For each element we look at, we pop (remove) any elements from the stack that are smaller than the current element. This is because they can’t be the NGE for any previous elements; we only care about elements that are greater.

- **Finding NGE**: After popping smaller elements, if there are still elements left in the stack, the top element of the stack is the NGE for the current element. If the stack is empty, it means there’s no greater element to the right, so we set the NGE to -1.

- **Storing Results**: We store the found NGE in a separate array, and once we’ve processed all elements, we print the results.

This method is efficient because it ensures that each element is pushed and popped from the stack at most once, making the solution fast and straightforward.

### [](#time-complexity-3)Time Complexity:

**O(n)**, where `n` is the number of elements in the array, as each element is pushed and popped from the stack at most once.

### [](#space-complexity-4)Space Complexity:

**O(n)**, since we are using a stack to hold elements, which in the worst case can grow to the size of the input array.

</details>
