# Hussain Set

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COOK82C |
| Difficulty Rating | 2608 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Standard Template Library |
| Official Link | [COOK82C](https://www.codechef.com/practice/course/2to3stars/LP2TO304/problems/COOK82C) |

---

## Problem Statement

Hussain is very bored, and has a lot of exams lined up next week. But he doesn't want to study. As usual, he decided to fail his exams and play with Hasan instead (who has already failed). Hussain invented this new game to play with Hasan.

Hussain shows Hasan a multiset of integers. (A multiset is a collection of elements where there can be duplicates). In every move Hussain removes a maximum number from this multiset and divides it by 2 (integer division, which is rounded down).

If after dividing, the number is still positive (greater than 0) he re-inserts it back into the multiset.

Before the start of the game, Hussain shows Hasan the numbers in his multiset.

Hussain asks Hasan, **M** questions. The **i-th** question will be denoted by **Q[i]**, and Hasan must find the value of the number Hussain will be dividing (before he performs the division) after **Q[i]**-1 moves. That is, what is the value of the number on which the **Q[i]**-th division is performed?

Can you help Hasan and answer the queries?

### Input

- The first line contains 2 space separated integers **N, M** denoting the initial size of the multiset and the number of questions respectively.

- The next line contains **N** space separated integers, the initial elements of the multiset.

- Of the next **M** lines, the **i-th** line will contain **Q[i]**.

### Output

- Output **M** lines, the i-th of which contains the answer for the i-th query.

### Constraints

- 1 ≤ **N, M** ≤ 106

- The queries are given in chronological order. That is, ** Q[i] > Q[i-1] **

- Every element of the multiset will be a positive integer less than 263

- It's guaranteed that the set will contain at least one element at the time of any query.

---

## Examples

**Example 1**

**Input**

```text
4 6
8 5 3 1
1
2
3
4
6
8
```

**Output**

```text
8
5
4
3
2
1
```

**Explanation**

We show the multiset sorted at each step, for convenience.

- Before any move, the multiset is (8, 5, 3, 1).

- In the first move, 8 is removed, dived by 2, and thus becomes 4, and then re-inserted. So, the multiset, after the first move is (5, 4, 3, 1).

- In the second move, 5 is removed and after division, it become 2, which is re-inserted. The multiset becomes (4, 3, 2, 1).

- After the third move, the multiset becomes (3, 2, 2, 1).

- After the fourth move, it becomes (2, 2, 1, 1).

- After the fifth move, it becomes (2, 1, 1, 1).

- After the sixth move, it becomes (1, 1, 1, 1).

- In the seventh move, 1 is removed, and on division, it no longer is greater than 0. Hence, it is not re-inserted. So, after the seventh move, the multiset becomes (1, 1, 1).

- After the eight move, the multiset becomes (1, 1).

The value being divided on the first move is 8. Hence the first output is 8.

The value being divided on the first move is 5. Hence the first output is 5.

The value being divided on the eight move is 1. Hence the last output is 1.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COOK82C)

[Contest](https://www.codechef.com/COOK82/problems/COOK82C)

**Author:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

**Primary Tester:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Secondary Tester:** [Istvan Nagi](https://www.codechef.com/users/iscsi)

**Editorialist:** [Udit Sanghi](https://www.codechef.com/users/mathecodician)

### DIFFICULTY:

EASY-Medium

### PREREQUISITES:

Queue

### PROBLEM:

Given an array of numbers and m queries. You have the keep doing the following operation -

Divide the take the maximum number and divide it by 2. Now for each query, tell the number we were taking in the Q[i]th operation

### QUICK EXPLANATION:

Take 2 queues, q1 and q2. Push all elements in decreasing order to q1. Now as you are taking the elements see the maximum of q1 and q2, store it and then divide it by 2 and push it in q2. When q1 becomes empty then only look at q2.

### EXPLANATION:

First let’s calculate the constraint on Q[i]. So a[i] < 2^{63}. This means that at most an element will can be divided 63 times before reaching 0. And, there are totally 10^6 items. That means that Q[i] will be at max 63(10^6).

First of all, can u think of a brute-force solution.

Just keep doing all stuff manually like taking the maximum in an array and then dividing it by 2 and putting in the array again. This will take time O(n*6.3*{10^6}).

Now, can we do better.

So taking the max right now takes O(n). We can reduce this to O(log n) by using a priority_queue.

Now the complexity will be This will take time O(logN*6.3*{10^6}).

Hmm… Too slow. We need to do this operation in constant time.

Here’s a key observation -

``After every number has been once divided, you only need to divide the numbers again in the same order as before. So, currently it doesn't make much sense but it will once you see an example.
Before that, you only need to compare between the highest number which has been divided yet and which has not been divided yet.

n = 5
old_a = [28,25,17,14,13]
new_a = []
// old array contains the element which have not yet been divided yet and new array contains those which have been divided atleast once.
operation 1 - 28
old_a = [25,17,14,13]
new_a = [14]

operation 2 - 25
old_a = [17,14,13]
new_a = [14,12]

operation 3 - 17
old_a = [14,13]
new_a = [14,12,8]

operation 4 - 14
old_a = [13]
new_a = [14,12,8,7]

operation 5 - 14
old_a = [13]
new_a = [12,8,7,7]

operation 6 - 13
old_a = []
new_a = [12,8,7,7,6]

// Now you will realize that we only select [12,8,7,7,6] in order now and keep dividing them.
Like 12,8,7,7,6,12/2,8/2,7/2,7/2,6/2,(12/2)/2,(8/2)/2 etc.
``

For these purposes we can use a queue.

Make 2 queue, q1 and q2.

Push all elements in q1 in decreasing order.

Now for the first operation u’ll choose the maximum element which is the front of q1 and push half of that number in q2.

After that, you’'l have 2 queues to choose from q1,q2, choose the queue which has has the maximum element and keep repeating this until… q1 is empty.

Then, you can just repeat the process with the elements of q2.

Remember to store the answer after each operation. Then, process the queries and answer the queries with the answers you stored.

### EDITORIALIST’s, AUTHOR’S AND TESTER’S SOLUTIONS:

**EDITORIALIST’s solution**: [Here] [333](https://pastebin.com/XH2FmNPw)

**AUTHOR’s solution**:  [Here] [444](http://www.codechef.com/download/Solutions/COOK82/Setter/COOK82C.cpp)

**TESTER’s solution**: [Here] [555](http://www.codechef.com/download/Solutions/COOK82/Tester1/COOK82C.cpp)

</details>
