# Chef and String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHRL2 |
| Difficulty Rating | 1751 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [CHRL2](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CHRL2) |

---

## Problem Statement

###  Read problems statements in [Russian](https://www.codechef.com/download/translated/LTIME08/russian/CHRL2.pdf) also.

Chef likes playing with strings. The most interesting game are named "CHEF in string". The move of the game consists of the following: Chef takes a **subsequence** of string's letters that form the word "CHEF" and then he removes that symbols. The goal of the game is to make the maximal number of moves. Please, help Chef and tell him the maximal possible number of moves that he is able to make for the given string **S**.

### Input

 The first line of each test case contains a given string. This string consists of uppercase letters from the set {"C", "H", "E", "F"}.

### Output

Output a single line containing the maximal possible number of moves.

### Constraints

- **1 ** ≤ **|S|** ≤ **100000**

### Scoring
Subtask 1 (25 points): **|S|** ≤ 2000

Subtask 2 (75 points):  See the constraints.

---

## Examples

**Example 1**

**Input**

```text
CHEFCHEFFFF
```

**Output**

```text
2
```

**Explanation**

- In the first move, Chef can pick the subsequence $[1, 2, 3, 4]$. Thus the characters at these indices are `C`, `H`, `E`, and `F`. Chef removes this subsequence. The remaining string is `CHEFFFF`.
- In the second move, Chef can pick the indices $[1, 2, 3, 4]$ of the remaining string `CHEFFFF` as the subsequence. The characters at these indices are `C`, `H`, `E`, and `F`. Chef removes this subsequence. The remaining string is `FFF`.
- Chef cannot make any more valid moves.

**Example 2**

**Input**

```text
CHHHEEEFFCC
```

**Output**

```text
1
```

**Explanation**

- In the first move, Chef can pick the subsequence $[1, 2, 5, 8]$. Thus the characters at these indices are `C`, `H`, `E`, and `F`. Chef removes this subsequence. The remaining string is `HHEEFCC`.
- Chef cannot make any more valid moves.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Contest](http://www.codechef.com/LTIME08/problems/CHRL2)

[Practice](http://www.codechef.com/problems/CHRL2)

**Author**: [Roman Furko](http://www.codechef.com/users/furko)

**Tester**: [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Editorialist**: [Vinod Reddy](http://www.codechef.com/users/vinodreddy@iitb)

### DIFFICULTY:

simple

### PREREQUISITES:

basic dp

### EXPLANATION

**Subtask 1:**

We will implement an O(N^2) algorithm for this subtask as N < 2000 this will pass. So the main observation of this algorithm is that consider the ‘F’ with smallest index such that there exists a subsequence ending at this ‘F’ with characters ‘C’,’H’,’E’,’F’.Now consider such a subsequence T {‘C’,’H’,’E’,’F’}. Now this ‘F’ should be removed from the string in one of the moves in the optimal solution or else if this ‘F’ is not removed and the ‘E’ is removed then we can exchange the ‘F’ removed with the ‘E’ with our ‘F’. if ‘E’ is also not removed then we can extend our logic to ‘H’. if ‘H’ is not removed then we extend the same logic to ‘C’. It cannot be that all of the four characters are not removed.

Now when we remove this ‘F’ in a move it can always be removed along with the nearest ‘E’ to the left of it because if it’s not the case either ‘E’ is not removed at all in which case the presently used ‘E’ can be replaced with the nearest ‘E’ or this ‘E’ is used with another ‘F’ in which case the ‘CHE’ of second ‘F’ can be exchanged with ‘CHE’ of the first. Similarly we ‘H’ be the nearest one to the  left of chosen ‘E’ and similar case for ‘C’. So we find such subsequence and remove those four characters and repeat the same procedure for remaining string

So for example lets take the string CHECHFECF.

``1  2  3 4  5 6  7 8  9
C H E C H F E C F
``

The first ‘F’ with a sequence possible will be the one at position 6. And the corresponding ‘E’ will be the one at position 3 and ‘H’ at 2 and C at 1. When we remove the characters we will be left with CHECF and again we follow same logic and remove one more ‘CHEF’.

Implementation :

It can be implemented in O(N^2). You can use a boolean array to track whether a symbol is removed or not and for each ’F’ from left to right try to find the first ‘E’ to the left of it  which is not removed and then first ‘H’ which not removed to the left of ‘E’ and then ‘C’. Then remove these characters by making their tracking variables to true. It’s easy to implement. For the code please check editorials solution.

Subtask 2 :

This is almost same as above algorithm but just a good implementation.

Since at every time in the above algorithm we check for the nearest next character to left which is not used (for ‘F’ we check for nearest left ‘E’,for ‘E’ we check for ‘H’,for ‘H’ we check for ‘C’) we will precompute the information. We will maintain four vectors one each for positions of each of characters ‘C’,’H’,’E’,’F’. so the arrays will be P[char][int[]].

We loop from left to right. Whenever ‘C’ comes we insert it’s position into P[‘C’] . Whenever we encounter ‘H’ we check if P[‘C’] is empty. If it’s empty then this ‘H’ is not useful as we cannot use it to form a subsequence so we throw it away. If P[‘C’] is not empty then we can map ‘H’ to the last position in P[‘C’] and so whenever ‘H’ is used we use it with ‘C’. Since the ‘C’ is mapped to ‘H’ we just remove the last element of P[‘C’]. So the array P[‘H’] are positions of ‘H’ for which there is a ‘C’ mapping and not mapped to any ‘E’. whenever ‘E,’F’’ comes we do the same thing as ‘H’. So finally the elements of C[‘F’] contains positions of ‘F’ for which there is a mapping to ‘E’ and this ‘E’ has a mapping to ‘H’ and this ‘H’ has a mapping to ‘C’.So finally no of elements in C[‘F’] will be our answer.

Here  a simple observation will help. We really need not maintain the positions in P[char][int[]]. We just need to know the size of P[‘C’],P[‘H’],P[‘E’],P[‘F’].So now new array will be NP[char][int] .When removing element originally in P[‘C’],P[‘E’],P[‘H’] we just decrease the value in NP[‘C’],NP[‘H’],NP[‘E’].  When we were inserting before we just increase the value against character. See the setter’s code for exact implementation.

### SOLUTIONS

**Setter’s Solution**: [CHRL2.cpp](http://www.codechef.com/download/Solutions/LTIME08/Setter/CHRL2.cpp)

**Tester’s Solution**: [CHRL2.cpp](http://www.codechef.com/download/Solutions/LTIME08/Tester/CHRL2.cpp)

**Editorialist’s Solution**: [CHRL2.cpp](http://www.codechef.com/download/Solutions/LTIME08/Editorialist/CHRL2.cpp)

</details>
