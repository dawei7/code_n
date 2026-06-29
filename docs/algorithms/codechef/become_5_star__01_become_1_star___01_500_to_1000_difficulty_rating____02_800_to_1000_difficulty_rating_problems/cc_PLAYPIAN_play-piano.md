# Play Piano

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PLAYPIAN |
| Difficulty Rating | 980 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [PLAYPIAN](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/PLAYPIAN) |

---

## Problem Statement

Two sisters, A and B, play the piano every day. During the day, they can play in any order. That is, A might play first and then B, or it could be B first and then A. But each one of them plays the piano exactly once per day. They maintain a common log, in which they write their name whenever they play.

You are given the entries of the log, but you're not sure if it has been tampered with or not. Your task is to figure out whether these entries could be valid or not.

### Input
- The first line of the input contains an integer $T$ denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a string $s$ denoting the entries of the log.

### Output
- For each test case, output `yes` or `no` according to the answer to the problem.

### Constraints
- $1 \le T \le 500$
- $2 \le |s| \le 100$
- $|s|$ is even
- Each character of $s$ is either 'A' or 'B'

---

## Examples

**Example 1**

**Input**

```text
4
AB
ABBA
ABAABB
AA
```

**Output**

```text
yes
yes
no
no
```

**Explanation**

**Testcase 1**: There is only one day, and both A and B have played exactly once. So this is a valid log. Hence 'yes'.

**Testcase 2**: On the first day, A has played before B, and on the second day, B has played first. Hence, this is also a valid log.

**Testcase 3**: On the first day, A played before B, but on the second day, A seems to have played twice. This cannot happen, and hence this is 'no'.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
AB
```

**Output for this case**

```text
yes
```



#### Test case 2

**Input for this case**

```text
ABBA
```

**Output for this case**

```text
yes
```



#### Test case 3

**Input for this case**

```text
ABAABB
```

**Output for this case**

```text
no
```



#### Test case 4

**Input for this case**

```text
AA
```

**Output for this case**

```text
no
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Play Piano Practice Problem in](https://www.codechef.com/practice/course/python-beginner-v2-p2/BP00BP24_V2/problems/PLAYPIAN)

### [](#problem-statement-1)Problem Statement:

Two sisters, A and B, play the piano once per day, in any order. They record each session in a log, writing their name whenever they play. You are given a log and must check if it’s valid, meaning every day (pair of entries) has exactly one ‘A’ and one ‘B’.

### [](#approach-2)Approach:

To solve this problem, we need to verify if each string represents valid log entries:

- Each day will have only two entries

- Each day must consist of exactly one ‘A’ and one ‘B’, so we need to check that every consecutive pair of characters contains exactly one ‘A’ and one ‘B’.

- For each day either ‘AB’ will be valid or ‘BA’ will be valid.

- **Steps**: Iterate through the array and check if for one day the adjacent element is equal or not. If it is equal return false otherwise check for next pair.

### [](#complexity-3)Complexity:

- **Time Complexity:** O(N) N is the length of the string. We are traversing through the string length.

- **Space Complexity:** O(1) No extra space required.

</details>
