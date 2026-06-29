# Hashing Function Example

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HSH02B |
| Difficulty Rating | 932 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Hashing |
| Official Link | [HSH02B](https://www.codechef.com/learn/course/hashing/HASH01/problems/HSH02B) |

---

## Problem Statement

We can use multiple Hash Functions. \
One simple example of a Hash function is the modulo operator $\%$ (We had used this to explain how hashing works).

We can define the Hash function as $f(x) = x$ $\%$ $M$. Here $M$ is an arbitrary integer. \
The output range of this function will be $[0, M-1]$. \
So we need to choose $M$ such that we are able to index all the values from $0$ to $M-1$.

We can safety make $M$ as large as $10^6$. \
Also we will try to choose $M$ as a prime number so that the output is distributed evenly.

Let's fix $M$ as $999983$ for now - it's a prime number and is small enough to be indexed.

### Task
Run the code in the IDE and check the output.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

For each test case, output on a new line the maximum value of $A_1+A_N$ you can get after several right rotations.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
13
1000000000
342561313
1341234
523151339
```

**Output**

```text
x = 13, f(x) = 13
x = 1000000000, f(x) = 17000
x = 342561313, f(x) = 567127
x = 1341234, f(x) = 341251
x = 523151339, f(x) = 160230
```
