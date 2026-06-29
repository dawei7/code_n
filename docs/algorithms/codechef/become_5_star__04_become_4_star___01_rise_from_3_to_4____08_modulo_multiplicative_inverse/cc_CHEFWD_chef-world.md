# Chef World

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFWD |
| Difficulty Rating | 2049 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Modulo Multiplicative Inverse |
| Official Link | [CHEFWD](https://www.codechef.com/practice/course/3to4stars/LP3TO408/problems/CHEFWD) |

---

## Problem Statement

Chef Ciel lives in a long street which can be thought as of x-axis of coordinate system.
Her house is at coordinate 0 whereas her restaurant is situated at coordinate **N**.
Usually Ciel goes from home to restaurant taking a step of size 1 or 2 in forward direction.
We all know how much Chef loves Fibonacci numbers.

But today, Ciel being little casual stepped in wrong direction on her way to her restaurant exactly once and of course she did not set her foot wrong at home.
Now she wonders how many ways she can reach her restaurant provided that she stepped wrong once but not at home.

 She does not go past her restaurant because it is altogether different world and once she reaches her restaurant she stops.

For example, if **N** is **3** then
**0** -> **1** -> **-1** -> **0** -> **1** -> **3**,
**0** -> **2** -> **1** -> **3**

are some possible ways where as
**0** -> **-1** -> **1** -> **3**, (She did not set her foot wrong at her home)
**0** -> **1** -> **3**, (She sets her foot wrong direction exactly once)
**0** -> **1** -> **0** -> **3**, (Her steps are always size 1 or 2)
**0** -> **1** -> **2** -> **4** -> **3**, (She does not go past her restaurant)
**0** -> **1** -> **2** -> **3** -> **2** -> **3** (Once she reaches her restaurant, she stops)

are not.

### Input

First line of input contains **T**, number of test cases which is at most 10000.
Then **T** lines follows each containing a positive integer **N** which is at most 1000000000000000 (1015).

### Output

Number of ways Ciel can reach her restaurant modulo 1000000007 (109+7).

---

## Examples

**Example 1**

**Input**

```text
2
3
4
```

**Output**

```text
18
44
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
18
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
44
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFWD)

[Contest](http://www.codechef.com/SEP12/problems/CHEFWD)

# DIFFICULTY

EASY

# PREREQUISITES

Math, Repeated Squaring, Fibonacci Numbers

# PROBLEM

Find the number of ways to go from 0 to N, taking steps of 1 or 2, and taking exactly 1 back-step on the way of -1 or -2.

# QUICK EXPLANATION

Let us assume that Ciel takes `k` steps forward, then one back, and the rest forward.

The number of ways she can accomplish this is `fib(k) * [ fib(N-k + 1) + fib(N-k + 2) ]`; since she can take only 1 or 2 steps back.

We have to find a summation of the above sequence for all k between 1 and N-1 inclusive. We can see that this needs to us to find summation of the form

?k = 0 to N`fib(k)*fib(N-k)`

This is also known as the convolution of the fibonacci series onto itself. Once we know how to solve this convolution efficiently, we can solve the problem.

# EXPLANATION

There are several ways `F(N) =` ?`k = 0 to N``fib(k)*fib(N-k)` can be found.

Formulas regarding the same have been listed on [Wikipedia](http://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Convolved_Fibonacci_sequences) as well as [OEIS](http://oeis.org/A001629). Finding a couple of smaller values and searching on OEIS is a solution to many a problem that asks you to find the result for a sequence of numbers.

If you’re into math, then using the concept of fibonacci polynomials, one can derive several relations as outlined in this wonderful [paper](http://www.fq.math.ca/Scanned/15-2/hoggatt1.pdf).

### I. F(N) = F(N-1) + F(N-2) + fib(N)

You can use the above identity and build a `4x4` matrix as follows

`
                                                                    |1 1 0 0|
[F(N) F(N-1) fib(N) fib(N-1)] = [F(N-1) F(N-2) fib(N-1) fib(N-2)] * |1 0 0 0|
                                                                    |1 0 1 1|
                                                                    |1 0 1 0|
`

Now you can use matrix exponentiation to calculate `F(N)` till the desired N to solve the problem.

### II. F(N) = 2*F(N-1) + F(N-2) - 2*F(N-3) - F(N-4)

Similar to (I) you can construct a 4x4 matrix and use matrix exponentiation.

4x4 matrix and its exponentiation leads to slightly larger constants and needs several micro optimizations to stay within the time limit. Thus, a better approach is to not need to do matrix exponentiation over 4x4 matrices at all, as outlined in (III) below.

### III. 5*F(N) = (n - 1)*fib(N + 1) + (n + 1)*fib(N - 1)

This elegant result is derived in [this paper](http://www.fq.math.ca/Scanned/15-2/hoggatt1.pdf). Note that they assume fib[0] as 0 and fib[1](http://www.codechef.com/problems/CHEFWD) as 1.

Using the above result we can say that we need to find

?`k = 1 to (N-1)``fib(k+1) * [fib(N-k + 2) + fib(N-k + 3)]`

or ?`k = 1 to (N-1)``fib(k+1) * fib(N-k + 4)`

We can rewrite the above as

`F(N+5) - fib(0)*fib(N+5) - fib(1)*fib(N+4) - fib(N+1)*fib(4) - fib(N+2)*fib(3) - fib(N+3)*fib(2) - fib(N+4)*fib(1) - fib(N+5)*fib(0)`

``= F(N+5) - 2*fib(N+4) - fib(N+3) - 2*fib(N+2) - 3*fib(N+1)
``

A fibonacci number can be calculated by doing matrix exponentiation of a `2x2` matrix, which is very fast. We cal find fib(N+1) and fib(N) through one exponentiation of the matrix representation of fibonacci numbers and calculate fib(N+2), fib(N+3), fib(N+4), fib(N+5) and fib(N+6) from them.

You may notice that calculating F(N) requires you to divide an integer by 5. Since we maintain modulo all along to avoid overflows, we must calculate the division modulo 1000000007 as well.

This can be accomplished by finding the [modular multiplicative inverse](http://en.wikipedia.org/wiki/Modular_multiplicative_inverse) of 5, modulo 1000000007.

# SETTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/September/Setter/CHEFWD.cpp)

# TESTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/September/Tester/CHEFWD.c)

</details>
