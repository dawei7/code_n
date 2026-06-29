# Bear and AB

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ABREPEAT |
| Difficulty Rating | 1754 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [ABREPEAT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/ABREPEAT) |

---

## Problem Statement

Limak has a string **S**, that consists of **N** lowercase English letters.
Limak then created a new string by repeating **S** exactly **K** times.
For example, for **S** = "abcb" and **K** = 2, he would get "abcbabcb".

Your task is to count the number of subsequences "ab" (not necessarily consecutive) in the new string.

In other words, find the number pairs of indices i < j, such that the i-th and j-th characters in the new string are 'a' and 'b' respectively.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains two integers **N** and **K**, denoting the length of the initial string **S** and the number of repetitions respectively.

The second line contains a string **S**.
Its length is exactly **N**, and each of its characters is a lowercase English letter.

### Output

For each test case, output a single line containing one integer — the number of subsequences "ab" in the new string.
For the given constraints, it can be proved that the answer fits in the 64-bit signed type.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 105

- 1 ≤ **N** * **K** ≤ 109 (in other words, the new string has length up to 109)

---

## Examples

**Example 1**

**Input**

```text
3
4 2
abcb
7 1
aayzbaa
12 80123123
abzbabzbazab
```

**Output**

```text
6
2
64197148392731290
```

**Explanation**

**Test case 1.** Limak repeated the string "abcb" 2 times, and so he got "abcbabcb". There are 6 occurrences of the subsequence "ab":

- ABcbabcb (the two letters marked uppercase)

- AbcBabcb

- AbcbaBcb

- AbcbabcB

- abcbABcb

- abcbAbcB

**Test case 2.** Since **K** = 1, the new string is equal to the given **S** ("aayzbaa"). There are 2 occurrences of the subsequence "ab" in this string: AayzBaa and aAyzBaa.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2
abcb
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
7 1
aayzbaa
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
12 80123123
abzbabzbazab
```

**Output for this case**

```text
64197148392731290
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ABREPEAT)

[Contest](https://www.codechef.com/COOK81/problems/ABREPEAT)

**Author:** [Kamil Debowski](https://www.codechef.com/users/errichto)

**Primary Tester:** [Marek Soko?owski](https://www.codechef.com/users/mnbvmar)

**Secondary Tester:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

**Editorialist:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

### DIFFICULTY:

simple

### PREREQUISITES:

combinatorics

### PROBLEM:

You are provided a string s of length N. Suppose t be the string formed by concatenating the string s K times, i.e. t = s + s + \dots + s (K times). We want to find the number of occurrences of subsequence “ab” in it.

### Finding number of subsequences “ab” in a given string s.

Finding number of subsequences “ab” in a given string s is same as finding number of pair of indices (i, j), i < j such that s_i = ‘a’ and s_j = ‘b’. The brute force way of iterating over all such pairs of indices i, j and checking the conditions s_i = ‘a’ and s_j = ‘b’ would be \mathcal{O}({|s|}^2).

However, you can do better. In fact, you can find this in a single pass over the string in \mathcal{O}(|s|) time. Consider an index j such that s_j = ‘b’, suppose we want to find number of i's such that i < j and s_i =  ‘a’. It will be same as number of occurrences of character ‘a’ till position j. We can maintain the count of a’s by iterating over the array from left to right. This way, we will be able to find the  answer in single iteration over the string s in \mathcal{O}(|s|) time. Pseudo code follows.

``cnta = 0;
ans = 0;
for i = 1 to |s|:
    if s[i] == a:
        cnta++;
    if s[i] == b:
        ans += cnta;
``

### Can we use this idea directly?

Now we construct the string t and find the number of subsequences “ab” in it in \mathcal{O}(|t|) time, which will be \mathcal{O}(N \cdot K). Constraints of the problem say that N \cdot K could go up to 10^9. So, this won’t work in time.

### Towards a counting based solution idea.

Let t = s_1 + s_2 + s_3 + \dots + s_K, where s_i = s. We call s_i the i-th occurrence of string s.

Let us view the occurrences of subsequence “ab” in t as follows. One of the below two cases can happen.

-

“ab” lies strictly inside some occurrence of string s in t, i.e. “ab” lies strictly inside some s_i. We can find the number of occurrences of “ab” in s. Let us denote it by C. The total number of occurrences “ab” in this case will be C \cdot K.

-

In the other case, “a” lies inside some string s_i, whereas “b” lies in some other string s_j such that i < j. Finding the number of occurrences of “ab” in this case will be same as choosing the two strings s_i, s_j (\binom{K}{2} ways), and multiplying it by the number of occurrences of “a” in s_i (denote by cnt_a) and the number of occurrences of “b” in s_j (denote by cnt_b), i.e. \binom{K}{2} \cdot cnt_a \cdot cnt_b. As s_i = s, cnt_a will be number of occurrences of “a” in s and cnt_b will be the number of occurrences of “b” in s.

We can find C, cnt_a, cnt_b in \mathcal{O}(N) time. Thus, overall time complexity of this approach is \mathcal{O}(N) which will easily pass in time for N \leq 10^5. Pseudo code follows.

``cnta = 0
cntb = 0;
C = 0;
for i = 1 to N:
    if s[i] == 'a':
        cnta++;
    if s[i] == 'b':
        cntb++;
        C += cnta;
// First case, i.e. "ab" lies strictly inside some occurences of s, i.e. s_i in t
ans = C * K
// The other case, i.e. "a" lies inside some string s_i, where as "b" lies in other string s_j such that i < j
ans += K * (K - 1) / 2 * cnta * cntb ;
``

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter](http://www.codechef.com/download/Solutions/COOK81/Setter/ABREPEAT.cpp)

[Tester1](http://www.codechef.com/download/Solutions/COOK81/Tester1/ABREPEAT.cpp)

[Tester2](http://www.codechef.com/download/Solutions/COOK81/Tester2/ABREPEAT.java)

</details>
