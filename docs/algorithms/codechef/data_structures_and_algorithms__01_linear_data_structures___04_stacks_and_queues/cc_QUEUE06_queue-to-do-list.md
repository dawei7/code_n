# Queue - To do list

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | QUEUE06 |
| Difficulty Rating | 932 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [QUEUE06](https://www.codechef.com/learn/course/stacks-and-queues/LQUEUES/problems/QUEUE06) |

---

## Problem Statement

Create a program that simulates a to-do list manager using a queue. \
The program should allow users to perform the following operations:
- Add a task to the to-do list.
- If the task is already present in the list - then ignore the task
- Display the current to-do list once all tasks have been added

The code given here has implemented queues using arrays. \
Update the code to solve the problem.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of documents to be printed.
- Following this are $T$ lines - Each line consists of a string displaying the document id and an integer denoting the priority. \
The string and the integer are space separated

---

## Output Format

Output the sequence in which the document ids will be printed.

---

## Constraints

There are a maximum of 10 tasks in the input.

---

## Examples

**Example 1**

**Input**

```text
1
2
4
5
1
2
3
9
4
9
```

**Output**

```text
1
2
4
5
3
9
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Queue - To do list](https://www.codechef.com/learn/course/stacks-and-queues/LQUEUES/problems/QUEUE06)

### [](#problem-statement-1)Problem Statement:

Create a program that simulates a to-do list manager using a queue.

The program should allow users to perform the following operations:

- Add a task to the to-do list.

- If the task is already present in the list - then ignore the task

- Display the current to-do list once all tasks have been added

The code given here has implemented queues using arrays.

Update the code to solve the problem.

### [](#approach-2)Approach:

The main idea is to manage a to-do list using a queue structure, where tasks are added only if they do not already exist in the list. A separate array tracks the current tasks in the list, while the queue stores and processes the tasks. The queue follows a circular structure, ensuring that both insertion and deletion are handled efficiently.

**`addTask(int task)`**:

-

This function adds a new task to the list if it is not already present.

-

It first checks if the current number of tasks (`taskListsize`) is less than the maximum size of the queue (`maxSize`).

-

Then, it loops through the `taskList` to ensure that the task does not already exist. If the task is already present, it skips adding the task.

-

If the task is not found, it enqueues the task using the `enqueue` function and adds it to the `taskList`. The `taskListsize` is incremented to track the number of tasks.

### [](#time-complexity-3)Time Complexity:

-

**`enqueue` and `dequeue` operations**: Both take constant time, **O(1)**.

-

**`addTask` function**: Takes **O(n)** time, where `n` is the current number of tasks, as it checks for duplicates in the task list

</details>
