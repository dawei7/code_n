# Aggressive Cows

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAAGP1098 |
| Difficulty Rating | 932 |
| Difficulty Band | Binary Search |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to binary search |
| Official Link | [DSAAGP1098](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSAAGP1098) |

---

## Problem Statement

Farmer John has built a new long barn, with $N$ stalls. The stalls are located along a straight line at positions $x_1 ... x_N$.

His $C$ cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, Farmer John wants to assign the cows to stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Take some time to think about how you can use predicate binary search to solve this problem and then continue reading.

This problem can be broken into two parts.
- Check if keeping a certain distance $d$ he can assign a stall to each cow.
- Find the minimum $d$ so that he can assign a stall to each cow.

Let's first focus on the first part of the problem.
### Task
You are given a function $check$ with the array of positions of stalls, the size of the array $n$, the number of cows $c$, and a distance $d$. You have to return a boolean value denoting if all the cows can be assigned a stall such that the minimum distance between them is $d$ or not. The array passed in the $check$ function is **sorted**.

---

## Input Format

- The first line of input contains two space-separated integers $N$ and $K$  denoting the number of elements in the array $A$ and the element to search.
- The second line contains $N$ space-separated integers denoting the elements in the array $A$.

---

## Output Format

- Output position of $K$ or the position where $K$ is to be inserted.

---

## Constraints

- $2 \leq N \leq 10^5$
- $2 \leq C \leq N$
- $0 \leq x_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
5 3
1 2 4 8 9
```

**Output**

```text
3
```

**Explanation**

We can place three cows in the stalls at positions x = 1, x = 4, and x = 9, ensuring that the maximum gap between them is 3.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Aggressive Cows in Binary Search](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSAAGP1098)

### [](#problem-statement-1)Problem Statement:

Farmer John has built a barn with N stalls located at positions x_1, x_2, …, x_N along a straight line. He wants to place C cows in these stalls such that the **minimum distance** between any two cows is as large as possible. Your task is to determine this **largest possible minimum distance**.

In this problem we have to check if keeping a certain distance d he can assign a stall to each cow.

### [](#approach-2)Approach:

The **`check`** function is a key part of solving this problem. Its purpose is to determine if it’s possible to place **C cows** in the stalls such that the minimum distance between any two cows is at least a given distance d.

- **Place the First Cow**: Start by placing the first cow in the first stall (position `arr[0]`). This ensures we leave the largest possible space for the remaining cows.

- **Track Remaining Cows**:

- We initialize a count for the remaining cows (`cows = c - 1`) since we’ve already placed the first cow.

- We also keep track of the position of the last placed cow (`prev = arr[0]`).

- **Place the Rest of the Cows**:

- Iterate through the stalls, starting from the second one.

- For each stall, check if it’s at least `d` distance away from the last placed cow.

- If it is, place a cow there and update `prev` to the current stall’s position.

- Decrease the `cows` count after placing a cow.

- **Check if All Cows Are Placed**:

- If all cows are placed successfully (i.e., `cows == 0`), return `true`, meaning it’s possible to place the cows with at least `d` distance between them.

- **If Not All Cows Are Placed**:

- If the loop finishes and we haven’t placed all cows, return `false`, meaning it’s not possible to place the cows with that distance.

### [](#complexity-3)Complexity:

- **Time Complexity**: `O(N)` We are iterating through the array once.

- **Space Complexity**: `O(1)` We have not used extra space.

</details>
