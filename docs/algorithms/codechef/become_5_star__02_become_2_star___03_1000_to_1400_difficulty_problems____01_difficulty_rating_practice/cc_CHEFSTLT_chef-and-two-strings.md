# Chef and Two Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSTLT |
| Difficulty Rating | 1036 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CHEFSTLT](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CHEFSTLT) |

---

## Problem Statement

Chef has found two very old sheets of paper, each of which originally contained a string of lowercase Latin letters. The strings on both the sheets have equal lengths. However, since the sheets are very old, some letters have become unreadable.

Chef would like to estimate the *difference* between these strings. Let's assume that the first string is named **S1**, and the second **S2**. The unreadable symbols are specified with the question mark symbol '?'. The *difference* between the strings equals to the number of positions **i**, such that **S1i** is not equal to **S2i**, where **S1i** and **S2i** denote the symbol at the **i** the position in **S1** and **S2**, respectively.

Chef would like to know the minimal and the maximal difference between the two strings, if he changes all unreadable symbols to lowercase Latin letters. Now that you're fully aware of Chef's programming expertise, you might have guessed that he needs you help solving this problem as well. Go on, help him!

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of a test case contains a string **S1**.

The second line of a test case contains a string **S2**.

Both strings consist of lowercase Latin letters and question marks in places where the symbols are unreadable.

### Output

For each test case, output the minimal and the maximal difference between two given strings separated with a single space.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **|S1|, |S2|** ≤ **100**

- Subtask 1 (25 points): **|S1| = 1**

- Subtask 2 (10 points): neither **S1** nor **S2** contains unreadable symbols

- Subtask 3 (65 points): **1** ≤ **|S1|, |S2|** ≤ **100**

---

## Examples

**Example 1**

**Input**

```text
3
a?c
??b
???a
???a
?abac
aba?w
```

**Output**

```text
1 3
0 3
3 5
```

**Explanation**

**Example case 1**. You can change the question marks in the strings so that you obtain **S1** = abc and **S2** = abb. Then **S1** and **S2** will differ in one position. On the other hand, you can change the letters so that **S1** = abc and **S2** = bab. Then, the strings will differ in all three positions.

**Example case 2**. Change the question marks this way: **S1** = dcba, **S2** = dcba, then the strings will differ in **0** positions. You can also change the question marks so that **S1** = aaaa, **S2** = dcba, then the strings will differ in **3** positions.

**Example case 3**. Change the question marks this way: **S1** = aabac, **S2** = abaaw, then the strings will differ in **3** positions. Then, change the question marks this way: **S1** = xabac, **S2** = abayw, then they will differ in **5** positions.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
a?c
??b
```

**Output for this case**

```text
1 3
```



#### Test case 2

**Input for this case**

```text
???a
???a
```

**Output for this case**

```text
0 3
```



#### Test case 3

**Input for this case**

```text
?abac
aba?w
```

**Output for this case**

```text
3 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFSTLT)

[Contest](http://www.codechef.com/LTIME25/problems/CHEFSTLT)

**Author:** [Roman Furko](http://www.codechef.com/users/furko)

**Testers:** [Pushkar Mishra](http://www.codechef.com/users/pushkarmishra) and [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Editorialist:** [Pawel Kacprzak](http://www.codechef.com/users/pkacprzak)

**Russian Translator:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Mandarian Translator:** [Gedi Zheng](http://www.codechef.com/users/stzgd)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Implementation

### PROBLEM:

You are given two strings **S1**, **S2** with equal lengths. Both strings, on any position, can contain a lowercase latin letter or a question mark ‘?’.

A question mark can be equal to any of lowercase latin letters. We define the difference between the strings as the number of positions ***i***, such that the strings are different on this position. Your task is to compute the minimal and the maximal difference between the strings.

### QUICK EXPLANATION:

Let’s consider any position ***i*** in the strings. Since a question mark can be any letter, if at least one of the strings have a question mark on the i-th position, we can always change it to match the letter in the other string or we can always change it  to a letter which produces a mismatch. Therefore, the minimal difference is the number of positions for which none of the strings contain a question mark and there is a mismatch between them on this position. On the other hand, the maximal difference is the length of the strings reduced by the number of positions for which none of the strings contain a question mark and there is a match between them on this position.

### EXPLANATION:

We define a **strong match** as the position i, such that none of the strings contain a question mark at the i-th position, and the letters in the strings at the i-th position match.

We define a **strong mismatch** as the position i, such that none of the strings contain a question mark at the i-th position, and the letters in the strings at the i-th position do not match.

Let’s consider any position i in both strings. If at least one string contain a question mark on the i-th position, we can create a match or a mismatch between the strings at this position.

There are basically two cases to consider:

-

If only one string contains a

question mark on the i-th position.

Without loss of the generality,

let’s assume that S1[i] = ‘?’ and

S2[i] = ‘a’. Since the latin

alphabet has 26 letters, we can

produce a mismatch by setting up

S1[i] to any letter different by ‘a’

and we can produce a match by

setting up S1[i] to ‘a’.

-

Both strings contain a question mark

on the i-th position

Since the latin alphabet has 26

letters, we can produce a match by

setting up S1[i] = S2[i] = ‘a’ and

we can produce a mismatch by setting

up S1[i] = ‘a’ and S2[i] = ‘b’.

Based on these two facts, we for any position which is not a strong match or a strong mismatch, we can make it a match or a mismatch.

Therefore, the minimal difference is the number of strong mismatches. On the other hand, the maximal difference is the length of the strings reduced by the number of strong matches.

**Time complexity:**

Linear in terms of the length of input strings.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Tester](http://www.codechef.com/download/Solutions/LTIME25/Tester/CHEFSTLT.cpp)

</details>
