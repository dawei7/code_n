# Smallest Numbers of Notes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOW005 |
| Difficulty Rating | 839 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [FLOW005](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/FLOW005) |

---

## Problem Statement

Consider a currency system in which there are notes of six denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
 If the sum of Rs. **N** is input, write a program to compute smallest number of notes that will combine to give Rs. **N**.

### Input

The first line contains an integer **T**, total number of testcases. Then follow **T** lines, each line contains an integer **N**.

### Output

For each test case, display the smallest number of notes that will combine to give **N**, in a new line.

### Constraints

- 1 **≤** **T** **≤** 1000

- 1 **≤** **N** **≤** 1000000

---

## Examples

**Example 1**

**Input**

```text
3 
1200
500
242
```

**Output**

```text
12
5
7
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1200
```

**Output for this case**

```text
12
```



#### Test case 2

**Input for this case**

```text
500
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
242
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Smallest Numbers of Notes Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/FLOW005)

### [](#problem-statement-1)Problem Statement:

Given a currency system with six denominations of notes: Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100, you need to find the smallest number of notes that combine to give a sum `N` for each test case.

### [](#approach-2)Approach:

- **Greedy Algorithm**:

- The approach should be greedy because we want to use the highest denomination first to minimize the total number of notes.

- Start by trying to use as many Rs. 100 notes as possible, then Rs. 50 notes, and so on, until we reach Rs. 1.

- **Steps**:

- For each test case:

- Start with the largest denomination (Rs. 100) and divide `N` by the denomination to get the maximum number of notes for that denomination.

- Subtract the equivalent amount from `N` and move to the next smaller denomination.

- Repeat until `N` becomes `0`.

- The number of notes used for each denomination should be added together to get the total number of notes for that test case.

- **Constraints**:

- Since `N` can be as large as `1,000,000`, the solution needs to be efficient. A greedy approach works in this case, as it guarantees an optimal solution.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(1)` as the loop only runs six times because of the number of elements or currency note in the array.

- **Space Complexity:** `O(1)` No extra space is needed.

</details>
