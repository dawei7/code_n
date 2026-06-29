# Anti Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ANTIPALINDR |
| Difficulty Rating | 1488 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [ANTIPALINDR](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/ANTIPALINDR) |

---

## Problem Statement

**Definitions:**

A string $T$ is called **semi-palindrome** if you can rearrange the characters of $T$ to make it into a [palindrome](https://en.wikipedia.org/wiki/Palindrome).\
For eg. if $T = aabb$, it isn't a palindrome as of now, but it can be rearranged to form $abba$, which is a palindrome. Thus, $T = aabb$ is a semi-palindrome.

An **anti-palindrome** is the opposite of a semi-palindrome. In particular, a string $T$ is called an anti-palindrome if it is not possible to rearrange the characters of $T$ to make it into a palindrome.\
For eg. if $T = abc$, there is no rearrangement of this string which makes it into a palindrome. Hence, $T = abc$ is an anti-palindrome.

---
Now on to the problem:

You are given a string $S = S_1S_2 \ldots S_N$ consisting of $N$ english lowercase letters.

Your aim is to convert $S$ into an anti-palindrome. For this, you are allowed to do the following operation as many times as you want (even 0 times) :
- Select an index $i$ $(1 \leq i \leq N)$ and change $S_i$ to any other english lowercase letter.

Find the minimum number of operations needed to make $S$ into an anti-palindrome.

**Note:** It can be proven that for the given constraints ($2 \leq N \leq 10^5$), it is always possible to make $S$ into an anti-palindrome using the operations.

---

## Input Format

- The first line of input will contain a single integer $C$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the length of the string $S$.
    - The next line contains the string $S$ of length $N$.

---

## Output Format

For each test case, output the minimum number of operations needed to make $S$ into an anti-palindrome.

---

## Constraints

- $1 \leq C \leq 5 \cdot 10^5$
- $2 \leq N \leq 10^5$
- $S$ contains only english lowercase letters.
- The sum of $N$ over all testcases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
5
2
ab
2
aa
3
abc
3
aaa
3
abb
```

**Output**

```text
0
1
0
2
1
```

**Explanation**

**Testcase 1:** The given string $ab$ is already an anti-palindrome, since there is no way to rearrange the letters to make it into a palindrome. So, we don't need to do any operations on it to make it an anti-palindrome. Hence the answer is $0$.

**Testcase 2:** The given string $aa$ is a palindrome, and so it is not an anti-palindrome. We can change it to $ab$ using $1$ operation, and it becomes an anti-palindrome. Hence the answer is $1$.

**Testcase 3:** The given string $abc$ is already an anti-palindrome, since there is no way to rearrange the letters to make it into a palindrome. So, we don't need to do any operations on it to make it an anti-palindrome. Hence the answer is $0$.

**Testcase 4:** The given string $aaa$ is a palindrome, and so it is not an anti-palindrome. We can change it to $abc$ using $2$ operations, and it becomes an anti-palindrome. There is no way to make it into an anti-palindrome using only 1 operation. Hence the answer is $2$.

**Testcase 5:** The given string $abb$ is a semi-palindrome, since it can be rearranged to form $bab$ which is a palindrome. So $abb$ is not an anti-palindrome. We can change it to $abc$ using $1$ operation, and it becomes an anti-palindrome. Hence the answer is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
ab
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
aa
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
abc
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
3
aaa
```

**Output for this case**

```text
2
```



#### Test case 5

**Input for this case**

```text
3
abb
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ANTIPALINDR)

[Contest: Division 1](https://www.codechef.com/START90A/problems/ANTIPALINDR)

[Contest: Division 2](https://www.codechef.com/START90B/problems/ANTIPALINDR)

[Contest: Division 3](https://www.codechef.com/START90C/problems/ANTIPALINDR)

[Contest: Division 4](https://www.codechef.com/START90D/problems/ANTIPALINDR)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Tester:*** [udhav2003](https://www.codechef.com/users/udhav2003)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1488

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You’re given a string S of length N. In one move, you can replace one of its characters with any other lowercase Latin letter.

Find the minimum number of moves required to make S an anti-palindrome, i.e, no rearrangement of S is a palindrome.

#
[](#explanation-5)EXPLANATION:

First, let’s check whether S is itself an anti-palindrome, in which case the answer will be 0.

To do this, we need to check whether S can be rearranged into a palindrome.

Checking for this is somewhat well-known, and can be done as follows:

- If N is even, then S can be rearranged to form a palindrome if and only if every character appears an even number of times.

- If N is odd, S can be rearranged to form a palindrome if and only if exactly one character appears an odd number of times; and everything else appears an even number of times.

Proof

Let’s prove the even case first. It should be fairly obvious if you think about it a bit.

If S can be rearranged into a palindrome, then every element of S has an opposite ‘pair’ element in this rearrangement.

This means each character appears an even number of times in total, as claimed.

On the other hand, if every character appears an even number of times, we can then pair up copies of the same character and use them to form a palindrome by placing them at opposing sides of the string.

The odd case is similar: there’s a unique ‘middle’ character which accounts for the odd frequency because everything else is paired up; but the proof is otherwise the same.

So, check if S satisfies the respective condition for its parity; if it doesn’t, the answer is of course 0.

What about the case when S does satisfy those conditions, i.e, can be rearranged into a palindrome?

Let’s analyze what we can change.

- If N is even, we know every character occurs an even number of times.

just replace any character of S with any *other* character; and both the new and the old character will now have an odd frequency.

So, the answer in this case is 1

- If N is odd, we need slightly more casework.

Exactly one character has an odd frequency; let it be \alpha. Then,

- If S has some character that’s *not* \alpha, then one move is enough.

Replace a non-\alpha character with another different non-\alpha character, now there are three characters with odd occurrences.

- If S consists of *only* the letter \alpha repeated N times, the answer is 2: replacing one occurrence of \alpha with something else isn’t enough (since the new character will have odd frequency but \alpha will be even).

However, after one replacement we’ll be back in the first case; and from there we know the answer is 1.

Putting it together, we have the following cases:

- If S is already an anti-palindrome, the answer is 0.

- Otherwise,

- If N is even, the answer is 1.

- If N is odd and S contains at least two distinct characters, the answer is 1.

- Else, the answer is 2.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    freq = Counter(s)
    odds = 0
    for x in freq.values(): odds += x%2
    if n%2 == 0:
        if odds == 0: print(1)
        else: print(0)
    else:
        if len(freq) == 1: print(2)
        elif odds == 1: print(1)
        else: print(0)
``

</details>
