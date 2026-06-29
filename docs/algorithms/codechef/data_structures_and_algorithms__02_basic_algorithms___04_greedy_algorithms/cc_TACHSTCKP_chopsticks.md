# Chopsticks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TACHSTCKP |
| Difficulty Rating | 1320 |
| Difficulty Band | Greedy Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Greedy Algorithms |
| Official Link | [TACHSTCKP](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA02/problems/TACHSTCKP) |

---

## Problem Statement

Actually, the two sticks in a pair of chopsticks need not be of the same length. A pair of sticks can be used to eat as long as the difference in their length is at most **D**. The Chef has **N** sticks in which the ith stick is **L[i]** units long. A stick can't be part of more than one pair of chopsticks. Help the Chef in pairing up the sticks to form the maximum number of usable pairs of chopsticks.

### Input

The first line contains two space-separated integers **N** and **D**. The next **N** lines contain one integer each, the ith line giving the value of **L[i]**.

### Output

Output a single line containing the maximum number of pairs of chopsticks the Chef can form.

### Constraints

- **1** ≤ **N** ≤ **100,000 (10 5 ) **

- **0** ≤ **D** ≤ **1,000,000,000 (10 9 ) **

- **1** ≤ **L[i]** ≤ **1,000,000,000 (10 9 )** for all integers **i** from **1** to **N**

---

## Examples

**Example 1**

**Input**

```text
5 2
1
3
3
9
4
```

**Output**

```text
2
```

**Explanation**

The 5 sticks have lengths 1, 3, 3, 9 and 4 respectively. The maximum allowed difference in the lengths of two sticks forming a pair is at most 2.
It is clear that the 4th stick (length 9) cannot be used with any other stick.
The remaining 4 sticks can can be paired as (1st and 3rd) and (2nd and 5th) to form 2 pairs of usable chopsticks.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Chopsticks in Greedy Algorithms](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA02/problems/TACHSTCKP)

### [](#problem-statement-1)Problem Statement:

Actually, the two sticks in a pair of chopsticks need not be of the same length. A pair of sticks can be used to eat as long as the difference in their length is at most D. The Chef has N sticks in which the ith stick is L[i] units long. A stick can’t be part of more than one pair of chopsticks. Help the Chef in pairing up the sticks to form the maximum number of usable pairs of chopsticks.

### [](#approach-2)Approach:

- Sort the list of chopstick lengths. This allows us to easily compare adjacent lengths to determine if they can be paired.

- Initialize a counter to keep track of the number of pairs formed.

- Iterate through the sorted list:

- For each chopstick, check if it can form a pair with the next chopstick (i.e., the difference between the lengths is less than or equal to D).

- If a pair is formed, skip the next chopstick (since a chopstick can’t be part of more than one pair), and move to another pair.

- Continue this process until all chopsticks are evaluated.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N logN)` due to sorting, and `O(N)` for the pairing process, leading to an overall complexity of `O(N logN)`.

- **Space Complexity:** `O(1)`.

</details>
