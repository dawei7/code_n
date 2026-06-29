# Art of Balance

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARTBALAN |
| Difficulty Rating | 1788 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [ARTBALAN](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/ARTBALAN) |

---

## Problem Statement

"Everything in the universe is balanced. Every disappointment you face in life will be balanced by something good for you! Keep going, never give up."

Let's call a string *balanced* if all characters that occur in this string occur in it the same number of times.

You are given a string $S$; this string may only contain uppercase English letters. You may perform the following operation any number of times (including zero): choose one letter in $S$ and replace it by another uppercase English letter. Note that even if the replaced letter occurs in $S$ multiple times, only the chosen occurrence of this letter is replaced.

Find the minimum number of operations required to convert the given string to a balanced string.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$.

### Output
For each test case, print a single line containing one integer ― the minimum number of operations.

### Constraints
- $1 \le T \le 10,000$
- $1 \le |S| \le 1,000,000$
- the sum of $|S|$ over all test cases does not exceed $5,000,000$
- $S$ contains only uppercase English letters

### Subtasks
**Subtask #1 (20 points):**
- $T \le 10$
- $|S| \le 18$

**Subtask #2 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
ABCB
BBC
```

**Output**

```text
1
1
```

**Explanation**

**Example case 1:** We can change 'C' to 'A'. The resulting string is "ABAB", which is a balanced string, since the number of occurrences of 'A' is equal to the number of occurrences of 'B'.

**Example case 2:** We can change 'C' to 'B' to make the string "BBB", which is a balanced string.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
ABCB
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
BBC
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ARTBALAN)

[Contest: Division 1](https://www.codechef.com/FEB19A/problems/ARTBALAN)

[Contest: Division 2](https://www.codechef.com/FEB19B/problems/ARTBALAN)

**Setter:** [Pranjal Rai](https://www.codechef.com/users/prnjl_rai)

**Tester:** [Alexey Zayakin](https://www.codechef.com/users/alex_2oo8) and [Yash Chandnani](https://www.codechef.com/users/yash_chandnani)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Easy

### PREREQUISITES:

Greedy and Basic Math would do.

### PROBLEM:

Given a string S consisting of uppercase characters only, you are to find out the minimum number of characters to change so as to make the string balanced. A string is balanced if all distinct characters present in string occur the exact same number of times.

### QUICK EXPLANATION

- In the final string, C*F = |S| where C is the number of distinct characters while F is the frequency of each character. Also, constraint 1 \leq C \leq 26 holds.

- So, We check all 26 values of C and count the maximum number of characters from the original string we can keep. It can be easily seen, that maximum characters that can be kept are \sum_1^C min(x[j], F) where x[j] denote jth greatest frequency among the set of frequencies of characters present in the initial string.

### EXPLANATION

Suppose in final string, each character occurs F times and there are C distinct characters present in the string. It can be seen that the length of such string is C*F. But we never change the length of the string. So, We need to consider only those values of C and F such that C*F = |S|. Also, we cannot have more than 26 distinct characters, so constraint 1 \leq C \leq 26 hold.

So, let’s check each value of C. If |S| \bmod C \neq 0 the string cannot be balanced using C distinct characters, so ignore such values of C. Otherwise, the balanced string shall contain |S|/C occurrences of each of distinct C characters. The question here is, who to identify which character to change?

To understand this, instead of changing the minimum number of characters, let us preserve the maximum number of characters. We can see, that we can choose any of the distinct C characters present, and preserve at most F = |S|/C occurrences of each chosen character. It makes sense to choose the characters with maximal frequencies and try to preserve maximum characters. If we sort the character frequencies in decreasing order, it can be seen that its optimal to choose first min(C, D) (D denote the number of distinct characters in initial string) characters and for each of these characters, preserve min(f, |S|/C) characters. The letters not preserved need to be replaced.

Hence, we can check for each value of C which gives the minimum number of characters to be changed and print this minimum number of characters to be changed.

### Time Complexity

The time complexity is O(|S|+A*log(A)) per test case where A = 26 is the size of the alphabet.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](https://www.codechef.com/download/Solutions/FEB19/setter/ARTBALAN.cpp)

[Tester’s solution](https://www.codechef.com/download/Solutions/FEB19/tester/ARTBALAN.cpp)

[Editorialist’s solution](https://www.codechef.com/download/Solutions/FEB19/editorialist/ARTBALAN.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
