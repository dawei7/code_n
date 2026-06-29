# Lavanya Loves DFA

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ICM2006 |
| Difficulty Rating | 1586 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [ICM2006](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/ICM2006) |

---

## Problem Statement

There are $5$ cities in the country.

The map of the country is given below.

The tour starts from the red city.

Each road is associated with a character.

Initially, there is an empty string.

Every time a road has been travelled the character associated gets appended to the string.

At the green city either the string can be printed or the tour can be continued.

In the problem, you are given a string tell whether it is possible to print the string while following the rules of the country?

### Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains a single line of input, a string $ s  $. The string consists only of $0's$ and $1's$.

### Output:
For each testcase, output "YES" or "NO" depending on the input.

### Constraints
- $1 \leq T \leq 10000$

- $1 \leq length~of~each~string \leq 10000$

- $ 1 \leq Summation~length \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
1
100
```

**Output**

```text
NO
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Lavanya Loves DFA](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/ICM2006)

### [](#problem-statement-1)Problem Statement:

There are 5 cities in the country.

The map of the country is given below.

The tour starts from the red city.

Each road is associated with a character.

Initially, there is an empty string.

Every time a road has been travelled the character associated gets appended to the string.

At the green city either the string can be printed or the tour can be continued.

In the problem, you are given a string tell whether it is possible to print the string while following the rules of the country?

### [](#approach-2)Approach:

The problem can be represented as a graph traversal, where each city is a node and each road, associated with a character, is an edge between nodes. Starting from the red city (node 1), we move through each character in the input string, treating each character as an instruction that directs us from one city to another according to a predefined adjacency matrix. This matrix defines each city’s possible transitions based on the input character (0 or 1). For each character in the string, we update our current city based on the specified transition in the matrix. By the end of the string, if we arrive at the green city (node 5), we print `"YES"`; otherwise, `"NO"`. This solution efficiently follows the transition rules to verify if the path is valid.

### [](#time-complexity-3)Time Complexity:

O(n), where n is the length of the input string.

### [](#space-complexity-4)Space Complexity:

O(1), as we use a fixed-size `matrix` and only a few auxiliary variables.

</details>
