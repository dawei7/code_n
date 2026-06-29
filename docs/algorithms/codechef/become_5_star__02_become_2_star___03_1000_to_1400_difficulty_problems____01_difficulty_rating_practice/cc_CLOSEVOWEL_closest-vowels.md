# Closest Vowels

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CLOSEVOWEL |
| Difficulty Rating | 1241 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CLOSEVOWEL](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CLOSEVOWEL) |

---

## Problem Statement

Chef considers a string consisting of lowercase English alphabets *beautiful* if **all** the characters of the string are **vowels**.

Chef has a string $S$ consisting of lowercase English alphabets, of length $N$. He wants to convert $S$ into a *beautiful* string $T$. In order to do so, Chef does the following operation on **every** character of the string:
- If the character is a **consonant**, change the character to its **closest vowel**.
- If the character is a **vowel**, don't change it.

Chef realizes that the final string $T$ is not unique. Chef wonders, what is the total number of **distinct** *beautiful* strings $T$ that can be obtained by performing the given operations on the string $S$.

Since the answer can be huge, print it modulo $10^9 + 7$.

Note:
- There are $26$ characters in the English alphabet. Five of these characters are vowels: `a`, `e`, `i`, `o`, and `u`. The remaining $21$ characters are consonants.
- The closest vowel to a consonant is the vowel that is least distant from that consonant. For example, the distance between the characters `d` and `e` is $1$ while the distance between the characters `d` and `a` is $3$.
- The distance between the characters `z` and `a` is $25$ and **not** $1$.

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$, denoting the length of the string $S$.
- The second line of each test case contains a string $S$ consisting of lowercase English alphabets.

---

## Output Format

For each test case, output the total number of **distinct** *beautiful* strings $T$ that can be obtained by performing the given operations on the string $S$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
5
aeiou
5
abcde
8
starters
8
codechef
```

**Output**

```text
1
2
4
4
```

**Explanation**

**Test case $1$:** All the characters of the string $S$ are **vowels**. Thus, none of the characters would be changed. The resulting string $T$ will be `aeiou`.

**Test case $2$:**There are $2$ possible strings that can be obtained by performing the given operations on the string $S$. Those are `aaaee` and `aaeee`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
aeiou
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
5
abcde
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
8
starters
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
8
codechef
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START39A/problems/CLOSEVOWEL)

[Contest Division 2](https://www.codechef.com/START39B/problems/CLOSEVOWEL)

[Contest Division 3](https://www.codechef.com/START39C/problems/CLOSEVOWEL)

[Contest Division 4](https://www.codechef.com/START39D/problems/CLOSEVOWEL)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1241

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef considers a string consisting of lowercase English alphabet *beautiful* if **all** the characters of the string are **vowels**.

Chef has a string S consisting of lowercase English alphabet, of length N. He wants to convert S into a *beautiful* string T. In order to do so, Chef does the following operation on **every** character of the string:

- If the character is a **consonant**, change the character to its **closest vowel**.

- If the character is a **vowel**, don’t change it.

Chef realizes that the final string T is not unique. Chef wonders, what is the total number of **distinct** *beautiful* strings T that can be obtained by performing the given operations on the string S.

Since the answer can be huge, print it modulo 10^9 + 7.

Note:

- There are 26 characters in the English alphabet. Five of these characters are vowels: `a`, `e`, `i`, `o`, and `u`. The remaining 21 characters are consonants.

- The closest vowel to a consonant is the vowel that is at least distant from that consonant. For example, the distance between the characters `d` and `e` is 1 while the distance between the characters `d` and `a` is 3.

- The distance between the characters `z` and `a` is 25 and **not** 1.

#
[](#explanation-5)EXPLANATION:

In this problem we need to change all the consonants to their nearest vowel. The consonants that have a unique vowel nearest to it will just have one choice, that is to change into that vowel, however for vowels that have 2 vowels at same closest distance, it will have 2 choices. Thus we just need to calculate all consonants that have 2 choices. Let us denote this by count. Then our final answer would be:

answer = 2^{count}

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/rzKX)

[Tester1’s Solution](http://p.ip.fi/7mEk)

[Tester2’s Solution](http://p.ip.fi/YEqz)

</details>
