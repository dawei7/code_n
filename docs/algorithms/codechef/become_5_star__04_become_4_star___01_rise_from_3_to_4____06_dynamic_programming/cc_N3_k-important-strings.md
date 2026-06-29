# K-important Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | N3 |
| Difficulty Rating | 1729 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [N3](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/N3) |

---

## Problem Statement

You are given a set of N strings S0, S1, …, SN-1. These strings consist of only lower case characters a..z and have the same length L.

A string H is said to be K-important if there are at least K strings in the given set of N strings appearing at K different positions in H. These K strings need not to be distinct.

Your task is to find the shortest K-important string. If there are more than one possible solution, your program can output any of them.

### Input

The first line contains a number t (about 10) which is the number of test cases.

Each test case has the following form.

The first line contains three integers N, L and K. The next N lines contain the strings in the given set.

Each test case's input is separated by a blank line.

### Constraints

- 1 ≤ N ≤ 150

- 1 ≤ L ≤ 300

- 1 ≤ K ≤ 500

### Output

For each test case, output the following information.

The first line contains the length of the shortest K-important strings.

The second line contains H, one of the K-important strings.

Each line in the next K lines contains the index of one string in the given set that appears in H and the corresponding position (0-based) in H.

Print a blank line after each test case's output.

---

## Examples

**Example 1**

**Input**

```text
3

3 3 1
abc
cde
bcf

3 3 2
abc
cde
bcf

3 3 3
abc
cde
bcf
```

**Output**

```text
3
abc
0 0

4
abcf
0 0
2 1

7
abcfabc
0 0
2 1
0 4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [K-important Strings](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/N3)

### [](#problem-statement-1)Problem Statement -

You are given a set of N strings S0, S1, …, SN-1. These strings consist of only lower case characters a..z and have the same length L.

A string H is said to be K-important if there are at least K strings in the given set of N strings appearing at K different positions in H. These K strings need not to be distinct.

Your task is to find the shortest K-important string. If there are more than one possible solution, your program can output any of them.

### [](#approach-2)Approach

The solution involves calculating overlaps and using dynamic programming (DP) to find the shortest concatenated string.

-

Calculate the overlap between every pair of strings using the overlap function, which determines how much of one string aligns with the end of another. Store the results in the `olap` matrix.

-

Initialize the `DP` table bf[i][j], where bf[i][j] represents the shortest length of a K- important string using i+1 strings and ending with string j. Set bf[0][j]=L for all strings j.

-

For each i from 1 to K−1, compute bf[i][j] by iterating over all possible previous strings k. Calculate the new length by adding L−olap[k][j] to bf[i−1][k]. Update bf[i][j] with the minimum value and store the previous string k in the previous table for reconstruction.

-

Find the string index with the shortest length in bf[K−1][j]. Backtrack through the previous table to reconstruct the sequence of strings forming the shortest $K-$important string.

-

Compute the final concatenated string by appending parts of strings based on the overlap and print the result. Additionally, print the sequence of indices and their positions in the concatenated string.

### [](#time-complexity-3)Time Complexity

The time complexity is O(N^2 \cdot K \cdot L) due to overlap calculation and DP transitions over N strings for K iterations.

### [](#space-complexity-4)Space Complexity

The space complexity is O(N^2 + K \cdot N) to store the overlap matrix and the DP tables.

</details>
