# Chef and Hamming Distance of arrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFHAM |
| Difficulty Rating | 1790 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [CHEFHAM](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CHEFHAM) |

---

## Problem Statement

### Read problems statements in [Vietnamese](https://www.codechef.com/download/translated/DEC17/vietnamese/CHEFHAM.pdf) .

Chef likes to work with arrays a lot. Today he has an array **A** of length **N** consisting of positive integers. Chef's little brother likes to follow his elder brother, so he thought of creating an array **B** of length **N**. The little brother is too small to think of new numbers himself, so he decided to use all the elements of array **A** to create the array **B**. In other words, array **B** is obtained by shuffling the elements of array **A**.

The little brother doesn't want Chef to know that he has copied the elements of his array **A**. Therefore, he wants to create the array **B** in such a way that the *Hamming distance* between the two arrays **A** and **B** is maximized. The Hamming distance between **A** and **B** is the number of indices **i** (1 ≤ **i** ≤ **N**) such that **Ai ≠ Bi**.

The brother needs your help in finding any such array **B**. Can you please find one such array for him?

Note that it's guaranteed that no element in **A** appears more than twice, i.e. frequency of each element is at most 2.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains an integer **N** denoting the length of the array **A**.

- The second line contains **N** space-separated integers **A1, A2 ... AN**.

### Output

- For each test case, print two lines.

- The first line should contain the maximum possible Hamming distance that array **B** can have from array **A**.

- The second line should contain **N** space-separated integers denoting the array **B**; the **i**-th integer should denote the value of **Bi**. Note that **B** should be an array obtained after shuffling the elements of **A**.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 105

- 1 ≤ **Ai** ≤ 105

- The frequency of each integer in the array **A** will be at most 2.

### Subtasks

**Subtask #1 (30 points):** all elements in the array **A** are unique

**Subtask #2 (30 points):** 5 ≤ **N** ≤ 105

**Subtask #3 (40 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2
1 2
3
1 2 1
4
2 6 5 2
```

**Output**

```text
2
2 1
2
2 1 1
4
6 2 2 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFHAM)

[Contest](http://www.codechef.com/DEC17/problems/CHEFHAM)

**Author:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

**Tester:** [Mugurel Ionut Andreica](http://www.codechef.com/users/mugurelionut)

**Editorialist:** [Kirill Gulin](http://www.codechef.com/users/kefaa)

# PROBLEM

You’re given an array a of size N, each number in the array appears no more than twice. Shuffle the array in such a way that the Hamming distance between the original and the shuffled array is maximized. The Hamming distance between two arrays a and b is the number of indexes i such that a_i \neq b_i.

### QUICK EXPLANATION

Count how many numbers in the array have their frequences equal to 1 or 2. Solve the problem depending on are these numbers more than 1.

### EXPLANATION

## Subtask 1

All elements in the array are unique. Just cyclically shift the array. So for the first substask the answer is 0 if N = 1 and N if N \geq 2.

## Subtask 2

If you pass only the second subtask it means you missed some corner cases while solving the 3rd subtask.

#### Subtask 3

For each number existing in the array count its frequence. Suppose there are x numbers with their frequence equal to 1 and y numbers with frequence equal to 2.

Suppose x, y \geq 2. We can separately shuffle the numbers with frequence 1 and with frequence 2,  getting the answer equal to N for this case. Shuffling here and below means you’ll need to write out indexes of number’s entries and set the other number on its entries (for example, cyclically shift the array of indexes by 1). For example, if the array is [a, b, c, d, d, c] you’ll get an array [b, a, d, c, c, d] after such a shuffle.

There are two ways of solving the problem now: random shuffle and dealing with corner cases.

### The first way

Random shuffle the array several times and choose the one with the maximum Hamming distance. The answer you’ve got is correct with high enough probability.

### The second way

Suppose x = 1 and y \geq 2. Then shuffle only the numbers with frequence 2 and swap the number with frequence 1 with any other number.

Suppose x \geq 2 and y = 1. Then shuffle only the numbers with frequence 1 and swap the indexes of the number with frequence 2 with any two other different indexes.

After these cases, N \leq 4 so you can try all possible shuffles of the array in O(N!) time. But still sorting out the cases is possible

If x = 2, y = 0 then N = 2. Just swap the values.

Cases with x = 0, y = 2 or x = y = 1 or x = 1, y = 0 or x = 0, y = 1 are left. For any of them you can cyclically shift the array twice. Calculate the Hamming distance and print the answer.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/DEC17/Setter/CHEFHAM.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/DEC17/Tester/CHEFHAM.cpp).

</details>
