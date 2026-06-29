# Cool Guys

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COOLGUYS |
| Difficulty Rating | 1758 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [COOLGUYS](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/COOLGUYS) |

---

## Problem Statement

Given an integer **N**. Integers **A** and **B** are chosen randomly in the range **[1..N]**. Calculate the probability that the Greatest Common Divisor(GCD) of **A** and **B** equals to **B**.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. Each test case consists of a single integer **N** on a separate line.

### Output
For each test case, output a single line containing probability as an irreducible fraction.

### Constraints

1<=**T**<=103

1<=**N**<=109

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3
```

**Output**

```text
1/1
3/4
5/9
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1/1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
3/4
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
5/9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/COOLGUYS)

[Contest](http://www.codechef.com/SEPT13/problems/COOLGUYS)

# Difficulty:

Easy

# Pre-requisites:

Number theory

# Problem:

Given an integer N. Two integers A and B are chosen randomly from [1…N]. Find the probability that gcd(A, B) = B as a reduced fraction.

# Explanation:

Stating that **gcd(A, B) = B** is same as saying that **B is a factor of A**. Therefore, our problem is equivalent to finding

number of ordered pairs (A, B) such that B is a factor of A / N * N

The numerator can be written equivalently in two forms as below:

sum [over A=1 to N] number of factors of A

sum [over B=1 to N] number of multiples of B less than N+1

While it is difficult to find the summands of First sum, the second sum can be written down very simply as

sum B=1 N **? N/B ?**

At this point a very handy fact comes to our rescue.

The sequence **? N/i ?** has at most **2 * ?N** distinct values.

This is because for i > ?N, ? N/i ? < ?N. Therefore for i = ?N + 1 to N, it has only ?N distinct values.

The above fact can be used to our advantage. We can sum up the series by summing up, for each distinct value in the sequence, its number of occurrences.

? N/i ? = K

? K ? N/i < K+1

? N/(K+1) < i ? N/K

? ? N/(K+1) ? < i ? ? N/K   ?

Using the ideas discussed above, here is the psudo code of final solution:

``
sum = 0
K = N
imin = 1
while imin ? N
    imax = ? N/K ?
    sum += K*(imax - imin + 1)
    imin = imax + 1
    K = N/imin
g = gcd(N * N, sum)
print sum/g, N * N/g

``

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/September/Setter/COOLGUYS.pas)

# Tester’s Solution:

- Mahbub’s

``
(http://www.codechef.com/download/Solutions/2013/September/Tester/Tester1/COOLGUYS.cpp)
 2. Sergey's

``

([http://www.codechef.com/download/Solutions/2013/September/Tester/Tester2/COOLGUYS.cpp](http://www.codechef.com/download/Solutions/2013/September/Tester/Tester2/COOLGUYS.cpp))

# Editorialist’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/September/Editorialist/COOLGUYS.cpp)

</details>
