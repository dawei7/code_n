# Longest Common Pattern

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LCPESY |
| Difficulty Rating | 1284 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [LCPESY](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/LCPESY) |

---

## Problem Statement

As we all know, Chef is cooking string for long days, his new discovery on string is the *longest common pattern length*. The *longest common pattern length* between two strings is the maximum number of characters that both strings have in common. Characters are case sensitive, that is, lower case and upper case characters are considered as different. Note that characters can repeat in a string and a character might have one or more occurrence in common between two strings. For example, if Chef has two strings **A = "Codechef"** and **B = "elfedcc"**, then the *longest common pattern length* of **A** and **B** is **5** (common characters are **c**, **d**, **e**, **e**, **f**).

Chef wants to test you with the problem described above. He will give you two strings of Latin alphabets and digits, return him the *longest common pattern length*.

### Input

The first line of the input contains an integer **T**, denoting the number of test cases. Then the description of **T** test cases follows.

The first line of each test case contains a string **A**. The next line contains another character string **B**.

### Output

For each test case, output a single line containing a single integer, the *longest common pattern length* between **A** and **B**.

### Constraints

- **1 ≤ T ≤ 100**

- **1 ≤ |A|, |B| ≤ 10000 (104)**, where **|S|** denotes the length of the string **S**

- Both of **A** and **B** can contain only alphabet characters (both lower and upper case) and digits

---

## Examples

**Example 1**

**Input**

```text
4
abcd
xyz
abcd
bcda
aabc
acaa
Codechef
elfedcc
```

**Output**

```text
0
4
3
5
```

**Explanation**

**Example case 1.** There is no common character.

**Example case 2.** All the characters are same.

**Example case 3.** Three characters (**a**, **a** and **c**) are same.

**Example case 4.** This sample is mentioned by the statement.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
abcd
xyz
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
abcd
bcda
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
aabc
acaa
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
Codechef
elfedcc
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/LCPESY)

[Contest](http://www.codechef.com/FEB14/problems/LCPESY)

**Author:** [Shiplu](http://www.codechef.com/users/shiplu)

**Tester:** [Hiroto Sekido](http://www.codechef.com/users/laycurse), [Gerald Agapov](http://www.codechef.com/users/gerald)

**Editorialist:** [Ajay K. Verma](http://www.codechef.com/users/djdolls)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

Ad-hoc

### PROBLEM:

Given two alphanumeric strings, find the number characters which occur in both of them.

### QUICK EXPLANATION:

For each string find the multiset of characters present in the string. The answer is the number of common elements in the two multisets. Since there are only 62 (26 + 26 + 10) possible characters, the multiset of characters present in a string can be represented by an integer array of size 62.

### EXPLANATION:

Since we are interested in the number of common characters present in both strings, the order in which they appear in the two strings is irrelevant. For each string one needs to find the multiset of characters which appear in it. The intersection of the two multisets will be the longest pattern. Note that in a multiset the same character may appear more than once.

Since there are only 256 possible characters, we can represent the multiset of characters present in a string by an integer array charSet of size 256, where charSet[i] represents how many times character i appear in the string. The code below computes such array for a string. Note that, even though in this problem the characters are limited to Latin alphabets and digits, for the sake of simplicity, we ignore this restriction and assume that any character can occur in the strings.

`
// Takes a string s, and computes the multiset of characters in it.
// The multiset is represented by the integer array charSet.
void computeSet(const string& s,  int* charSet) {
    for (auto c : s) {
        ++charSet[c];
    }
}
`

After we have computed the integer arrays for two strings, the number of common characters can be computed by iterating though all possible characters and checking how many occurrences of this character are common between the two strings.

`
count = 0;
for (int i = 0; i < 256; ++i)
    count += min(charSet1[i], charSet2[i]);
`

### TIME COMPLEXITY:

O (m + n),

where m and n are the lengths of the strings.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be put up soon.

Tester’s solution will be put up soon.

</details>
