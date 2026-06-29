# Easy Pronunciation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EZSPEAK |
| Difficulty Rating | 1000 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [EZSPEAK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/EZSPEAK) |

---

## Problem Statement

*Words that contain many consecutive consonants, like "`schtschurowskia`", are generally considered somewhat hard to pronounce.*

We say that a word is *hard to pronounce* if it contains $4$ or more consonants in a row; otherwise it is *easy to pronounce*. For example, "apple" and "polish" are easy to pronounce, but "schtschurowskia" is hard to pronounce.

You are given a string $S$ consisting of $N$ lowercase Latin characters. Determine whether it is easy to pronounce or not based on the rule above — print `YES` if it is easy to pronounce and `NO` otherwise.

For the purposes of this problem, the vowels are the characters $\{a, e, i, o, u\}$ and the consonants are the other $21$ characters.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, the length of string $S$.
    - The second line of each test case contains the string $S$.

---

## Output Format

For each test case, output on a new line the answer — `YES` if $S$ is easy to pronounce, and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase. For example, the strings `YES`, `yeS`, `yes`, and `YeS` will all be treated as identical.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $S$ contains only lowercase Latin characters, i.e, the characters $\{a, b, c, \ldots, z\}$

---

## Examples

**Example 1**

**Input**

```text
5
5
apple
15
schtschurowskia
6
polish
5
tryst
3
cry
```

**Output**

```text
YES
NO
YES
NO
YES
```

**Explanation**

**Test case $1$:** "$\text{apple}$" doesn't have $4$ or move consecutive consonants, which makes it easy to pronounce.

**Test case $2$:** "$\text{\textcolor{red}{schtsch}urowskia}$" has $7$ consecutive consonants, which makes it hard to pronounce.

**Test case $3$:** $\text{polish}$ doesn't contain $4$ or more consecutive consonants, so it's easy to pronounce.

**Test case $4$:** $\text{\textcolor{red}{tryst}}$ contains $5$ consecutive consonants, making it hard to pronounce.

**Test case $5$:** $\text{cry}$ doesn't contain any vowels, but its length is less than $4$ so it's still easy to pronounce.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
apple
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
15
schtschurowskia
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
6
polish
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
5
tryst
```

**Output for this case**

```text
NO
```



#### Test case 5

**Input for this case**

```text
3
cry
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/LTIME110/)

[Practice](https://www.codechef.com/problems/EZSPEAK)

**Setter:** [iceknight1093](https://www.codechef.com/users/iceknight1093)

**Testers:** [gamegame](https://www.codechef.com/users/gamegame)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

# [](#difficulty-2)DIFFICULTY:

1000

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You are given a string S consisting of N lowercase Latin characters. Determine whether it is easy to pronounce or not based on the rule given — print `YES` if it is easy to pronounce and `NO` otherwise. The rule is we say that a word is *hard to pronounce* if it contains 4 or more consonants in a row; otherwise it is *easy to pronounce*.

# [](#explanation-5)EXPLANATION:

We need to run a loop through the given string and maintain a counter - ‘count’

- If any of its elements is either of **‘a’, ‘e’, ‘i’, ‘o’, ‘u’**, then we keep the value of count as 0

- If any of its elements is a consonant, then we increment the counter as count = count + 1

- If the value of count rises to 4 - then it means there are 4 consecutive consonants. We can exit the loop and output ‘NO’ as this string is hard to pronounce.

- IF the value of count never reaches 4 - then it means the string is easy to pronounce

# [](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N), Where N is the length of string.

# [](#solution-7)SOLUTION:

Editorialist's Solution
``t=int(input())
for _ in range(t):
    n=int(input())
    s=str(input())
    i=0
    count=0
    while i<n:
        if s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='i' or s[i]=='u':
            count=0
        else:
            count=count+1
        if count==4:
            break
        i=i+1
    if count==4:
        print('NO')
    else:
        print('YES')
``

</details>
