# Chef and his Students

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSTUD |
| Difficulty Rating | 1047 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CHEFSTUD](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CHEFSTUD) |

---

## Problem Statement

Chef is instructor of the famous course "Introduction to Algorithms" in a famous univerisity. There are **n** students in his class. There is not enough space in the class room, so students sit in a long hallway in a linear fashion.

One day Chef was late to class. As a result, some of the students have formed pairs and are talking to each other, while the others are busy studying. This information is given to you by a string **s** of length **n**, consisting of characters '*', <' and '>', where '*' denotes that the student is studying, '>' denotes that the corresponding student is talking to the student to the right, and '<' denotes that the corresponding student is talking to the student to the left.

For example, consider a sample configuration of students - ***><***. Here students numbered 1 and 4 are busy studying, while the student 2 and 3 are talking to each other. In this example, **><><**, student 1 and 2 are talking to each other, and 3 and 4 are also talking to each other. You are guaranteed that the given input is a valid configuration, i.e. **<>** can not be a valid string **s**, as here student 1 is shown to be talking to left, but there is no student to the left. Same is the case for right. Similarly, **>><<** is also not a valid configuration, as students 2 and 3 are talking to each other, so student 1 won't be able to talk to student 2.

When the students see their teacher coming, those who were talking get afraid and immediately turn around, i.e. students talking to left have now turned to the right, and the one talking to right have turned to the left. When Chef sees two students facing each other, he will assume that they were talking. A student who is busy studying will continue doing so. Chef will call each pair of students who were talking and punish them. Can you find out how many pairs of students will get punished?

For example, in case ***><***, when students see Chef, their new configuration will be ***<>***. Chef sees that no students are talking to each other. So no one is punished. While in case **><><**, the new configuration of students will be **<><>**, Chef sees that student 2 and 3 are talking to each other and they will be punished.

### Input

The first line of the input contains an integer **T** denoting the number of the test cases.

Each test case contains a string **s** denoting the activities of students before students see Chef entering the class.

### Output

For each test case, output a single integer denoting the number of pairs of students that will be punished.

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **|s|** ≤ **105**

### Subtasks

**Subtask #1: (30 points)**

- **1** ≤ **T** ≤ **10**

- **1** ≤ **|s|** ≤ **105**

- No student is studying.

**Subtask #2: (70 points)**

- Original Constraints.

---

## Examples

**Example 1**

**Input**

```text
4
><
*><*
><><
*><><><*
```

**Output**

```text
0
0
1
2
```

**Explanation**

**Example case 1.** The updated configuration will be **<>**. No students are talking to each other, so no one will be punished.

**Example case 2 and 3.** These examples are already explained in the problem statement.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
><
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
*><*
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
><><
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
*><><><*
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFSTUD)

[Contest](https://www.codechef.com/LTIME42/problems/CHEFSTUD)

**Author:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

**Tester:** [Animesh Fatehpuria](https://www.codechef.com/users/animesh_f)

**Editorialist:** [Pawel Kacprzak](https://www.codechef.com/users/pkacprzak)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

None

### PROBLEM:

For a given string S[1..N] consisting of characters ‘>’, ‘<‘ and ‘*’, the goal is to find the number of its adjacent characters S[i] and S[i+1], such that after replacing each ‘<‘ in with ‘>’ and each ‘>’ with ‘<‘ in the original string, we have S[i] = ‘>‘ and S[i+1] = ‘<‘.

### QUICK EXPLANATION:

If one pays enough attention to the statement, he can notice that each ‘>’ has corresponding ‘<‘ to its right and each ‘<‘ has corresponding ‘>’ to its left. This observation can lead to one simple solution. On the other hand, a solution not taking any advantage of this fact is also simple and possible. Both these approaches are described below.

### EXPLANATION:

**Approach 1:**

Since each ‘>’ has corresponding ‘<‘ to its right and each ‘<‘ has corresponding ‘>’ to its left in the original string, then after all swaps of characters are made, each consecutive blocks of K characters, where no character is ‘*’ will produce (K-2) / 2 adjacent pairs of characters we are looking for. As an example, let’s consider such a block of characters “><><><”. Then after swaps are made it looks like this: “<><><>” and each character with the exception of the first and the last one participates in exactly one pair of consecutive characters we are looking for.

Based on the above approach we can solve the problem as follows.

Since in the first subtask there is no ‘*’ in the input string, then the answer is (N-2) / 2, where N is the length of the input string.

In the general case, one can at the beginning split the input string into substring containing only ‘<‘ and ‘>’ characters and then compute the final answer as the sum of results for all these substrings computed in the same way as described above as the solution for the first subtask.

**Approach 2:**

Since each ‘>’ is swapped with ‘<‘ and vice versa, then we can just find the number of adjacent characters S[i] and S[i+1] in the original string for which we have S[i] = ‘<‘ and S[i] = ‘>’. This is true because after all swaps are made then each such pair corresponds to a pair that we are interested in. Moreover, on the other hand, each pair of adjacent characters we are interested in the string after all swaps are performed is formed from a pair of adjacent characters ‘<‘ and ‘>’ in the original string. This observation allows us to not perform any swap operations at all.

The second observation is that no two pairs of characters we are interested in can overlap, which is quite straightforward.

Both these two observation can lead to approach based on just counting the number of adjacent pairs of characters ‘<‘ and ‘>’ in the original string. The following pseudocode illustrates this approach:

``
    result = 0
    for i = 1 to |s| - 1
       if s[i] == ‘<‘ and s[i+1] == ‘>’:
          result += 1
    print result

``

Both these approaches runs in linear time in terms of the length of the input string.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Setter’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME42/Setter/CHEFSTUD.cpp).

Tester’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME42/Tester/CHEFSTUD.cpp).

Editorialist’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME42/Editorialist/CHEFSTUD.cpp).

</details>
