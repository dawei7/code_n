# Fancy Quotes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FANCY |
| Difficulty Rating | 1279 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [FANCY](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/FANCY) |

---

## Problem Statement

"I don't have any fancy quotes." - vijju123

Chef was reading some quotes by great people. Now, he is interested in classifying all the fancy quotes he knows. He thinks that all fancy quotes which contain the word "not" are *Real Fancy*; quotes that do not contain it are *regularly fancy*.

You are given some quotes. For each quote, you need to tell Chef if it is Real Fancy or just regularly fancy.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$ denoting a quote.

### Output
For each test case, print a single line containing the string `"Real Fancy"` or `"regularly fancy"` (without quotes).

### Constraints
- $1 \le T \le 50$
- $1 \le |S| \le 100$
- each character of $S$ is either a lowercase English letter or a space

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
i do not have any fancy quotes
when nothing goes right go left
```

**Output**

```text
Real Fancy
regularly fancy
```

**Explanation**

**Example case 1:** "i do **not** have any fancy quotes"

**Example case 2**: The word "not" does not appear in the given quote.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
i do not have any fancy quotes
```

**Output for this case**

```text
Real Fancy
```



#### Test case 2

**Input for this case**

```text
when nothing goes right go left
```

**Output for this case**

```text
regularly fancy
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/FANCY)

[Contest: Division 1](https://www.codechef.com/JAN19A/problems/FANCY)

[Contest: Division 2](https://www.codechef.com/JAN19B/problems/FANCY)

**Setter:** [Shivam Gupta](https://www.codechef.com/users/shivam_g1470)

**Tester:** [Xiuhan Wang](https://www.codechef.com/users/wxh010910)

**Editorialist:** [Taranpreet Singh](http://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

Given a string, check if it contains the word “not” as a complete word. (Not as a part of another word, like nothing)

### SUPER QUICK EXPLANATION

- The quote is Real Fancy, if the quote is “not”, quote begin with “not*”, quote ends with “*not" or quote contains “*not*” where "*” represents space character.

### EXPLANATION

Consider the special case where quote itself is “not” separately.

After this, the word “not” can either appear as the prefix, as the suffix or in between the quote. So, check separately if the first word is “not”, the last word is “not” or the quote contains the word “not”. (Make sure to check that the word “not” is surrounded by space character on both sides.)

**Trick**

Those not interested in splitting the string into words can solve this by inputting the quote as a string, add space character at both ends of strings. Now, the quote will be “Real Fancy” if it contains “*not*” where “*” represents space character.

As a side fact, [@vijju123](/u/vijju123) actually have a thing about fancy quotes. He has another fancy quote, shared during the contest, “You made my non-fancy quote a fancy one”.

### Time Complexity

Time complexity is O(|S|) per test case where |S| is the length of the quote.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/JAN19/setter/FANCY.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/JAN19/tester/FANCY.cpp)

[Editorialist’s solution](http://www.codechef.com/download/Solutions/JAN19/editorialist/FANCY.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
