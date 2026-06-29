# Permutation and Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMPAL |
| Difficulty Rating | 1651 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [PERMPAL](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/PERMPAL) |

---

## Problem Statement

You are given a string **s** with length **n**. You should find a [permutation](https://en.wikipedia.org/wiki/Permutation) **P** of numbers 1 through **n** such that if you apply this permutation on the string **s**, you will get a [palindromic](https://en.wikipedia.org/wiki/Palindrome) string.

The result of applying a permutation **P** on the string **s** is a string **t** with length **n** such that for each **i** (1 ≤ **i** ≤ **n**), the **i**-th character of **t** is given as as **t**[**i**] = **s**[**Pi**].

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first and only line of each test case contains the string **s**.

### Output

For each test case, print a single line. If it is impossible to find a valid permutation **P**, this line should contain a single integer -1. Otherwise, it should contain **n** space-separated integers **P1, P2, ..., Pn**.

If there are multiple valid permutations, you may print any one.

### Constraints

- 1 ≤ **n** ≤ 105

- **s** will consist only of lowercase English letters (i.e. characters 'a' through 'z')

### Subtasks

**Subtask #1 (20 points)**: 1 ≤ **T**, **n** ≤ 10

**Subtask #2 (20 points)**: 1 ≤ **T**, **n** ≤ 100

**Subtask #3 (60 points)**: 1 ≤ **T** ≤ 10

---

## Examples

**Example 1**

**Input**

```text
4
aa
baa
abc
abab
```

**Output**

```text
1 2
2 1 3
-1
1 2 4 3
```

**Explanation**

**Example case 1:** The string **t** obtained using the identity permutation will have **t**[1] = **s**[1] and **t**[2] = **s**[2]. That means **t** = "aa", which is a palindrome.

**Example case 2:** The characters of the string **t** obtained by applying the permutation **2, 1, 3** are **t**[1] = **s**[2], **t**[2] = **s**[1] and **t**[3] = **s**[3]. Therefore, **t** = "aba", which is a palindrome.

**Example case 3:** There is no way to find a permutation **P** such that we can obtain a palindrome from **s** using it.

**Example case 4:** Applying the permutation **1, 2, 4, 3** on **s** results in **t** = "abba", which is a palindrome. Another permutation that you may apply is **2, 1, 3, 4**; this results in **t** = "baab", which is also a palindrome.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
aa
```

**Output for this case**

```text
1 2
```



#### Test case 2

**Input for this case**

```text
baa
```

**Output for this case**

```text
2 1 3
```



#### Test case 3

**Input for this case**

```text
abc
```

**Output for this case**

```text
-1
```



#### Test case 4

**Input for this case**

```text
abab
```

**Output for this case**

```text
1 2 4 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/PERMPAL)

[Contest](http://www.codechef.com/FEB18/problems/PERMPAL)

**Author:** [Praveen Dhinwa](http://www.codechef.com/users/admin2)

**Tester:** [Hanlin Ren](http://www.codechef.com/users/r_64)

**Editorialist:** [Hanlin Ren](http://www.codechef.com/users/r_64)

### DIFFICULTY:

SIMPLE

### PREREQUISITES:

None

### PROBLEM:

Given a string s[1\sim n], does there exist a permutation p of 1,2,\dots,n such that, if we let t[i]=s[p[i]], then t is palindrome?

### EXPLANATION:

This problem is equivalent to: can we rearrange the characters of s into a permutation?

Let’s count the number of occurrences of every characters in `a-z`. For a char c, let cnt[c] be the number of times c occur in s.

If there are two chars c_1,c_2(c_1\ne c_2) such that both cnt[c_1] and cnt[c_2] is odd, then the answer is no.

- To see this, consider any palindromic string t and any char c. Suppose t[i]=c.

- If the length n of t is even, then t[n-i+1]=c. Since n is even, n-i+1 and i has different parity and hence i\ne n-i+1. Also n-(n-i+1)+1=i, so we say i and n-i+1 is a pair. Any pair must use the same character, so any character must occur an even number of times.

- If the length n of t is odd, the above argument holds, too, except that the central char(t[\frac{n+1}{2}]) is matched with itself. In this case, this char appears an odd number of times, and is the only char that appears an odd number of times.

- See figure below. n=7, pairs are (1,7),(2,6),(3,5), and t[4] is matched with itself, and hence appears an odd number of times.

- In conclusion, if C is the number of chars c that cnt[c] is odd, and s can be arranged into a palindrome, then C\le 1.

The converse is also true: if there are at most 1 characters c with cnt[c] odd, then the answer is yes. Here is **one of** the constructions.

- Let’s construct the permutation char-by-char. Let c iterate from `a` to `z`.

- If cnt[c] is odd, we ignore c(that is, we consider c later). At most one such c exists.

- We maintain two pointers l and r. Initially l=0,r=n+1. The permutation p[1\sim l] and p[r\sim n] is already filled.

- We scan s. Each time we meet a c, say t[i]=c,

- if this is the 1,3,5,\dots,(odd) time we meet c, we assign it to the left: l\gets l+1 and p[l]\gets i;

- otherwise (this is the 2,4,6,\dots time we meet c), we assign it to the right: r\gets r-1 and p[r]\gets i.

- The picture below shows how we fill p when s=`abdacbabdccba`, i=`b`.

- At last, in case that n is odd, we need to deal with the c where cnt[c] is odd. That’s easy: p[l+1\sim r-1] is unfilled, and we fill them by char c.

- This is a valid answer. Time complexity: O(\sigma\cdot n). (\sigma=26)

### ALTERNATIVE SOLUTIONS

This is a constructive problem. I think there’ll be many solutions. **Please feel free to share your solution.**

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/FEB18/Setter/PERMPAL.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/FEB18/Tester/PERMPAL.cpp).

</details>
