# The Optimal Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | OPTPAIRS |
| Difficulty Rating | 1666 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [OPTPAIRS](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/OPTPAIRS) |

---

## Problem Statement

For two positive integers $a$ and $b$, let $g(a, b) =$ [gcd](https://en.wikipedia.org/wiki/Greatest_common_divisor)
$(a, b) +$ [lcm](https://en.wikipedia.org/wiki/Least_common_multiple)$(a, b)$.

For a positive integer $N$, let $f(N)$ denote the **minimum** value of $g(a, b)$ over all the pairs of positive integers $(a, b)$ such that $a+b = N$.

Find out the number of **ordered** pairs $(a, b)$ such that $a+b = N$ and $g(a, b) = f(N)$.

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a positive integer $N$.

---

## Output Format

For each test case, output the number of **ordered** pairs $(a, b)$ such that $a+b = N$ and $g(a, b) = f(N)$.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
4
105
```

**Output**

```text
3
14
```

**Explanation**

**Test case $1$:**
- For the pair $(1, 3)$, $g(1, 3) = gcd(1,3)+lcm(1,3)=1+3=4$.
- For the pair $(2, 2)$, $g(2, 2) = gcd(2,2)+lcm(2,2)=2+2=4$.
- For the pair $(3, 1)$, $g(3, 1) = gcd(3,1)+lcm(3,1)=1+3=4$.

Hence, $f(4) = 4$. There are three pairs $(a, b)$ satisfying $a+b = N$ and $g(a, b) = f(N)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
105
```

**Output for this case**

```text
14
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START43A/problems/OPTPAIRS)

[Contest Division 2](https://www.codechef.com/START43B/problems/OPTPAIRS)

[Contest Division 3](https://www.codechef.com/START43C/problems/OPTPAIRS)

[Contest Division 4](https://www.codechef.com/START43D/problems/OPTPAIRS)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1666

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

For two positive integers a and b, let g(a, b) = [gcd](https://en.wikipedia.org/wiki/Greatest_common_divisor)

(a, b) + [lcm](https://en.wikipedia.org/wiki/Least_common_multiple)(a, b).

For a positive integer N, let f(N) denote the **minimum** value of g(a, b) over all the pairs of positive integers (a, b) such that a+b = N.

Find out the number of **ordered** pairs (a, b) such that a+b = N and g(a, b) = f(N).

#
[](#explanation-5)EXPLANATION:

Observation 1: For all 1 \leq a \leq N, which are factors of N,

gcd(N-a,a) = a

Proof:

By the property

gcd(A,B) = gcd(A-B,B)

We can write

gcd(N-a,a) = gcd(N-2a,a) = gcd(N-(\frac{N}{a} - 1)a) = gcd(a,a) = a

Also using the property

gcd(a,b) \times lcm(a,b) = a \times b

we get,

g(a,N-a) = a + \frac{a \times (N-a)}{a} = N

which is the minimum value we can get. To prove this let us assume a is not a factor of N.

Then g(a,N-a) = gcd(a,N-a) + \frac{a(N-a)}{gcd(a,N-a)}.

Let us assume:

L = N - g(a,N-a) \\
L = N - gcd(a,N-a) - \frac{a(N-a)}{gcd(a,N-a)}

Simplifying it we get

L = (1 - \frac{a}{gcd(a,N-a)})((N-a) - gcd(a,N-a))

Since gcd(a,b) \leq min(a,b), therefore we can see that the first term of L will always be \leq 0 while the second term will always be \geq 0, so we conclude that

L \leq 0 =\gt N \leq g(a,N-a)

Thus we can select all possible factors of N as a and b would be (N-a). This way we can find all possible pairs (a,b) that gives minimum value of g(a,b).

#
[](#time-complexity-6)TIME COMPLEXITY:

O(\sqrt{N}), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/7QtY)

[Setter’s Solution](http://p.ip.fi/bp-N)

[Tester1’s Solution](http://p.ip.fi/B344)

[Tester2’s Solution](http://p.ip.fi/uQDh)

</details>
