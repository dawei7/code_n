# Oracle Devu and Longest Common Subsequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ORACLCS |
| Difficulty Rating | 1726 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [ORACLCS](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/ORACLCS) |

---

## Problem Statement

Devu is a disastrous oracle: his predictions about various events of your life are horrifying. Instead of providing good luck, he "blesses" you with bad luck. The secret behind his wickedness is a hidden omen which is a string of length **m**. On your visit to him, you can ask a lot of questions about your future, each of which should be a string of length **m**. In total you asked him **n** such questions, denoted by strings **s1**, **s2**, ... , **sn** of length **m** each. Each of the question strings is composed of the characters 'a' and 'b' only.

Amount of bad luck this visit will bring you is equal to the length of longest common subsequence ([LCS](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)) of all the question strings and the hidden omen string. Of course, as the omen string is hidden, you are wondering what could be the least value of bad luck you can get.

Can you find out what could be the least bad luck you can get? Find it fast, before Devu tells you any bad omens.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

First line of each test case contains a single integer **n** denoting number of strings.

For each of next **n** lines, the **i**th line contains the string **si**.

### Output
For each test case, output a single integer corresponding to the answer of the problem.

### Constraints

- All the strings (including the hidden omen) contain the characters 'a' and 'b' only.

** Subtask #1:** (40 points)

- **1** ≤ **T, n, m** ≤ **14**

** Subtask #2:** (60 points)

- **1** ≤ **T, n, m** ≤ **100**

---

## Examples

**Example 1**

**Input**

```text
3
2
ab
ba
2
aa
bb
3
aabb
abab
baab
```

**Output**

```text
1
0
2
```

**Explanation**

**In the first example**, the minimum value of LCS of all the strings is 1, the string by oracle can be one of these {aa, ab, ba, bb}.

**In the second example**, whatever string oracle has does not matter, LCS will always be zero.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/DEC15/problems/ORACLCS)

[Practice](http://www.codechef.com/problems/ORACLCS)

**Author:** [Praveen Dhinwa](http://www.codechef.com/users/admin2)

**Tester:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### PREREQUISITES:

longest common subsequence

### PROBLEM:

You are given n strings, each of length m and consisting only of the characters `a` or `b`. Find another such string such that the longest common subsequence (LCS) of all n+1 strings is minimized. Output only this smallest LCS.

### QUICK EXPLANATION:

The smallest LCS is always a constant string, i.e. either `aaa...a` or `bbb...b`. Thus the answer is the minimum number of `a`s or `b`s in any string.

### EXPLANATION:

First, we introduce a little bit of notation. Let s be a string of length, say, m. We write this as |s| = m. For 0 \le i \le m, we denote by s[i] the i th character of s, and s_i the prefix of s consisting of the first i characters. Thus, s_m = s, and s_0 = \varepsilon, the empty string. As an example, suppose s is `codechef`. Then s_4 is `code` and s[4] is `c`.

# Longest common subsequence

The problem of *finding the longest common subsequence* (LCS) is quite standard, and there is a well known (dynamic programming) algorithm for it: Suppose we want to find the length of the LCS of two strings of length m, say s and t. Let f(a,b) be the LCS of s_a and t_b. Then (the length of) the LCS of s and t themselves is f(m,m). The following gives one way to compute f recursively:

- As base cases, we have f(a,b) = 0 if a = 0 or b = 0, because in these cases, one of the strings is empty.

- If a > 0, b > 0 and s[a] = t[b], then f(a,b) = f(a-1,b-1) + 1.

- If a > 0, b > 0 and s[a] \not= t[b], then f(a,b) = \max(f(a-1,b), f(a,b-1)).

By tabulating all (m+1)^2 possible sets of arguments to f and filling the table in the right order, one can achieve an O((m+1)^2), or O(m^2), time algorithm to compute (the length of) the LCS of two strings.

This algorithm can be extended to more strings. However, the complexity becomes greater and greater the more strings you add. For example, for three strings, you would need a three-dimensional array for f, so the running time is O(m^3). In general, to compute the LCS of n strings this way would require O(nm^n) time, which is not polynomial-time. In fact, the problem of computing the LCS of a set of strings is NP-complete!

It’s not even clear how to brute-force the problem to pass the first subtask. One idea might be to try all binary strings of length m, and for each string, compute its LCS together with the other n strings. To compute the LCS, one can use the algorithm above. But there are n+1 strings, so the complexity is O(nm^{n+1}), which is too slow for the worst case m = n = 14.

A faster way would be to simply try all 2^{m+1} - 1 possible LCSes, i.e. for each string of length at most m, check if it is a subsequence of all strings, and get the longest. Checking subsequences can be done in linear time, so this check runs in O(mn), which is much more acceptable.

However, since there are 2^{m+1}-1 strings to try, this procedure will be called 2^{m+1}-1 times and so the overall complexity is O(mn 2^m), which is too large even for the smallest subtask!

# n = 1

Let’s start small. Suppose n = 1, that is, suppose there is only one string of length m. Our goal is to find another such string such that the length of the LCS is minimized. Clearly this is a special case of the current problem and so we must be able to solve this case.

As an example, suppose the string we have is `bbbbaaaaaa`. Let’s try to concoct a string that minimizes the LCS.

Let’s try a simple candidate: `aaaaaaaaaa`. What is the LCS? Obviously it’s `aaaaaa`, and the length is 6. So we now have an upper bound for the answer: 6. But can we do better?

To do better, the first thought is that you can’t use too many `a`s, because otherwise you might have `aaaaaa` as a common subsequence again, so we’d have failed to improve on our bound. In fact, why don’t we try avoiding any `a`s at all? Let’s try the string `bbbbbbbbbb`. This way, the LCS is `bbbb`, which only has length 4. We now have a better upper bound! But again, can we do better?

In order to do better, similar to the `a` case, we can’t use more than three `b`s, otherwise `bbbb` will be a common subsequence, and we wouldn’t have improved on our best solution. This means that we can use at most 3 `b`s. But if there are only up to 3 `b`s, then *there are at least 7 `a`s*, which means `aaaaaa` will be a common subsequence. And this is longer than `bbbb`! Thus, we have just shown that it’s impossible to improve on the smallest LCS of 4, and in fact the smallest LCS for this case is 4.

The nice thing about this argument is that it easily works for any other string! More specifically:

- Suppose our string has a `a`s and b `b`s. (Thus a + b = m.)

- We can force the LCS to be \min(a,b) in length, by using the string `aaa...a` or `bbb...b`, whichever of a or b is smaller respectively.

- But we can show that we can’t do any better than \min(a,b). Because suppose we found another string of length m with LCS less than \min(a,b). This string cannot have \min(a,b) `a`s, or \min(a,b) `b`s, otherwise the LCS would have been \min(a,b) (or longer). Thus, there are less than \min(a,b) `a`s and `b`s in this string. But this means that the total length of the string is less than \min(a,b) + \min(a,b) \le a + b = m, a contradiction.

- Thus, the answer is \min(a,b).

Thus, we have just shown that answer for a single string is \min(a(s),b(s)), where a(s) and b(s) are the number of `a`s and `b`s in s, respectively.

# n > 1

Now, what if n > 1? Similarly to the above, it’s immediately clear that we have the following upper bound:

\min_{\text{string $s$}} \min(a(s),b(s))

Where s runs across all n strings in the input. This LCS is achieved by trying the strings `aaa...a` and `bbb...b`. Now, this time can we do better?

In fact, we can easily adjust the argument above to show that this is the smallest LCS we can get!

- We can force the LCS to be C = \min_s \min(a(s),b(s)) in length, by using the string `aaa...a` or `bbb...b`, whichever yields the smaller LCS. Note that a(s) + b(s) = m for any string s.

- But we can show that we can’t do any better than C. Because suppose we found another string of length m with LCS less than C. This string cannot have C `a`s, or C `b`s, otherwise the LCS would have been C (or longer). Thus, there are less than C `a`s and `b`s in this string. But this means that the total length of the string is less than C + C \le a(s) + b(s) = m (for any string s), a contradiction.

- Thus, the answer is C = \min_s \min(a(s),b(s)).

The value \min_s \min(a(s),b(s)), can be computed by simply counting the `a`s and `b`s in each string! This runs in linear time in the input.

Here’s an implementation in Python:

``for cas in xrange(input()):
    A = B = 10**9
    for i in xrange(input()):
        s = raw_input()
        A = min(A, sum(c == 'a' for c in s))
        B = min(B, sum(c == 'b' for c in s))
    print min(A, B)
``

Here’s a shorter (and codegolfier) implementation:

``from collections import Counter
for cas in xrange(input()):
    print min(min(Counter(raw_input()+'ab').values()) for i in xrange(input()))-1
``

**Bonus question**: Does the above algorithm still work if the alphabet were larger than \{a,b\}?

### Time Complexity:

O(nm)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter](https://www.codechef.com/download/Solutions/DEC15/Setter/ORACLCS.cpp)

[Tester](https://www.codechef.com/download/Solutions/DEC15/Tester/ORACLCS.cpp)

[Editorialist](https://www.codechef.com/download/Solutions/DEC15/Editorialist/ORACLCS.py)

</details>
