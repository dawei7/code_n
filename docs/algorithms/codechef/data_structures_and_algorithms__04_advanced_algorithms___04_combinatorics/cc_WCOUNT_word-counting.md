# Word Counting

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WCOUNT |
| Difficulty Rating | 1640 |
| Difficulty Band | Combinatorics |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Combinatronics |
| Official Link | [WCOUNT](https://www.codechef.com/learn/course/combinatorics/COMBI03/problems/WCOUNT) |

---

## Problem Statement

Chef has decided to retire and settle near a peaceful beach. He had always been interested in literature & linguistics. Now when he has leisure time, he plans to read a lot of novels and understand structure of languages. Today he has decided to learn a difficult language called Smeagolese. \
**Smeagolese** is an exotic  language whose alphabet is lowercase and uppercase roman letters. \
Also every word on this alphabet is a meaningful word in Smeagolese. Chef, we all know is a fierce learner - he has given himself a tough exercise. \
He has taken a word $S$ and wants to determine all possible anagrams of the word which mean something in Smeagolese.  Can you help him ?

## Function Declaration

### Function Name

$countSmeagoleseAnagrams$ – This function calculates the number of distinct anagrams of a given word that are meaningful in the Smeagolese language.

### Parameters

* $S$ : A string representing the word chosen by Chef.
  The string consists of lowercase and uppercase English letters.
  All permutations (anagrams) of the string are considered valid words in Smeagolese.

### Return Value

* Returns an integer representing the number of **distinct anagrams** of the string $S$.
* Since the answer can be very large, return the result **modulo $10^9 + 7$**.

## Constraints

* $1 \leq T \leq 500$
* $1 \leq |S| \leq 500$
* Each character appears **at most 10 times** in the string
* Characters may include:

  * lowercase letters (`a`–`z`)
  * uppercase letters (`A`–`Z`)
* Modulo value: $10^9 + 7$

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* For each test case:

  * A single line containing a string $S$ — the word chosen by Chef.

---

## Output Format

* For each test case, output a single integer on a new line:

  * The number of **distinct anagrams** of the given string $S$, taken modulo $10^9 + 7$.

---

## Examples

**Example 1**

**Input**

```text
4
ab
aa
aA
AAbaz
```

**Output**

```text
2
1
2
60
```

**Explanation**

In first case "ab" & "ba" are two different words. In third case, note that A & a are different alphabets and hence "Aa" & "aA" are different words.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
ab
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
aa
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
aA
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
AAbaz
```

**Output for this case**

```text
60
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/WCOUNT/)

[Contest](http://www.codechef.com/FEB12/problems/WCOUNT/)

### DIFFICULTY

EASY

### EXPLANATION

The original version I had proposed had much tighter constraints though tester suggested bringing the constraints down so that various easier approached could be used. Here are four different solutions that the current constraints would allow. But before that lets understand the solution. Essentially problem asks you to find number of permutations of some alphabets when they might repeat. The formula for this is : N!/ (a1! * a2! * … * ak!) if there are a1 letter of first type, a2 of second type and so on. Further this has to be computed modulo 109 + 7 which we denote as MOD everywhere below. The main difficulty lies in computing. So the simplest solution is to compute N! and divide it by a1! , a2!, …, ak!. The mistake is when you compute N! you’ve probably overflown the 32bit and even 64bit integer type. Here are the four different correct approaches each of which we tested to run in time :

-

**Approach 1 : Big Integers**

If you know how to use BigIntegers in Java or have written a BigInteger library in language of your choice, or you use python, you sail easy. Do all intermediate calculations in big integers so that there is no overflow and finally take the modulo. Heavy machinery, easy enough. See the corresponding tester solution to see how to implement this approach using only (BigInt *= Small) and (BigInt /= Small).

-

**Approach 2 : Modular Inverses**

If you don’t know about modular inverse, read more [here](http://en.wikipedia.org/wiki/Modular_multiplicative_inverse). Solution is give away from here : the formula is (N! * inv(a1!) * inv(a2!) * … * inv(ak!) ) % MOD where **inv(a)** denotes multiplicative inverse of **a** with respect to MOD. Here you use the fact that MOD is a prime number and hence all modular inverses would exist. The intended solution to original constraints was to precompute all factorials and factorial inverses, however here precomputation is also not necessary.

Before I discuss other two approaches, lets look at the formula again : N!/ (a1! * a2! * … * ak!). So numerator has product of N numbers from 1 to N. Denominator has product of 1 to ai for each i. We know that its an integer in the end. So its possible to ‘cancel’ each number in denominator with some number of numerator. Next two approaches try this only. Imagine you have an array A of size N containing numbers 1 to N initially. We’d try to cancel numbers from denominator and in process reduce some numbers in A. Finally we’d take the product of remaining numbers only.

-

**Approach 3 : Prime factorization of denominator**

As its given that all ai are no more 10, prime factorization of denominator contains only 2, 3, 5 and 7. We can count the exponent of each of the primes coming from ak! : simply loop from 1 to ak and add to exponent of 2, 3, 5 or 7 based on number. Add exponents from all ai. Now we know prime factorization of denominator. Loop over each number in A and reduce from it requisite number of powers or 2, 3, 5 or 7. Look at the setter’s official solution for this approach.

-

**Approach 4 : Reduction using GCD**

Denominator looks like : (1 * 2 * … * a1) * (1 * 2 * … * a2) * … * (1 * 2 * … * ak). We know that each of these numbers can be cancelled from numerator. So lets pick a number from denominator and move over numerator and cancel the gcd from both. Eventually the number in denominator would become 1. Look at sample program here.

-

**Approach 5 : Reduction without GCD (WRONG!!!)**

As in the previous approach lets pick a number (say x) from denominator and move over numerator until we find the value A[i] that is divisible by x and reduce A[i] by x. **This approach is wrong** even if we try some smart schemes when finding what A[i] choose to cancel if it is not unique. The simplest test is 15!/6!/9!. Clearly it is advantageous to cancel 9! as it is so we left with the fraction 10 * 11 * 12 * 13 * 14 * 15 / ( 1 * 2 * 3 * 4 * 5 * 6 ). And now look: the only number that can handle 4 and 6 is 12 but it can’t be reduced by both 4 and 6. More complicated example is 50!/ 10!/ 10!/ 10!/ 10!/ 10!. It is a good exercise to prove that there is no way to cancel using this approach. And if the first example can be simply calculated in int this one is a hard nut for trying to add some hacks to this approach in order to get Accepted.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/February/Setter/WCOUNT.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/February/Tester/WCOUNT.cpp).

</details>
