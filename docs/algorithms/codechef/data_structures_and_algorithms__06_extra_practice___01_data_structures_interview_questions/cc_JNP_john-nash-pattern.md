# John Nash Pattern

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JNP |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [JNP](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_05/problems/JNP) |

---

## Problem Statement

John Nash got another secret task from William Parcher and he needs your help. John found two strings $S$ and $T$ in the newspaper. Later, he found an integer $N$ (as the registration number of his car). He needs to find out whether string $T$ is a subsequence of the string $SS...S$ ($N$ times) - string that you get when you concatenate string $S$ with itself $N$ times.

Complete the function "patternNash" in the code snippet that takes three arguments: strings $S$ and $T$ and an integer $N$. The function should return a string "YES" or "NO" - depending on whether the string $T$ is subsequence of the string $S$ concatenated $N$ times. The function will be called multiple times.

Note: Subsequence is any string that can be obtained by deleting zero or more symbols from a given string without changing their order

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two strings and an integer: $S, T, N$.

Note: You need to complete the functions in the submit solution tab:

string patternNash(string S, string T, int n){...}

---

## Output Format

For each testcase, output will be in a single line containing a single string passed by function patternNash and it should be either "YES" or "NO".

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^9$
- $1 \leq |S|, |T| \leq 10^5$
- Sum of $|S|$ and $|T|$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
aa aaa 2
abc ap 1000
codechef feh 3
```

**Output**

```text
YES
NO
YES
```

**Explanation**

In the first test case, when we concatenate "aa" and "aa" we get "aaaa". Obviously, "aaa" is subsequence of "aaaa".

In the second test case, the string "abcabcabc....abc" has no character 'p' - so the answer is no.

In the third test case, the string "codechefcodechefcodechef" has a subsequence "feh".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
aa aaa 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
abc ap 1000
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
codechef feh 3
```

**Output for this case**

```text
YES
```


