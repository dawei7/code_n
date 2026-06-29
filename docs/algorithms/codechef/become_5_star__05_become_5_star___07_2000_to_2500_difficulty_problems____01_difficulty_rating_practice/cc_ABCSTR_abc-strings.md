# ABC-Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ABCSTR |
| Difficulty Rating | 2264 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ABCSTR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ABCSTR) |

---

## Problem Statement

Mike likes strings. He is also interested in algorithms. A few days ago he discovered for himself a very nice problem:

*
You are given an AB-string **S**. You need to count the number of substrings of S, which have an equal number of 'A'-s and 'B'-s.
*

Do you know how to solve it? Good. Mike will make the problem a little bit more difficult for you.

*
You are given an ABC-string **S**. You need to count the number of substrings of S, which have an equal number of 'A'-s, 'B'-s and 'C'-s.
*

A string is called AB-string if it doesn't contain any symbols except 'A' or 'B'. A string is called ABC-string if it doesn't contain any symbols except 'A', 'B' or 'C'.

### Input

The first line of the input contains an ABC-string **S**.

### Output

Your output should contain the only integer, denoting the number of substrings of **S**, which have an equal number of 'A'-s, 'B'-s and 'C'-s.

The answer can go above a 32-bit integer. Please, use 64-bit integers for storing and processing data.

### Constraints

1 ≤ **|S|** ≤  1 000 000; where **|S|** denotes the length of the given ABC-string.

### Example
`**Input:**
ABACABA

**Output:**
2
`

### Explanation

In the example you should count **S**[2..4] = "BAC" and **S**[4..6] = "CAB".

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/ABCSTR)

[Contest](http://www.codechef.com/COOK44/problems/ABCSTR)

**Author:** [Konstantin Sokol](http://www.codechef.com/users/kostya_by)

**Tester:** [Gerald Agapov](http://www.codechef.com/users/gerald)

**Editorialist:** [Tasnim Imran Sunny](http://www.codechef.com/users/rustinpiece)

### DIFFICULTY:

Simple

### PREREQUISITES:

Ad-Hoc, Map

### PROBLEM:

Given a string **S** which is consisted of characters ‘A’, ‘B’ or ‘C’. Find the number of substrings of **S** which have equal number of ‘A’s, ‘B’s and ‘C’s.

### EXPLANATION:

Let,

Ai = Number of ‘A’s in **S** between the indexes 1 and i (inclusive).

Bi = Number of ‘B’s in **S** between the indexes 1 and i (inclusive).

Ci = Number of ‘C’s in **S** between the indexes 1 and i (inclusive).

Let’s consider the substring **Sj…i** :

Number of ‘**A**’-s in that substring =  **Ai - Aj-1**

Number of ‘**B**’-s in that substring =  **Bi - Bj-1**

Number of ‘**C**’-s in that substring =  **Ci - Cj-1**

So for that substring to be good:

**Ai - Aj-1 = Bi - Bj-1 = Ci - Cj-1**

Alternatively the following two conditions are enough for that substring to be good:

**Ai - Bi = Aj-1 - Bj-1

Ai - Ci = Aj-1 - Cj-1**

Go from left to right and for each index **i** find the number of valid good substrings which ends at **i**. The number of such substrings would be the number of indexes **k (k < i)** where **(Ai - Bi, Ai - Ci )= (Ak - Bk, Ak - Ck )**. That can be obtained if the pair **(Ak - Bk, Ak - Ck** )for all **k** are stored in a key-value storage where the key being the pair and value being the number indexes having that difference pair. If using C++, [STL Map](http://www.cprogramming.com/tutorial/stl/stlmap.html) can be used.

The author did not use a map, instead he computed all the difference pairs and then sorted those and then find the number of equal pairs.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/COOK44/Setter/ABCSTR.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/COOK44/Tester/ABCSTR.cpp).

</details>
