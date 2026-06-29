# A-E Hash Function

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AEHASH |
| Difficulty Rating | 1832 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [AEHASH](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/AEHASH) |

---

## Problem Statement

Chef Ash and Chef Elsh invented a new hash function! Their hash function will map a binary string consisting of characters 'A' and 'E' into an integer called the hash value of the string.

The pseudocode of the hash function is as below. hash(S) is the hash value of a binary string S. |S| denotes the length of S.

`function hash(S):
	result = number of characters 'A' in S
	if |S| > 1:
		(S1, S2) = split(S)
		result = result + max(hash(S1), hash(S2))
	end if
	return result
end function`

The function split in the above pseudocode takes a binary string S as the parameter and returns a pair of binary strings (S1, S2) such that:

- |S1| <= |S2|.

- The difference of |S1| and |S2| is at most 1.

- The concatenation of S1 and S2 (in that order) is S.

For example, split("AAAEE") returns ("AA", "AEE"), whereas split("AEAEAE") returns ("AEA", "EAE").

You doubt that this hash function have good distribution of different hash values. So, you wonder how many different binary strings consisting of A 'A' characters and E 'E' characters that have hash value of V.

### Input

The first line contains a single integer T, the number of test cases. T test cases follow. Each testcase consists of a single line consisting of three integers A, E, and V.

### Output

For each test case, output a single line consisting the number of different binary strings satisfying the rule, modulo 1000000007.

### Constraints

- 1 ≤ T ≤ 1000

- 0 ≤ A ≤ 50

- 0 ≤ E ≤ 50

- 0 ≤ V ≤ 1000

---

## Examples

**Example 1**

**Input**

```text
4
0 0 0
1 0 1
3 2 6
4 2 8
```

**Output**

```text
1
1
3
4
```

**Explanation**

For the last test case, the solutions are:

- AAEAAE

- AEAAAE

- AAEAEA

- AEAAEA

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0 0 0
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1 0 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3 2 6
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
4 2 8
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/AEHASH/)

[Contest](http://www.codechef.com/JULY11/problems/AEHASH/)

### DIFFICULTY

EASY

### EXPLANATION

This problem can be solved using dynamic programming approach.

Let DP(V, A, E) be the number of binary strings containing A ‘A’ characters and E ‘E’ characters, and have hash value V.

The base cases are

- DP(0, 0, 0) = 1, DP( * , 0 , 0 ) = 0 (* other than 0)

- DP(1, 1, 0) = 1, DP( * , 1 , 0 ) = 0 (* other than 1)

- DP(0, 0, 1) = 1, DP( * , 0 , 1 ) = 0 (* other than 0)

Then, we must define the recurrence formula. Let N = A + E. After the split, let the first half (N/2) of the string contains A1 'A’s, E1 'E’s, and has hash value V1. Let the second half (N - N/2) of the string contains A2 'A’s, E2 'E’s, and has hash value V2. Because they are independent, we can simply take the product.

So, the recurrence becomes

DP(V, A, E) = sum { DP(V1, A1, E1) * DP(V2, A2, E2) }

for all

A1 + A2 = A

E1 + E2 = E

A1 + E1 = N/2

A2 + E2 = N - N/2

max(V1, V2) = V - A

So, the idea is to try all possible values of A1, A2, E1, E2, V1, V2, then take the sum of the products. First, we try all possible values of A1. We automatically get A2, E1, and E2 by exploiting the above equation. After that, try all possible values of V1 and V2 whose max value is V - A.

This is our current solution in pseudocode.

for A1 := 0 to A

A2 := A - A1;

E1 := N/2 - A2;

E2 := E - E1;

for V1 := 0 to V - A

for V2 := 0 to V - A

if max(V1, V2) = V - A

DP(V, A, E) += DP(V1, A1, E1) * DP(V2, A2, E2);

The above algorithm is not very efficient, since there are only O(V - A) pairs of (V1, V2) that satisfy max(V1, V2) = V - A, i.e. when one of them is V - A. So, we can improve that into

for A1 := 0 to A

A2 := A - A1

E1 := N/2 - A2

E2 := E - E1

// both are V - A

V1 := V - A;

V2 := V - A;

DP(V, A, E) += DP(V1, A1, E1) * DP(V2, A2, E2);

// V1 is V - A, V2 < V - A

V1 := V - A;

for V2 := 0 to V - A - 1

DP(V, A, E) += DP(V1, A1, E1) * DP(V2, A2, E2);

// V2 is V - A, V1 < V - A

V2 := V - A;

for V1 := 0 to V - A - 1

DP(V, A, E) += DP(V1, A1, E1) * DP(V2, A2, E2);

The algorithm can still be improved further, by replacing the two for’s by partial sum, like this:

for A1 := 0 to A

A2 := A - A1

E1 := N/2 - A2

E2 := E - E1

// both are V - A

DP(V, A, E) += DP(V-A, A1, E1) * DP(V-A, A2, E2);

// V1 is V - A, V2 < V - A

DP(V, A, E) += DP(V-A, A1, E1) * SUM(V-A-1, A2, E2);

// V2 is V - A, V1 < V - A

DP(V, A, E) += SUM(V-A-1, A1, E1) * DP(V-A, A2, E2);

where SUM(V, A, E) = sum {DP(V, A, E)} for all v := 0 to V.

The complexity then becomes O(A^2 E V). If you have completed the solution, you can easily check that the maximum value of V is 152.

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/July_Long/Tester/AEHASH.cpp).

</details>
