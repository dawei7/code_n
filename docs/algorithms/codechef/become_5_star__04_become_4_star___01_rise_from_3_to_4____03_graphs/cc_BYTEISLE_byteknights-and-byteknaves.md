# Byteknights and Byteknaves

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BYTEISLE |
| Difficulty Rating | 1919 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [BYTEISLE](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/BYTEISLE) |

---

## Problem Statement

A long school holiday has come, and you decided to visit the famous Byte Island. You know there are only two types of Bytelandians: Byteknights and Byteknaves. A Byteknight always tells the truth, whereas a Byteknave always lies.

It is known that there are *N* Bytelandians in the island, and now you meet all of them. You are curious about their types. Because you are a smart logician, you don't want to ask them questions that immediately reveal their types (that's too boring). Instead, to each Bytelandian you ask, "How many Byteknights are there here?"

To your surprise, they also don't answer your questions directly. Instead, the *i*-th Bytelandian answers of the form "The number of Byteknights here is between *ai* and *bi*, inclusive". You record all answers in your pocket note.

Now that you have collected all information you need, determine the type of each Bytelandian.

### Input

The first line contains a single integer *T*, the number of test cases. *T* test cases follow. The first line of each test case contains a single integer *N*. *N* lines follow. The *i*-th line contains two integers *ai* and *bi*.

### Output

For each test case, output two lines. In the first line, output a single integer indicating the number of different solutions, modulo 1000000007. In the next line, output the lexicographically smallest solution. A solution is a string consisting of *N* characters, where the *i*-th character of the string is '1' if the *i*-th Bytelandian is a Byteknight, or '0' in case of a Byteknave. It is guaranteed that there is at least one valid solution.

### Constraints

- 1 <= *T* <= 5

- 1 <= *N* <= 50000

- 0 <= *ai* <= *bi* <= *N*

---

## Examples

**Example 1**

**Input**

```text
3
1
0 1
4
1 4
2 4
3 4
4 4
3
1 2
0 0
1 3
```

**Output**

```text
1
1
5
0000
1
101
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/BYTEISLE/)

[Contest](http://www.codechef.com/DEC10/problems/BYTEISLE/)

### DIFFICULTY

EASY

### EXPLANATION

Note that the type of each Bytelandian is completely determined by the number of Byteknights in the island. Because there are between 0 and N Bytelandians, the number of solutions is actually only between 0 and N (modulo 1000000007 :P).

Firstly, we have to determine the number of Byteknights. Let knight[n] be the number of Bytelandian that satisfies a _ i <= n <= b _ i; that is, the number of Bytelandians that said it is possible to have n Byteknights in the island. It is easy to see that the number of Byteknights can be n iff knight[n] = n.

So, we need a data structure that can perform these operations efficiently:

- Increase the values of knight[a _ i]…knight[b _ i], for each Bytelandian i by 1

- Query the value of knight[i], for each 0 <= i <= N

Because all queries are needed only after the updates, the so-called ‘partial difference’ data structure suffices. Let diff[i] be knight[i]-knight[i-1]. Operation 1 can be simulated by increasing diff[a _ i] and decreasing diff[b _ i + 1]. Operation 2 is simply the sum of diff[1]…diff[i], which can be precalculated after the updates take place.

Secondly, we have to determine the lexicographically smallest solution. If it is possible for a Bytelandian to be a Byteknaves, then we should assign it Byteknaves, otherwise the solution would not be lexicographically smallest because ‘1’ is greater than ‘0’. A Bytelandian i can be assigned Byteknave iff there is n is a possible number of Byteknights (valid solution) and n is not in range a _ i…b _ i, i.e., he is lying.

A segment tree will perform the step efficiently. Let tree[n] = 1 if knight[n] = n, or 0 otherwise. Then we can query the number of valid solutions in a range in logarithmic time. After we decide that Bytelandian i is a Byteknave, we set all elements of the tree in the range a _ i…b _ i to zero. If it is not possible for Bytelandian i to be a Byteknave, because the number of valid solutions in the range a _ i … b _ i is the same of the number of valid solutions in the range 0…N, we must assign it a Byteknight.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/December/Setter/BYTEISLE.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/December/Tester/BYTEISLE.cpp).

</details>
