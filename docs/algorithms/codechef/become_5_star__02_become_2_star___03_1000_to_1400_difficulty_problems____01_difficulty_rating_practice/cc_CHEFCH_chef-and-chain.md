# Chef and Chain

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFCH |
| Difficulty Rating | 1332 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHEFCH](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHEFCH) |

---

## Problem Statement

Chef had a hard day and want to play little bit. The game is called "Chain". Chef has the sequence of symbols. Each symbol is either '**-**' or '**+**'. The sequence is called Chain if each two neighboring symbols of sequence are either '**-+**' or '**+-**'.

 For example sequence '**-+-+-+**' is a Chain but sequence '**-+-+--+**' is not.

 Help Chef to calculate the minimum number of symbols he need to replace (ex. '**-**' to '**+**' or '**+**' to '**-**') to receive a Chain sequence.

### Input

- First line contains single integer **T** denoting the number of test cases.

- Line of each test case contains the string **S** consisting of symbols '**-**' and '**+**'.

### Output

- For each test case, in a single line print single interger - the minimal number of symbols Chef needs to replace to receive a Chain.

### Constraints

- **1** ≤ **T** ≤ **7**

- **1** ≤ **|S|** ≤ **10^5**

### Subtasks

- Subtask **1** ≤ **|S|** ≤ **10**, **1** ≤ **T** ≤ **7** Points: 20

- Subtask **1** ≤ **|S|** ≤ **1000**, **1** ≤ **T** ≤ **7** Points: 30

- Subtask **1** ≤ **|S|** ≤ **10^5**, **1** ≤ **T** ≤ **7**Points: 50

---

## Examples

**Example 1**

**Input**

```text
2
---+-+-+++
-------
```

**Output**

```text
2
3
```

**Explanation**

**Example case 1.**

We can change symbol **2** from '**-**' to '**+**' and symbol **9** from '**+**' to '**-**' and receive '**-+-+-+-+-+**'.

**Example case 2.**

We can change symbols **2, 4 and 6** from '**-**' to '**+**' and receive '**-+-+-+-**'.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
---+-+-+++
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
-------
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFCH)

[Contest](http://www.codechef.com/FEB15/problems/CHEFCH)

**Author:** [Dmytro Berezin](http://www.codechef.com/users/berezin)

**Tester:** [Pushkar Mishra](http://www.codechef.com/users/pushkarmishra)

**Editorialist:** [Florin Chirica](http://www.codechef.com/users/elfus)

### PROBLEM

You’re given a string of + and - symbols. A string is called a chain if it does not have two or more equal characters. Our target is to convert the given string into a chain. For doing that, you can flip a character (from +  to - and vice versa) of the string. Find out minimum number of flips needed.

### QUICK EXPLANATION

We can notice that by fixing the first character, the rest of the chain is also fixed. There are two ways to fix the first character, by putting either + or -. For both of these possibilities, we can find minimum number of flips needed and take minimum of both to get our final answer.

### EXPLANATION

**Fixing first character fixes entire chain**

We can notice that by fixing the first character, the rest of the chain is also fixed.

If the first character is +, the second one *must* be -, the third one *must* be + and so on.

So, the final string will be something like +-+-+- which is a valid chain.

Similarly, we can say the same when the first character of chain is -.

**Computing minimum number of flips needed to convert a string init into a fixed chain fin**

Given two strings init and fin (init is the initial string, fin is the desired chain), the task now  becomes to compute number of positions i where init[i] \neq fin[i]. If we find such a position, we’re forced to make a flip. Otherwise, we don’t need any flip.

**Computing the final answer**

There are two possibilities for chain fin given as follows.

- +-+- \dots

- -+-+- \dots

So we can try each one of these. For each case, we can compute the number of differing position between it and the initial array as stated above.

As we have to find overall minimum number of flips needed, we can take minimum of both of these cases.

**Time Complexity**

Since computing the number of differing position between two strings of size n takes O(n) time. We do this for two cases, so the overall complexity is also O(n).

**Subtask 1 Solution**

As length of string s is very small (|s| \leq 10), we can brute-force over all possible flips in s. As each character can be either + or -, there are total 2^n possibilities which will be at max 1024 for the given n.

**Time Complexity**

We are brute-forcing over all possible 2^n strings, for a fixed string we need \mathbb{O}(n) time. So overall time required will  \mathbb{O}(2^n * n)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Tester’s solution](http://www.codechef.com/download/Solutions/FEB15/Tester1/CHEFCH.cpp)

[Setter’s solution](http://www.codechef.com/download/Solutions/FEB15/Setter/CHEFCH.cpp)

</details>
