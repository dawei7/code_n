# Area OR Perimeter

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AREAPERI |
| Difficulty Rating | 858 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [AREAPERI](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/AREAPERI) |

---

## Problem Statement

Write a program to obtain length $(L)$ and breadth $(B)$ of a rectangle and check whether its area is greater or perimeter is greater or both are equal.

---

## Input Format

- First line will contain the length $(L)$ of the rectangle.
- Second line will contain the breadth $(B)$ of the rectangle.

---

## Output Format

Output 2 lines.

In the first line print "Area" if area is greater otherwise print "Peri" and if they are equal print "Eq".(Without quotes).

In the second line print the calculated area or perimeter (whichever is greater or anyone if it is equal).

---

## Constraints

- $1 \leq L \leq 1000$
- $1 \leq B \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
1
2
```

**Output**

```text
Peri
6
```

**Explanation**

Area = 1 * 2 = 2 \
Peri = 2 * (1 + 2) = 6 \
Since Perimeter is greater than Area, hence the output is : \
Peri \
6

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Area OR Perimeter Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/AREAPERI)

### [](#problem-statement-1)Problem Statement:

Write a program to obtain length (L) and breadth (B) of a rectangle and check whether its area is greater or perimeter is greater or both are equal.

### [](#approach-2)Approach:

- **Computation**:

- Compute the area as `Area = L * B`.

- Compute the perimeter as `Perimeter = 2 * (L + B)`.

- **Comparison**:

- Compare the area with the perimeter:

- If `Area > Perimeter`, print “Area” and the value of the area.

- If `Perimeter > Area`, print “Peri” and the value of the perimeter.

- If both are equal, print “Eq” and the value.

### [](#complexity-3)Complexity:

- **Time Complexity:** The time complexity is `O(1)` since the computation involves simple arithmetic operations (multiplication and addition) which are constant-time operations.

- **Space Complexity:** The space complexity is `O(1)` as the program only uses a few variables.

</details>
