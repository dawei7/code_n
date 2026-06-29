# Chef and Proportion

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFCBA |
| Difficulty Rating | 1122 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CHEFCBA](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CHEFCBA) |

---

## Problem Statement

Chef recently learned about ratios and proportions. He wrote some positive integers **a, b, c, d** on a paper. Chef wants to know whether he can shuffle these numbers so as to make some proportion? Formally, four numbers **x, y, z, w** are said to make a proportion if ratio of **x : y** is same as that of **z : w**.

### Input

Only line of the input contains four space separated positive integers - **a, b, c, d**.

### Output

Print "Possible" if it is possible to shuffle **a, b, c, d** to make proportion, otherwise "Impossible" (without quotes).

### Constraints

- 1 ≤ **a, b, c, d ** ≤ 1000

---

## Examples

**Example 1**

**Input**

```text
1 2 4 2
```

**Output**

```text
Possible
```

**Explanation**

By swapping 4 and the second 2, we get 1 2 2 4. Note that 1 2 2 4 make proportion as 1 : 2 = 2 : 4. Hence answer is "Possible"

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFCBA)

[Contest](http://www.codechef.com/COOK72/problems/CHEFCBA)

**Author:** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Tester:** [Karan Aggarwal](https://www.codechef.com/users/karanaggarwal)

**Editorialist:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

### DIFFICULTY:

Simple

### PREREQUISITES:

None

### PROBLEM:

Given four numbers a, b, c, d, tell whether it is possible to pair them up such that a:b is equal to c:d. We are allowed to shuffle the order of the numbers.

### EXPLANATION:

We can simply try all the possible pairings. A way to model this is to cycle through all the permutations of the four numbers, pair up the first two together and the last two together. Then find the ratio of the first two and the last two; if they are equal, output “Possible”, else “Impossible”. Cycling through permutations can be done through functions like next\_permutation in the C library or simply by recursion. Either way works since we just have 4 numbers.

A more intelligent solution is to sort the four numbers and pair up the first 2 together and the last 2 together and check their ratios. This works because ratios are symmetric.

For checking the ratio equality, we can use an simple property that if a:b = c:d then a*d = b*c. This way, we can avoid dealing with floats.

Please see editorialist’s/setter’s program for implementation details.

### COMPLEXITY:

\mathcal{O}(1)

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/COOK72/Setter/CHEFCBA.cpp)

[Tester](http://www.codechef.com/download/Solutions/COOK72/Tester/CHEFCBA.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/COOK72/Editorialist/CHEFCBA.cpp)

[Admin](http://www.codechef.com/download/Solutions/COOK72/Admin/CHEFCBA.cpp)

</details>
