# Gravel

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPREAD |
| Difficulty Rating | 1822 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [SPREAD](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/SPREAD) |

---

## Problem Statement

Bob has n heap(s) of gravel (initially there are exactly c piece(s) in each). He wants to do m operation(s) with that heaps, each maybe:

- adding pieces of gravel onto the heaps from u to v, exactly k pieces for each,

- or querying "how many pieces of gravel are there in the heap p now?".

### Request

Help Bob do operations of the second type.

### Input

- The first line contains the integers n,m,c, respectively.

- m following lines, each forms:

- **S u v k** to describe an operation of the first type.

- **Q p** to describe an operation of the second type.

***(Each integer on a same line, or between the characters S, Q and the integers is separated by at least one space character)***

### Output

For each operation of the second type, output (on a single line) an integer answering to the respective query (follows the respective Input order).

### Limitations

- 0 < n <= 10 6

- 0 < m <= 250000

- 0 < u <= v <=n

- 0 <= c, k <= 10 9

- 0 < p <= n

---

## Examples

**Example 1**

**Input**

```text
7 5 0
Q 7
S 1 7 1
Q 3
S 1 3 1
Q 3
```

**Output**

```text
0
1
2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/SPREAD/)

[Contest](http://www.codechef.com/APRIL11/problems/SPREAD/)

### DIFFICULTY

EASY

### EXPLANATION

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/April/Setter/Spread.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/April/Tester/Spread.cpp).

</details>
