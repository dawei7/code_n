# Split Sums

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPSUM |
| Difficulty Rating | 1524 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [SPSUM](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/SPSUM) |

---

## Problem Statement

A and B are brothers and like playing with marbles.Their mother buys them **N** marbles to play with.The preciousness of each marble is a natural number from 1 to **N** and no two marbles have same preciousness.

Since A and B are good at maths they want to divide all those **N** marbles among them in such a way that sum of the preciousness of all marbles that A receives and sum of the preciousness of all marbles that B receives after distribution are co-primes i.e the gcd(greatest common divisor) of their sum is 1.

Also the absolute value of difference between the sum of the preciousness of marbles of A and B should be exactly **M**.

Help A and B in finding whether such a distribution of **N** marbles between them is possible or not.

Formally, you have to tell whether you can distribute first **N** natural numbers in two sets such that the absolute difference of the sum of numbers in the two sets is equal to **M** and the gcd of their sum is 1.

Note that one of the set can be empty and greatest common divisor of **0** and **k** is **k**

### Input

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains two integers **N**  and **M** denoting the number of marbles and the absolute difference of sum respectively.

### Output

- For each test case, output a single line.

Print “Yes” if there exist a valid distribution of marbles between A and B else print “No”.

### Constraints

- **1** ≤ **T** ≤ **20**

- **1** ≤ **N** ≤ **1,000,000,000**

- **0** ≤ **M** ≤ **1018**

---

## Examples

**Example 1**

**Input**

```text
2
5 7
1 2
```

**Output**

```text
Yes
No
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 7
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
1 2
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Links:

Contest:  [Contest](https://www.codechef.com/INSO2018/problems/SPSUM)

Author: [Ashish Ranjan](https://www.codechef.com/users/rashish2202)

Editorialist:[Ashish Ranjan](https://www.codechef.com/users/rashish2202)

# **Difficulty Level:**Easy

# PRE-REQUISITES:Ad-Hoc,Maths

## Explanation

Let S1 and S2 denote the set of marbles that A and B have.

It can be seen that sum(S1)+sum(S2)=n*(n+1)/2.(sum of first n natural numbers)

sum(S1)-sum(S2)=M.

So we know sum(S1) and sum(S2) from here.If sum(S1) and sum(S2) are integers,then we can split the first N natural numbers into two sets.

Now check if their GCD is 1 or not.If the GCD is 1,print Yes otherwise print No.

</details>
