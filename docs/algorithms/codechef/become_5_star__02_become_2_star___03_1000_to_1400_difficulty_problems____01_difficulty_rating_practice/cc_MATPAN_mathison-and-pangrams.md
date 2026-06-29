# Mathison and pangrams

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATPAN |
| Difficulty Rating | 1127 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MATPAN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MATPAN) |

---

## Problem Statement

Mathison recently inherited an ancient papyrus that contained some text. Unfortunately, the text was not a **pangram** (a string using every letter of the Latin alphabet at least once). Now, Mathison has a particular liking for holoalphabetic strings and the text bothers him. The good news is that Mathison can buy letters from the local store in order to turn his text into a pangram.

  However, each letter has a price and Mathison is not very rich. Can you help Mathison find the cheapest way to obtain a pangram?

### Input

The first line of the input file will contain one integer, **T**, representing the number of tests.

Each test will be formed from two lines. The first one contains **26** space-separated integers, representing the prices of all letters.
  The second will contain Mathison's initial text (a string of **N** lowercase letters).

### Output

The output file will contain **T** lines, one for each test. Each line will contain the answer for the corresponding test.

### Constraints and notes

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 50,000

- All prices are natural numbers between 1 and 1,000,000 (i.e. 106).

- A pangram is a string that contains every letter of the Latin alphabet at least once.

- All purchased letters are added to the end of the string.

### Subtaks

**Subtask #1** (30 points):

- **N** = 1

**Subtask #2** (70 points):

- Original constraints

---

## Examples

**Example 1**

**Input**

```text
2
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
abcdefghijklmopqrstuvwz
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
thequickbrownfoxjumpsoverthelazydog
```

**Output**

```text
63
0
```

**Explanation**

`
First test
There are three letters missing from the original string: n (price 14), x (price 24), and y (price 25).
Therefore the answer is 14 + 24 + 25 = 63.

Second test
No letter is missing so there is no point in buying something. The answer is 0.
`

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
abcdefghijklmopqrstuvwz
```

**Output for this case**

```text
63
```



#### Test case 2

**Input for this case**

```text
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
thequickbrownfoxjumpsoverthelazydog
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](https://www.codechef.com/problems/MATPAN)

[Contest](https://www.codechef.com/LTIME51/problems/MATPAN)

**Author:** [Alexandru Valeanu](https://www.codechef.com/users/alexvaleanu)

**Tester:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Editorialist:** [Bhuvnesh Jain](https://www.codechef.com/users/likecs)

# Difficulty

CAKEWALK

# Prerequisites

Looping Techniques

# Problem

You are given a string consisting of letters and the cost of adding a specific character to it. You need to convert the string into a pangram, i.e. it contains all the lower case alphabets (a-z) in it. The cost of above operation is to be minimised.

# Explanation

### Subtask - 1

For this subtask, N = 1. This means the string contains only 1 lower case character. So, we would need to add all the remaining characters so that it becomes pangram. To minimise the cost, it is easy to see that we would add each character only once.

### Subtask - 2

Similar to above solution, we would like to only add those characters which are missing in the substring so that it becomes a pangram. Also, each character should be added only once to minimise the cost.

Thus, we need to find efficiently which characters occur in the string and which do not. To do this, we just maintain an array, of size equal to the alphabet size (in this case 26), such that all of it’s value are initialised to 0. Now, we simply traverse the array from left to right and set the corresponding character to 1 in the array. Thus, at the end of the loop, we just need to find the location of 0 in the above array and add the corresponding cost of the character to the answer.

# Time Complexity

O(n)

# Space Complexity

O(n + ALPHABET), where ALPHABET = number of lowercase characters (here 26)

# Solution Links

[Setter’s solution](http://www.codechef.com/download/Solutions/LTIME51/Setter/MATPAN.py)

[Tester’s solution](http://www.codechef.com/download/Solutions/LTIME51/Tester/MATPAN.cpp)

[Editorialist solution](http://www.codechef.com/download/Solutions/LTIME51/Editorialist/MATPAN.py)

</details>
