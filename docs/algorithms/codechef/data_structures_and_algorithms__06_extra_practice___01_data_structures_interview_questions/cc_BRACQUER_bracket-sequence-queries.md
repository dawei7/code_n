# Bracket Sequence Queries

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BRACQUER |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [BRACQUER](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/BRACQUER) |

---

## Problem Statement

A string consisting only of parentheses '(' and ')' is called a bracket sequence. Some bracket sequences are called correct bracket sequences. More formally:

- An empty string is a correct bracket sequence.

- If a string $S$ is a correct bracket sequence, then the string $(S)$ is also a correct bracket sequence.

- If strings $S$ and $T$ are correct bracket sequences, then the string $ST$ is also correct bracket sequence.

You are given a bracket sequence $S$. You have to answer $Q$ queries. In each query, you are given two integers $L$ and $R$ ($L \leq R$) which denote the substring of $S$ from position $L$ to position $R$, which we will call $S_{L,R}$. You need to find the length of the longest substring of $S_{L,R}$ which is a correct bracket sequence.

A substring is a contiguous sequence of characters within a string.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single string $S$.

- The second line of each test case contains a single integer $Q$.

- $Q$ lines follow. The $i$-th of these lines contains two space-separated integers $L_i$ and $R_i$.

---

## Output Format

- For each test case, print a single line containing $Q$ space-separated integers. The $i$-th of these integers should be the length of the longest correct bracket substring of the substring of $S$ that is given in the $i$-th query.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |S| \leq 5 \cdot 10^{3}$
- $1 \leq Q \leq 2 \cdot 10^{5}$
- the sum of $|S|$ over all test cases does not exceed $5 \cdot 10^{3}$
- the sum of $Q$ over all test cases does not exceed $2 \cdot 10^{5}$
- $1 \leq L_i \leq R_i \leq |S|$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
2
()))
3
1 4
1 2
3 3
((())()
3
1 7
5 7
1 6
```

**Output**

```text
2 2 0
6 2 4
```

**Explanation**

**Example case 1:** The longest correct bracket substring of $S_{1,4}$ is '()'.

**Example case 2:** The longest correct bracket substring of $S_{1,2}$ is '()'.

**Example case 3:** The longest correct bracket substring of $S_{3,3}$ is the empty bracket sequence.

**Example case 4:** The longest correct bracket substring of $S_{1,7}$ is '(())()'.

**Example case 5:** The longest correct bracket substring of $S_{5,7}$ is '()'.

**Example case 6:** The longest correct bracket substring of $S_{1,6}$ is '(())'.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
()))
3
1 4
1 2
3 3
```

**Output for this case**

```text
2 2 0
```



#### Test case 2

**Input for this case**

```text
((())()
3
1 7
5 7
1 6
```

**Output for this case**

```text
6 2 4
```



**Example 2**

**Input**

```text
1
())()
3
1 5
3 4
1 4
```

**Output**

```text
2 0 2
```

**Explanation**

**Example case 1:** The longest correct bracket substring of $S_{1,5}$ is '()'. A subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements. Note that the longest correct bracket subsequence would be '()()', however, we are interested in substrings, not subsequences.

**Example case 2:** The longest correct bracket substring of $S_{3,4}$ is the empty bracket sequence.

**Example case 3:** The longest correct bracket substring of $S_{1,4}$ is '()'.
