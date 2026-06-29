# Odd Binomial Coefficients

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ODDBIN |
| Difficulty Rating | 2107 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [ODDBIN](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/ODDBIN) |

---

## Problem Statement

If P(x) is a polynomial in x with integer coefficients, let W(P(x)) = number of odd coefficients of P(x).

Given a1, a2, ... , am, find W( (1+x)a1 + (1+x)a2 + ... + (1+x)am ).

### Input

First line contains TC, the number of test cases.
Each test case consists of a single line in the format:
m a1 a2 ... am

### **Limits**

1 <= m <= 15
0 <= ai < 260
1 <= TC <= 1000

### Output

Output one line per test case, the value W( (1+x)a1 + (1+x)a2 + ... + (1+x)am ).

---

## Examples

**Example 1**

**Input**

```text
4
1 1
1 3
2 1 3
3 1 2 3
```

**Output**

```text
2
4
2
2
```

**Explanation**

`(1+x) + (1+x)3 = 2 + 4x + 3x2 + x3. Hence the output for "2 1 3" is 2. (2 odd coefficients)
(1+x) + (1+x)2 + (1+x)3 = 3 + 6x + 4x2 + x3. Hence the output for "3 1 2 3" is 2.
`

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
1 3
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
2 1 3
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
3 1 2 3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/ODDBIN/)

[Contest](http://www.codechef.com/DEC10/problems/ODDBIN/)

### DIFFICULTY

MEDIUM

### EXPLANATION

Notation

``--------
``

Let C(n,r) represent the binomial coefficient of choosing r items out of n.

Let BitSet(n) = { i | 2^i is used in the binary representation of n }. Bitset(5) = {0, 2} since  5 = 1 + 4 = 2^0 + 2^2.

Let H(x) = (1+x)^a1 + (1+x)^a2 + … + (1+x)^am (the ai and m are as given in input)

Let G(x) = H(x) modulo 2. (i.e., coefficients of H reduced modulo 2)

Let #(A) represent the cardinality of A for a finite set A.

Let S = {1, 2, …, m} (the m is as given in input)

Let F(s) = Intersection { BitSet(ai) | i belongs to s }, where s is a subset of S.

Let T = {0, 1, …, 59}

Let N(t) = SUM (i belongs to t) { 2^i } where t is a subset of T.  N( {0,2,3} ) = 2^0 + 2^2 + 2^3 = 13.

We say  p is “present” in G(x) to mean that the coefficient of x^p in G(x) is 1.

L(t) = { i | t is a subset of Bitset(ai) }

Observation 1

``-------------
``

For n>0, 0 <= r <= n, C(n,r) is odd if and only if BitSet® is a subset of Bitset(n).

Proof

``-----
``

Let us compute (1+x)^n where the coefficients are reduced modulo ‘2’. Then, the terms of (1+x)^n correspond to the odd coefficients of

C(n,r). For example (1+x)^2 = 1 + x^2 (modulo 2), indicating that C(2,0) and C(2,2) are odd while C(2,1) is not.

a) (1+x)^(2^k) = 1 + x^(2^k) by induction.

b) Let n = 2^b1 + 2^b2 + … + 2^bk where 0<= b1 < b2 < b3 … < bk. Then, (1+x)^n = Product(1<=i<=k){(1+x)^(2^bi)}

= SUM ( x^p ) where BitSet§ is a subset of BitSet(n).

From the above, it should be clear that the coefficient of x^r modulo 2 is ‘1’ (and hence odd) if and only if BitSet® is a subset of

BitSet(n).

Observation 2

``-------------
``

G(x) = SUM {x^p} where p satisfies the following condition: #{ i | Bitset§ is a subset of Bitset(ai) } is odd.

Put another way: if t is a subset of T, then N(t) is present in G(x) if and only if #L(t) is odd.

Proof

``-----
``

This is rather trivial, since (1+x)^ai contributes x^p to G(x) if and only if BitSet§ is a subset of BitSet(ai). Since x^p has coefficient 1 if and only if an odd number of (1+x)^ai contribute x^p to G(x), the observation follows.

Observation 3

``-------------
``

(1-2)^n = (-1)^n = SUM ( 0 <= r <= n ) { (-1)^r * C(n,r) * 2^r }

Hence, 1 - (-1)^n = SUM ( 1 <= r <= n ) { (-1)^(r+1) * C(n,r) * 2^r }

Note that 1 - (-1)^n = 0 if n is even, and 2 if n is odd.

Observation 4

``-------------
``

If t is a subset of T, then 2*x = SUM ( s is a non empty subset of L(t)) { (-1)^(#(s)+1) * 2^#(s) } where x = 1 if N(t) is present in G(x) and 0 otherwise.

Proof

``-----
``

Another way of looking at Observation 3 is: 1 - (-1)^#(B) = SUM ( b is a non empty subset of B ) { (-1)^(#(b)+1) * 2^#(b) } where B is a finite set. (Note how C(#(B),r) in the summand is replaced by r-element subsets of B in the summation index (and unity in the summand))

Now, substitute L(t) for B and s for b in the above to obtain 1 - (-1)^#L(t) = 2 * x Since x = 1(resp. 0) if #L(t) is odd(resp. even) and N(t) is present in G(x) if and only if #L(t) is odd, the result follows.

Observation 5

``-------------
``

“s is a non empty subset of L(t)” if and only if “s is a non empty subset of S, t is a subset of F(s)”

Observation 6

``-------------
``

Adding both sides of observation 4 over all possible t and using Observation 5, we get  2 * (number of odd coefficients of G(x)) = SUM (s is a non empty subset of S, t is a subset of F(s)) { (-1)^(1+#(s)) * 2^#(s) } or, after eliminating t, 2 * (number of odd coefficients of G(x)) = SUM (s is a non empty subset of S) { (-1)^(1+#(s)) * 2^(#(s) + #F(s)) }

Note that we used #{t | t is a subset of F(s)} = 2^#F(s)

or, W(G(x)) = W(H(x)) = SUM (s is a non empty subset of S) { (-1)^(1+#(s)) * 2^(#(s) + #F(s) - 1) }

The algorithm

``-------------
``

The above observations make it simple enough to compute the desired answer.

We just loop over all possible non empty subsets s of S, and for each s, find #F(s) and compute the sum.

We can use 64 bit unsigned integers to store BitSet(ai) and the fact that unsigned long long additions are performed modulo 2^64 to compute

F(s) fast enough and not worry about overflow of the intermediate sum.

Complexity of this algorithm is O(2^m) (using Dynamic Programming on F(s) computation and bitwise AND for set intersection) per case.

For mask > 0, (mask representing a subset of S) F[mask] = ai if mask = (1 << i )  = F[mask & (mask-1)] & F [ mask & ~ mask-1)], if bitcount(mask) > = 2

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/December/Setter/ODDBIN.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/December/Tester/ODDBIN.cpp).

</details>
