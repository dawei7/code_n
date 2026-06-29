# Queue - Print Numbers with a Given Pattern

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | QUEUE05 |
| Difficulty Rating | 932 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [QUEUE05](https://www.codechef.com/learn/course/stacks-and-queues/LQUEUES/problems/QUEUE05) |

---

## Problem Statement

Let us see if you have understood 'Queues' with an implementation problem.

### Task
Write a program to print numbers in a specific pattern using a queue.\
The pattern starts with 1 and alternates between printing one number and enqueueing the next number.
The pattern follows these rules:
- Print 1.
- Enqueue 2.
- Print 3.
- Enqueue 4.
- Print 5.
- Enqueue 6.
- Print 7.
... and so on.
- Once all numbers are completed - dequeue the remaining numbers

Check the sample output below for $N = 10$.

Update the `NumberPattern` class in the IDE to solve this problem.

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

Document id and priority are unique. \
No 2 documents have the same document id or priority.

---

## Examples

**Example 1**

**Input**

```text

```

**Output**

```text
1 3 5 7 9 2 4 6 8 10
```
