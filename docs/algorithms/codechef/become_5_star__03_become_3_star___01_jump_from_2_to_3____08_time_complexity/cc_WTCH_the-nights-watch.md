# The Nights Watch

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WTCH |
| Difficulty Rating | 1441 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [WTCH](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/WTCH) |

---

## Problem Statement

There are $N$ watchtowers built in a row. Each watchtower can only accommodate one person. Some of them are already occupied by members of the Night's Watch. Since the members of the Night's Watch do not get along, no two consecutive towers can be occupied at any moment.

Arya heard that the wildlings are planning an attack. She is not satisfied by the current security, so she plans to place more members of the Night's Watch in the empty towers. What is the maximum number of people she can place in the towers such that no two consecutive towers are occupied afterwards? Note that Arya may not remove anyone from already occupied towers.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The next line contains a single string $S$ with length $N$. For each valid $i$, the $i$-th character of this string is '1' if the $i$-th watchtower is initially occupied or '0' if it is empty.

### Output
For each test case, print a single line containing one integer — the maximum number of people Arya can place in the towers.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 10^6$
- $S$ contains only characters '0' and '1'
- initially, no two consecutive towers are occupied
- the sum of $N$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (20 points):** initially, all towers are empty

**Subtask #2 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
6
010001
11
00101010000
```

**Output**

```text
1
3
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
010001
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
11
00101010000
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/WTCH)

[Contest](http://www.codechef.com/LTIME68/problems/WTCH)

**Author:** [Michael Nematollahi](http://www.codechef.com/users/watcher)

**Tester:** [Teja Vardhan Reddy](http://www.codechef.com/users/teja349)

**Editorialist:** [Michael Nematollahi](http://www.codechef.com/users/watcher)

### PREREQUISITES:

NONE

### PROBLEM:

You’re given a string consisting of characters ‘0’ and ‘1’. Initially, no two '1’s are adjacent. You should output the maximum number of '0’s that can be flipped to ‘1’ without having any two '1’s adjacent.

### QUICK EXPLANATION:

For each maximal substring consisting of only '0’s, find out its contribution to the answer.

### EXPLANATION:

First, let’s answer the first subtask.

If we have x '0’s in a row, the maximum number of them that can be flipped to ‘1’ is \lceil \frac{x}{2} \rceil. The reason is that if you group the first 2 positions together, the second 2 positions together and so on, you can flip at most one position in each group to ‘1’. This bound can be achieved by flipping the odd positions (1, 3, 5, …).

Now let’s get back to the original problem. Consider the maximal substrings of the given string that consist of only '0’s. For example, if the input string is “0101000”, these maximal substrings are “0”, “0” and “000”. It’s easy to see that we can solve the problem for these substrings independently and sum the results.

Let’s solve the problem for one of these substrings, t. If there is a ‘1’ immediately to the left of t, the first character of t is useless and cannot be flipped. Similarly, if there is a ‘1’ to the right of t, the last character of t is useless and can’t be flipped. Hence, we can reduce t's length appropriately depending on what’s to its left and right. What remains is a string consisting of only '0’s each of whose characters can be flipped. This is the same as the first subtask, and we already know how to solve it.

So we solve the problem for each of the maximal substrings and sum the results to find the answer to the original problem.

This solution runs in O(N). Refer to the setter’s solution to see the implementation.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME68/setter/WTCH.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME68/tester/WTCH.cpp).

</details>
