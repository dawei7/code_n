# Second Max of Three Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SNDMAX |
| Difficulty Rating | 300 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [SNDMAX](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SNDMAX) |

---

## Problem Statement

### Problem Statement

Write a program that accepts sets of three numbers, and prints the *second-maximum number* among the three.

### Input

- First line contains the number of triples, **N**.

- The next **N** lines which follow each have three space separated integers.

### Output

For each of the **N** triples, output one new line which contains the second-maximum integer among the three.

### Constraints

- **1** ≤ **N** ≤ **6**

- **1** ≤ every integer ≤ **10000**

- The three integers in a single triplet are all distinct. That is, no two of them are equal.

---

## Examples

**Example 1**

**Input**

```text
3
1 2 3
10 15 5
100 999 500
```

**Output**

```text
2
10
500
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
10 15 5
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
100 999 500
```

**Output for this case**

```text
500
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Second Max of Three Numbers Practice Problem in 500 difficulty rating](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SNDMAX)

### [](#problem-statement-1)Problem Statement:

Write a program that accepts sets of three numbers, and prints the *second-maximum number* among the three.

### [](#approach-2)Approach:

- Since the three integers are distinct, sorting the list of three numbers and selecting the second element will directly give the second-largest number.

- Sorting three numbers has constant time complexity `O(1)`, making this approach efficient.

### [](#complexity-3)Complexity:

- **Time Complexity**: **Sorting the three numbers** takes constant time `O(1)`, since there are only three elements.

- **Space Complexity**: No extra space used.

</details>
