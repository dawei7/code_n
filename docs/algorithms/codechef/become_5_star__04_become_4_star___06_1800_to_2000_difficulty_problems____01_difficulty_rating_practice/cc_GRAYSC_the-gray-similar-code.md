# The Gray-Similar Code

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GRAYSC |
| Difficulty Rating | 1910 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [GRAYSC](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/GRAYSC) |

---

## Problem Statement

The Gray code (see [wikipedia](http://en.wikipedia.org/wiki/Gray_code) for more details) is a well-known concept.
One of its important properties is that every two adjacent numbers have exactly one different digit in their binary representation.

In this problem, we will give you **n** non-negative integers in a sequence **A[1..n] (0<=A[i]<2^64)**, such that every two adjacent integers have exactly one different digit in their binary representation, similar to the Gray code.

Your task is to check whether there exist 4 numbers **A[i1], A[i2], A[i3], A[i4] (1 <= i1 < i2 < i3 < i4 <= n)** out of the given **n** numbers such that **A[i1] xor A[i2] xor A[i3] xor A[i4] = 0**. Here **xor** is a [bitwise operation](http://en.wikipedia.org/wiki/Bitwise_operation#XOR) which is same as **^** in C, C++, Java and **xor** in Pascal.

### Input

First line contains one integer **n (4<=n<=100000)**.
Second line contains **n** space seperated non-negative integers denoting the sequence **A**.

### Output

Output “Yes” (quotes exclusive) if there exist four distinct indices **i1, i2, i3, i4** such that **A[i1] xor A[i2] xor A[i3] xor A[i4] = 0**. Otherwise, output "No" (quotes exclusive) please.

---

## Examples

**Example 1**

**Input**

```text
5
1 0 2 3 7
```

**Output**

```text
Yes
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINK:

[Practice](http://www.codechef.com/problems/GRAYSC)

[Contest](http://www.codechef.com/JULY12/problems/GRAYSC)

## DIFFICULTY:

Easy-Medium

## PREREQUISITES:

Pigeonhole Principle, Sets

## PROBLEM:

You’re given **N 64** bit integers such that any two successive numbers differ at exactly 1 bit. Your job is to find out if there are 4 integers such that their xor is equal to 0.

## QUICK EXPLANATION:

Whenever **N** >= 130, it is always possible to find 4 integers of the given list such that their xor is 0. For smaller N, one could do an exhaustive search in **O(N^3 log N)**.

## DETAILED EXPLANATION:

Solution of this problem is simpler than many of you might’ve imagined. For all

**N** >= 130, answer is always YES. Let’s see why : Assume there are >= 130

numbers in input array **A**.

Let **xi = A[2i] xor A[2i+1]** for **i** in **[0, N/2)**

As any two successive values of **A** differ at exactly one bit, binary

representation of each **xi** has exactly 1 bit as 1 and all other bits are

0. Also as **N** >= 130, we’ve at least 65 values of **xi**. Note all of them can

be distinct as each **xi** has only 1 bit set and all xi are at maximum 64 bits

long. So say **xj = xk** for some **j** and **k**

Then **xj xor xk = 0**

=> **A(2j) xor A(2j+1) xor A(2k) xor A(2k+1) = 0**

And so the answer is YES.

Small Case:

What if **N** < 130? We could do an exhaustive search. One could try moving all

4 numbers and see if their xor is 0 or not. This takes **O(N^4)** time and is probably

too costly. We can do this in **O(N^3 log N)** as well. Let’s see how.

Say if there are four indices **i1, i2, i3, i4** such that

**A[i1] xor A[i2] xor A[i3] xor A[i4] = 0.**

Then **A[i1] xor A[i2] xor A[i3] = A[i4]**

So we could move over all three numbers of array, find their xor and

check if it is present in set as well or not.

``for i in 1 to N
  for j in i+1 to N
    for k in j+1 to N
      x = A[i] ^ A[j] ^ A[k]
      if A[k+1...N] contains x, return true

return false
``

**Note** : Actually 130 is only an upper bound. We don’t have a case for **N** > 67 for

which answer is No. Maybe such a case doesn’t exist and our proof given above could

be strengthened. If you have a case where **N** > 67 and answer is NO, please share it here.

## SETTER’S SOLUTION:

Can be found [here](http://www.codechef.com/download/Solutions/2012/July/Setter/GRAYSC.cpp).

## TESTER’S SOLUTION:

Can be found [here](http://www.codechef.com/download/Solutions/2012/July/Tester/GRAYSC.cpp).

## RELATED PROBLEMS:

[UVA 11898](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=226&page=show_problem&problem=2998)

</details>
