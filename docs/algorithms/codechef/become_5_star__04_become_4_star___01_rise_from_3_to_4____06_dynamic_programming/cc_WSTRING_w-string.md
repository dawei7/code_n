# W String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WSTRING |
| Difficulty Rating | 1809 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [WSTRING](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/WSTRING) |

---

## Problem Statement

Kira likes to play with strings very much. Moreover he likes the shape of 'W' very much. He takes a string and try to make a 'W' shape out of it such that each angular point is a '#' character and each sides has same characters. He calls them *W strings*.

For example, the *W string* can be formed from "aaaaa#bb#cc#dddd" such as:

`
    a
     a             d
      a     #     d
       a   b c   d
        a b   c d
         #     #
`

He also call the strings which can generate a 'W' shape (satisfying the above conditions) *W strings*.

More formally, a string **S** is a *W string* if and only if it satisfies the following conditions (some terms and notations are explained in **Note**, please see it if you cannot understand):

- The string **S** contains **exactly** **3** '#' characters. Let the indexes of all '#' be **P1 < P2 < P3** (indexes are **0**-origin).

- Each substring of **S[0, P1−1], S[P1+1, P2−1], S[P2+1, P3−1], S[P3+1, |S|−1]** contains exactly one kind of characters, where **S[a, b]** denotes the non-empty substring from **a+1**th character to **b+1**th character, and **|S|** denotes the length of string **S** (See **Note** for details).

Now, his friend Ryuk gives him a string **S** and asks him to find the length of the longest *W string* which is a subsequence of **S**, with only one condition that there must not be any '#' symbols between the positions of the first and the second '#' symbol he chooses, nor between the second and the third (here the "positions" we are looking at are in **S**), i.e. suppose the index of the '#'s he chooses to make the *W string* are **P1, P2, P3** (in increasing order) in the original string **S**, then there must be no index **i** such that **S[i]** = '#' where **P1 < i < P2 or P2 < i < P3**.

Help Kira and he won't write your name in the **Death Note**.

**Note**:

For a given string **S**, let **S[k]** denote the **k+1**th character of string **S**, and let the index of the character **S[k]** be **k**. Let **|S|** denote the length of the string **S**. And a substring of a string **S** is a string **S[a, b] = S[a] S[a+1] ... S[b]**, where **0 ≤ a ≤ b < |S|**. And a subsequence of a string **S** is a string **S[i0] S[i1] ... S[in−1]**, where **0 ≤ i0 < i1 < ... < in−1 < |S|**.

For example, let **S** be the string "kira", then **S[0]** = 'k', **S[1]** = 'i', **S[3]** = 'a', and **|S| = 4**. All of **S[0, 2]** = "kir", **S[1, 1]** = "i", and **S[0, 3]** = "kira" are substrings of **S**, but "ik", "kr", and "arik" are not. All of "k", "kr", "kira", "kia" are subsequences of **S**, but "ik", "kk" are not.

From the above definition of *W string*, for example, "a#b#c#d", "aaa#yyy#aaa#yy", and "o#oo#ooo#oooo" are *W string*, but "a#b#c#d#e", "#a#a#a", and "aa##a#a" are not.

### Input

First line of input contains an integer **T**, denoting the number of test cases. Then **T** lines follow. Each line contains a string **S**.

### Output

Output an integer, denoting the length of the longest *W string* as explained before. If **S** has no *W string* as its subsequence, then output **0**.

### Constraints

- **1 ≤ T ≤ 100 **

- **1 ≤ |S| ≤ 10000 (104)**

- **S** contains no characters other than lower English characters ('a' to 'z') and '#' (without quotes)

---

## Examples

**Example 1**

**Input**

```text
3
aaaaa#bb#cc#dddd
acb#aab#bab#accba
abc#dda#bb#bb#aca
```

**Output**

```text
16
10
11
```

**Explanation**

In the first case: the whole string forms a *W String*.

In the second case: acb#aab#bab#accba, the longest *W string* is ac**b#aa**b**#b**a**b#a**ccb**a**

In the third case: abc#dda#bb#bb#aca, note that even though **a**bc**#dd**a**#bb**#**bb#a**c**a** (boldened characters form the subsequence) is a *W string* of length **12**, it violates Ryuk's condition that there should not be any #'s inbetween the **3** chosen # positions. One correct string of length **11** is **a**bc#dd**a#bb#bb#a**c**a**

**Separated test cases**

#### Test case 1

**Input for this case**

```text
aaaaa#bb#cc#dddd
```

**Output for this case**

```text
16
```



#### Test case 2

**Input for this case**

```text
acb#aab#bab#accba
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
abc#dda#bb#bb#aca
```

**Output for this case**

```text
11
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/WSTRING)

[Contest](http://www.codechef.com/JUNE13/problems/WSTRING)

# Difficulty:

Easy

# Pre-requisites:

Dynamic Programming

# Problem:

A W-String is defined as a string consisting of lower-case alphabets, and exactly 3 "#"s that divide the string into 4 non-empty contiguous parts, where each part consists of the same alphabet. Given a string S, find the length of the longest W-String that is a subsequence of S, with the added constraint that the three chosen #-positions in W, are consecutive #-positions in S.

# Explanation:

Let us suppose that we choose our three #-positions as P1, P2 and P3. After fixing P1, P2, P3, we greedily choose the most frequent character from [0, P1-1], [P1+1, P2-1], [P2+1, P3-1], [P3+1, N-1]. We further should disregard cases when any one of the above yields an “empty” string.

Let cnt[i][k] = Number of times character k occurs in S[0…i]. Then, given P1, P2, P3, we just need to calculate

max(cnt[P1][k] : 1<=k<=26) (greedy choice of character in [0, P1-1]

-

1 (# character)

-

max(cnt[P2][k] - cnt[P1][k] : 1<=k<=26) (greedy choice of character in [P1+1, P2-1]

-

1 (# character)

-

max(cnt[P3][k] - cnt[P2][k] : 1<=k<=26) (greedy choice of character in [P2+1, P3-1]

-

1 (# character)

-

max(cnt[N-1][k] - cnt[P1][k] : 1<=k<=26) (greedy choice of character in [P3+1, N-1],

for all potential W-Strings (that is, they have all “greedy choice of character” values > 0).

Precomputing values of cnt[i][k] will take time O(N * 26). Further, we can iterate over all consecutive P1,P2,P3 in O(N) time, and each will lead to a calculation of 26 time. Thus overall complexity will be O(N * 26 * T). This can  be sped up by a constant factor by precomputing MaxLeft(i) and MaxRight(i) which will find the maximum frequency of a single letter to the left or to the right of position i respectively.

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/June/Setter/WSTRING.cpp)

# Tester’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/June/Tester/WSTRING.cpp)

</details>
