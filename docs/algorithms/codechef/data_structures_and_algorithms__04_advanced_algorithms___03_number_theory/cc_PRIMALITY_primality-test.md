# Primality Test

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRIMALITY |
| Difficulty Rating | 794 |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | Sieve of Eratosthenes |
| Official Link | [PRIMALITY](https://www.codechef.com/learn/course/number-theory/LINTDSA08/problems/PRIMALITY) |

---

## Problem Statement

Alice and Bob are meeting after a long time. As usual they love to play some math games. This times Alice takes the call and decides the game. The game is very simple, Alice says out an integer and Bob has to say whether the number is prime or not. Bob as usual knows the logic but since Alice doesn't give Bob much time to think, so Bob decides to write a computer program.

Help Bob accomplish this task by writing a computer program which will calculate whether the number is prime or not .

### Input

The first line of the input contains an integer T, the number of testcases. T lines follow.

 Each of the next T lines contains an integer N which has to be tested for primality.

### Output

For each test case output in a separate line, "yes" if the number is prime else "no."

### Constraints

- 1 **≤** **T** **≤** 20

- 1 **≤** **N** **≤** 100000

---

## Examples

**Example 1**

**Input**

```text
5
23
13
20
1000
99991
```

**Output**

```text
yes
yes
no
no
yes
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
23
```

**Output for this case**

```text
yes
```



#### Test case 2

**Input for this case**

```text
13
```

**Output for this case**

```text
yes
```



#### Test case 3

**Input for this case**

```text
20
```

**Output for this case**

```text
no
```



#### Test case 4

**Input for this case**

```text
1000
```

**Output for this case**

```text
no
```



#### Test case 5

**Input for this case**

```text
99991
```

**Output for this case**

```text
yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Primality Test in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA08/problems/PRIMALITY)

### [](#problem-statement-1)Problem Statement:

Alice and Bob are playing a math game where Alice announces a number, and Bob must quickly determine if it’s prime.

### [](#approach-2)Approach:

- **See the reference**: [Sieve of Eratosthenes in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA08/problems/SIEV00)

- You initialize a boolean array `prime` where `prime[i]` will be `true` if `i` is a prime number. The algorithm iterates through each number starting from 2 and marks its multiples as non-prime.

### [](#complexity-3)Complexity:

- **Time Complexity:** The sieve runs in `O(n log ⁡log ⁡n)` time for `n=100,000`

- **Space Complexity:** The space used is `O(n)` for the prime array

</details>
