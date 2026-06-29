# Find the Maximum Value

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LOSTMAX |
| Difficulty Rating | 1392 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [LOSTMAX](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/LOSTMAX) |

---

## Problem Statement

The Chef had a box with **N** numbers arranged inside it: **A1**, **A2**, ..., **AN**. He also had the number **N** at the front, so that he knows how many numbers are in it. That is, the box actually contains **N**+1 numbers. But in his excitement due the ongoing [IOI](http://ioi2017.org/), he started dancing with the box in his pocket, and the **N**+1 numbers got jumbled up. So now, he no longer knows which of the **N**+1 numbers is **N**, and which the actual numbers are.

He wants to find the largest of the **N** numbers. Help him find this.

### Input

- The first line of the input contains an integer **T**, denoting the number of test cases. The description of each testcase follows.

- Each of the next **T** lines will contain **N** and **N** numbers, but it is not guaranteed that **N** is the first number.

### Output

 For each test case, output a single line containing the maximum value of the **N** numbers in that testcase.

### Constraints

- 1 ≤ **T** ≤ 100

- 1 ≤ **N** ≤  50

- 1 ≤ **Ai** ≤ 109

---

## Examples

**Example 1**

**Input**

```text
3
1 2 1
3 1 2 8
1 5 1 4 3 2
```

**Output**

```text
1
8
4
```

**Explanation**

**Test case 1:**

** N** = 2 and the numbers are {1, 1}. The maximum among these 2 numbers is 1, and hence the output is 1.

**Test case 2:**

** N** = 3 and the numbers are {1, 2, 8}. The maximum among these 3 numbers is 8, and hence the output is 8.

**Test case 3:**

** N** = 5 and the numbers are {1, 1, 4, 3, 2}. The maximum among these 5 numbers is 4, and hence the output is 4.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 1 2 8
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
1 5 1 4 3 2
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK** -

[Practice](https://www.codechef.com/problems/LOSTMAX)

[Contest](https://www.codechef.com/LTIME50/problems/LOSTMAX)

Author and Editoriallist - [AmirReza PoorAkhavan](https://www.codechef.com/users/arpa)

Tester - [MohammadSina Pakseresht](https://www.codechef.com/users/msina)

Second Tester - [Shayan CheshmJahan](https://www.codechef.com/users/shayan1999)

**DIFFICULTY** –

Cakewalk

**PREREQUISITES** –

Nothing.

### PROBLEM

Given a list of N + 1 numbers, N mixed up with them, find the maximum number between this N numbers.

### EXPLANATION

Let A be the original list of size N. The number N was added in this list. Let the updated list be B. We can find the list A from the list B by finding any occurrence of the number N  and deleting it. Finding maximum in a list can be done by iterating over its elements in linear time.

**Parsing the input into a list of integers**

For reading a line from standard input, you can use

`` getline(cin, s)
``

, it will read a line and save it in string s.

``

You can parse the input string into integers as follows. Use [string stream][4], read a line by
``

getline

`` and put it into some stringstream, then read ints one by one until it has some. You can check if it has some using
``

ss >> a

``, it will return false if nothing is remained in stringstream (see my code for better understanding).

**IMPLEMENTATION** -

Setter's code - [here][1] (using getline and stringstream).

Tester's code - [here][2] (using getline and parsing the input manually).

Second tester's code - [here][3] (using getline and parsing the input manually).

[1]: http://www.codechef.com/download/Solutions/LTIME50/Setter/LOSTMAX.cpp
[2]: http://www.codechef.com/download/Solutions/LTIME50/Tester1/LOSTMAX.cpp
[3]: http://www.codechef.com/download/Solutions/LTIME50/Tester2/LOSTMAX.cpp
[4]: http://www.cplusplus.com/reference/sstream/stringstream/``

</details>
