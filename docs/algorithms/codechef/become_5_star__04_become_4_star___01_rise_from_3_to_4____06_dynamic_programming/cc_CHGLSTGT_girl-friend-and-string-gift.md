# Girl Friend and String Gift

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHGLSTGT |
| Difficulty Rating | 1986 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [CHGLSTGT](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/CHGLSTGT) |

---

## Problem Statement

###  Read problems statements in Russian [here](https://www.codechef.com/download/translated/LTIME05/russian/CHGLSTGT.pdf)

Chef's Girl Friend has given him a unique gift. She has given him a string **S**. Chef being a gentleman wants to return her gift in a unique way. He wants to break the string he has received into some number of substrings so that each substring is a palindrome. However he does not want break the string into too many substrings, otherwise the average size of his strings will become small. What is the minimum number of substrings in which the given string can be broken so that each substring is a palindrome.

### Tips:

Refer [http://en.wikipedia.org/wiki/Palindrome](http://en.wikipedia.org/wiki/Palindrome) for the definition of a "palindrome"

### Input

Input description.

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows:

- The first line of each test case contains a single integer **N** denoting the number of alphabets in the given string. The second line contains the given string.

### Output

For each test case output a single integer the answer to the given test case. Print answer for each test case on a separate line.

### Constraints

All characters in the given string are upper case English alphabets.

- **1** ≤ **T** ≤ **10**

- **1** ≤ **|S|** ≤ **5000**

###  Scoring

 ** Subtask 1: (15 points):**

- **1** ≤ **|S|** ≤ **20**

 ** Subtask 2: (25 points):**

- **1** ≤ **|S|** ≤ **250**

 ** Subtask 1: (60 points):**

- **1** ≤ **|S|** ≤ **5000**

---

## Examples

**Example 1**

**Input**

```text
1 
7
ABCCBDA
```

**Output**

```text
4
```

**Explanation**

**Example case 1.** The given string can be broken into **"A" , "BCCB" , "D" , "A"**. It can be verified that you can't break the given string into less than 4 substrings such that each substring in a palindrome.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/CHGLSTGT)

[Contest](http://www.codechef.com/LTIME05/problems/CHGLSTGT)

**Author** and **Editorialist** [Vineet Paliwal](http://www.codechef.com/users/vineetpaliwal)

**Tester** [Roman Rubanenko](http://www.codechef.com/users/rubanenko)

# Difficulty:

Simple

# PREREQUISITES :

Dynamic Programming , Strings , Palindromes

# PROBLEM :

Given a string , what is the minimum number of substrings in which you can break the given string so that each substring is a palindrome .

# EXPLANATION:

### The Naive Solution :

Consider all possible ways of breaking the string into substrings . This number of ways will be exponential and hence only one subtask can be solved using this .

### Using Dynamic Programming :

Let dp[i] denote the minimum number of partitions for breaking the the first i characters of the string into palindromes .

Then for a given i , dp[i] = min of dp[j] + 1 ( if string[j+1 … i] is a palindrome , j belongs to { 0 … i }) .

This gives an O(n^3) solution .

However we can precompute whether string[a…b] is a palindrome or not by dynamic programming again reducing the overall complexity to O(n^2) .

isPalindrome(a,b) = true if string[a] = string[b] and isPalindrome(a+1,b-1) otherwise false .

Note : Please take care of boundary conditions while using recursive formula for isPalindrome and dp.

# Solutions:

[Setter’s Solution](http://www.codechef.com/download/Solutions/LTIME05/Setter/CHGLSTGT.java)

[Tester’s Solution](http://www.codechef.com/download/Solutions/LTIME05/Tester/CHGLSTGT.cpp)

</details>
