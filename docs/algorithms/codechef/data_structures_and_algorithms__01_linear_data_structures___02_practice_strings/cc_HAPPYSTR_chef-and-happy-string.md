# Chef and Happy String 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HAPPYSTR |
| Difficulty Rating | 956 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [HAPPYSTR](https://www.codechef.com/practice/course/strings/STRINGS/problems/HAPPYSTR) |

---

## Problem Statement

Chef has a string $S$ with him. Chef is happy if the string contains a **contiguous substring** of length **strictly greater** than $2$ in which all its characters are vowels.

Determine whether Chef is happy or not.

Note that, in english alphabet, vowels are `a`, `e`, `i`, `o`, and `u`.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, a string $S$.

---

## Output Format

For each test case, if Chef is happy, print `HAPPY` else print `SAD`.

You may print each character of the string in uppercase or lowercase (for example, the strings `hAppY`, `Happy`, `haPpY`, and `HAPPY` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $3 \leq |S| \leq 1000$, where $|S|$ is the length of $S$.
- $S$ will only contain lowercase English letters.

---

## Examples

**Example 1**

**Input**

```text
4
aeiou
abxy
aebcdefghij
abcdeeafg
```

**Output**

```text
Happy
Sad
Sad
Happy
```

**Explanation**

**Test case $1$:** Since the string `aeiou` is a contiguous substring and consists of all vowels and has a length $\gt 2$, Chef is happy.

**Test case $2$:** Since none of the contiguous substrings of the string consist of all vowels and have a length $\gt 2$, Chef is sad.

**Test case $3$:** Since none of the contiguous substrings of the string consist of all vowels and have a length $\gt 2$, Chef is sad.

**Test case $4$:** Since the string `eea` is a contiguous substring and consists of all vowels and has a length $\gt 2$, Chef is happy.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
aeiou
```

**Output for this case**

```text
Happy
```



#### Test case 2

**Input for this case**

```text
abxy
```

**Output for this case**

```text
Sad
```



#### Test case 3

**Input for this case**

```text
aebcdefghij
```

**Output for this case**

```text
Sad
```



#### Test case 4

**Input for this case**

```text
abcdeeafg
```

**Output for this case**

```text
Happy
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/HAPPYSTR)

[Contest: Division 1](https://www.codechef.com/START59A/problems/HAPPYSTR)

[Contest: Division 2](https://www.codechef.com/START59B/problems/HAPPYSTR)

[Contest: Division 3](https://www.codechef.com/START59C/problems/HAPPYSTR)

[Contest: Division 4](https://www.codechef.com/START59D/problems/HAPPYSTR)

***Author:*** [Mradul Bhatnagar](https://www.codechef.com/users/mradul_adm)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is happy with a string if it contains a substring of length strictly larger than 2 consisting of only vowels. Is Chef happy with string S?

#
[](#explanation-5)EXPLANATION:

If there exists a substring of length more than 2 consisting of only vowels, then there definitely exists a substring of length 3 containing only vowels: for example, just take the first 3 characters of this substring.

So, all we need to do is determine whether some substring of length 3 consists of only vowels. There are N-2 such substrings, so we can simply use a loop and check all of them.

That is, run a loop of i from 1 to N-2. For each i, check if all 3 of \{S_i, S_{i+1}, S_{i+2}\} are vowels. If this is true for any i, the answer is “Happy”. Otherwise, the answer is “Sad”.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``def count(s):
    return sum('aeiou'.count(x) for x in s) == 3
for _ in range(int(input())):
    s = input()
    print('Happy' if sum(count(s[i:i+3]) for i in range(len(s)-2)) > 0 else 'Sad')
``

</details>
