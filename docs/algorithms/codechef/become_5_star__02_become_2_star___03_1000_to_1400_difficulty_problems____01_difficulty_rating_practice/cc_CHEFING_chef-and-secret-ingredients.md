# Chef and Secret Ingredients

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFING |
| Difficulty Rating | 1376 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHEFING](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHEFING) |

---

## Problem Statement

Chef recently visited ShareChat Cafe and was highly impressed by the food. Being a food enthusiast, he decided to enquire about the ingredients of each dish.

There are $N$ dishes represented by strings $S_1, S_2, \ldots, S_N$. Each ingredient used for making dishes in ShareChat Cafe is represented by a lowercase English letter. For each valid $i$, the ingredients used to make dish $i$ correspond to characters in the string $S_i$ (note that ingredients may be used multiple times). A *special ingredient* is an ingredient which is present in each dish at least once.

Chef wants to know the number of special ingredients in ShareChat Cafe. Since Chef is too busy with work, can you help him?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains a single string $S_i$.

### Output
For each test case, print a single line containing one integer ― the number of special ingredients in the dishes.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 1,000$
- $1 \le |S_i| \le 200$ for each valid $i$
- $S_1, S_2, \ldots, S_N$ contain only lowercase English letters
- The sum of length of strings over all test cases $\le$ 3500000

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
abcaa
bcbd
bgc
3
quick
brown
fox
```

**Output**

```text
2
0
```

**Explanation**

**Example case 1:** Ingredients 'b' and 'c' are present in all three dishes, so there are two special ingredients.

**Example case 2:** No ingredient is common to all three dishes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
abcaa
bcbd
bgc
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
quick
brown
fox
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFING)

[Contest: Division 1](https://www.codechef.com/FEB19A/problems/CHEFING)

[Contest: Division 2](https://www.codechef.com/FEB19B/problems/CHEFING)

**Setter:** [Aditya Dimri](https://www.codechef.com/users/adityad1998)

**Tester:** [Alexey Zayakin](https://www.codechef.com/users/alex_2oo8) and [Yash Chandnani](https://www.codechef.com/users/yash_chandnani)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Simple.

### PREREQUISITES:

Basic Data structures.

### PROBLEM:

Given N dishes each represented by a string of lowercase characters, each character representing a different ingredient, find out the number of special ingredients. A special ingredient is an ingredient which is present in all dishes.

### QUICK EXPLANATION

- Initially, all characters are considered special.

- For every string, we can mark the characters not present in the string as non-special. Hence, the characters marked special after considering all strings are the required set of characters.

### EXPLANATION

The problem is really simple. We just need to check for each character from ‘a’ to ‘z’ whether this character is present in all strings or not.

This can be done in many ways, such as

- For each character, iterate over all strings and check if this character is present in all strings. If yes, increment the answer by one. The final value of the answer is the number of special ingredients.

- Maintain a special integer array of size A being the size of the alphabet, and for every unique occurrence of a character in the string, increase the character position in the array by one. The final answer is the number of characters, which have special array value equal to N.

The method which can be a learning experience is, by using bitmasks. Let us represent each character by a bit. Initially, all bits are set. Now, we represent each string as a bitmask, corresponding bit on for each character present in the string. Can you figure out the bitwise operation required here?

Click to view

We need to preserve only the bits which are set in both masks. This is what AND operation does.

### Time Complexity

Time complexity is O(|S|) per test case.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](https://www.codechef.com/download/Solutions/FEB19/setter/CHEFING.cpp)

[Tester’s solution](https://www.codechef.com/download/Solutions/FEB19/tester/CHEFING.cpp)

[Editorialist’s solution](https://www.codechef.com/download/Solutions/FEB19/editorialist/CHEFING.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
