# Check Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR11 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR11](https://www.codechef.com/learn/course/recursion/LRECUR02/problems/RECUR11) |

---

## Problem Statement

You are given a string and you have to tell if it is a Palindrome or not.

**Note**: A Palindrome is a string that is same when reversed.
For example: 'BOB', 'TENET' are Palindromes, while 'TENT' is not a Palindrome

---

## Input Format

- The first line contains a single string $S$.

---

## Output Format

You have to output "Yes" if the string is a Palindrome. Otherwise output "No"

---

## Constraints

- $1 \leq $Length of the String$ \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
tenet
```

**Output**

```text
Yes
```

**Example 2**

**Input**

```text
rabbit
```

**Output**

```text
No
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## [](#problem-explanation-1)Problem Explanation

You are given a string and you have to tell if it is a Palindrome. Palindromes are strings that are the same when reversed.

## [](#approach-2)Approach

Palindromes are mirrored in the middle. So we can check if the 0^{th} index character is the same as the (n-1)^{th} character, the 1^{st} character is the same as the (n-2)^{th} character and so on untill the middle which is n/2. So we iterate from the beginning of the string till the middle and check for every i, the i^{th} character is equal to the (n-i-1)^{th} character or not. If not then we output that it is not a palindrome and if the whole string is iterated then it is a Palindrome.

## [](#code-3)Code
``def check_palindrome(s, n):
    if(n>len(s)//2):
        return "Yes"
    if(s[n]!=s[len(s)-n-1]):
        return "No"
    return check_palindrome(s, n+1)
``

</details>
