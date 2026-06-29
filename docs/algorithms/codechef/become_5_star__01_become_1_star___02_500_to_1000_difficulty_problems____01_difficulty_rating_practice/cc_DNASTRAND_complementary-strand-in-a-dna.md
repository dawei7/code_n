# Complementary Strand in a DNA

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DNASTRAND |
| Difficulty Rating | 660 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [DNASTRAND](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DNASTRAND) |

---

## Problem Statement

You are given the sequence of Nucleotides of one strand of DNA through a string $S$ of length $N$. $S$ contains the character $A, T, C,$ and $G$ only.

Chef knows that:
- $A$ is complementary to $T$.
- $T$ is complementary to $A$.
- $C$ is complementary to $G$.
- $G$ is complementary to $C$.

Using the string $S$, determine the sequence of the complementary strand of the DNA.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case contains an integer $N$ - denoting the length of string $S$.
- Second line contains $N$ characters denoting the string $S$.

---

## Output Format

For each test case, output the string containing $N$ characters - sequence of nucleotides of the complementary strand.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $S$ contains `A`, `T`, `C`, and `G` only

---

## Examples

**Example 1**

**Input**

```text
4
4
ATCG
4
GTCC
5
AAAAA
3
TAC
```

**Output**

```text
TAGC
CAGG
TTTTT
ATG
```

**Explanation**

**Test case $1$:** Based on the rules, the complements of `A`, `T`, `C`, and `G` are `T`, `A`, `G`, and `C` respectively. Thus, the complementary string of the given string `ATCG` is `TAGC`.

**Test case $2$:** Based on the rules, the complements of `G`, `T`, and `C` are `C`, `A`, and `G` respectively. Thus, the complementary string of the given string `GTCC` is `CAGG`.

**Test case $3$:** Based on the rules, the complement of `A` is `T`. Thus, the complementary string of the given string `AAAAA` is `TTTTT`.

**Test case $4$:** Based on the rules, the complements of `T`, `A`, and `C` are `A`, `T`, and `G` respectively. Thus, the complementary string of the given string `TAC` is `ATG`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
ATCG
```

**Output for this case**

```text
TAGC
```



#### Test case 2

**Input for this case**

```text
4
GTCC
```

**Output for this case**

```text
CAGG
```



#### Test case 3

**Input for this case**

```text
5
AAAAA
```

**Output for this case**

```text
TTTTT
```



#### Test case 4

**Input for this case**

```text
3
TAC
```

**Output for this case**

```text
ATG
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUN222A/problems/DNASTRAND)

[Contest Division 2](https://www.codechef.com/JUN222A/problems/DNASTRAND)

[Contest Division 3](https://www.codechef.com/JUN222A/problems/DNASTRAND)

[Contest Division 4](https://www.codechef.com/JUN222A/problems/DNASTRAND)

**Setter:** [daanish_adm](http://codechef.com/users/daanish_adm), [Utkarsh_25dec](https://www.codechef.com/users/Utkarsh_25dec)

**Testers:** [inov_360](https://www.codechef.com/users/inov_360), [iceknight1093](https://www.codechef.com/users/iceknight1093)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

660

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

We are given a string S of length N. The only characters in the string are ‘A’, ‘T’, ‘C’ and ‘G’. We know that A is complementary to T and T is complementary to A. Similarly, C is complementary to G and G is complementary to C.

We have to output the string that is complementary to S.

#
[](#explanation-5)EXPLANATION:

This is an implementation problem.

There are 2 lines per test case, your input acceptance needs to take this into consideration.

We start with defining an empty string S’ that is complementary to S.

We need to iterate through string S from left to right once

For each element of the string S, we check the character and append its complementary character to S’. Once we have traversed the entire string S, our complementary string S’ will be completely populated and we can output the same

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N).

#
[](#solution-7)SOLUTION:

Tester's Solution
``for _ in range(int(input())):
	n = int(input())
	s = input()
	mapping = {ord('A') : ord('T'), ord('T') : ord('A'), ord('G') : ord('C'), ord('C') : ord('G')}
	s.translate(mapping)
	print(s.translate(mapping))
``

Editorialist's Solution
``t=int(input())
for _ in range(t):
    n=int(input())
    S=str(input())
    Scomp=str()
    i=0
    while i<n:
        if S[i]=='A':
            Scomp = Scomp + 'T'
        elif S[i]=='T':
            Scomp = Scomp + 'A'
        elif S[i]=='C':
            Scomp = Scomp + 'G'
        elif S[i]=='G':
            Scomp = Scomp + 'C'
        i=i+1
    print(Scomp)
``

</details>
