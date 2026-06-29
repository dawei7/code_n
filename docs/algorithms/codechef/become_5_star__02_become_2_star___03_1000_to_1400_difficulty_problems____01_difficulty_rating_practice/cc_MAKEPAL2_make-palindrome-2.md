# Make Palindrome 2

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEPAL2 |
| Difficulty Rating | 1393 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [MAKEPAL2](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/MAKEPAL2) |

---

## Problem Statement

You are given a binary string $S$ of length $N$. You want to obtain a [palindrome](https://en.wikipedia.org/wiki/Palindrome) from $S$ by applying the following operation **at most** $\left\lfloor \frac{N}{2} \right\rfloor$ times:
- Choose an index $i\;(1 \le i \le \lvert S \rvert)$, delete the character $S_i$ from $S$ and concatenate the remaining parts of the string. Here $\lvert S \rvert$ denotes the current length of string $S$.

For example, if $S =$ `11010`, then applying the operation on index $i=2$ makes $S=$ `1010`.

Note that after each operation, the length of the string $S$ decreases by one.

Find **any palindrome** you can obtain after the operations. It can be proved that it is always possible to obtain a palindrome from $S$ under the given constraints.

Here, $\left\lfloor \frac{N}{2} \right\rfloor$ denotes [floor division](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) of the integer $N$ by $2$. For example, $\left\lfloor \frac{5}{2} \right\rfloor = 2$, $\left\lfloor \frac{8}{2} \right\rfloor = 4$. A binary string is a string that consists of only the characters `0` and `1`.

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first line of each test case contains an integer $N$, denoting the length of the binary string $S$.
- The second line of each test case contains the binary string $S$.

---

## Output Format

For each test case, print on a separate line **any** palindromic string that can be obtained from $S$ by applying the given operation at most $\left\lfloor \frac{N}{2} \right\rfloor$ times.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $S$ contains only the characters `0` and `1`.

---

## Examples

**Example 1**

**Input**

```text
4
3
101
3
001
4
1011
6
010011
```

**Output**

```text
101
00
111
1001
```

**Explanation**

**Test case $1$:** The given string is already a palindrome.

**Test case $2$:** Applying the operation on index $i=3$ makes $S =$ `00` which is a palindrome.

**Test case $3$:** Applying the operation on index $i=2$ makes $S =$ `111` which is a palindrome.

**Test case $4$:** Applying the operation on index $i=1$ makes $S =$ `10011`. Then applying the operation on index $i=5$ makes $S =$ `1001` which is a palindrome.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
101
```

**Output for this case**

```text
101
```



#### Test case 2

**Input for this case**

```text
3
001
```

**Output for this case**

```text
00
```



#### Test case 3

**Input for this case**

```text
4
1011
```

**Output for this case**

```text
111
```



#### Test case 4

**Input for this case**

```text
6
010011
```

**Output for this case**

```text
1001
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START48/)

[Practice](https://www.codechef.com/problems/MAKEPAL2)

**Setter:** [soumyadeep_21](https://www.codechef.com/users/soumyadeep_21)

**Testers:** [tabr](https://www.codechef.com/users/tabr), [tejas10p](https://www.codechef.com/users/tejas10p)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

1393

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Calling out the main points here that are important to the solution

- We are given a binary string S of length N

- We can remove any element from the string S. We can perform this operation **at most** \left\lfloor \frac{N}{2} \right\rfloor times

- The important point is we have to output **any palindrome** that can be obtained in this manner. Kindly note - it can be any palindrome and doesnt specifically have to be a palindrome of the longest length

#
[](#explanation-5)EXPLANATION:

S is a binary string and has only **0s** and **1s**

The special constrain around removal of \left\lfloor \frac{N}{2} \right\rfloor simplifies this problem.

We just need to count the number of 0s and 1s in the original string

- If Count(1) \gt Count(0) - we can remove all the zeros and print a string containing only 1s

- If Count(0) \geq Count(1) - we can remove all the ones and print a string containing only 0s

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``t=int(input())
for _ in range(t):
    n=int(input())
    S=list(input())
    zero = S.count('0')
    one = S.count('1')
    #print(zero,one)
    if zero<one:
        i=0
        final=str()
        while i<one:
            final = final + '1'
            i=i+1
        print(final)
    if zero>=one:
        i=0
        final=str()
        while i<zero:
            final = final + '0'
            i=i+1
        print(final)
``

</details>
