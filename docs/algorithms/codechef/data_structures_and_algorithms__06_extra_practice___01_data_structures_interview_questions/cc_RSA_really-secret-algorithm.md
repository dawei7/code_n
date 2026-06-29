# Really Secret Algorithm

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RSA |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [RSA](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_05/problems/RSA) |

---

## Problem Statement

The Chef is really into cyber security. Recently he's learning about the brand new Really Secret Algorithm. It goes like this: given a message of uppercase alphabet letters ('A'-'Z'), each letter is converted in its index (for example 'A' to 1, 'B' to 2, ..., 'Z' to 26). For example, the string "ABCZ" is encrypted into 12326.

However, there is a problem with this algorithm - there is no unique reverse algorithm, because some encryptions are not unique. For example 12326 is encryption of "ABCZ", but "ABCBF" is the valid solution as well. The Chef is interested in the number of valid messages given the encryption.

Complete the function "calculateRSA" in the code snippet that takes a single argument: a string $X$ - representing the message. The function returns an integer representing the answer to the problem. Since the solution may be large, return the solution mod $10^9+7$. The function will be called multiple times.

---

## Input Format

- First line will contain $T$, number of times the function will be called.
- Each of the next $T$ lines contains a string $X$ - representing the message

Note: You need to complete the functions in the submit solution tab:

int calculateRSA(string X){...}

---

## Output Format

For each testcase, output will be in a single line containing a single integer passed by function calculateRSA and it should be an integer modulo $10^9+7$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq |X| \leq 10^5$ - representing the length of the message $X$
- Sum of $|X|$ over all test cases does not exceed $2\cdot 10^5$
- Characters of string $X$ are digits $0-9$

---

## Examples

**Example 1**

**Input**

```text
2
123
321
```

**Output**

```text
3
2
```

**Explanation**

In the first test case the only possible solutions are: ABC, AW, LC - so the answer is 3.

In the second test case the only possible solutions are: CBA, CU - so the answer is 2.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
123
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
321
```

**Output for this case**

```text
2
```


