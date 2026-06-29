# Count palindromes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COUNTPAL |
| Difficulty Rating | 1631 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [COUNTPAL](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/COUNTPAL) |

---

## Problem Statement

Each palindrome can be always created from the other palindromes, since a single character is also a palindrome. For example, the string "bobseesanna" can be created by some ways:

* bobseesanna = bob + sees + anna

* bobseesanna = bob + s + ee + s + anna

* bobseesanna = b + o + b + sees + a + n + n + a

...

We want to take the value of function CountPal(s) which is the number of different ways to use the palindromes to create the string s by the above method.

### Input

The string s

### Output

The value of function CountPal(s), taking the modulo of 1 000 000 007 (109+7)

### Limitations

0 < |s| <= 1000

---

## Examples

**Example 1**

**Input**

```text
bobseesanna
```

**Output**

```text
18
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### [](#problem-links-1)PROBLEM LINKS

[Practice](http://www.codechef.com/problems/COUNTPAL/)

[Contest](http://www.codechef.com/OCT10/problems/COUNTPAL/)

### [](#difficulty-2)DIFFICULTY

EASY

### [](#explanation-3)EXPLANATION

The problem can be solved easily by dynamic programming:

F(i) = CountPal(s’) for s’ is the subtring of s_1 .. s_i

so F(i) = sum of F(j) with j < i whether the substring of s[j+1]…s[i] is a palindrome.

To verify a substring is a palindrome or not, we can pre-compute to save time of DP.

Complexity: O(|s|^2)

</details>
