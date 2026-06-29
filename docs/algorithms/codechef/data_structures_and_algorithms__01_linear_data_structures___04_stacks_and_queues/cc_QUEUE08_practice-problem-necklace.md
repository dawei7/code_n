# Practice problem - Necklace

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | QUEUE08 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [QUEUE08](https://www.codechef.com/learn/course/stacks-and-queues/LQUEUES02/problems/QUEUE08) |

---

## Problem Statement

Your best friend has a very interesting necklace with $n$ pearls. On each of the pearls of the necklace there is an integer. However, your friend wants to modify the necklace a bit and asks you for help. She wants to move the first pearl $k$ spots to the left (and do so with all other pearls).

For example: if the necklace was originally $1, 5, 3, 4, 2$ and $k = 2$, now it becomes $3, 4, 2, 1, 5$.

Help your best friend determine how the necklace will look after the modification.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input, the first containing two integers $n, k$.
- The second line of each test case contains $n$ integers $a_1, a_2, ..., a_n$ representing the integers on the pearls starting from the first one.

---

## Output Format

For each testcase, output in a single line $n$ integers representing the necklace after modification.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq n \leq 10^5$
- The sum of $n$ over all test cases does not exceed $3 \cdot 10^5$
- $0 \leq k \leq n$
- $-10^9 \leq a_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
5 3
1 5 3 4 2
6 5
10 1 2 9 8 2
```

**Output**

```text
4 2 1 5 3
2 10 1 2 9 8
```

**Explanation**

The first test case is the example from the statement.
In the second test case, when we move every element 5 to the left we get the answer.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
1 5 3 4 2
```

**Output for this case**

```text
4 2 1 5 3
```



#### Test case 2

**Input for this case**

```text
6 5
10 1 2 9 8 2
```

**Output for this case**

```text
2 10 1 2 9 8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Practice problem - Necklace](https://www.codechef.com/learn/course/stacks-and-queues/LQUEUES02/problems/QUEUE08)

### [](#problem-statement-1)Problem Statement:

Your best friend has a necklace with **n** pearls, each having an integer written on it. She wants to modify the necklace by moving each pearl **k** spots to the `left`. After this modification, you need to print the new order of the pearls on the necklace.

### [](#approach-2)Approach:

The key idea of the code is to use a **queue** to efficiently simulate the rotation of the pearls. A queue allows us to easily add and remove elements from both ends.

-

We first read the number of test cases and for each test case, the number of pearls (**n**) and the number of positions (**k**) to move them.

-

We store all the pearls in a queue. This helps us manage the order of pearls effectively.

-

To rotate the pearls to the left by **k** positions, we repeatedly remove the front pearl and place it at the back of the queue for **k** iterations.

-

Finally, we print the pearls in their new order by dequeuing each pearl until the queue is empty.

### [](#time-complexity-3)Time Complexity:

The overall time complexity for each test case is **O(n + k)**, where **O(n)** accounts for inserting all **n** pearls into the queue and **O(k)** for performing **k** rotations.

### [](#space-complexity-4)Space Complexity:

**O(n)**, as we use a queue to store all **n** pearls.

</details>
