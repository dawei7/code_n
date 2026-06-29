# Studying Alphabet

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALPHABET |
| Difficulty Rating | 1123 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [ALPHABET](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/ALPHABET) |

---

## Problem Statement

Not everyone probably knows that Chef has younger brother Jeff. Currently Jeff learns to read.

He knows some subset of the letter of Latin alphabet. In order to help Jeff to study, Chef gave him a book with the text consisting of **N** words. Jeff can read a word if it consists only of the letters he knows.

Now Chef is curious about which words his brother will be able to read, and which are not. Please help him!

### Input

The first line of the input contains a lowercase Latin letter string **S**, consisting of the letters Jeff can read. Every letter will appear in **S** no more than once.

The second line of the input contains an integer **N** denoting the number of words in the book.

Each of the following **N** lines contains a single lowercase Latin letter string **Wi**, denoting the **i**th word in the book.

### Output

For each of the words, output "Yes" (without quotes) in case Jeff can read it, and "No" (without quotes) otherwise.

### Constraints

- **1** ≤ **|S|** ≤ **26**

- **1** ≤ **N** ≤ **1000**

- **1** ≤ **|Wi|** ≤ **12**

- Each letter will appear in **S** no more than once.

- **S, Wi** consist only of lowercase Latin letters.

### Subtasks

- **Subtask #1 (31 point)**: **|S|** = **1**, i.e. Jeff knows only one letter.

- **Subtask #2 (69 point)**	: no additional constraints

---

## Examples

**Example 1**

**Input**

```text
act
2
cat
dog
```

**Output**

```text
Yes
No
```

**Explanation**

The first word can be read.

The second word contains the letters d, o and g that aren't known by Jeff.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ALPHABET)

[Contest](https://www.codechef.com/LTIME39/problems/ALPHABET)

**Author:** [Sergey Kulik](https://www.codechef.com/users/xcwgf666)

**Tester:** [Harshil Shah](https://www.codechef.com/users/harshil7924)

**Editorialist:** [Pawel Kacprzak](https://www.codechef.com/users/pkacprzak)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

Strings, Implementation

### PROBLEM:

For a fixed set of Latin letters **S**, for each of given **N** words decide if it can be formed using only letters from **S**.

### QUICK EXPLANATION:

For each of given words, check if all its letters are in the given set of known letters **S** by iterating over letters in **S** explicitly or using any data structure with fast lookup operation.

### EXPLANATION:

## Subtask 1

In the first subtask, the set **S** contains exactly one letter. In this case, it is very easy to decide if a given word can be formed using only letters from **S**, because there is only one letter that can be used, so for example if the letter in **S** is **c**, then all possible words that can be written using it are: **c, cc, ccc, …**. Since the length of any word in the input can be at most 12, then there are exactly 12 different words for which the answer is `"Yes"`. For all other words the answer is `“No”`, because each of them contains at least one letter not in **S**.

## Subtask 2

In the second subtask, **S** can contain at most 26 letters. In this case, for a given input word **W**, we want to check if all its letters are in **S**. In order to do that, we can iterate over all letters of **W** and for each one check if it is in **S**. Since **S** is very small, that check can be performed actually by iterating over all letters in **S** explicitly. The answer is `“Yes”` if all letters of **W** are in **S**, otherwise the answer is `“No”`. Thus, for a single word **W**, the answer can be computed in **O(|W| * |S|)** time, so the total running time is **O(|total_len|*|S|)**, where **total_len** is the sum of lengths of all **N** words in the input.

For a faster solution, first we can store letters from **S** in any data structure that provides fast lookup - array will work the best here, since there are at most 26 different letters, but hash table is also fine here. If array is used this step building the array takes **O(|S|)** time. Then, for a given input word **W**, we can check if all of its letters are in **S** using the lookup in our data structure. It follows that the total running time of this method is **O(|S|+|total_len|)**, where **total_len** is the sum of lengths of all **N** words in the input.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Tester’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME39/Tester/ALPHABET.cpp).

Editorialist’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME39/Editorialist/ALPHABET.cpp).

</details>
